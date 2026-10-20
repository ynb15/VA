#!/usr/bin/env python3
"""Transkript einer lokalen Tondatei, mit Zeitmarken und Sprecherzuordnung.

    python3 video/transkript_lokal.py --ton roh_mix.flac --model medium \
            --spuren spur1.mp3 spur2.mp3 spur4.mp3 \
            --namen Aaronson Yannick Raum \
            --out video/transkripte/aaronson.transkript.md

Fuer veroeffentlichte Folgen gibt es `yt-transkript.py` — das holt die
automatischen Untertitel und kostet nichts. Dieses Werkzeug ist fuer
Material, das noch nicht online steht.

Die Sprecherzuordnung kommt NICHT aus einem Diarisierungsmodell, sondern
aus den Einzelspuren: wer gerade spricht, ist auf seinem eigenen Mikrofon
am lautesten. Jede Spur wird dafuer zuerst auf ihren eigenen Sprechpegel
normiert, sonst gewinnt immer die lauteste Aufnahme. Ohne `--spuren`
bleibt die Zuordnung weg.
"""
import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def huelle(pfad, rate=100):
    """Lautstaerkeverlauf in dB, `rate` Werte je Sekunde."""
    roh = subprocess.run(
        [FFMPEG, "-nostdin", "-v", "error", "-i", str(pfad),
         "-ac", "1", "-ar", str(rate * 10), "-f", "s16le", "-"],
        capture_output=True).stdout
    a = np.frombuffer(roh, dtype=np.int16).astype(np.float32) / 32768
    n = len(a) // 10
    e = np.sqrt((a[:n * 10].reshape(n, 10) ** 2).mean(1)) + 1e-9
    return 20 * np.log10(e)


def sprecher_zuordnen(segmente, spuren, namen, rate=100):
    """Je Segment die Spur mit dem hoechsten Pegel ueber ihrem eigenen Mittel.

    Der Bezug ist das 75. Perzentil der jeweiligen Spur — ihr Sprechpegel.
    Dadurch zaehlt der Abstand zum eigenen Normal, nicht die absolute
    Lautstaerke; sonst gewaenne eine heiss ausgesteuerte Aufnahme immer.
    """
    h = [huelle(p, rate) for p in spuren]
    bezug = [np.percentile(x, 75) for x in h]
    for seg in segmente:
        a, b = int(seg["start"] * rate), int(seg["end"] * rate)
        if b <= a:
            continue
        werte = [float(np.percentile(x[a:b], 80) - r) if b <= len(x) else -99
                 for x, r in zip(h, bezug)]
        i = int(np.argmax(werte))
        zweiter = sorted(werte)[-2] if len(werte) > 1 else -99
        seg["sprecher"] = namen[i]
        seg["abstand"] = round(werte[i] - zweiter, 1)
    return segmente


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ton", required=True)
    ap.add_argument("--model", default="medium")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--titel", default=None)
    ap.add_argument("--spuren", nargs="*", default=None)
    ap.add_argument("--namen", nargs="*", default=None)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    from faster_whisper import WhisperModel
    m = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=4)
    segs, info = m.transcribe(a.ton, language=a.lang, vad_filter=True,
                              condition_on_previous_text=False)
    segmente = []
    for s in segs:
        segmente.append({"start": s.start, "end": s.end, "text": s.text.strip()})
        if len(segmente) % 200 == 0:
            print(f"  {s.end / 60:.0f} min, {len(segmente)} Segmente", flush=True)

    # Erst sichern, dann zuordnen: das Transkript kostet eine Stunde, die
    # Zuordnung Sekunden. Wer die Spuren spaeter anders benennt, laesst nur
    # den zweiten Schritt neu laufen.
    roh = Path(a.out).with_suffix(".json")
    roh.write_text(json.dumps(segmente, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"  Segmente gesichert: {roh}")

    if a.spuren:
        namen = a.namen or [Path(p).stem for p in a.spuren]
        segmente = sprecher_zuordnen(segmente, a.spuren, namen)

    dauer = segmente[-1]["end"] if segmente else 0
    zeilen = [f"# {a.titel or Path(a.ton).stem}", "",
              f"**Dauer** {dauer:.0f} s ({int(dauer // 60)}:{int(dauer % 60):02d}) · "
              f"**Sprache** {info.language} · **Modell** {a.model}", "",
              "Quelle: eigenes Transkript aus dem Rohton, Zeiten in **Rohzeit**.", ""]
    if a.spuren:
        zeilen += ["Sprecher aus den Einzelspuren: wer spricht, ist auf seinem "
                   "Mikrofon am lautesten. Der Wert in Klammern ist der Abstand "
                   "zur zweitlautesten Spur in dB — unter 2 dB ist die "
                   "Zuordnung unsicher.", ""]
    zeilen.append("---")
    zeilen.append("")
    for s in segmente:
        t = int(s["start"])
        marke = f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"
        if "sprecher" in s:
            zeilen.append(f"**[{marke}] {s['sprecher']}** ({s['abstand']:+.1f}) "
                          f"{s['text']}")
        else:
            zeilen.append(f"**[{marke}]** {s['text']}")
        zeilen.append("")
    Path(a.out).write_text("\n".join(zeilen), encoding="utf-8")
    print(f"{a.out} — {len(segmente)} Segmente, {dauer / 60:.1f} min")


if __name__ == "__main__":
    main()
