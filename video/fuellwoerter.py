#!/usr/bin/env python3
"""„You know" und Verwandtes aus einem Clip herausschneiden.

Auf seine Bitte vom 21.10.: einmal mit, einmal ohne. Rick sagt „you know"
im Advice-Teil im Sekundentakt; satzweise bekommt man das nicht weg, das
geht nur wortweise.

Geschnitten wird **zwischen** den Woertern: vom Ende des Wortes davor bis
zum Anfang des Wortes danach, abzueglich eines kleinen Puffers, damit kein
Konsonant abreisst. Jede Naht bekommt eine kurze Blende.

Was NICHT entfernt wird: ein Fuellwort, das einen Satz eroeffnet und nach dem
eine echte Pause steht — dort traegt es den Rhythmus, und sein Wegfall klingt
gehetzt. Das ist eine Entscheidung, keine Messung; `--alle` schaltet sie ab.
"""
import argparse, json, os, re, subprocess, sys, tempfile
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
PUFFER = 0.04          # bleibt an jeder Seite stehen
BLENDE = 0.03


def kern(w):
    return re.sub(r"[^a-z']", "", w.lower())


def ton_lesen(clip, rate=16000):
    roh = subprocess.run([FF, "-nostdin", "-v", "quiet", "-i", clip, "-f", "f32le",
                          "-ac", "1", "-ar", str(rate), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype=np.float32)


def woerter(clip, modell="medium"):
    from faster_whisper import WhisperModel
    m = WhisperModel(modell, device="cpu", compute_type="int8")
    # condition_on_previous_text=False: der Decoder nimmt sonst den
    # vorher erkannten Text als Vorlage und unterdrueckt Wiederholungen.
    # Rick sagt „you know" im Sekundentakt — gemessen am selben Fenster
    # von rick5_mit: mit Vorlage 170 Woerter und 0x „you know", ohne
    # Vorlage 188 Woerter und 7x. Eine ganze Fassung verlor so 90 Woerter.
    seg, _ = m.transcribe(ton_lesen(clip), language="en", word_timestamps=True,
                          condition_on_previous_text=False)
    return [{"t": w.word, "k": kern(w.word), "start": w.start, "end": w.end}
            for s in seg for w in (s.words or []) if w.word.strip()]


def finden(ws, muster, alle=False):
    """Stellen finden, an denen ein Fuellwort steht."""
    treffer, i = [], 0
    while i < len(ws):
        passt = None
        for m in muster:
            teile = m.split()
            if [x["k"] for x in ws[i:i+len(teile)]] == teile:
                passt = len(teile); break
        if passt:
            j = i + passt - 1
            davor_luecke = ws[i]["start"] - ws[i-1]["end"] if i > 0 else 9e9
            danach_luecke = ws[j+1]["start"] - ws[j]["end"] if j+1 < len(ws) else 9e9
            satzanfang = i == 0 or davor_luecke >= 0.45
            if alle or not (satzanfang and danach_luecke >= 0.25):
                treffer.append((i, j))
            i = j + 1
        else:
            i += 1
    return treffer


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--clip", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--muster", default="you know,y'know,i mean,sort of,kind of")
    p.add_argument("--alle", action="store_true",
                   help="auch Fuellwoerter am Satzanfang entfernen")
    p.add_argument("--nur-zaehlen", action="store_true")
    a = p.parse_args()

    muster = [kern(x).replace("", "") if False else " ".join(kern(y) for y in x.split())
              for x in a.muster.split(",") if x.strip()]
    ws = woerter(a.clip)
    treffer = finden(ws, muster, a.alle)
    gesamt = sum(ws[j]["end"] - ws[i]["start"] for i, j in treffer)
    print(f"{len(ws)} Woerter · {len(treffer)} Fuellstellen · {gesamt:.1f}s", flush=True)
    zaehler = {}
    for i, j in treffer:
        s = " ".join(ws[k]["k"] for k in range(i, j + 1))
        zaehler[s] = zaehler.get(s, 0) + 1
    for s, n in sorted(zaehler.items(), key=lambda x: -x[1]):
        print(f"   {n:3d}x  {s}")
    if a.nur_zaehlen:
        return

    # Eine Null muss auffallen. Am 21.10. lief dieses Werkzeug auf ein
    # lueckenhaftes Transkript, fand 0 von 43 Stellen, meldete „fertig" und
    # legte eine Datei ab, die mit der Eingabe identisch war. Der naechste
    # Schritt rechnete damit weiter. Ohne Fund gibt es jetzt keine Datei
    # und keinen Erfolg, sondern einen Abbruch mit Grund.
    if not treffer:
        sys.exit(f"Keine Fuellstelle gefunden in {len(ws)} Woertern — das ist "
                 f"bei diesem Material unwahrscheinlich. Wahrscheinlich ist "
                 f"das Transkript lueckenhaft. Nichts geschrieben.")

    # Behalten-Strecken bilden
    dauer = float(subprocess.run([FF, "-hide_banner", "-i", a.clip],
                                 capture_output=True, text=True).stderr
                  .split("Duration: ")[1].split(",")[0].strip()
                  .replace(":", " ").split()[-1]) + 0  # Sekundenanteil
    p2 = subprocess.run([FF, "-hide_banner", "-i", a.clip], capture_output=True, text=True)
    h, m, s = p2.stderr.split("Duration: ")[1].split(",")[0].strip().split(":")
    gesamtdauer = int(h) * 3600 + int(m) * 60 + float(s)

    schnitte = []
    for i, j in treffer:
        von = ws[i-1]["end"] + PUFFER if i > 0 else ws[i]["start"]
        bis = ws[j+1]["start"] - PUFFER if j + 1 < len(ws) else ws[j]["end"]
        if bis - von > 0.06:
            schnitte.append((von, bis))
    schnitte.sort()
    behalten, zeiger = [], 0.0
    for von, bis in schnitte:
        if von > zeiger + 0.08:
            behalten.append((zeiger, von))
        zeiger = max(zeiger, bis)
    if gesamtdauer > zeiger + 0.08:
        behalten.append((zeiger, gesamtdauer))
    weg = gesamtdauer - sum(b - v for v, b in behalten)
    print(f"  {len(behalten)} Strecken, {weg:.1f}s entfernt "
          f"({gesamtdauer:.1f} -> {gesamtdauer-weg:.1f}s)", flush=True)

    with tempfile.TemporaryDirectory() as td:
        teile = []
        for k, (v, b) in enumerate(behalten):
            q = os.path.join(td, f"t{k:04d}.mp4")
            subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                            "-ss", f"{v:.3f}", "-i", a.clip, "-t", f"{b-v:.3f}",
                            "-c:v", "libx264", "-crf", "16", "-preset", "veryfast",
                            "-af", f"afade=t=in:st=0:d={BLENDE},"
                                   f"afade=t=out:st={max(b-v-BLENDE,0):.3f}:d={BLENDE}",
                            "-c:a", "aac", "-b:a", "192k", "-video_track_timescale",
                            "30000", q], check=True)
            teile.append(q)
        liste = os.path.join(td, "l.txt")
        open(liste, "w").write("\n".join(f"file '{q}'" for q in teile))
        subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                        "-f", "concat", "-safe", "0", "-i", liste,
                        "-c", "copy", a.out], check=True)
    print(f"  -> {a.out}")


if __name__ == "__main__":
    main()
