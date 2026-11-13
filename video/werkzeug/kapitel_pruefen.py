#!/usr/bin/env python3
"""Einen Kapitelblock pruefen, bevor er in eine Beschreibung geht.

    python3 -I kapitel_pruefen.py kapitel.txt

Prueft, was YouTube still verschluckt:
  * `0:05:30` unter einer Stunde -- wird nicht erkannt, muss `5:30` heissen
  * `60:36` ab einer Stunde      -- wird nicht erkannt, muss `1:00:36` heissen
  * erste Marke ist nicht 0:00
  * Marken nicht aufsteigend
  * Abstand unter 10 s
  * weniger als drei Marken

Beide Formatfehler sind mir schon passiert, in beide Richtungen:
am 26.10. `60:36` statt `1:00:36` (15 tote Kapitel, zwei Tage online),
am 13.11. `0:05:30` statt `5:30`. Ein Format, das im Werkzeug stimmt,
stimmt nicht automatisch im Zielfeld.
"""
import re
import sys

ZEILE = re.compile(r"^\s*(?:(\d+):)?(\d{1,2}):(\d{2})\s+(\S.*)$")


def main(pfad):
    marken, fehler = [], []
    for nr, roh in enumerate(open(pfad, encoding="utf-8"), 1):
        if not roh.strip():
            continue
        m = ZEILE.match(roh)
        if not m:
            fehler.append(f"Zeile {nr}: keine Kapitelzeile -- {roh.strip()[:60]}")
            continue
        h, mi, s, text = m.groups()
        sek = (int(h) if h else 0) * 3600 + int(mi) * 60 + int(s)
        marke = roh.strip().split()[0]
        if h is not None and sek < 3600:
            fehler.append(f"Zeile {nr}: `{marke}` unter einer Stunde mit fuehrender "
                          f"Stunde -- YouTube erkennt das nicht, richtig ist "
                          f"`{sek//60}:{sek%60:02d}`")
        if h is None and int(mi) >= 60:
            fehler.append(f"Zeile {nr}: `{marke}` ab einer Stunde ohne Stundenfeld -- "
                          f"richtig ist `{sek//3600}:{sek//60%60:02d}:{sek%60:02d}`")
        marken.append((nr, sek, marke, text))

    if marken and marken[0][1] != 0:
        fehler.append(f"Zeile {marken[0][0]}: erste Marke ist `{marken[0][2]}`, "
                      f"YouTube verlangt 0:00")
    if len(marken) < 3:
        fehler.append(f"nur {len(marken)} Marken -- YouTube verlangt mindestens 3")
    for (n1, s1, m1, _), (n2, s2, m2, _) in zip(marken, marken[1:]):
        if s2 <= s1:
            fehler.append(f"Zeile {n2}: `{m2}` laeuft nicht nach `{m1}`")
        elif s2 - s1 < 10:
            fehler.append(f"Zeile {n2}: `{m2}` nur {s2-s1} s nach `{m1}` -- "
                          f"YouTube verlangt mindestens 10")

    for f in fehler:
        print("FEHLER:", f)
    print(f"{len(marken)} Marken geprueft, {len(fehler)} Fehler.")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
