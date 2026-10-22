#!/usr/bin/env python3
"""Einblendungen nachbessern, immer gleich und nachvollziehbar.

Seine Anpassungen gehen sonst bei jedem neuen Transkript verloren, weil
Whisper nicht deterministisch ist. Was hier steht, sind **seine stehenden
Vorgaben**, als Code statt als Notiz:

* **Woerter ohne Dauer bekommen eine.** Whisper gibt manchen Woertern
  `start == end`; die fielen bis zum 21.10.2026 stumm aus dem Bild
  (`FUCKING` war so verschwunden). Der Renderer zeigt sie inzwischen, aber
  ohne Dauer leuchtet die gelbe Hervorhebung nie auf.
* **Seine Abschlussfrage steht in EINER Einblendung**, mitsamt Fragezeichen
  — seine Ansage vom 21.10.: *„for you habe ich doch gesagt, soll zusammen
  in einer Einblendung mit Fragezeichen."* Die Zeile ist dabei breiter als
  die Preset-Schranke von 72 %; sie passt aufs Bild, und seine Ansage gilt.

    python3 video/cues_nachbessern.py roh.json fertig.json
"""
import json
import sys
from pathlib import Path

# Paare, die zusammengelegt werden: (Text der ersten, Text der zweiten).
ZUSAMMEN = [("meaningful for", "you?")]


def dauer_heilen(cues):
    """Wort ohne Dauer borgt sich Zeit vom naechsten Wort derselben Zeile."""
    n = 0
    for c in cues:
        ws = c["woerter"]
        for i, w in enumerate(ws):
            if w["end"] - w["start"] < 0.01 and i + 1 < len(ws):
                folge = ws[i + 1]
                spanne = folge["end"] - folge["start"]
                if spanne > 0.2:
                    schnitt = folge["start"] + min(0.25, spanne * 0.4)
                    w["end"] = schnitt
                    folge["start"] = schnitt
                    n += 1
    return n


def zusammenlegen(cues):
    n = 0
    for erst, zweit in ZUSAMMEN:
        i = 0
        while i < len(cues) - 1:
            if cues[i]["text"] == erst and cues[i + 1]["text"] == zweit:
                a, b = cues[i], cues[i + 1]
                cues[i:i + 2] = [{"start": a["start"], "end": b["end"],
                                  "text": f'{a["text"]} {b["text"]}',
                                  "woerter": a["woerter"] + b["woerter"],
                                  "grund": b["grund"]}]
                n += 1
            i += 1
    return n


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cues = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    z = zusammenlegen(cues)
    h = dauer_heilen(cues)
    Path(sys.argv[2]).write_text(json.dumps(cues, ensure_ascii=False, indent=1),
                                 encoding="utf-8")
    print(f"{len(cues)} Einblendungen · {z} zusammengelegt · "
          f"{h} Woerter ohne Dauer geheilt -> {sys.argv[2]}")


if __name__ == "__main__":
    main()
