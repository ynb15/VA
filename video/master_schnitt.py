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
    quelle = DriveDatei(bestaetigte_url(file_id), groesse=groesse)
    ein = av.open(quelle)
    v_ein = next(s for s in ein.streams if s.type == 'video')
    a_ein = next(s for s in ein.streams if s.type == 'audio')

    aus = av.open(ziel, 'w')
    v_aus = aus.add_stream_from_template(v_ein)
    a_aus = aus.add_stream_from_template(a_ein)

    # Auf das Schluesselbild vor dem Fensterbeginn setzen.
    ein.seek(int(start / v_ein.time_base), stream=v_ein)

    erster_pts = {}
    versatz_ts = None
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
        # Die Zeitstempel auf null ziehen. Vorher behielt das Fenster die
        # Uhr des Masters: eine Datei, die bei Master 5775 anfing, meldete
        # start_time=5775 und duration=75. Jedes Werkzeug danach rechnet
        # aber ab null — `--start 13` suchte dann eine Stelle, die vor dem
        # ersten Bild liegt, und ffmpeg nahm stillschweigend den Anfang.
        # Am 22.10. sind daraus drei Renderings mit falschem Ausschnitt
        # geworden, die im Standbild richtig aussahen.
        # Ein gemeinsamer Versatz fuer beide Spuren, sonst laufen Bild und
        # Ton auseinander.
        if versatz_ts is None:
            versatz_ts = t
        schieben = int(round(versatz_ts / pkt.time_base))
        if pkt.pts is not None:
            pkt.pts -= schieben
        if pkt.dts is not None:
            pkt.dts -= schieben
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
    print(f'  Datei laeuft ab 0 (entspricht Master {beginn:.2f}s) · gewuenschter '
          f'Start liegt {versatz:.2f}s hineinversetzt · {n} Pakete · {bilanz}')
