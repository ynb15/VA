#!/usr/bin/env python3
"""Gegenprobe an der fertigen Datei: sitzt jede Einstellungsgrenze richtig?

Bekommt ein Bild der alten Kamera schon den neuen Ausschnitt, dann springt
das Bild ZWEIMAL dicht hintereinander statt einmal - einmal auf den neuen
Ausschnitt, einmal auf die neue Kamera. Genau daran erkennt man den Fehler,
ohne ihn zu suchen.

Geeicht an der Fassung, die er am 26.11. beanstandet hat: dort meldet der
Test an den beiden Grenzen, die er genannt hat, zwei Spruenge, an der
dritten einen. Ein Pruefwerkzeug, das den bekannten Fehler nicht findet,
ist keins - also vor dem Einsatz an der kaputten Fassung pruefen.

    python3 video/nahtprobe.py fertig.mp4 18.867 31.233 46.267
"""
"""Bild fuer Bild um eine Einstellungsgrenze: passt der Ausschnitt zur Kamera?

Ein Bild, das noch die alte Kamera zeigt, aber schon den neuen Ausschnitt
bekommt, faellt in der Bilddifferenz als ZWEI dicht aufeinander folgende
Spruenge auf statt als einer. Genau das war der Fehler.
"""
import av, numpy as np, sys
f=sys.argv[1]
c=av.open(f); st=c.streams.video[0]; tb=float(st.time_base)
for ziel in [float(x) for x in sys.argv[2:]]:
    c.seek(max(0,int((ziel-0.5)/tb)), stream=st)
    vor=None; reihe=[]
    for fr in c.decode(st):
        t=float(fr.pts*tb)
        if t < ziel-0.4: 
            vor=fr.to_ndarray(format='rgb24')[::4,::4].astype(np.int16); continue
        if t > ziel+0.4: break
        a=fr.to_ndarray(format='rgb24')[::4,::4].astype(np.int16)
        if vor is not None: reihe.append((t, float(np.abs(a-vor).mean())))
        vor=a
    gross=[r for r in reihe if r[1] > 20]
    print(f'--- Grenze {ziel:.3f}: {len(gross)} Sprung/Spruenge ueber 20 '
          f'({", ".join(f"{t:.4f}:{d:.0f}" for t,d in gross)})'
          f'   {"OK - ein Schnitt" if len(gross)==1 else "FEHLER"}')
