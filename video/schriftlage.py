#!/usr/bin/env python3
"""Oberkante der Untertitel Bild fuer Bild aus einer fertigen Datei lesen.

Die Gegenprobe zu "die Schrift springt". Sucht im Band 850..1250 je Bild die
oberste Zeile mit genug hellen Pixeln und zaehlt die Werte aus. Steht dort
ueber die ganze Laufzeit ein Wert (plus/minus die Glyphenform), dann steht die
Schrift still - und die Beschwerde gilt dem ABSTAND zum Kinn, nicht der
absoluten Hoehe. Das ist ein Unterschied, an dem ich zweimal vorbeigemessen
habe.

Ausreisser nach oben sind meist keine Schrift, sondern helle Stellen im Bild
(Hand, Hemd): bei denen bleibt `unten` gleich, waehrend `oben` springt.

    python3 video/schriftlage.py fertig.mp4 [sekunden]
"""
import av, numpy as np, sys
f=sys.argv[1]; bis=float(sys.argv[2]) if len(sys.argv)>2 else 72.0
c=av.open(f); st=c.streams.video[0]
zeilen={}
for fr in c.decode(st):
    t=float(fr.pts*st.time_base)
    if t>bis: break
    a=fr.to_ndarray(format='rgb24')
    b=a[850:1250,100:980]
    hell=((b[:,:,0]>235)&(b[:,:,1]>225)&(b[:,:,2].astype(int)<260))
    anz=hell.sum(axis=1)
    kand=np.nonzero(anz>12)[0]
    zeilen[round(t,3)]= (850+int(kand[0]), 850+int(kand[-1])) if len(kand) else None
werte=[v[0] for v in zeilen.values() if v]
import collections
print('Oberkanten:', collections.Counter(werte).most_common(12))
vor=None
for t,v in sorted(zeilen.items()):
    if v and (vor is None or abs(v[0]-vor)>6):
        print(f'{t:7.3f}  oben={v[0]}  unten={v[1]}')
        vor=v[0]
