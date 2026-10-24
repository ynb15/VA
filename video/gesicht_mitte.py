#!/usr/bin/env python3
"""Wo steht das Gesicht im Bild? Spaltenmitte der Hautfarbe, ueber mehrere Bilder.

Warum das gebraucht wird: ein 9:16-Ausschnitt aus einem Querformat zeigt nur
rund ein Fuenftel der Breite. Wer darin am Rand steht, wird von den
Bedienelementen von YouTube Shorts teilweise verdeckt — sein Befund vom
24.10.2026: *„die sind alle am Rand und der wird auf YT noch teilweise
rausgeschnitten, d.h. du musst wirklich darauf achten, dass wir alle zentral
im Bild sind."*

Gemessen wird nicht geraten: Hautfarbene Pixel im oberen Teil des Bildes
(dort sitzen die Koepfe), ihre Spaltenverteilung ueber mehrere Bilder
gemittelt, und davon der Schwerpunkt. Das Ergebnis ist die x-Mitte in
Quellpixeln; der Ausschnitt wird dann darum gelegt.

    python3 video/gesicht_mitte.py datei.mp4 --von 14.9 --bis 15.93 \
            [--feld b:h:x:y] [--breite 513] [--bilder 8]

**Das Ergebnis ist ein Vorschlag, kein Befund.** Am 24.10.2026 an sechs
Stuecken geprueft: vier stimmten, zwei nicht. Die uebliche Hautmaske ist auf
helle Haut geeicht und hat bei einem dunkelhaeutigen Sprecher stattdessen einen
orangefarbenen Hintergrund gegriffen — der Ausschnitt lag 1093 px daneben, also
voellig im Leeren. **Jeden Wert mit einem Kontaktabzug nachsehen, in den eine
Mittellinie eingezeichnet ist.** Das kostet eine Minute und entscheidet.
"""
import argparse
import io
import subprocess

import numpy as np
from PIL import Image


def bild(datei, t, feld):
    vf = f"crop={feld}," if feld else ""
    r = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-ss", f"{t:.4f}",
                        "-i", datei, "-frames:v", "1", "-vf", vf + "scale=480:-1",
                        "-f", "image2pipe", "-vcodec", "png", "-"],
                       capture_output=True)
    return np.asarray(Image.open(io.BytesIO(r.stdout)).convert("RGB"), dtype=np.int16)


def haut(a):
    """Grobe Hautmaske. Absichtlich grob: gesucht ist eine Spalte, kein Umriss."""
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(axis=2), a.min(axis=2)
    return ((r > 95) & (g > 40) & (b > 20) & (mx - mn > 15)
            & (r > g) & (g > b)).astype(np.float32)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("datei")
    p.add_argument("--von", type=float, required=True)
    p.add_argument("--bis", type=float, required=True)
    p.add_argument("--feld", default=None,
                   help="crop-Ausdruck der Quelle in ffmpeg-Reihenfolge: b:h:x:y")
    p.add_argument("--breite", type=int, default=None,
                   help="Breite des 9:16-Ausschnitts; gibt den passenden x-Wert aus")
    p.add_argument("--bilder", type=int, default=8)
    a = p.parse_args()

    zeiten = np.linspace(a.von, a.bis, a.bilder)
    spalten = None
    for t in zeiten:
        f = bild(a.datei, float(t), a.feld)
        m = haut(f)[: int(f.shape[0] * 0.6)]      # oberer Teil: dort sind die Koepfe
        s = m.sum(axis=0)
        spalten = s if spalten is None else spalten + s
    if spalten.sum() < 1:
        raise SystemExit("keine Hautflaeche gefunden — Feld oder Zeiten pruefen")
    breite_px = len(spalten)
    # Nicht der Schwerpunkt ueber das ganze Bild: stehen zwei Leute darin — etwa
    # der Gesuchte links und der Reporter rechts —, landet der Schwerpunkt
    # genau zwischen ihnen, also auf niemandem. Gesucht ist das STAERKSTE
    # Vorkommen. Darum erst glaetten, dann den Gipfel nehmen und nur um ihn
    # herum mitteln.
    k = max(3, breite_px // 24)
    glatt = np.convolve(spalten, np.ones(k) / k, mode="same")
    gipfel = int(glatt.argmax())
    fenster = max(k, breite_px // 10)
    a0, b0 = max(0, gipfel - fenster), min(breite_px, gipfel + fenster + 1)
    teil = spalten[a0:b0]
    schwer = a0 + float((teil * np.arange(len(teil))).sum() / max(teil.sum(), 1e-9))
    anteil = schwer / breite_px
    print(f"Gesichtsmitte bei {anteil:.3f} der Feldbreite "
          f"({a.bilder} Bilder von {a.von:.2f} bis {a.bis:.2f} s)")
    if a.feld and a.breite:
        fb, _, fx, _ = (int(v) for v in a.feld.split(":"))
        mitte = fx + anteil * fb
        x = int(round(mitte - a.breite / 2))
        x = max(fx, min(x, fx + fb - a.breite))
        print(f"  Mitte in Quellpixeln: {mitte:.0f}")
        print(f"  Ausschnitt {a.breite} breit -> x = {x}")


if __name__ == "__main__":
    main()
