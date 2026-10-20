#!/usr/bin/env python3
"""Einzelbilder aus einer Drive-Kameradatei holen, fensterweise.

Nur die Bloecke, die im Fenster liegen, werden geholt. Pro Fenster wird ab dem
letzten Schluesselbild davor dekodiert und jedes n-te Bild gespeichert.
"""
import argparse, os, sys, time
sys.path.insert(0, '/home/user/VA/video')
from drive_fernzugriff import bestaetigte_url, SITZUNG
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from drive_fest import FesteDriveDatei as DriveDatei
import av


def fenster(fid, fenster_liste, ziel_ordner, pro_sekunde=2.0, groesse=None):
    os.makedirs(ziel_ordner, exist_ok=True)
    q = DriveDatei(bestaetigte_url(fid), groesse=groesse, sitzung=SITZUNG,
                   url_neu=lambda: bestaetigte_url(fid))
    c = av.open(q)
    v = next(s for s in c.streams if s.type == 'video')
    v.thread_type = 'AUTO'
    n_gesamt = 0
    for start, dauer in fenster_liste:
        ende = start + dauer
        c.seek(int(start / v.time_base), stream=v)
        letzte = -99.0
        for bild in c.decode(v):
            t = float(bild.pts * v.time_base)
            if t < start - 0.05:
                continue
            if t > ende:
                break
            if t - letzte < 1.0 / pro_sekunde - 1e-3:
                continue
            letzte = t
            p = os.path.join(ziel_ordner, f'{t:08.2f}.jpg')
            bild.to_image().save(p, quality=95)
            n_gesamt += 1
    bilanz = q.bilanz if hasattr(q, 'bilanz') else ''
    c.close(); q.close()
    return n_gesamt, bilanz


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--id', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--fps', type=float, default=2.0)
    p.add_argument('--fenster', required=True,
                   help='start:dauer,start:dauer,... in Sekunden')
    a = p.parse_args()
    fl = [tuple(float(x) for x in w.split(':')) for w in a.fenster.split(',')]
    t0 = time.time()
    n, bilanz = fenster(a.id, fl, a.out, a.fps)
    print(f'{n} Bilder in {time.time()-t0:.1f}s -> {a.out}')
    print(' ', bilanz)
