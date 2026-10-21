#!/usr/bin/env python3
"""Untertitel und Transkripte auf Ortsangaben absuchen.

Seine Regel, aus seinem eigenen Arbeits-Slack (02.09.2026, an seine
Cutterin): *„Vielleicht doch den Scarborough-Teil rausnehmen in diesem
Short? Gewisse Menschen muessen nicht so easy wissen wo wir wohnen."*

Kein Short und kein Clip darf verraten, wo er wohnt — im Bild, im Ton und
im Untertitel. Dieses Skript deckt den Untertitel ab, also den Teil, der
sich lesen laesst. **Das Bild prueft es nicht** (Fassaden, Aussicht,
Schilder) — das bleibt Augenarbeit vor jeder Abnahme.

    python3 video/ortscheck.py datei.srt [weitere ...]

Ausgabe: je Treffer Zeitmarke, Wort und die Zeile. Rueckgabe 1, wenn
etwas gefunden wurde — so faellt es in einem Lauf auf.
"""
import re, sys
from pathlib import Path

# Sein Wohnort und sein Umfeld. Erweitern, sobald etwas auffaellt —
# lieber ein Fehlalarm zu viel als eine Adresse im Bild.
ORTE = [
    "scarborough", "cape town", "kapstadt", "kommetjie", "misty cliffs",
    "noordhoek", "fish hoek", "simon's town", "simons town", "muizenberg",
    "chapman's peak", "chapmans peak", "table mountain", "tafelberg",
    "camps bay", "hout bay", "sea point", "constantia", "stellenbosch",
    "western cape", "south africa", "suedafrika", "südafrika",
]
# Formen, die eine Adresse verraten, ohne einen bekannten Namen zu nennen.
MUSTER = [
    (r"\b\d{1,4}\s+[A-Z][a-z]+\s+(street|st|road|rd|avenue|ave|drive|dr|lane|ln)\b",
     "Hausnummer + Strassenname"),
    (r"\bwe live in\b|\bi live in\b|\bour house in\b|\bmy house in\b",
     "wohnt-in-Formel"),
]


def zeilen(pfad):
    """SRT oder reiner Text -> [(zeitmarke, zeile)]."""
    txt = Path(pfad).read_text(encoding="utf-8", errors="replace")
    marke = ""
    for zeile in txt.splitlines():
        z = zeile.strip()
        if "-->" in z:
            marke = z.split("-->")[0].strip()
            continue
        if z and not z.isdigit():
            yield marke, z


def pruefen(pfad):
    treffer = []
    for marke, z in zeilen(pfad):
        klein = z.lower()
        for ort in ORTE:
            if ort in klein:
                treffer.append((marke, ort, z))
        for muster, name in MUSTER:
            if re.search(muster, z, re.I):
                treffer.append((marke, name, z))
    return treffer


def main(argv):
    gesamt = 0
    for pfad in argv:
        treffer = pruefen(pfad)
        gesamt += len(treffer)
        if treffer:
            print(f"\n{pfad} — {len(treffer)} Stelle(n):")
            for marke, was, z in treffer:
                print(f"  {marke or '?':>12}  [{was}]  {z}")
        else:
            print(f"{pfad} — sauber")
    if gesamt:
        print(f"\n{gesamt} Stelle(n) gefunden. Pruefen, im Zweifel rausschneiden.")
    return 1 if gesamt else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
