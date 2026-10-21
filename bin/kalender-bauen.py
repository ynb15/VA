#!/usr/bin/env python3
"""Erzeugt plan/kalender.md aus den Folgen und dem Takt.

Takt (von ihm am 21.10.2026): 7 Stücke pro Woche, Untergrenze 5.
Hauptpodcast am Wochenende — "da sind die meisten Leute auf YouTube".
Shorts und Clips unter der Woche drumherum.
"""
import datetime, sys

START = datetime.date(2026, 10, 22)
ENDE  = datetime.date(2026, 12, 31)

# Podcast-Samstage: zwei im Monat, 26.12. gemieden (zweiter Weihnachtstag)
PODCASTS = {
    datetime.date(2026, 10, 25): ("Scott Aaronson",  "21.08.2026"),
    datetime.date(2026, 10, 31): ("Kyle Kingsbury",  "31.08.2026"),
    datetime.date(2026, 11, 13): ("Rick Strassman",  "18.09.2026"),
    datetime.date(2026, 11, 27): ("Matt Defina",     "04.09.2026"),
    datetime.date(2026, 12,  4): ("Marian Goodell",  "06.10.2026"),
}

VORLAUF = [(10, "Transkript", "Content Assistant (Shorts)"),
           (8,  "Clip- und Short-Auswahl", "Content Assistant (Shorts)"),
           (6,  "Titel · Beschreibung · Tags", "YouTube Manager"),
           (5,  "Thumbnails", "Thumbnail Assistant"),
           (3,  "Shorts gebaut", "Content Assistants"),
           (2,  "Paket vollständig bei ihm", "Alfred")]

WOCHENTAG = ["Mo","Di","Mi","Do","Fr","Sa","So"]

def art(d):
    """Was an diesem Tag rausgeht."""
    if d in PODCASTS:
        return "**PODCAST**", PODCASTS[d][0]
    if d.weekday() == 6:          # Sonntag
        return "Clip", "10–20 Min"
    if d.weekday() == 5:          # Samstag ohne Podcast
        return "Clip", "3–10 Min"
    return "Short", ""

zeilen, n_pod, n_clip, n_short = [], 0, 0, 0
d = START
while d <= ENDE:
    a, zusatz = art(d)
    if "PODCAST" in a: n_pod += 1
    elif a == "Clip":  n_clip += 1
    else:              n_short += 1
    zeilen.append((d, a, zusatz))
    d += datetime.timedelta(days=1)

aus = []
aus.append("# Der Kalender — 22.10. bis 31.12.2026\n")
aus.append("**Erzeugt von `bin/kalender-bauen.py`, nicht von Hand gepflegt.**")
aus.append("Takt und Wochenendlage sind seine Vorgaben vom 21.10.2026:")
aus.append("*„mindestens fünf, idealerweise sieben Content Pieces pro Woche …")
aus.append("ich veröffentliche in der Regel auch am Wochenende die Main Podcasts")
aus.append("und dann drumherum unter der Woche Shorts und Clips.\u201c\n")
aus.append(f"**{len(zeilen)} Tage · {n_pod} Podcasts · {n_clip} Clips · {n_short} Shorts**\n")
aus.append("Termine von ihm am 21.10. gesetzt. Nach dem 04.12. ist offen —")
aus.append("seine Worte: „und ab dann schauen wir da nochmal.\u201c\n")
aus.append("---\n")
aus.append("## Die Vorlauftermine — danach löse ich die Aufträge aus\n")
aus.append("| Podcast | Datum | T−10 Transkript | T−8 Auswahl | T−6 Text | T−5 Thumbnail | T−3 Shorts | T−2 bei ihm |")
aus.append("|---|---|---|---|---|---|---|---|")
for pd in sorted(PODCASTS):
    gast = PODCASTS[pd][0]
    felder = [(pd - datetime.timedelta(days=t)).strftime("%d.%m.") for t,_,_ in VORLAUF]
    aus.append(f"| **{gast}** | {WOCHENTAG[pd.weekday()]} {pd.strftime('%d.%m.')} | " + " | ".join(felder) + " |")
aus.append("")
heute = datetime.date(2026,10,21)
aus.append(f"**Stand {heute.strftime('%d.%m.%Y')}:** die Frist T−10 für Kingsbury ist **heute**.")
aus.append("Was heute nicht anläuft, verschiebt den 31.10.\n")
aus.append("---\n")
aus.append("## Tag für Tag\n")
aus.append("Leere Zellen fülle ich beim täglichen Lauf — jedes Stück bekommt seine")
aus.append("Quelle und seinen Zustand, sobald es gebaut ist.\n")
monat = None
for d, a, zusatz in zeilen:
    if d.month != monat:
        monat = d.month
        aus.append(f"\n### {['','Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'][monat]} {d.year}\n")
        aus.append("| Tag | Art | Quelle | Zustand |")
        aus.append("|---|---|---|---|")
    q = zusatz if zusatz else "—"
    aus.append(f"| {WOCHENTAG[d.weekday()]} {d.strftime('%d.%m.')} | {a} | {q} | offen |")
open("plan/kalender.md","w").write("\n".join(aus) + "\n")
print(f"{len(zeilen)} Tage · {n_pod} Podcasts · {n_clip} Clips · {n_short} Shorts")
