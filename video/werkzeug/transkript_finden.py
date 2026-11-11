#!/usr/bin/env python3
"""Phrase -> Zeitstempel in einem Transkript, und eine lesbare Verdichtung.

Warum es das gibt: Kapitelmarken und Zitatzeilen duerfen nicht geschaetzt
werden. Die Segmentgrenzen eines Whisper-Transkripts liegen beliebig im
Satz, also reicht es nicht, das Segment zu suchen, das eine Phrase enthaelt
-- gesucht wird die Zeichenposition im fortlaufenden Text, und von dort aus
das Segment, in dem das Wort faellt.

    python3 -I transkript_finden.py pfad.md "erste phrase" "zweite phrase"
    python3 -I transkript_finden.py pfad.md --verdichten 30 > lesbar.md

Die Verdichtung fasst Segmente zu Bloecken von N Sekunden zusammen. Sie ist
zum Lesen da, nicht zum Messen: eine Blockzeit ist bis zu N Sekunden zu
frueh. Wer eine Marke setzt, nimmt die Suche, nicht die Verdichtung.

Erwartetes Format je Zeile: **[H:MM:SS]** Text   (auch [MM:SS])
"""
import re
import sys

ZEILE = re.compile(r"^\*\*\[(?:(\d+):)?(\d+):(\d+)\]\*\*\s*(.*)$")


def lesen(pfad):
    segs = []
    for zeile in open(pfad, encoding="utf-8"):
        m = ZEILE.match(zeile)
        if not m:
            continue
        h, mi, s, text = m.groups()
        sek = int(h or 0) * 3600 + int(mi) * 60 + int(s)
        segs.append((sek, text.strip()))
    if not segs:
        sys.exit(f"keine Segmente in {pfad} -- anderes Format?")
    return segs


def hms(s):
    return f"{s // 3600}:{s // 60 % 60:02d}:{s % 60:02d}"


def suchen(segs, phrasen):
    """Zeichenindex ueber den ganzen Text, damit die Phrase exakt sitzt."""
    voll, zeiten = [], []
    for sek, text in segs:
        voll.append(text)
        zeiten.extend([sek] * (len(text) + 1))
    text = " ".join(voll)
    klein = text.lower()
    fehlend = 0
    for p in phrasen:
        pos = klein.find(p.lower())
        if pos < 0:
            print(f"NICHT GEFUNDEN: {p}")
            fehlend += 1
            continue
        n = klein.count(p.lower())
        warnung = "  ACHTUNG: mehrdeutig" if n > 1 else ""
        print(f"{hms(zeiten[pos])}  (n={n})  {p}{warnung}")
    return fehlend


def verdichten(segs, schritt):
    block, puffer = None, []
    for sek, text in segs:
        b = sek // schritt
        if block is None:
            block = b
        if b != block:
            print(f"[{hms(block * schritt)}] {' '.join(puffer)}\n")
            puffer, block = [], b
        puffer.append(text)
    if puffer:
        print(f"[{hms(block * schritt)}] {' '.join(puffer)}\n")


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    segs = lesen(argv[1])
    if argv[2] == "--verdichten":
        schritt = int(argv[3]) if len(argv) > 3 else 30
        verdichten(segs, schritt)
        return 0
    return 1 if suchen(segs, argv[2:]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
