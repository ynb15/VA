#!/usr/bin/env python3
"""Kapitelmarken vom Rohtranskript in die Zeitachse der Schnittfassung tragen.

Nicht gerechnet, sondern gesucht. Eine Schnittfassung ist beschleunigt und
enthaelt Einschuebe (Fundraiser, Promo), also ist jede Umrechnung
"Rohzeit / Tempo + Versatz" falsch, sobald irgendwo etwas eingefuegt oder
herausgeschnitten wurde -- und zwar um einen Betrag, den man vorher nicht
kennt. Stattdessen wird zu jeder Rohzeit der Wortlaut an dieser Stelle geholt
und derselbe Wortlaut im Transkript der Schnittfassung gesucht.

    python3 -I marken_uebertragen.py kapitel.txt roh.md schnitt.md [schnitt2.md ...]

kapitel.txt: eine Marke je Zeile, "H:MM:SS Titel" oder "MM:SS Titel".
Eine Zeile "CUT:MM:SS Titel" ist eine Marke, die im Rohmaterial nicht
vorkommt (der Fundraiser-Einschub): ihre Zeit ist in der Schnittfassung
gemessen und wird durchgereicht, nicht gesucht.

Die Transkripte brauchen das Format  **[H:MM:SS]** Text  je Zeile, so wie
`fenster.py` und die Whisper-Laeufe es schreiben.

Verglichen werden Wortfolgen, nicht Zeichen: Whisper schreibt denselben Satz
in zwei Durchgaengen unterschiedlich ("gonna" / "going to", Zahl als Wort oder
als Ziffer, Komma anders). Der Aehnlichkeitswert steht in der Ausgabe --
unter 0,55 ist die Marke nicht belegt und darf nicht gesetzt werden.

Die Suche laeuft vorwaerts: eine Marke liegt immer hinter der vorigen. Das
macht sie schnell und verhindert, dass eine wiederkehrende Wendung
("you know, yeah") irgendwo weit vorne einrastet.
"""
import difflib
import re
import sys

ZEILE = re.compile(r"^\*\*\[(?:(\d+):)?(\d+):(\d+)\]\*\*\s*(.*)$")
WORT = re.compile(r"[a-z0-9*']+")
ANKER = 16      # Woerter, die den Anker bilden
RUECK = 3       # Toleranz in Woertern, um die der Suchzeiger zurueckbleibt
SCHWELLE = 0.55


def sek(s):
    p = [int(x) for x in s.split(":")]
    while len(p) < 3:
        p.insert(0, 0)
    return p[0] * 3600 + p[1] * 60 + p[2]


def fmt(t):
    t = int(round(t))
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def lesen(pfade):
    """-> (woerter, zeiten) mit zeiten[i] = Sekunde, in der Wort i faellt."""
    woerter, zeiten = [], []
    for pfad in pfade:
        with open(pfad, encoding="utf-8") as f:
            for z in f:
                m = ZEILE.match(z)
                if not m:
                    continue
                h, mi, s, text = m.groups()
                t = int(h or 0) * 3600 + int(mi) * 60 + int(s)
                for w in WORT.findall(text.lower()):
                    woerter.append(w)
                    zeiten.append(t)
    if not woerter:
        sys.exit(f"keine Segmente in {pfade} -- anderes Format?")
    return woerter, zeiten


def kapitel_lesen(pfad):
    marken = []
    with open(pfad, encoding="utf-8") as f:
        for z in f:
            z = z.strip()
            if not z or z.startswith("#"):
                continue
            ts, _, titel = z.partition(" ")
            marken.append((ts, titel.strip()))
    return marken


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    marken = kapitel_lesen(sys.argv[1])
    rw, rz = lesen([sys.argv[2]])
    cw, cz = lesen(sys.argv[3:])
    print(f"# {len(marken)} Marken · roh {len(rw)} Woerter bis {fmt(rz[-1])} · "
          f"Schnitt {len(cw)} Woerter bis {fmt(cz[-1])}", file=sys.stderr)

    schwach = 0
    ab = 0
    for ts, titel in marken:
        if ts.startswith("CUT:"):
            print(f"{fmt(sek(ts[4:]))}\t----\t{titel}")
            continue
        ziel = sek(ts)
        i = next((k for k, t in enumerate(rz) if t >= ziel), None)
        if i is None or i + ANKER > len(rw):
            print(f"--:--\t----\t{titel}  # kein Rohtext an {ts}")
            schwach += 1
            continue
        anker = rw[i:i + ANKER]
        best, bestj = 0.0, None
        sm = difflib.SequenceMatcher(b=anker, autojunk=False)
        for j in range(ab, len(cw) - ANKER):
            sm.set_seq1(cw[j:j + ANKER])
            if sm.quick_ratio() <= best:
                continue
            r = sm.ratio()
            if r > best:
                best, bestj = r, j
        if bestj is None:
            print(f"--:--\t----\t{titel}  # nicht gefunden")
            schwach += 1
            continue
        print(f"{fmt(cz[bestj])}\t{best:.2f}\t{titel}")
        if best >= SCHWELLE:
            ab = max(ab, bestj - RUECK)
        else:
            schwach += 1
    if schwach:
        print(f"# {schwach} Marken unter {SCHWELLE} -- nicht belegt",
              file=sys.stderr)
    return 1 if schwach else 0


if __name__ == "__main__":
    sys.exit(main())
