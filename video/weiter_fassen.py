#!/usr/bin/env python3
"""Das Sprecherbild weiter fassen, als ein 9:16-Ausschnitt es zulaesst.

Hintergrund: aus einem 1920x1080-Bild ist der breiteste randlose 9:16-Ausschnitt
608 px breit — die volle Hoehe. Weiter herauszugehen ist in 9:16 nicht moeglich,
ohne oben und unten etwas hinzuzufuegen. Sein Wunsch vom 24.10.2026: "du musst
nochmal ein bisschen rauszoomen. Mein Gesicht und auch David."

Hier wird je Einstellung ein 3:4-Ausschnitt (810x1080) genommen, scharf auf
1080x1440 gebracht und mittig gesetzt; darueber und darunter steht dasselbe
Bild vergroessert, unscharf und abgedunkelt — dieselbe Fuellung wie bei der
B-Roll aus dem Into-the-Wild-Short. Das Motiv wird dadurch um den Faktor 1,33
kleiner als bisher, und der scharfe Teil wird sogar SCHAERFER: 810 statt 608
Quellpixel auf dieselbe Breite.
"""
import json
import subprocess
import sys

QUELLE, ZIEL, PLAN = sys.argv[1], sys.argv[2], sys.argv[3]
BREIT, HOCH = 810, 1080          # 3:4 aus der Quelle
W, H = 1080, 1920
SCHARF_H = int(round(W * HOCH / BREIT))   # 1440

plan = json.load(open(PLAN))
teile, v, a = [], [], []
for i, e in enumerate(plan["einstellungen"]):
    x, y, b, h = (int(t) for t in e["kasten"].split(":"))
    mitte = x + b / 2
    bx = int(round(max(0, min(mitte - BREIT / 2, 1920 - BREIT))))
    von, bis = e["start"], e["ende"]
    teile.append(
        f"[0:v]trim={von:.4f}:{bis:.4f},setpts=PTS-STARTPTS,"
        f"crop={BREIT}:{HOCH}:{bx}:0,split=2[bg{i}][fg{i}]")
    teile.append(
        f"[bg{i}]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
        f"scale={W // 4}:{H // 4},gblur=sigma=11,scale={W}:{H}:flags=bilinear,"
        f"eq=brightness=-0.16[bgu{i}]")
    teile.append(f"[fg{i}]scale={W}:{SCHARF_H}[fgs{i}]")
    teile.append(f"[bgu{i}][fgs{i}]overlay=0:(H-h)/2,setsar=1[v{i}]")
    teile.append(f"[0:a]atrim={von:.4f}:{bis:.4f},asetpts=PTS-STARTPTS[a{i}]")
    v.append(f"[v{i}]"); a.append(f"[a{i}]")
    print(f"  {von:6.2f}-{bis:6.2f}  Kasten {e['kasten']:>18s} -> 3:4 bei x={bx}")

n = len(v)
teile.append("".join(x + y for x, y in zip(v, a)) + f"concat=n={n}:v=1:a=1[vv][aa]")
cmd = ["ffmpeg", "-nostdin", "-v", "error", "-stats", "-i", QUELLE,
       "-filter_complex", ";".join(teile), "-map", "[vv]", "-map", "[aa]",
       "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", ZIEL, "-y"]
subprocess.run(cmd, check=True)
print(f"-> {ZIEL}")
