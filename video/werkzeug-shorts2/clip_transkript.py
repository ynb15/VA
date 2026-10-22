#!/usr/bin/env python3
"""Transkript eines Clips mit Wortzeiten — Zeiten in Clipzeit.

    python3 clip_transkript.py <ton-oder-video> <ziel.json> [modell]

Warum der Ton selbst dekodiert wird: `faster-whisper` 1.2.1 oeffnet Dateien
ueber PyAV, und die hier installierte PyAV-Fassung kennt das Argument
`metadata_errors` nicht — der Lauf bricht in `av.open` ab. Die Bibliothek
nimmt aber auch ein float32-Array bei 16 kHz. ffmpeg 6.1.1 dekodiert, und
die Abhaengigkeit entfaellt.
"""
import json
import subprocess
import sys

import numpy as np
from faster_whisper import WhisperModel


def ton(pfad, rate=16000):
    roh = subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "error", "-i", str(pfad),
         "-map", "0:a", "-ac", "1", "-ar", str(rate), "-f", "f32le", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype=np.float32).copy()


def main():
    quelle, ziel = sys.argv[1], sys.argv[2]
    modell = sys.argv[3] if len(sys.argv) > 3 else "medium"
    a = ton(quelle)
    print(f"{len(a) / 16000:.1f} s Ton, Modell {modell}", flush=True)
    m = WhisperModel(modell, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(a, language="en", word_timestamps=True,
                           vad_filter=False)
    aus = []
    for s in segs:
        aus.append({"start": s.start, "end": s.end, "text": s.text,
                    "words": [{"w": w.word, "s": w.start, "e": w.end}
                              for w in (s.words or [])]})
        print(f"[{int(s.start // 60):02d}:{s.start % 60:05.2f}] "
              f"{s.text.strip()}", flush=True)
    json.dump(aus, open(ziel, "w"), ensure_ascii=False, indent=1)
    print(f"FERTIG — {len(aus)} Segmente -> {ziel}")


if __name__ == "__main__":
    main()
