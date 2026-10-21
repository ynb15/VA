#!/usr/bin/env python3
"""Fuer einen Freisteller ausrechnen, welches `box_h` einen gewuenschten
Pupillenabstand im fertigen Thumbnail ergibt.

Groessen vergleicht man am Pupillenabstand, nicht an der Rahmenhoehe — die
haengt von Frisur und Kopfhaltung ab. `box_h` ist aber das, was der Setzer
nimmt, also wird hier umgerechnet.
"""
import sys, os
import numpy as np, cv2
from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
YUNET = os.path.join(HIER, '..', 'modelle', 'yunet.onnx')


def mass(png):
    rgba = np.asarray(Image.open(png).convert('RGBA'))
    al = rgba[:, :, 3:4] / 255.0
    rgb = (rgba[:, :, :3] * al + 128 * (1 - al)).astype('uint8')
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    h, w = bgr.shape[:2]
    d = cv2.FaceDetectorYN.create(YUNET, "", (w, h), 0.6, 0.3, 5000)
    d.setInputSize((w, h))
    _, r = d.detect(bgr)
    r = max(r, key=lambda x: x[3])
    pd = ((r[4] - r[6]) ** 2 + (r[5] - r[7]) ** 2) ** 0.5
    return float(r[3]), float(pd)


if __name__ == '__main__':
    ziel = float(sys.argv[1])
    for p in sys.argv[2:]:
        bh, pd = mass(p)
        print('%-46s box_h=%6.0f pd=%6.1f  ->  box_h=%.0f fuer pd %.0f'
              % (os.path.basename(p), bh, pd, ziel * bh / pd, ziel))
