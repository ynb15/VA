#!/usr/bin/env python3
"""Entscheidet am Wortlaut, ob seine Zeitmarkenliste zu diesem Video gehoert.

Hintergrund: im Slack-Thread `1788525418.826269` steht seine Liste
(15.09.2026 17:01) unmittelbar nach dem Link auf `q3_kLgYIXGQ` (14.09. 22:20)
— aber einen Tag spaeter, und oben im selben Thread steht ein zweites Video
(`ud5kr_LoqU4`, die Rob-Paddock-Folge seines eigenen Kanals). Gegen die
Kapitel allein ist die Zuordnung **plausibel, nicht belegt**: 1 von 7 Marken
stimmt woertlich mit einem Kapiteltitel ueberein, und 4 von 6 Stichworten
kommen auf der Videoseite ueberhaupt nicht vor.

Dieses Skript beantwortet die Frage am Transkript, mit **vorab
festgelegter** Schwelle — damit die Entscheidung nicht davon abhaengt, was
herauskommt. Genau dieser Fehler (eine Lesart fuer eine Tatsache halten) hat
am 21.10. an zwei Stellen Arbeit gekostet.

    python3 video/garden-pruefplan.py <transkript>

Frisst das Markdown-Format aus `yt-transkript.py` (`**[HH:MM:SS]** text`),
SRT und VTT. Rueckgabe 0 = gehoert zu diesem Video, 1 = gehoert woanders
hin, 2 = unentschieden.
"""
import re
import sys
from pathlib import Path

# --- vorab festgelegt, vor dem ersten Blick ins Transkript ----------------
# Fenster um seine Marke. Asymmetrisch, weil eine Marke eher der Anfang des
# Schnitts ist als dessen Mitte: er schreibt auf, wo er anfangen will.
VOR, NACH = 30, 120
WEIT = 180            # zweites, weiteres Fenster, nur zur Einordnung

# Je Marke: die Frage, die das Transkript beantworten muss, und die Woerter,
# an denen sie sich entscheidet. `name=True` markiert einen Eigennamen —
# der ist selten, also ist ein Treffer stark und ein Fehlen aussagekraeftig.
MARKEN = [
    (960,  "16:00 Movie",
     "Rahmt er seine Entscheidungen als Film bzw. fragt er, was der Held taete?",
     [r"\bhero\b", r"\bmovie\b", r"\bfilm\b", r"\bmain character\b",
      r"\bprotagonist\b"], False),
    (2440, "40:40 Joe Hudson",
     "Faellt der Name Joe Hudson?",
     [r"\bjoe hudson\b", r"\bhudson\b"], True),
    (2460, "41:00 Integration",
     "Spricht er ueber Integration (nach Retreat/Erfahrung)?",
     [r"\bintegrat"], False),
    (2640, "44:00 Workaholism",
     "Spricht er ueber Arbeitssucht?",
     [r"\bworkahol", r"\bwork addict", r"\baddicted to work\b"], False),
    (3623, "1:00:23 Hormozi",
     "Faellt der Name Hormozi?",
     [r"\bhormozi\b", r"\balex hormozi\b"], True),
    (3960, "1:06:00 Confidence",
     "Spricht er ueber Selbstvertrauen?",
     [r"\bconfidence\b", r"\bconfident\b", r"\bself-?confiden"], False),
    (4860, "1:21:00 My Why",
     "Nennt er sein Warum / seinen Antrieb?",
     [r"\bmy why\b", r"\bthe why\b", r"\breason why i\b", r"\bgive a voice\b",
      r"\bmission\b", r"\bpurpose\b"], False),
]
# Entscheidungsregel, ebenfalls vorab:
JA, NEIN = 5, 2       # >=5 Treffer: gehoert hierher. <=2: gehoert woanders hin.


def transkript_lesen(pfad):
    """-> [(sekunde, text)] aus Markdown, SRT oder VTT."""
    roh = Path(pfad).read_text(encoding="utf-8", errors="replace")
    cues = []

    def sek(h, m, s):
        return int(h) * 3600 + int(m) * 60 + int(s)

    # yt-transkript.py: **[01:02:03]** Text
    for h, m, s, text in re.findall(
            r"\*\*\[(\d\d):(\d\d):(\d\d)\]\*\*\s*(.+)", roh):
        cues.append((sek(h, m, s), text))
    if cues:
        return cues
    # SRT / VTT: 01:02:03,456 --> ...
    for h, m, s, body in re.findall(
            r"(\d\d):(\d\d):(\d\d)[,.]\d+\s*-->[^\n]*\n(.*?)(?=\n\s*\n|\Z)",
            roh, re.S):
        text = re.sub(r"<[^>]+>", " ", body)
        cues.append((sek(h, m, s), re.sub(r"\s+", " ", text).strip()))
    return cues


def fenster(cues, mitte, vor, nach):
    return " ".join(t for s, t in cues if mitte - vor <= s <= mitte + nach).lower()


def naechster_treffer(cues, muster):
    """Wo im ganzen Transkript kommt das Wort sonst vor?"""
    for s, t in cues:
        for m in muster:
            if re.search(m, t.lower()):
                return s
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pfad = sys.argv[1]
    cues = transkript_lesen(pfad)
    if not cues:
        sys.exit(f"keine Zeitmarken in {pfad} erkannt")
    dauer = cues[-1][0]
    print(f"{pfad} — {len(cues)} Zeitmarken, bis {dauer // 60}:{dauer % 60:02d}\n")
    print(f"Fenster: -{VOR} s / +{NACH} s um die Marke "
          f"(weit: ±{WEIT} s). Schwelle vorab: ≥{JA} ja, ≤{NEIN} nein.\n")

    treffer = namen_treffer = namen_gesamt = 0
    zeilen = []
    for marke, name, frage, muster, ist_name in MARKEN:
        if ist_name:
            namen_gesamt += 1
        eng = fenster(cues, marke, VOR, NACH)
        weit = fenster(cues, marke, WEIT, WEIT)
        if any(re.search(m, eng) for m in muster):
            stand, ok = "ja", True
        elif any(re.search(m, weit) for m in muster):
            stand, ok = f"nur ±{WEIT}s", True
        else:
            woanders = naechster_treffer(cues, muster)
            stand = ("nein" if woanders is None
                     else f"nein (sonst bei {woanders // 60}:{woanders % 60:02d})")
            ok = False
        if marke > dauer:
            stand, ok = "AUSSERHALB der Laufzeit", False
        if ok:
            treffer += 1
            if ist_name:
                namen_treffer += 1
        zeilen.append((name + (" *" if ist_name else ""), stand, frage))

    breite = max(len(z[0]) for z in zeilen)
    for n, stand, frage in zeilen:
        print(f"  {n:<{breite}}  {stand:<28}  {frage}")
    print(f"\n  * Eigenname — selten, darum aussagekraeftig: "
          f"{namen_treffer} von {namen_gesamt} gefunden.")
    print(f"\n  Treffer gesamt: {treffer} von {len(MARKEN)}")

    if treffer >= JA:
        print("\n  URTEIL: die Liste gehoert zu diesem Video. Seine Auswahl bauen,\n"
              "  nicht eine eigene.")
        return 0
    if treffer <= NEIN:
        print("\n  URTEIL: die Liste gehoert NICHT zu diesem Video — dann zur\n"
              "  Rob-Paddock-Folge (`ud5kr_LoqU4`) aus demselben Thread.\n"
              "  Die Kandidatenliste hier neu aus dem Transkript bauen.")
        return 1
    print("\n  URTEIL: unentschieden. Vor dem Bauen dasselbe Skript gegen das\n"
          "  Transkript von `ud5kr_LoqU4` laufen lassen und vergleichen —\n"
          "  wer mehr Treffer hat, bekommt die Liste.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
