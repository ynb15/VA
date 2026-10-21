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

Zwei Stufen: `GROB` (Cape Town, South Africa) ist **erlaubt** und wird nur
nachrichtlich gezaehlt; `ORTE` ist feiner als die Stadt und schlaegt an.

Ausgabe: je Treffer Zeitmarke, Wort und die Zeile. Rueckgabe 1, wenn
etwas gefunden wurde — so faellt es in einem Lauf auf.
"""
import re, sys
from pathlib import Path

# Zwei Stufen, nach seiner Praezisierung vom 21.10.2026: *„Cape Town oder
# South Africa — ich moechte es halt nur nicht genauer veroeffentlichen."*
# Stadt und Land duerfen also fallen; alles Feinere nicht.
GROB = [
    "cape town", "kapstadt", "south africa", "suedafrika", "südafrika",
    "western cape", "table mountain", "tafelberg",
]
# Genauer als die Stadt — das faellt raus.
ORTE = [
    "scarborough", "kommetjie", "misty cliffs", "noordhoek", "fish hoek",
    "simon's town", "simons town", "muizenberg", "chapman's peak",
    "chapmans peak", "camps bay", "hout bay", "sea point", "constantia",
    "stellenbosch", "glencairn", "witsand", "soetwater", "red hill",
    "ocean view", "masiphumelele", "sun valley", "capri village",
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
    """-> (treffer, grob). `treffer` muss raus, `grob` ist nur zur Kenntnis."""
    treffer, grob = [], []
    for marke, z in zeilen(pfad):
        klein = z.lower()
        for ort in ORTE:
            if ort in klein:
                treffer.append((marke, ort, z))
        for ort in GROB:
            if ort in klein:
                grob.append((marke, ort, z))
        for muster, name in MUSTER:
            if re.search(muster, z, re.I):
                treffer.append((marke, name, z))
    return treffer, grob


def main(argv):
    gesamt = 0
    for pfad in argv:
        treffer, grob = pruefen(pfad)
        gesamt += len(treffer)
        if treffer:
            print(f"\n{pfad} — {len(treffer)} Stelle(n), die raus muessen:")
            for marke, was, z in treffer:
                print(f"  {marke or '?':>12}  [{was}]  {z}")
        if grob:
            print(f"\n{pfad} — {len(grob)} Mal Stadt/Land (erlaubt, nur zur "
                  f"Kenntnis):")
            for marke, was, z in grob:
                print(f"  {marke or '?':>12}  ({was})  {z}")
        else:
            print(f"{pfad} — sauber")
    if gesamt:
        print(f"\n{gesamt} Stelle(n) gefunden. Pruefen, im Zweifel rausschneiden.")
    return 1 if gesamt else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
