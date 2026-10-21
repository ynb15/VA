#!/usr/bin/env python3
"""Aus einem Clip eine durchstreichbare Schnittliste machen — und zurück.

Warum es das gibt: Yannick am 21.10. — „Ich glaube, es geht einfacher. Du gibst
mir ein Transkript, ich streiche durch, was raus soll." Sonst ist es
Hin und Her: er beschreibt eine Stelle, ich suche die falsche.

Zwei Richtungen:

  bauen    Clip -> Textliste mit Nummern und Zeiten (wie im fertigen Short)
  anwenden Liste + gestrichene Nummern -> neuer Clip, Schnitte in der Stille

Die Schnitte werden auf die nächste Sprechpause gezogen, damit kein Wort
abgeschnitten wird, und mit 40 ms Blende gesetzt, damit es nicht knackt.
"""
import argparse, json, os, re, subprocess, sys, tempfile
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def mmss(t):
    t = max(0.0, t)
    return f"{int(t) // 60:02d}:{t % 60:04.1f}"


def ton_lesen(clip, rate=16000):
    roh = subprocess.run([FF, "-nostdin", "-v", "quiet", "-i", clip, "-f", "f32le",
                          "-ac", "1", "-ar", str(rate), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype=np.float32)


def stillen(ton, rate=16000, mindest=0.20, schwelle_db=-45.0):
    """Sprechpausen aus dem Pegel. Whispers Zeitstempel taugen dafuer nicht —
    es zieht Wortenden an den naechsten Wortanfang (Befund vom 20.10.)."""
    f = int(rate * 0.02)
    n = len(ton) // f
    rms = np.sqrt(np.maximum([(ton[i*f:(i+1)*f] ** 2).mean() for i in range(n)], 1e-12))
    db = 20 * np.log10(rms)
    leise = db < schwelle_db
    paus, i = [], 0
    while i < n:
        if leise[i]:
            j = i
            while j + 1 < n and leise[j + 1]:
                j += 1
            if (j - i + 1) * 0.02 >= mindest:
                paus.append(((i + j + 1) / 2 * 0.02, i * 0.02, (j + 1) * 0.02))
            i = j + 1
        else:
            i += 1
    return paus


def ziehen(t, paus, max_versatz=1.2):
    """Einen Schnittpunkt auf die naechste Pausenmitte ziehen."""
    nah = [p for p in paus if abs(p[0] - t) <= max_versatz]
    return min(nah, key=lambda p: abs(p[0] - t))[0] if nah else t



def saetze_bilden(woerter, pause=0.45):
    """Woerter zu SAETZEN gruppieren, nicht zu Whisper-Abschnitten.

    Sein Strich vom 21.10. hat den Fehler aufgedeckt: Whispers Abschnitte
    enden mitten im Satz („...translation and commentary" | „on the book of
    Genesis"), also zerreisst jeder Strich an so einer Grenze einen Satz.
    Er streicht nach Sinn — die Liste muss deshalb nach Sinn gebaut sein.

    Getrennt wird an Satzzeichen und an einer Sprechpause ueber `pause`.
    Beides zusammen, weil Whispers Zeichensetzung mal fehlt und die Pause
    allein mitten im Satz stehen kann.
    """
    saetze, lauf = [], []
    for i, w in enumerate(woerter):
        lauf.append(w)
        text = w["t"].rstrip()
        endet = text.endswith((".", "!", "?"))
        luecke = (woerter[i + 1]["start"] - w["end"]) if i + 1 < len(woerter) else 9e9
        if endet or luecke >= pause:
            saetze.append({"start": lauf[0]["start"], "end": lauf[-1]["end"],
                           "text": " ".join(x["t"].strip() for x in lauf).strip()})
            lauf = []
    if lauf:
        saetze.append({"start": lauf[0]["start"], "end": lauf[-1]["end"],
                       "text": " ".join(x["t"].strip() for x in lauf).strip()})
    # Sehr kurze Schnipsel („Yeah.", „Right.") an den Nachbarn haengen, sonst
    # wird die Liste unlesbar lang.
    gelegt = []
    for s in saetze:
        if gelegt and len(s["text"].split()) <= 2 and s["start"] - gelegt[-1]["end"] < 0.8:
            gelegt[-1]["end"] = s["end"]
            gelegt[-1]["text"] += " " + s["text"]
        else:
            gelegt.append(dict(s))
    return gelegt


def woerter_holen(clip, modell="medium"):
    from faster_whisper import WhisperModel
    m = WhisperModel(modell, device="cpu", compute_type="int8")
    # condition_on_previous_text=False: der Decoder nimmt sonst den
    # vorher erkannten Text als Vorlage und unterdrueckt Wiederholungen.
    # Rick sagt „you know" im Sekundentakt — gemessen am selben Fenster
    # von rick5_mit: mit Vorlage 170 Woerter und 0x „you know", ohne
    # Vorlage 188 Woerter und 7x. Eine ganze Fassung verlor so 90 Woerter.
    seg, _ = m.transcribe(ton_lesen(clip), language="en", word_timestamps=True,
                          condition_on_previous_text=False)
    return [{"t": w.word, "start": w.start, "end": w.end}
            for s in seg for w in (s.words or []) if w.word.strip()]


def bauen(clip, abschnitte, tempo, out, titel, ende_clip=None):
    zeilen = [f"# {titel}", f"# Quelle: {os.path.basename(clip)} · Tempo {tempo}",
              "#",
              "# Zeiten sind die im FERTIGEN Short — also das, was Du im Player siehst.",
              "# Was raus soll: Zeile loeschen oder die Nummer nennen. Zurueckschicken genuegt.",
              "#"]
    # Der Clip endet irgendwo; was danach kommt, bleibt stehen und wird
    # markiert — so sieht er auch, was er DAZUnehmen koennte, nicht nur was raus soll.
    marke_gesetzt = False
    for i, a in enumerate(abschnitte, 1):
        if ende_clip is not None and not marke_gesetzt and a["start"] >= ende_clip:
            zeilen.append("")
            zeilen.append(f"# ----- hier endet die aktuelle Fassung "
                          f"({mmss(ende_clip/tempo)}) -----")
            zeilen.append("# Alles darunter ist NICHT drin. Willst Du etwas davon,")
            zeilen.append("# sag mir die Nummer — dann nehme ich es dazu.")
            zeilen.append("")
            marke_gesetzt = True
        zeilen.append(f"{i:3d}  [{mmss(a['start']/tempo)}–{mmss(a['end']/tempo)}]  "
                      f"{a['text']}")
    open(out, "w", encoding="utf-8").write("\n".join(zeilen) + "\n")
    return len(abschnitte)


def anwenden(clip, abschnitte, raus, out, tempo):
    """Die nicht gestrichenen Abschnitte aneinandersetzen."""
    behalten = [a for i, a in enumerate(abschnitte, 1) if i not in raus]
    if not behalten:
        raise SystemExit("Es bliebe nichts uebrig.")
    paus = stillen(ton_lesen(clip))
    # Benachbarte Abschnitte verschmelzen — nach ihrer STELLE in der Liste,
    # nicht nach dem Zeitabstand. Der erste Entwurf verschmolz nur bei unter
    # 0,05 s Abstand; zwischen zwei Saetzen liegt aber fast immer eine
    # Atempause. Ergebnis waren 46 Einzelstuecke fuer 3 gestrichene Zeilen,
    # jedes mit eigener Ein- und Ausblendung — der Ton haette gepumpt.
    # Zwischen zwei behaltenen Nachbarn gehoert die Pause dazu.
    behalten_idx = [i for i in range(1, len(abschnitte) + 1) if i not in raus]
    strecken, letzte = [], None
    for i in behalten_idx:
        a = abschnitte[i - 1]
        if letzte is not None and i == letzte + 1:
            strecken[-1][1] = a["end"]
        else:
            strecken.append([a["start"], a["end"]])
        letzte = i
    gezogen = [[ziehen(v, paus), ziehen(b, paus)] for v, b in strecken]
    gezogen = [s for s in gezogen if s[1] - s[0] > 0.1]   # leere Reste raus
    print(f"  {len(abschnitte)} Abschnitte, {len(raus)} gestrichen, "
          f"{len(gezogen)} Strecke(n):", flush=True)
    for v, b in gezogen:
        print(f"    {mmss(v)}–{mmss(b)}  ({b-v:.2f}s)", flush=True)

    with tempfile.TemporaryDirectory() as td:
        teile = []
        for k, (v, b) in enumerate(gezogen):
            p = os.path.join(td, f"t{k:03d}.mp4")
            subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                            "-ss", f"{v:.3f}", "-i", clip, "-t", f"{b-v:.3f}",
                            "-c:v", "libx264", "-crf", "16", "-preset", "veryfast",
                            "-af", "afade=t=in:st=0:d=0.04,"
                                   f"afade=t=out:st={max(b-v-0.04,0):.3f}:d=0.04",
                            "-c:a", "aac", "-b:a", "192k", p], check=True)
            teile.append(p)
        liste = os.path.join(td, "liste.txt")
        open(liste, "w").write("\n".join(f"file '{p}'" for p in teile))
        subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                        "-f", "concat", "-safe", "0", "-i", liste,
                        "-c", "copy", out], check=True)
    return sum(b - v for v, b in gezogen)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--clip", required=True)
    p.add_argument("--transkript", help="JSON mit start/end/text; sonst wird transkribiert")
    p.add_argument("--versatz", type=float, default=0.0,
                   help="Sekunde im Transkript, an der der Clip beginnt")
    p.add_argument("--tempo", type=float, default=1.15)
    p.add_argument("--pause", type=float, default=0.45,
                   help="Sprechpause, ab der ohne Satzzeichen getrennt wird")
    p.add_argument("--titel", default="Short")
    p.add_argument("--liste", help="Schnittliste hierhin schreiben")
    p.add_argument("--ende-clip", type=float, default=None,
                   help="Clipsekunde, an der die aktuelle Fassung endet")
    p.add_argument("--raus", default="", help="zu streichende Nummern: 3,7,9-11")
    p.add_argument("--out", help="neuer Clip (nur mit --raus)")
    a = p.parse_args()

    if a.transkript:
        roh = json.load(open(a.transkript))
        dauer = float(subprocess.run(
            [FF, "-hide_banner", "-i", a.clip], capture_output=True, text=True
        ).stderr.split("Duration: ")[1][:11].replace(":", " ").split()[-1]) if False else None
        ab = [{"start": s["start"] - a.versatz, "end": s["end"] - a.versatz,
               "text": s["text"]} for s in roh]
        ab = [s for s in ab if s["end"] > 0]
    else:
        ab = saetze_bilden(woerter_holen(a.clip), pause=a.pause)
        ab = [{"start": round(s["start"], 2), "end": round(s["end"], 2),
               "text": s["text"]} for s in ab]

    if a.liste:
        n = bauen(a.clip, ab, a.tempo, a.liste, a.titel, a.ende_clip)
        print(f"{n} Abschnitte -> {a.liste}")

    if a.raus:
        weg = set()
        for teil in a.raus.split(","):
            teil = teil.strip()
            if "-" in teil:
                v, b = (int(x) for x in teil.split("-"))
                weg.update(range(v, b + 1))
            elif teil:
                weg.add(int(teil))
        if not a.out:
            raise SystemExit("--raus braucht --out")
        laenge = anwenden(a.clip, ab, weg, a.out, a.tempo)
        print(f"  -> {a.out}  {laenge:.1f}s roh, {laenge/a.tempo:.1f}s bei Tempo {a.tempo}")


if __name__ == "__main__":
    main()
