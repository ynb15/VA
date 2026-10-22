#!/usr/bin/env python3
"""Die Tonspur aus einer grossen Drive-Datei holen, ohne sie zu laden.

    python3 video/ton_holen.py --id <drive-id> --groesse <bytes> \
            --out /pfad/ton.flac

Warum nicht nur die Tonpakete? Gemessen am 20.10.2026 am Aaronson-Master
(16,1 GB, 101 min): `demux(audio)` ueberspringt die Videopakete NICHT —
fuer 120 s Ton wurden 327 MB geholt, also genau die 120 s Video dazu.
PyAV setzt zwar `discard` auf den uebrigen Spuren, der mov-Demuxer liest
die Bytes aber trotzdem. Also wird einmal sequentiell durchgelesen und das
Ergebnis als FLAC abgelegt — 16 kHz Mono reicht fuer Whisper und macht aus
16,1 GB rund 150 MB, die hier bleiben.

Einmal holen, beliebig oft transkribieren.
"""
import argparse
import sys
import time
from pathlib import Path

import av

sys.path.insert(0, str(Path(__file__).resolve().parent))
from drive_fernzugriff import DriveDatei, bestaetigte_url


def ton_holen(file_id, ziel, groesse=None, rate=16000, melden=60.0,
              von=0.0, bis=None):
    """Tonspur holen, wahlweise nur das Stueck von `von` bis `bis`.

    **Warum stueckweise.** Am 22.10. starb ein Zug ueber einen 27-GB-Master
    nach fuenf Minuten: der Container wurde eingezogen, der Proxy bekam
    einen neuen Port, und der laufende Prozess lief ins Leere
    (`Unable to connect to proxy ... Connection refused`). Ein sequentieller
    Lauf ueber eine Stunde ueberlebt das nie. Also in Stuecken, jedes in
    einem frischen Prozess mit frischem Proxy, und was fertig ist, bleibt
    fertig.
    """
    quelle = DriveDatei(bestaetigte_url(file_id), groesse=groesse)
    ein = av.open(quelle)
    a_ein = next(s for s in ein.streams if s.type == "audio")
    dauer = float(ein.duration) / 1e6 if ein.duration else None
    if von > 0:
        ein.seek(int(von / a_ein.time_base), stream=a_ein)

    aus = av.open(str(ziel), "w")
    a_aus = aus.add_stream("flac", rate=rate)
    a_aus.layout = "mono"

    neu = av.audio.resampler.AudioResampler(format="s16", layout="mono", rate=rate)
    t0 = zuletzt = time.time()
    pos = 0.0
    for rahmen in ein.decode(a_ein):
        if rahmen.pts is not None:
            pos = float(rahmen.pts * rahmen.time_base)
        if pos < von - 0.05:
            continue
        if bis is not None and pos >= bis:
            break
        for r in neu.resample(rahmen):
            r.pts = None
            for pkt in a_aus.encode(r):
                aus.mux(pkt)
        if time.time() - zuletzt > melden:
            zuletzt = time.time()
            anteil = f"{pos / dauer * 100:.0f} %" if dauer else "?"
            print(f"  {pos / 60:.1f} min ({anteil}), "
                  f"{quelle.gelesen / 1e9:.2f} GB geholt, "
                  f"{(time.time() - t0) / 60:.1f} min gelaufen", flush=True)

    for r in neu.resample(None) or []:
        r.pts = None
        for pkt in a_aus.encode(r):
            aus.mux(pkt)
    for pkt in a_aus.encode(None):
        aus.mux(pkt)
    aus.close()
    ein.close()
    return pos, quelle.gelesen, time.time() - t0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True, help="Drive-Datei-ID")
    ap.add_argument("--groesse", type=int, default=None,
                    help="Dateigroesse in Bytes, spart eine HEAD-Anfrage")
    ap.add_argument("--rate", type=int, default=16000)
    ap.add_argument("--out", required=True)
    ap.add_argument("--von", type=float, default=0.0,
                    help="Sekunde, ab der geholt wird (fuer stueckweise Zuege)")
    ap.add_argument("--bis", type=float, default=None,
                    help="Sekunde, bis zu der geholt wird")
    a = ap.parse_args()
    dauer, bytes_, sek = ton_holen(a.id, a.out, groesse=a.groesse, rate=a.rate,
                                   von=a.von, bis=a.bis)
    print(f"{a.out} — {dauer / 60:.1f} min Ton, {bytes_ / 1e9:.2f} GB geholt, "
          f"{sek / 60:.1f} min")
