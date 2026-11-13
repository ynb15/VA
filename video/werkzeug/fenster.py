#!/usr/bin/env python3
"""Ein Zeitfenster aus einer Drive-Videodatei transkribieren.

    python3 -I fenster.py <sekunde> <dauer> ["erwarteter text"]

Holt nur die Bytes des Fensters ueber Bereichsanfragen, dekodiert die
Tonspur und laeuft faster-whisper darueber. Dient dem Verorten von
Ankern in einer Schnittfassung, nicht dem Volltranskript.
"""
import sys
import av
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import numpy as np
from drive_lesen import DriveDatei, bestaetigte_url

FID = "1fu-An5KuRVtKQGkLAQgtP1agZ4LPyY5M"
GROESSE = 26226700133


def ton_fenster(start, dauer, rate=16000):
    d = DriveDatei(bestaetigte_url(FID), GROESSE)
    with av.open(d) as ein:
        spur = next(s for s in ein.streams if s.type == "audio")
        ein.seek(int(start / spur.time_base), stream=spur, backward=True)
        wandler = av.AudioResampler(format="s16", layout="mono", rate=rate)
        stuecke, gesehen = [], 0.0
        for rahmen in ein.decode(spur):
            t = float(rahmen.pts * spur.time_base)
            if t < start - 1:
                continue
            if t > start + dauer:
                break
            gesehen = t
            for neu in wandler.resample(rahmen):
                stuecke.append(neu.to_ndarray().reshape(-1))
        for neu in wandler.resample(None):
            stuecke.append(neu.to_ndarray().reshape(-1))
    gelesen = getattr(d, "bilanz", None)
    roh = np.concatenate(stuecke)
    return roh.astype(np.float32) / 32768.0, gesehen, gelesen


def main():
    start, dauer = float(sys.argv[1]), float(sys.argv[2])
    ton, letzte, gelesen = ton_fenster(start, dauer)
    print(f"# Fenster {start:.0f}-{start+dauer:.0f} s, {len(ton)/16000:.1f} s Ton"
          f"{'' if gelesen is None else f', {gelesen}'}", file=sys.stderr)
    from faster_whisper import WhisperModel
    m = WhisperModel("medium", device="cpu", compute_type="int8")
    segmente, _ = m.transcribe(ton, language="en", vad_filter=True)
    for s in segmente:
        print(f"[{start + s.start:8.1f}] {s.text.strip()}")


if __name__ == "__main__":
    main()
