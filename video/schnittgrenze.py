#!/usr/bin/env python3
"""Die exakte Bildnummer eines Kameraschnitts - und zwar bildgenau.

Warum das noetig ist: `select=gt(scene,...)` meldet die Stelle um Zehntel
daneben, und ein einziges Bild, das den Ausschnitt der falschen Einstellung
bekommt, zuckt sichtbar. Am 26.11. hat er genau zwei solche Stellen gefunden,
beide ein Bild daneben.

Gemessen wird die Differenz zweier aufeinanderfolgender Bilder. Der Schnitt
ist der Ausreisser (hier Faktor 60 ueber dem Grundrauschen), nicht die
Schaetzung. Die Grenze im Plan gehoert auf die Zeit des ERSTEN Bildes der
neuen Kamera.

Zwei Fallen, beide am 26.11. aufgelaufen:
* Aneinandergehaengte Teile: die Bildzahl von Teil a nachzaehlen, nicht aus
  der Dauer rechnen. Teil a hatte 936 Bilder, gerechnet waren es 935 - und
  damit lag die Grenze ein Bild zu frueh. Am Stoss kann im Zeitraster sogar
  ein Bild fehlen.
* Dieses Skript liest rohe pts; ffmpeg schiebt den Stream beim Filtern auf
  Null (hier start_time 328 Ticks = 21 ms). Die Grenze so waehlen, dass sie
  in BEIDEN Lesarten zwischen dem letzten alten und dem ersten neuen Bild
  liegt.

    python3 video/schnittgrenze.py clip.mp4 18.9 31.2 46.3
"""
"""Exakte Bildnummer eines Kameraschnitts: Differenz zweier aufeinander
folgender Bilder. Der Schnitt ist der Ausreisser, nicht die Schaetzung."""
import av, numpy as np, sys
f=sys.argv[1]
c=av.open(f); st=c.streams.video[0]
tb=float(st.time_base)
for ziel in [float(x) for x in sys.argv[2:]]:
    c.seek(int((ziel-0.7)/tb), stream=st)
    vor=None; reihe=[]
    for fr in c.decode(st):
        t=float(fr.pts*tb)
        if t < ziel-0.7: continue
        if t > ziel+0.7: break
        a=fr.to_ndarray(format='rgb24')[::4,::4].astype(np.int16)
        if vor is not None:
            reihe.append((t, round(t*30,2), float(np.abs(a-vor).mean())))
        vor=a
    gr=max(reihe, key=lambda r: r[2])
    print(f'--- um {ziel:.3f} s: groesster Sprung bei t={gr[0]:.4f} (Bild {gr[1]:.1f}), Diff {gr[2]:.1f}')
    for t,b,d in reihe:
        if abs(t-gr[0])<0.12: print(f'    t={t:.4f}  Bild {b:7.2f}  Diff {d:6.1f}')
