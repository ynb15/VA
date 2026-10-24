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
    datetime.date(2026, 11, 27): "Matt Defina",
    datetime.date(2026, 12,  4): "Marian Goodell",
}
# Ausnahmen: Folge -> Fristen, die fuer sie nicht gelten (von ihm so entschieden)
ENTFAELLT = {"Kyle Kingsbury": {5}}   # Thumbnail macht er selbst ueber ChatGPT, 21.10.

# Angehaltene Folgen: Folge -> (frei ab, worauf gewartet wird).
# Von ihm so entschieden. Fristen davor werden nicht als ueberfaellig gemeldet
# — sie sind nicht verpasst, sie sind ausgesetzt. Die Zeile bleibt sichtbar,
# damit ein Halt nicht aus dem Blick geraet.
WARTET = {
    "Kyle Kingsbury": (datetime.date(2026, 10, 26),
                       "Endfassung seines menschlichen Cutters; er reviewt die "
                       "Folge erst"),
}

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

# Erledigte Fristen: Folge -> die T-Marken, die abgeschlossen sind.
# Eine erledigte Frist darf nicht als ueberfaellig gemeldet werden — sonst
# steht am Stichtag eine Falschmeldung neben der erledigten Arbeit. Dasselbe
# Muster wie WARTET: ein Zustand, den das Werkzeug nicht kennt, wird als der
# naechste aehnliche gemeldet.
ERLEDIGT = {
    "Scott Aaronson": {10, 8, 6, 5, 3, 2},   # Paket am 23.10. uebergeben
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
        if folge == "Kyle Kingsbury":
            print("              BEOBACHTEN: Drive-Ordner des Cutters "
                  "1MsT1Cnp_FdPRrgFkdiEPmr-SCCzBg42M.")
            print("              Dort liegt nur v1_LOW_RES (1,29 GB, 05.10.). "
                  "Eine v2 oder eine Fassung")
            print("              ohne LOW_RES heisst: die Endfassung ist da.")
        rest_bis = (frei - heute).days
        print(f"              Das sind noch {rest_bis} Tg. Alles, was am Schnitt "
              f"haengt, ruht mit.")
if not etwas:
    print("  keine in den naechsten drei Tagen")

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
