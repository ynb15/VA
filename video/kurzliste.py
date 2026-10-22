#!/usr/bin/env python3
"""Aus der .srt eines fertigen Shorts eine Liste zum Durchstreichen machen.

Seine Regel vom 22.10.2026: *„dass die Shorts mit dem Transkript geliefert
werden müssen, damit ich einfacher Feedback geben kann, beziehungsweise
einfach dir sagen kann, was raus soll."*

Die .srt selbst taugt dafür schlecht — drei Wörter je Zeile, hundert
Einblendungen. Hier werden sie zu Sätzen zusammengefasst und durchnummeriert,
mit den Zeiten **im fertigen Short**, also dem, was er im Player sieht.

    python3 video/kurzliste.py short.srt [--titel "..."] [--out liste.txt]
"""
import argparse, re, sys
from pathlib import Path

ENDE = ".!?"


def srt_lesen(pfad):
    cues, block = [], []
    for roh in Path(pfad).read_text(encoding="utf-8").splitlines() + [""]:
        if roh.strip():
            block.append(roh)
            continue
        if len(block) >= 2:
            zeile = next((z for z in block if "-->" in z), None)
            if zeile:
                a, b = [t.strip().replace(",", ".") for t in zeile.split("-->")]
                text = " ".join(block[block.index(zeile) + 1:]).strip()
                if text:
                    cues.append((_sek(a), _sek(b), text))
        block = []
    return cues


def _sek(t):
    h, m, s = t.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def mmss(t):
    return f"{int(t // 60):02d}:{t % 60:05.2f}"


def saetze(cues, pause=0.35, max_worte=14):
    """Einblendungen buendeln: Satzzeichen, echte Pause oder Laenge.

    In eingebrannten Untertiteln steht fast kein Satzzeichen — nur das
    Fragezeichen bleibt stehen. Satzenden allein ergaben darum zwei
    Bloecke von zwanzig Sekunden, in denen sich nichts durchstreichen
    laesst. Deshalb bricht die Liste zusaetzlich an Sprechpausen und
    spaetestens nach `max_worte` Woertern um.
    """
    gruppen, akt, n = [], [], 0
    for i, (a, b, text) in enumerate(cues):
        akt.append((a, b, text))
        n += len(text.split())
        schluss = text.rstrip().endswith(tuple(ENDE))
        luecke = cues[i + 1][0] - b if i + 1 < len(cues) else 9e9
        if schluss or luecke >= pause or n >= max_worte:
            gruppen.append(akt)
            akt, n = [], 0
    if akt:
        gruppen.append(akt)
    return [(g[0][0], g[-1][1], " ".join(x[2] for x in g)) for g in gruppen]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("srt")
    p.add_argument("--titel", default=None)
    p.add_argument("--out", default=None)
    p.add_argument("--pause", type=float, default=0.35)
    p.add_argument("--worte", type=int, default=14)
    a = p.parse_args()

    teile = saetze(srt_lesen(a.srt), a.pause, a.worte)
    kopf = [f"# {a.titel or Path(a.srt).stem}",
            "#",
            "# Zeiten sind die im FERTIGEN Short — das, was Du im Player siehst.",
            "# Was raus soll: Zeile loeschen oder die Nummer nennen.",
            "#"]
    zeilen = [f"{i:3d}  [{mmss(v)}–{mmss(b)}]  {t}"
              for i, (v, b, t) in enumerate(teile, 1)]
    text = "\n".join(kopf + zeilen) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"{len(teile)} Zeilen nach {a.out}")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
