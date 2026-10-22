#!/usr/bin/env python3
"""Pausen fuer die Kuerzung auswaehlen - nach gemessener Sichtbarkeit.

Eine Pause innerhalb derselben Kameraeinstellung zu kuerzen ergibt einen
Sprungschnitt. Unsichtbar wird er nur, wenn das Bild am Ausstieg und am
Wiedereinstieg fast gleich aussieht. Darum wird hier nicht nach Laenge
ausgewaehlt, sondern nach der gemessenen Bilddifferenz im Kopfbereich
zwischen dem letzten gezeigten und dem ersten folgenden Bild. Der Ruhepegel
daneben (Differenz zweier benachbarter Bilder an derselben Stelle) sagt,
wieviel Bewegung dort ohnehin im Bild ist.

    python3 video/pausen_waehlen.py clip.mp4 --budget 4.7 [--puffer 0.15]

Gibt die ausgewaehlten Schnitte als JSON-Liste aus, aufsteigend sortiert.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageChops


def silben(video, pegel="-38dB", dauer=0.28):
    roh = subprocess.run(["ffmpeg", "-nostdin", "-i", video, "-af",
                          f"silencedetect=noise={pegel}:d={dauer}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    stillen, start = [], None
    for zeile in roh.splitlines():
        if "silence_start:" in zeile:
            start = float(zeile.split("silence_start:")[1].split()[0])
        elif "silence_end:" in zeile and start is not None:
            stillen.append((start, float(zeile.split("silence_end:")[1].split()[0])))
            start = None
    # unmittelbar aneinandergrenzende Stillen zusammenfassen
    zusammen = []
    for a, b in stillen:
        if zusammen and a - zusammen[-1][1] < 0.02:
            zusammen[-1] = (zusammen[-1][0], b)
        else:
            zusammen.append((a, b))
    return zusammen


def bild(video, t, pfad):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-ss", f"{t:.4f}",
                    "-i", video, "-frames:v", "1", "-vf", "scale=360:-1",
                    pfad, "-y"], check=True)
    return Image.open(pfad).convert("L")


def unterschied(a, b):
    """Mittlere Helligkeitsdifferenz im oberen Bildteil - dort sitzt der Kopf."""
    w, h = a.size
    kasten = (0, 0, w, int(h * 0.55))
    d = ImageChops.difference(a.crop(kasten), b.crop(kasten))
    hist = d.histogram()
    return sum(j * hist[j] for j in range(256)) / sum(hist)


def feinsuche(a, s, e, tmp):
    """Innerhalb einer Pause die Paarung suchen, bei der das Bild am besten passt.

    Feste Puffer treffen die Stelle nur zufaellig. Hier werden alle Bilder der
    Pause einmal geholt und dann jede Paarung verglichen, die genug Gewinn
    bringt. Gewaehlt wird die mit der kleinsten Bilddifferenz.
    """
    schritt = 1 / a.fps
    rand = 0.10                      # so nah darf kein Schnitt an ein Wort
    ziel = max(a.mindest, (e - s - 2 * rand) * 0.6)
    zeiten, t = [], s + rand
    while t <= e - rand + 1e-6:
        zeiten.append(round(t, 4))
        t += schritt
    if len(zeiten) < 2:
        return None
    bilder = {z: bild(a.video, z, os.path.join(tmp, f"f{i}.png"))
              for i, z in enumerate(zeiten)}
    best = None
    for i, aus in enumerate(zeiten):
        for ein in zeiten[i + 1:]:
            if ein - aus < ziel:
                continue
            d = unterschied(bilder[aus], bilder[ein])
            if best is None or d < best[0]:
                best = (d, aus, ein)
    if best is None:
        return None
    d, aus, ein = best
    nachbar = zeiten[zeiten.index(aus) + 1]
    return {"von": round(aus, 3), "bis": round(ein, 3),
            "gewinn": round(ein - aus, 3), "sprung": round(d, 2),
            "ruhe": round(unterschied(bilder[aus], bilder[nachbar]), 2)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--budget", type=float, required=True,
                   help="soviele Sekunden muessen zusammenkommen")
    p.add_argument("--puffer", type=float, default=0.15,
                   help="soviel Pause bleibt an beiden Seiten stehen")
    p.add_argument("--ab", type=float, default=4.0, help="davor nicht schneiden")
    p.add_argument("--bis", type=float, default=0.0, help="danach nicht schneiden (0 = Ende)")
    p.add_argument("--fps", type=float, default=30.0)
    p.add_argument("--mindest", type=float, default=0.25,
                   help="kleinere Gewinne lohnen den Schnitt nicht")
    p.add_argument("--fein", action="store_true",
                   help="Ein- und Ausstieg innerhalb der Pause suchen, "
                        "statt feste Puffer zu nehmen")
    a = p.parse_args()

    ende = a.bis or float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", a.video], capture_output=True, text=True).stdout.strip())

    gemessen = []
    with tempfile.TemporaryDirectory() as tmp:
        for s, e in silben(a.video):
            aus, ein = s + a.puffer, e - a.puffer
            if aus < a.ab or ein > ende or ein - aus < a.mindest:
                continue
            if a.fein:
                best = feinsuche(a, s, e, tmp)
                if best:
                    gemessen.append(best)
                continue
            f_aus = bild(a.video, aus, os.path.join(tmp, "a.png"))
            f_ein = bild(a.video, ein, os.path.join(tmp, "b.png"))
            f_ruhe = bild(a.video, aus + 1 / a.fps, os.path.join(tmp, "c.png"))
            gemessen.append({"von": round(aus, 3), "bis": round(ein, 3),
                             "gewinn": round(ein - aus, 3),
                             "sprung": round(unterschied(f_aus, f_ein), 2),
                             "ruhe": round(unterschied(f_aus, f_ruhe), 2)})

    gemessen.sort(key=lambda g: g["sprung"])
    gewaehlt, summe = [], 0.0
    for g in gemessen:
        if summe >= a.budget:
            break
        gewaehlt.append(g)
        summe += g["gewinn"]

    print(f"{'Sprung':>7} {'Ruhe':>6} {'von':>8} {'bis':>8} {'Gewinn':>7}  gewaehlt",
          file=sys.stderr)
    for g in gemessen:
        marke = "ja" if g in gewaehlt else ""
        print(f"{g['sprung']:7.2f} {g['ruhe']:6.2f} {g['von']:8.2f} {g['bis']:8.2f} "
              f"{g['gewinn']:7.2f}  {marke}", file=sys.stderr)
    print(f"\ngewaehlt: {len(gewaehlt)} Schnitte, {summe:.2f} s "
          f"(Budget {a.budget:.2f} s), schlechtester Sprung "
          f"{max((g['sprung'] for g in gewaehlt), default=0):.2f}", file=sys.stderr)

    gewaehlt.sort(key=lambda g: g["von"])
    print(json.dumps(gewaehlt, indent=1))


if __name__ == "__main__":
    main()
