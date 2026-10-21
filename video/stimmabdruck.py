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
        X = normiert(np.concatenate([f[2] for f in fenster]))
        texte, herkunft = [], []
        for basis, d, e, idx in fenster:
            for j, i in enumerate(idx):
                texte.append(d[i]["text"].strip())
                herkunft.append((os.path.basename(basis), i))
        gr = AgglomerativeClustering(n_clusters=2, metric="cosine",
                                     linkage="average").fit_predict(X)

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
        etikett = ["YNB" if g == ynb else "Gast" for g in gr]
        ergebnis[k] = {"etikett": etikett, "texte": texte,
                       "herkunft": herkunft, "anker": anker}
        n = sum(1 for e in etikett if e == "YNB")
        print(f"{k}: {len(etikett)} Abschnitte, {n} YNB / {len(etikett)-n} Gast"
              f"  | Anker: \"{texte[anker][:60]}\"", flush=True)
    np.save(os.path.join(HIER, "stimmabdruck_gruppen.npy"),
            np.array([ergebnis], dtype=object), allow_pickle=True)
    return ergebnis


if __name__ == "__main__":
    {"einbetten": einbetten, "gruppieren": gruppieren}[sys.argv[1]]()
