#!/usr/bin/env python3
"""Eingebrannte Untertitel in einem Fremdvideo finden — und die freien
Strecken ausgeben.

Warum das sein muss: Einspieler aus Trailern tragen oft eingebrannte
Untertitel. Unter den eigenen Einblendungen sieht das unbrauchbar aus.
Am 22.10. habe ich versucht, sie an einem Kontaktabzug mit 200 Pixel
Breite abzulesen, und lag um Sekunden daneben - in einem fertigen
Einspieler stand dann "Where are your mum and dad?" im Bild.

**Ein Kontaktabzug beantwortet, WAS zu sehen ist. Er beantwortet nicht,
ob an einer bestimmten Sekunde Text steht.** Dafuer braucht es eine
Messung ueber jedes Bild.

Verfahren: im unteren Teil des Filmbildes die nahezu weissen Pixel mit
geringer Farbspreizung zaehlen (so sieht Untertitelschrift aus, egal
welche Schrift). Liegt der Anteil ueber der Schwelle, steht dort Text.

    python3 video/untertitel_finden.py datei.mp4 \
            --feld 2138:961:242:153 --takt 0.5 --mindestens 5
"""
import argparse, subprocess, sys
import numpy as np


def bilder(pfad, feld, takt):
    b, h, x, y = feld
    r = subprocess.run(
        ['ffmpeg', '-nostdin', '-v', 'error', '-i', pfad,
         '-vf', f'crop={b}:{h}:{x}:{y},fps={1/takt},format=gray',
         '-f', 'rawvideo', '-'], capture_output=True)
    roh = np.frombuffer(r.stdout, dtype=np.uint8)
    n = len(roh) // (b * h)
    return roh[:n * b * h].reshape(n, h, b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('datei')
    ap.add_argument('--feld', required=True,
                    help='Filmbild als breite:hoehe:x:y')
    ap.add_argument('--takt', type=float, default=0.5,
                    help='Abstand der Proben in Sekunden')
    ap.add_argument('--band', type=float, default=0.72,
                    help='ab welchem Anteil der Hoehe gesucht wird')
    ap.add_argument('--schwelle', type=float, default=0.0025,
                    help='Anteil heller Pixel, ab dem Text angenommen wird')
    ap.add_argument('--mindestens', type=float, default=4.0,
                    help='kuerzere freie Strecken werden nicht gemeldet')
    ap.add_argument('--rand', type=float, default=0.5,
                    help='Sicherheitsabstand zu jeder Textstelle')
    a = ap.parse_args()

    b, h, x, y = (int(v) for v in a.feld.split(':'))
    folge = bilder(a.datei, (b, h, x, y), a.takt)
    y0 = int(h * a.band)
    band = folge[:, y0:, :].astype(np.int16)

    # Helle Pixel allein reichen nicht: ein Sonnenuntergang hat ein helles
    # unteres Band und wurde am 22.10. als Text gemeldet. Untertitelschrift
    # ist hell UND hat unmittelbar daneben etwas Dunkles - Kontur oder
    # Hintergrund. Ein heller Himmel hat das nicht.
    dunkel_daneben = band.copy()
    for v in range(1, 12):
        dunkel_daneben[:, :, v:] = np.minimum(dunkel_daneben[:, :, v:],
                                              band[:, :, :-v])
        dunkel_daneben[:, :, :-v] = np.minimum(dunkel_daneben[:, :, :-v],
                                               band[:, :, v:])
    schrift = (band > 215) & (dunkel_daneben < 110)
    anteil = schrift.mean(axis=(1, 2))
    text = anteil > a.schwelle

    print(f'{len(folge)} Proben im Abstand {a.takt}s '
          f'({len(folge)*a.takt:.0f}s), Band ab y={y0}', file=sys.stderr)

    # Freie Strecken, mit Sicherheitsabstand zu jeder Textstelle.
    frei, start = [], None
    for i, t in enumerate(text):
        if not t and start is None:
            start = i
        elif t and start is not None:
            frei.append((start, i)); start = None
    if start is not None:
        frei.append((start, len(text)))

    print('freie Strecken (Sekunden im Video):')
    for v, bb in frei:
        von, bis = v * a.takt + a.rand, bb * a.takt - a.rand
        if bis - von >= a.mindestens:
            print('  %7.1f - %7.1f   %5.1f s' % (von, bis, bis - von))


if __name__ == '__main__':
    main()
