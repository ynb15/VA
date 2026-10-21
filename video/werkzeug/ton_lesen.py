#!/usr/bin/env python3
"""Eine Tondatei als 16-kHz-Mono-float32-Array lesen.

Warum nicht `faster_whisper` die Datei selbst oeffnen lassen: es ruft
`av.open(..., metadata_errors="ignore")`, und das Argument gibt es im hier
installierten PyAV nicht mehr (TypeError, am 21.10. gemessen). PyAV auf eine
alte Fassung festzunageln wuerde `ton_holen.py` brechen, das die neue braucht.
Also dekodieren wir selbst und uebergeben das Array — `transcribe()` nimmt es.
"""
import av
import numpy as np


def ton_als_array(pfad, rate=16000):
    with av.open(str(pfad)) as ein:
        spur = next(s for s in ein.streams if s.type == "audio")
        wandler = av.AudioResampler(format="s16", layout="mono", rate=rate)
        stuecke = []
        for rahmen in ein.decode(spur):
            for neu in wandler.resample(rahmen):
                stuecke.append(neu.to_ndarray().reshape(-1))
        for neu in wandler.resample(None):
            stuecke.append(neu.to_ndarray().reshape(-1))
    if not stuecke:
        raise IOError(f"{pfad}: keine Tondaten dekodiert")
    roh = np.concatenate(stuecke).astype(np.float32) / 32768.0
    return roh
