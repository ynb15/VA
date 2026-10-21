#!/usr/bin/env python3
"""Stimmabdruck von Yannick — ein Anker statt blinder Sprechertrennung.

Er ist in jeder Folge. Also muss nur EINE Klasse gelernt werden: seine Stimme.
Was ihr nicht aehnlich genug ist, ist der Gast. Das ist robuster als
Diarisierung, weil die eine Klasse mit jeder Folge besser belegt wird.

    python3 video/stimmabdruck.py einbetten      # Einbettungen je Fenster
    python3 video/stimmabdruck.py gruppieren     # zwei Sprecher je Folge
    python3 video/stimmabdruck.py messen         # Trefferquote und Verweigerung

Wiederaufnehmbar wie alles hier: was fertig ist, wird an den Dateien erkannt.
Einbettungen liegen neben dem Fenster als <fenster>.npy.
"""
import glob
import json
import os
import subprocess
import sys

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
MINDEST = 1.2          # kuerzere Abschnitte tragen keine Stimmfarbe

# Schwellen, folgenweise bestimmt (nicht abschnittsweise — siehe messen()).
# Ab AB_YNB ist es er, unter AB_GAST der Gast, dazwischen wird nicht geraten.
# Gemessen am 21.10.2026 an 93 handbeschrifteten Abschnitten aus vier Folgen:
# 89 % entschieden, davon 100 % richtig, 11 % verweigert.
AB_YNB, AB_GAST = 0.442, 0.166
ABDRUCK = os.path.join(HIER, "stimmabdruck-ynb.npy")
ECAPA = os.path.join(os.path.dirname(HIER), ".ecapa")


def ton(mp4, von, bis, rate=16000):
    import imageio_ffmpeg
    roh = subprocess.run(
        [imageio_ffmpeg.get_ffmpeg_exe(), "-nostdin", "-v", "quiet",
         "-ss", f"{von:.3f}", "-i", mp4, "-t", f"{bis - von:.3f}",
         "-f", "f32le", "-ac", "1", "-ar", str(rate), "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype=np.float32)


def abschnitte(jf):
    """Abschnitte ab MINDEST Sekunden, mit Index im Originaltranskript."""
    d = json.load(open(jf))
    return [(i, s) for i, s in enumerate(d) if s["end"] - s["start"] >= MINDEST]


def einbetten():
    import torch
    from speechbrain.inference.speaker import EncoderClassifier
    modell = EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb", savedir=ECAPA,
        run_opts={"device": "cpu"})

    for jf in sorted(glob.glob(os.path.join(HIER, "*_f[0-9].json"))):
        mp4 = jf.replace(".json", ".mp4")
        npy = jf.replace(".json", ".npy")
        if not os.path.exists(mp4):
            continue
        if os.path.exists(npy):
            print(f"{os.path.basename(npy)}: schon da", flush=True)
            continue
        paare = abschnitte(jf)
        werte = []
        for i, s in paare:
            a = ton(mp4, s["start"], s["end"])
            if len(a) < 16000 * MINDEST * 0.8:
                werte.append(np.zeros(192, dtype=np.float32))
                continue
            with torch.no_grad():
                e = modell.encode_batch(torch.from_numpy(a.copy()).unsqueeze(0))
            werte.append(e.squeeze().numpy().astype(np.float32))
        np.save(npy, np.stack(werte))
        json.dump([i for i, _ in paare], open(npy + ".idx", "w"))
        print(f"{os.path.basename(npy)}: {len(werte)} Einbettungen", flush=True)


# Ein Anker je Folge: ein Abschnitt, von dem sicher ist, dass ER spricht.
# Bei drei Folgen steht er im Befund (seine Abschlussfrage). Bei den beiden
# ohne Befund ist er am Wortlaut eindeutig — Abmoderation und Dank spricht
# der Gastgeber, nicht der Gast.
ANKER_TEXT = {
    "bennett": "Thank you so much, Rob",
    "crane": "Ladies and gentlemen, this was Dr. Curtis Crane",
}


def folgen():
    """{schluessel: [(fenster_basis, transkript, einbettungen, indizes)]}"""
    aus = {}
    for npy in sorted(glob.glob(os.path.join(HIER, "*_f[0-9].npy"))):
        basis = npy[:-4]
        k = os.path.basename(basis).split("_")[0]
        d = json.load(open(basis + ".json"))
        aus.setdefault(k, []).append(
            (basis, d, np.load(npy), json.load(open(npy + ".idx"))))
    return aus


def normiert(x):
    return x / np.maximum(np.linalg.norm(x, axis=-1, keepdims=True), 1e-9)


def gruppieren():
    """Je Folge zwei Sprecher trennen und den Anker zuordnen.

    Innerhalb EINER Folge ist die Trennung leicht — zwei Stimmen, ein Raum,
    eine Aufnahme. Schwer ist erst die Frage, WER von beiden er ist, und die
    beantwortet der Anker. Das Ergebnis ist die Beschriftung, gegen die
    danach der folgenuebergreifende Stimmabdruck gemessen wird.
    """
    from sklearn.cluster import AgglomerativeClustering
    ergebnis = {}
    for k, fenster in sorted(folgen().items()):
        roh = np.concatenate([f[2] for f in fenster])
        texte, herkunft = [], []
        for basis, d, e, idx in fenster:
            for j, i in enumerate(idx):
                texte.append(d[i]["text"].strip())
                herkunft.append((os.path.basename(basis), i))
        # Abschnitte, fuer die keine Einbettung zustande kam (zu wenig Ton),
        # tragen einen Nullvektor. Die fliegen hier raus und bekommen spaeter
        # kein Etikett, sondern "?" — das ist die eingebaute Verweigerung.
        gilt = np.linalg.norm(roh, axis=1) > 1e-6
        X = normiert(roh[gilt])
        gr_klein = AgglomerativeClustering(n_clusters=2, metric="cosine",
                                           linkage="average").fit_predict(X)
        gr = np.full(len(roh), -1, dtype=int)
        gr[gilt] = gr_klein
        if (~gilt).any():
            print(f"{k}: {int((~gilt).sum())} Abschnitte ohne Einbettung",
                  flush=True)

        anker = None
        bef = os.path.join(HIER, f"{k}_befund.json")
        if os.path.exists(bef):
            frage = json.load(open(bef)).get("frage", "")[:40]
            anker = next((i for i, t in enumerate(texte)
                          if frage and frage in t), None)
        if anker is None and k in ANKER_TEXT:
            anker = next((i for i, t in enumerate(texte)
                          if ANKER_TEXT[k] in t), None)
        if anker is None:
            print(f"{k}: KEIN ANKER — uebersprungen", flush=True)
            continue

        ynb = gr[anker]
        etikett = ["?" if g < 0 else ("YNB" if g == ynb else "Gast") for g in gr]
        ergebnis[k] = {"etikett": etikett, "texte": texte,
                       "herkunft": herkunft, "anker": anker,
                       "einbettung": roh}
        n = sum(1 for e in etikett if e == "YNB")
        g_ = sum(1 for e in etikett if e == "Gast")
        print(f"{k}: {len(etikett)} Abschnitte, {n} YNB / {g_} Gast"
              f"  | Anker: \"{texte[anker][:60]}\"", flush=True)
    np.save(os.path.join(HIER, "stimmabdruck_gruppen.npy"),
            np.array([ergebnis], dtype=object), allow_pickle=True)
    return ergebnis


def _nachschlagen():
    """{(fensterbasis, textanfang): einbettung} aus allen Fenstern."""
    tab = {}
    for npy in sorted(glob.glob(os.path.join(HIER, "*_f[0-9].npy"))):
        basis = os.path.basename(npy)[:-4]
        d = json.load(open(npy[:-4] + ".json"))
        e = np.load(npy)
        idx = json.load(open(npy + ".idx"))
        for j, i in enumerate(idx):
            tab[(basis, d[i]["text"].strip())] = e[j]
    return tab


def _holen(tab, paare):
    """Beschriftete Abschnitte ueber Fenster + Textanfang aufloesen."""
    aus, fehlt = [], []
    for fenster, anfang in paare:
        treffer = [v for (f, t), v in tab.items()
                   if f == fenster and t.startswith(anfang)]
        if len(treffer) == 1 and np.linalg.norm(treffer[0]) > 1e-6:
            aus.append(treffer[0])
        else:
            fehlt.append((fenster, anfang, len(treffer)))
    return np.array(aus), fehlt


def abdruck_bauen():
    """Den Stimmabdruck aus allen beschrifteten YNB-Abschnitten ablegen."""
    lab = json.load(open(os.path.join(HIER, "stimmabdruck-labels.json")))
    tab = _nachschlagen()
    teile = []
    for teil in ("train", "test"):
        e, _ = _holen(tab, lab[teil]["YNB"])
        if len(e):
            teile.append(normiert(e))
    mitte = normiert(np.concatenate(teile).mean(0))
    np.save(ABDRUCK, mitte)
    print(f"{ABDRUCK}: aus {sum(len(t) for t in teile)} Abschnitten")
    return mitte


def kennzeichnen_liste(segmente, mp4):
    """Dieselbe Zuordnung auf einer Abschnittsliste statt auf einer Datei.

    Das ist der Einstieg fuer transkript_lokal.py --stimmabdruck.
    """
    import torch
    from speechbrain.inference.speaker import EncoderClassifier
    mitte = np.load(ABDRUCK) if os.path.exists(ABDRUCK) else abdruck_bauen()
    modell = EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb", savedir=ECAPA,
        run_opts={"device": "cpu"})
    for sgm in segmente:
        if sgm["end"] - sgm["start"] < MINDEST:
            sgm["sprecher"], sgm["aehnlichkeit"] = "?", None
            continue
        a = ton(mp4, sgm["start"], sgm["end"])
        with torch.no_grad():
            e = modell.encode_batch(torch.from_numpy(a.copy()).unsqueeze(0))
        c = float(normiert(e.squeeze().numpy()) @ mitte)
        sgm["aehnlichkeit"] = round(c, 3)
        sgm["sprecher"] = ("YNB" if c >= AB_YNB
                           else "Gast" if c <= AB_GAST else "?")
    return segmente


def kennzeichnen(jf=None, mp4=None):
    """Ein Transkript mit Sprechern versehen — oder mit '?', wo es unsicher ist.

        python3 video/stimmabdruck.py kennzeichnen <transkript.json> <ton.mp4>

    Gibt dieselbe Abschnittsliste zurueck, je Abschnitt um "sprecher" und
    "aehnlichkeit" ergaenzt. Unter der Sicherheitsschwelle steht "?" — ein
    Transkript, das an einer Stelle schweigt, ist brauchbar; eins, das ueberall
    etwas behauptet und manchmal irrt, ist es nicht.
    """
    import torch
    from speechbrain.inference.speaker import EncoderClassifier
    jf = jf or sys.argv[2]
    mp4 = mp4 or sys.argv[3]
    mitte = np.load(ABDRUCK) if os.path.exists(ABDRUCK) else abdruck_bauen()
    modell = EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb", savedir=ECAPA,
        run_opts={"device": "cpu"})
    d = json.load(open(jf))
    for sgm in d:
        if sgm["end"] - sgm["start"] < MINDEST:
            sgm["sprecher"], sgm["aehnlichkeit"] = "?", None
            continue
        a = ton(mp4, sgm["start"], sgm["end"])
        with torch.no_grad():
            e = modell.encode_batch(torch.from_numpy(a.copy()).unsqueeze(0))
        c = float(normiert(e.squeeze().numpy()) @ mitte)
        sgm["aehnlichkeit"] = round(c, 3)
        sgm["sprecher"] = ("YNB" if c >= AB_YNB
                           else "Gast" if c <= AB_GAST else "?")
    n = {x: sum(1 for s in d if s["sprecher"] == x) for x in ("YNB", "Gast", "?")}
    print(f"{len(d)} Abschnitte: {n['YNB']} YNB, {n['Gast']} Gast, "
          f"{n['?']} ohne Zuordnung ({100*n['?']/max(1,len(d)):.0f} %)", flush=True)
    json.dump(d, open(jf.replace(".json", ".sprecher.json"), "w"),
              indent=1, ensure_ascii=False)
    return d


def messen():
    """Stimmabdruck bauen und gegen die Handbeschriftung messen.

    Die Schwellen werden AUSSCHLIESSLICH auf den Trainingsdaten gesetzt und
    dort ueber Leave-one-out bestimmt, damit kein Abschnitt seine eigene
    Schwelle mitbestimmt. Zwischen den beiden Schwellen wird nicht geraten,
    sondern verweigert.
    """
    lab = json.load(open(os.path.join(HIER, "stimmabdruck-labels.json")))
    tab = _nachschlagen()
    tr_y, f1 = _holen(tab, lab["train"]["YNB"])
    tr_g, f2 = _holen(tab, lab["train"]["Gast"])
    te_y, f3 = _holen(tab, lab["test"]["YNB"])
    te_g, f4 = _holen(tab, lab["test"]["Gast"])
    for name, f in (("train/YNB", f1), ("train/Gast", f2),
                    ("test/YNB", f3), ("test/Gast", f4)):
        for e in f:
            print(f"  nicht aufgeloest [{name}]: {e[0]} / {e[1][:40]!r} -> {e[2]} Treffer")

    Y = normiert(tr_y)
    G = normiert(tr_g)

    # Leave-one-out auf den Trainings-YNB: jeder Abschnitt wird gegen einen
    # Schwerpunkt gemessen, in den er selbst NICHT eingeflossen ist.
    s_y = np.array([float(normiert(np.delete(Y, i, axis=0).mean(0)) @ Y[i])
                    for i in range(len(Y))])
    mitte = normiert(Y.mean(0))
    s_g = G @ mitte

    hoch = float(np.quantile(s_y, 0.10))
    tief = float(np.quantile(s_g, 0.90))
    print(f"\nStimmabdruck aus {len(Y)} Abschnitten "
          f"({sum(1 for _ in lab['train']['YNB'])} beschriftet)")
    print(f"  Aehnlichkeit YNB (leave-one-out): {s_y.min():.3f} … {s_y.max():.3f}"
          f"  Median {np.median(s_y):.3f}")
    print(f"  Aehnlichkeit Gast:                {s_g.min():.3f} … {s_g.max():.3f}"
          f"  Median {np.median(s_g):.3f}")
    print(f"  Schwellen: ab {hoch:.3f} YNB, unter {tief:.3f} Gast"
          + ("  — SAUBERE LUECKE" if hoch > tief else "  — SIE UEBERLAPPEN"))

    def urteil(x):
        c = float(normiert(x) @ mitte)
        if c >= max(hoch, tief):
            return "YNB", c
        if c <= min(hoch, tief):
            return "Gast", c
        return "?", c

    treffer = falsch = weg = 0
    verwechselt = []
    for X, wahr in ((te_y, "YNB"), (te_g, "Gast")):
        for x in X:
            u, c = urteil(x)
            if u == "?":
                weg += 1
            elif u == wahr:
                treffer += 1
            else:
                falsch += 1
                verwechselt.append((wahr, u, round(c, 3)))
    ges = treffer + falsch + weg
    entschieden = treffer + falsch
    print(f"\nPruefung an {ges} handbeschrifteten Abschnitten aus zwei "
          f"zurueckgehaltenen Folgen (Crane, Wheelock):")
    print(f"  entschieden : {entschieden} ({100*entschieden/ges:.0f} %)")
    print(f"  davon richtig: {treffer} ({100*treffer/max(1,entschieden):.1f} %)")
    print(f"  verweigert  : {weg} ({100*weg/ges:.0f} %)")
    if verwechselt:
        print(f"  Verwechslungen: {verwechselt}")
    return mitte, hoch, tief


if __name__ == "__main__":
    {"einbetten": einbetten, "gruppieren": gruppieren, "messen": messen,
     "abdruck": abdruck_bauen, "kennzeichnen": kennzeichnen}[sys.argv[1]]()
