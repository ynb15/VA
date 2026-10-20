#!/usr/bin/env python3
"""Ein Fenster aus dem Drive-Master holen, ohne die ganze Datei zu laden.

    python3 video/master_schnitt.py --id <drive-id> --start 5520 --ende 5585 \
            --out /pfad/rohschnitt.mp4

Hintergrund: die Studio-Master sind zweistellige Gigabyte gross (Sutcliffe:
18,6 GB). Der Container kann sie nicht halten. Drive beantwortet aber
Bereichsanfragen, PyAV nimmt ein dateiaehnliches Objekt, und so werden nur die
Bloecke geholt, die im Fenster liegen — gemessen rund 170 MB pro Minute.

Kopiert die Pakete ohne Neukodierung (Remux), damit nichts an Qualitaet
verloren geht und es schnell bleibt. Der Schnitt beginnt am letzten
Schluesselbild vor `start`; der genaue Beginn wird als Versatz zurueckgegeben,
damit der Renderer exakt setzen kann.
"""
import argparse
import sys

import av

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from drive_fernzugriff import DriveDatei, bestaetigte_url


def fenster_holen(file_id, start, ende, ziel, groesse=None):
    quelle = DriveDatei(bestaetigte_url(file_id), groesse=groesse,
                        datei_id=file_id)
    ein = av.open(quelle)
    v_ein = next(s for s in ein.streams if s.type == 'video')
    a_ein = next(s for s in ein.streams if s.type == 'audio')

    aus = av.open(ziel, 'w')
    v_aus = aus.add_stream_from_template(v_ein)
    a_aus = aus.add_stream_from_template(a_ein)

    # Auf das Schluesselbild vor dem Fensterbeginn setzen.
    ein.seek(int(start / v_ein.time_base), stream=v_ein)

    erster_pts = {}
    geschrieben = 0
    for pkt in ein.demux(v_ein, a_ein):
        if pkt.dts is None:
            continue
        t = float(pkt.pts * pkt.time_base) if pkt.pts is not None else None
        if t is None:
            continue
        if t > ende:
            if pkt.stream.type == 'video':
                break
            continue
        if t < start - 6:          # Vorlauf begrenzen
            continue
        art = pkt.stream.type
        if art not in erster_pts:
            erster_pts[art] = t
        pkt.stream = v_aus if art == 'video' else a_aus
        aus.mux(pkt)
        geschrieben += 1

    aus.close()
    ein.close()
    beginn = min(erster_pts.values()) if erster_pts else start
    bilanz = quelle.bilanz
    quelle.close()
    return beginn, start - beginn, geschrieben, bilanz


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--id', required=True)
    p.add_argument('--start', type=float, required=True)
    p.add_argument('--ende', type=float, required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--groesse', type=int, default=None)
    a = p.parse_args()
    beginn, versatz, n, bilanz = fenster_holen(a.id, a.start, a.ende, a.out, a.groesse)
    print(f'{a.out}')
    print(f'  Datei beginnt bei Master {beginn:.2f}s · gewuenschter Start liegt '
          f'{versatz:.2f}s hineinversetzt · {n} Pakete · {bilanz}')
