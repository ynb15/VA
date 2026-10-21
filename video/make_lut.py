#!/usr/bin/env python3
"""Baut aus dem CapCut-Export (Video oder zugeschnittener Screenshot, quadratisch) die LUT luts/ynb_look.png.

  python3 make_lut.py capcut_export.mp4 [luts/ynb_look.png]
"""
import os, subprocess, sys, tempfile
from PIL import Image

N = 216  # Hald level 6
src = sys.argv[1]
dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "luts", "ynb_look.png")
if src.lower().endswith((".png", ".jpg", ".jpeg")):
    im = Image.open(src).convert("RGB")   # Screenshot: muss exakt auf das Bild zugeschnitten und quadratisch sein
else:
    tmp = os.path.join(tempfile.mkdtemp(), "f.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "0.5", "-i", src, "-frames:v", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB")
w, h = im.size
if w != h:
    sys.exit(f"Export ist {w}x{h}, muss quadratisch sein (Projekt auf 1:1 stellen).")
b = w / N
out = Image.new("RGB", (N, N))
px = out.load()
for y in range(N):
    for x in range(N):
        px[x, y] = im.getpixel((int((x + 0.5) * b), int((y + 0.5) * b)))
out.save(dst)
print(f"ok: {w}x{h} -> {N}x{N}, gespeichert als {dst}")
