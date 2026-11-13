#!/usr/bin/env python3
"""Was ist heute fällig, und was fehlt dafür?

Läuft im täglichen Sweep. Gibt aus, was ich wissen muss, um Aufträge
auszulösen — und sonst nichts. Keine Bewertung, das ist mein Teil.

    python3 bin/plan-pruefen.py            # heute
    python3 bin/plan-pruefen.py 2026-11-01 # ein anderer Tag
"""
import datetime, re, sys, os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
heute = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 \
        else datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).date()

PODCASTS = {
    datetime.date(2026, 10, 25): "Scott Aaronson",
    datetime.date(2026, 10, 31): "Kyle Kingsbury",
    datetime.date(2026, 11, 13): "Rick Strassman",
    datetime.date(2026, 11, 15): "Ken Stern",
    datetime.date(2026, 11, 27): "Matt Defina",
    datetime.date(2026, 12,  4): "Marian Goodell",
}
# Ausnahmen: Folge -> Fristen, die fuer sie nicht gelten (von ihm so entschieden)
ENTFAELLT = {"Kyle Kingsbury": {5}}   # Thumbnail macht er selbst ueber ChatGPT, 21.10.

# Angehaltene Folgen: Folge -> (frei ab, worauf gewartet wird).
# Von ihm so entschieden. Fristen davor werden nicht als ueberfaellig gemeldet
# — sie sind nicht verpasst, sie sind ausgesetzt. Die Zeile bleibt sichtbar,
# damit ein Halt nicht aus dem Blick geraet.
WARTET = {}   # Kingsbury-Pause am 26.10. abgelaufen, siehe BEOBACHTEN unten

# Dinge, die ich beobachte, weil ihr Eintreffen eine Frist freigibt. Steht hier,
# damit ich es nicht im Kopf tragen muss — und damit es nicht aufhoert, nur
# weil eine Pause ausgelaufen ist.
BEOBACHTEN = [
    ("Kingsbury", "Endfassung ANGEKOMMEN am 30.10. (39,25 GB, 129:50). "
     "Neun Shorts liegen fertig und bestehen die Abnahme; drei Entscheidungen "
     "bei ihm. Offen: 55 Min der Folge ohne Transkript \u2014 eine Niedrig"
     "aufloesung ab 74:40 ist bei Christoph angefragt."),
    ("Aaronson", "DREI fertige Shorts liegen seit dem 26.10. bei ihm und "
     "waren bis zum 03.11. nicht im Kalender: AI2027 (08:54), How safe is AI "
     "Fassung 2 (09:35, 58,0 s), What do you believe in? (10:27). Jetzt auf "
     "03., 04. und 05.11. gelegt — das ist MEIN Vorschlag, nicht seine "
     "Festlegung. Abnahme fehlt bei allen drei."),
    ("Ken Stern", "Lauft. Transkript am 10.11. fertig (1760 Segmente, 105,6 Min, ueber drei Anker belegt), Auswahl am 10.11. nachts, Strassenname an drei Stellen stumm. Master 1RGq-Mw0QEm5jE2WMthKPkP5OHrXvmotF, dazu ein fertiges Meaning-Short (6150,1-6189,3) und zwei Thumbnails, die schon vorher dalagen. OFFEN: T-6 Paket, T-5 Thumbnails, T-3 Shorts. SEINE ANSAGE vom 10.11.: er will Ken NAECHSTE WOCHE veroeffentlichen. MEINE LESART, nicht seine: der 13.11. bleibt Rick. Ein Datum fasse ich nicht an."),
]

# Wer eine Folge schneidet, entscheidet die Folge, nicht die Frist.
# Seine Regel vom 21.10.: "alle Shorts zu Scott werden von ein und demselben
# Agenten bearbeitet, nacheinander." Also steht hier ein Name pro Folge, und
# die Schnittfristen holen ihn sich von dort. Zwei Namen an einer Frist waren
# der Grund, warum am 22.10. dieselbe Stelle zweimal geschnitten wurde.
SCHNITT = {
    "Scott Aaronson":  "content-shorts-2",
    "Kyle Kingsbury":  "content-schlicht",
    "Rick Strassman":  "content-cinematic",
    "Matt Defina":     "content-schlicht",
    "Marian Goodell":  "content-cinematic",
}

# Rueckkatalog: wer welche veroeffentlichte Folge hat. Dieselbe Regel 9 —
# und am 24.10. zum dritten Mal von mir verletzt, weil ich nicht nachgesehen
# habe, wer schon sitzt. Vor jeder Zuweisung: git log --all ueber alle
# Branches, und ein Ordner im Drive ist eine Folge, kein Dateiname.
RUECKKATALOG = {
    "Craig Makhosi / Into the Wild": "content-cinematic",   # seit ~20.10., Fassung E
    "Logan Gonzalez":                "content-schlicht",    # ab 24.10.
    "Francis Chouler":               "content-cinematic",
}

# Erledigte Fristen: Folge -> die T-Marken, die abgeschlossen sind.
# Eine erledigte Frist darf nicht als ueberfaellig gemeldet werden — sonst
# steht am Stichtag eine Falschmeldung neben der erledigten Arbeit. Dasselbe
# Muster wie WARTET: ein Zustand, den das Werkzeug nicht kennt, wird als der
# naechste aehnliche gemeldet.
ERLEDIGT = {
    "Scott Aaronson": {10, 8, 6, 5, 3, 2},   # veroeffentlicht 25.10., 2_CZfN2iOFk
    # T-6 (Titel, Beschreibung, Tags) liegt seit 22.10. auf claude/youtube-manager,
    # Commit 3704044: 15 Titel, 23 Tags, Beschreibung ohne Zeitstempel. Die
    # Zeitmarken fehlen absichtlich -- sie haengen an der Endfassung des Cutters
    # und waeren mit Rohzeiten gefuellt am Schnitttag falsch. Das Werkzeug hat es
    # drei Tage lang als UEBERFAELLIG gemeldet, weil es "fertig mit benannter
    # Luecke" nicht kennt: dasselbe Muster wie bei WARTET und beim Vorratszaehler.
    "Kyle Kingsbury": {6},
    # T-10 am 02.11. erfuellt, einen Tag vor der Frist: Transkript liegt,
    # 1641 Segmente ueber 120,9 Minuten (claude/content-cinematic).
    # T-8 am 04.11. erfuellt, ebenfalls einen Tag vor der Frist:
    # video/strassman-auswahl.md — zwei lange Stuecke mit Ersatz, elf Shorts,
    # alle ueber den Wortlaut verortet statt ueber eine Rechnung. Rohzeiten
    # ausdruecklich als vorlaeufig gekennzeichnet; gerendert wird nicht, weil
    # die 15,50-GB-Datei die ganze Sitzung ist und nicht die Folge.
    # T-6 am 06.11. erfuellt, aber nur im Chat geliefert; am 07.11. 04:47
    # nachgesichert als drafts/strassman/paket-t6.md (9631002, youtube-manager).
    # Beschreibung, 15 Titel, 15 Thumbnail-Zeilen, 22 Tags, Pinned Comment,
    # drei Clip-Kommentare; Kapitelmarken bewusst als benannte Luecke, weil das
    # Transkript Rohzeiten traegt. Ich hatte T-6 am Morgen als "nicht da"
    # gemeldet -- es lag im Chat, nicht im Zweig. Deshalb gefragt statt gemahnt.
    # T-5 am 08.11. erfuellt, 16 Minuten nach dem Auftrag: sechs Thumbnails
    # aus gemessenen Gesichtern (b12512d, claude/thumbnails), 1280x720.
    "Rick Strassman": {10, 8, 6, 5, 3, 2},
    "Ken Stern":      {10, 8, 6, 5, 3, 2},
}

# Entscheidungspunkte: Tag -> was an diesem Tag entschieden werden muss, und
# von wem. Steht hier, damit ich es nicht im Kopf tragen muss — was nicht im
# Repo steht, passiert nicht.
ENTSCHEIDUNG = {
    datetime.date(2026, 10, 28):
        "Liegt Kingsburys Endfassung heute abend nicht im Drive, haelt der "
        "31.10. nicht mehr.\n  Dann waehlt ER: Folge wandert, oder "
        "31.10. aus dem Rueckkatalog. Vorlage von mir.",
}

# wer: ein fester Name, oder "SCHNITT" fuer "der Agent dieser Folge"
VORLAUF = [(10, "Transkript",                   "SCHNITT"),
           (8,  "Clip- und Short-Auswahl",      "SCHNITT"),
           (6,  "Titel · Beschreibung · Tags",  "youtube-manager"),
           (5,  "Thumbnails",                   "thumbnails"),   # Kingsbury: entfaellt, er macht es selbst
           (3,  "Shorts gebaut",                "SCHNITT"),
           (2,  "Paket vollständig bei ihm",    "alfred")]

print(f"PLANKONTROLLE · {heute.strftime('%a %d.%m.%Y')} Kapstadt\n")

# 1 — was geht heute raus
zeile = None
if os.path.exists("plan/kalender.md"):
    muster = re.compile(r"^\| \w\w " + heute.strftime("%d\\.%m\\.") + r" \| (.+?) \| (.+?) \| (.+?) \|")
    for z in open("plan/kalender.md"):
        m = muster.match(z)
        if m:
            zeile = m.groups(); break
if zeile:
    print(f"HEUTE RAUS:  {zeile[0]} · Quelle {zeile[1]} · Zustand {zeile[2]}")
    if zeile[2].strip() == "offen":
        print("             ^^ steht noch auf offen — liegt es wirklich bei ihm?")
else:
    print("HEUTE RAUS:  nichts im Kalender (ausserhalb des Zeitraums?)")

# 2 — Fristen, die heute oder in den naechsten drei Tagen greifen
print("\nFRISTEN:")
etwas = False
for pd in sorted(PODCASTS):
    for tage, was, wer in VORLAUF:
        if tage in ENTFAELLT.get(PODCASTS[pd], set()):
            continue
        if tage in ERLEDIGT.get(PODCASTS[pd], set()):
            continue
        frist = pd - datetime.timedelta(days=tage)
        rest = (frist - heute).days
        if -1 <= rest <= 3:
            etwas = True
            halt = WARTET.get(PODCASTS[pd])
            if halt and heute < halt[0]:
                marke = "ANGEHALTEN "
            else:
                marke = "HEUTE " if rest == 0 else ("UEBERFAELLIG " if rest < 0 else f"in {rest} Tg ")
            zustaendig = SCHNITT.get(PODCASTS[pd], "?") if wer == "SCHNITT" else wer
            print(f"  {marke:14s} {PODCASTS[pd]:16s} T-{tage:<2d} {was:28s} -> {zustaendig}")

for folge, (frei, grund) in sorted(WARTET.items()):
    if heute < frei:
        print(f"\n  ANGEHALTEN: {folge} ruht bis {frei.strftime('%a %d.%m.')} "
              f"— wartet auf {grund}.")
        rest_bis = (frei - heute).days
        print(f"              Das sind noch {rest_bis} Tg. Alles, was am Schnitt "
              f"haengt, ruht mit.")
if not etwas:
    print("  keine in den naechsten drei Tagen")

# 2b — was ich beobachte
if BEOBACHTEN:
    print("\nBEOBACHTEN:")
    for was, wo in BEOBACHTEN:
        print(f"  {was}: {wo}")

# 3 — was heute entschieden werden muss
if heute in ENTSCHEIDUNG:
    print(f"\nENTSCHEIDUNG HEUTE:\n  {ENTSCHEIDUNG[heute]}")

# 4 — Vorlauf im Kasten: wie viele fertige Stuecke liegen vor heute?
print("\nVORRAT:")
fertig = 0
if os.path.exists("plan/kalender.md"):
    for z in open("plan/kalender.md"):
        m = re.match(r"^\| \w\w (\d\d)\.(\d\d)\. \| (.+?) \| (.+?) \| (.+?) \|", z)
        if not m: continue
        tag, monat, _, _, zustand = m.groups()
        d = datetime.date(2026, int(monat), int(tag))
        # Der Zustand traegt oft noch eine Begruendung ("bei ihm — gestern
        # geliefert") und Markdown-Sterne. Es zaehlt, womit er anfaengt.
        z = zustand.strip().strip("*").lower()
        if d >= heute and (z.startswith("fertig") or z.startswith("bei ihm")):
            fertig += 1
print(f"  {fertig} Stuecke ab heute fertig im Kasten")
if fertig < 3:
    print("  ^^ unter drei Tagen Vorlauf. Er nimmt taeglich ab — ohne Puffer")
    print("     ist ein verpatzter Tag sofort eine Luecke im Kanal.")
