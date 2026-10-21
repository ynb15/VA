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
    datetime.date(2026, 10, 31): "Kyle Kingsbury",
    datetime.date(2026, 11, 14): "Scott Aaronson",
    datetime.date(2026, 11, 28): "David Sutcliffe",
    datetime.date(2026, 12, 12): "Matt Defina",
    datetime.date(2026, 12, 19): "Ken Stern",
}
VORLAUF = [(10, "Transkript",                   "content-schlicht"),
           (8,  "Clip- und Short-Auswahl",      "content-schlicht"),
           (6,  "Titel · Beschreibung · Tags",  "youtube-manager"),
           (5,  "Thumbnails",                   "thumbnails"),
           (3,  "Shorts gebaut",                "content-schlicht + content-cinematic"),
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
        frist = pd - datetime.timedelta(days=tage)
        rest = (frist - heute).days
        if -1 <= rest <= 3:
            etwas = True
            marke = "HEUTE " if rest == 0 else ("UEBERFAELLIG " if rest < 0 else f"in {rest} Tg ")
            print(f"  {marke:14s} {PODCASTS[pd]:16s} T-{tage:<2d} {was:28s} -> {wer}")
if not etwas:
    print("  keine in den naechsten drei Tagen")

# 3 — Vorlauf im Kasten: wie viele fertige Stuecke liegen vor heute?
print("\nVORRAT:")
fertig = 0
if os.path.exists("plan/kalender.md"):
    for z in open("plan/kalender.md"):
        m = re.match(r"^\| \w\w (\d\d)\.(\d\d)\. \| (.+?) \| (.+?) \| (.+?) \|", z)
        if not m: continue
        tag, monat, _, _, zustand = m.groups()
        d = datetime.date(2026, int(monat), int(tag))
        if d >= heute and zustand.strip() in ("fertig", "bei ihm"):
            fertig += 1
print(f"  {fertig} Stuecke ab heute fertig im Kasten")
if fertig < 3:
    print("  ^^ unter drei Tagen Vorlauf. Er nimmt taeglich ab — ohne Puffer")
    print("     ist ein verpatzter Tag sofort eine Luecke im Kanal.")
