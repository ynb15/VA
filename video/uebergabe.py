#!/usr/bin/env python3
"""Das Transkript zu einem Stueck, so dass er sagen kann, was raus soll.

    python3 video/uebergabe.py kyle

Seine Anweisung vom 22.10.2026: lieber zu defensiv schneiden und ihm das
Transkript geben, damit er die Auslassungen bestimmt statt sie zu suchen.
Dafuer muss sichtbar sein, was NICHT im Stueck ist — die 30 Sekunden davor und
danach stehen deshalb mit drin, deutlich abgesetzt.
"""
import json
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))


def text_aus_srt(pfad):
    zeilen = [z.strip() for z in open(pfad, encoding="utf-8")
              if z.strip() and not z.strip().isdigit() and "-->" not in z]
    return re.sub(r"\s+", " ", " ".join(zeilen))


def letzter_cue(pfad):
    """Ende der letzten Einblendung in Sekunden."""
    zeiten = re.findall(r"--> (\d\d):(\d\d):(\d\d),(\d\d\d)",
                        open(pfad, encoding="utf-8").read())
    if not zeiten:
        return None
    h, m, sek, ms = zeiten[-1]
    return int(h) * 3600 + int(m) * 60 + int(sek) + int(ms) / 1000


def bauen(k):
    b = json.load(open(os.path.join(HIER, f"{k}_befund.json")))
    srt = os.path.join(HIER, f"YNB Podcast {b['name']} Meaning.srt")
    dauer = b["master_bis"] - b["master_von"]
    t = [f"{b['name']} — „What makes life meaningful?\"",
         "=" * 60, "",
         f"Master im Drive : {b['drive_id']}",
         f"Zeitmarke       : {b['master_von']}–{b['master_bis']} s Masterzeit",
         f"Dauer im Master : {dauer:.1f} s · fertiges Stueck {dauer / 1.2:.1f} s "
         f"bei Tempo 1,2"]
    if b.get("anschlussfenster"):
        t.append("ACHTUNG         : die Antwort laeuft ueber zwei Suchfenster, "
                 "beim Nachschneiden beide holen")
    # Whisper gibt den angebrochenen letzten Abschnitt nicht aus, wenn die
    # Datei direkt dahinter endet. Der Satz ist dann im Ton und nicht im
    # Untertitel — wer das nicht weiss, sucht ihn im Stueck vergeblich.
    luecke = None
    if os.path.exists(srt):
        ende = letzter_cue(srt)
        if ende is not None and dauer / 1.2 - ende > 1.0:
            luecke = dauer / 1.2 - ende
    if luecke:
        t.append(f"ACHTUNG         : die letzten {luecke:.1f} s sind im Ton, "
                 f"aber ohne Untertitel")
        t.append("                  (Whisper gibt den letzten angebrochenen "
                 "Abschnitt nicht aus)")
    t += ["", "Keine Musik — am 22.10. sind vier Fassungen an einem Tag weltweit",
          "gesperrt worden, zuletzt sogar ein Klaviercover.", "",
          "-" * 60,
          "DAVOR, NICHT IM STUECK (die letzten 30 s vor dem Schnitt):", "",
          b.get("davor", "—") or "—", "",
          "-" * 60, "IM STUECK:", "",
          text_aus_srt(srt) if os.path.exists(srt) else "(Untertitel fehlen)", "",
          "-" * 60,
          "DANACH, NICHT IM STUECK (die ersten 30 s nach dem Schnitt):", "",
          b.get("danach", "—") or "—", "",
          "-" * 60,
          "Soll etwas davon rein oder raus? Eine Zeile genuegt, ich rendere neu —",
          "das kostet keinen Drive-Abruf, nur Rechenzeit.", ""]
    ziel = os.path.join(HIER, f"YNB Podcast {b['name']} Meaning.txt")
    open(ziel, "w", encoding="utf-8").write("\n".join(t))
    print(ziel)
    return ziel


if __name__ == "__main__":
    for k in sys.argv[1:]:
        bauen(k)
