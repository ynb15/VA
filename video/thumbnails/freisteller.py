#!/usr/bin/env python3
"""Einen Kopf aus einem Einzelbild freistellen — und die Freistellung pruefen.

Freistellen heisst trennen, nicht erfinden: U2-Net entscheidet nur, welche
Pixel des Originals bleiben. Es entsteht kein Pixel, der nicht aufgenommen
wurde.

Zwei Pruefungen, beide aus Fehlern gelernt, die er gesehen hat:

1. **Gegen Gruen pruefen, nicht gegen Dunkelgrau.** Ein Stueck Stirn, das
   fehlt, faellt vor dunklem Grund nicht auf — vor Gruen sofort.
2. **Den Kopfbereich in voller Aufloesung ansehen.** Bei 420 px Breite war
   ein Regalstueck neben der Schlaefe unsichtbar; im Thumbnail stand es dann
   mitten im Gesicht.

Und nie aus einem fertigen Thumbnail schneiden: dort ist der Hintergrund
schon schwarz, U2-Net nimmt die dunklen Haare gleich mit.
"""
import argparse, os, sys
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def freistellen(quelle, ziel, kasten=None, rand=0.0):
    """`kasten` = (x0, y0, x1, y1) im Original, `rand` weitet ihn anteilig."""
    from rembg import remove, new_session
    im = Image.open(quelle).convert('RGB')
    if kasten:
        x0, y0, x1, y1 = kasten
        if rand:
            dx, dy = (x1 - x0) * rand, (y1 - y0) * rand
            x0, y0, x1, y1 = x0 - dx, y0 - dy, x1 + dx, y1 + dy
        im = im.crop((int(max(0, x0)), int(max(0, y0)),
                      int(min(im.width, x1)), int(min(im.height, y1))))
    out = remove(im, session=new_session('u2net'), alpha_matting=True,
                 alpha_matting_foreground_threshold=240,
                 alpha_matting_background_threshold=15,
                 alpha_matting_erode_size=8)
    out.save(ziel)
    return ziel


def pruefblatt(png, ziel):
    """Freisteller vor Gruen, einmal ganz und einmal der Kopf in 1:1."""
    f = Image.open(png).convert('RGBA')
    gruen = Image.new('RGBA', f.size, (0, 220, 0, 255))
    gruen.alpha_composite(f)
    kopf = gruen.crop((0, 0, f.width, min(f.height, int(f.height * 0.55))))
    b = max(f.width, kopf.width)
    blatt = Image.new('RGB', (b, f.height + kopf.height), (0, 220, 0))
    blatt.paste(gruen.convert('RGB'), (0, 0))
    blatt.paste(kopf.convert('RGB'), (0, f.height))
    blatt.save(ziel, quality=95)
    return ziel


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--quelle', required=True)
    p.add_argument('--ziel', required=True)
    p.add_argument('--kasten', help='x0,y0,x1,y1 im Original')
    p.add_argument('--rand', type=float, default=0.0)
    p.add_argument('--pruefblatt')
    a = p.parse_args()
    k = tuple(float(v) for v in a.kasten.split(',')) if a.kasten else None
    freistellen(a.quelle, a.ziel, k, a.rand)
    print(a.ziel)
    if a.pruefblatt:
        print(pruefblatt(a.ziel, a.pruefblatt))
