#!/usr/bin/env python3
"""Abgenommene Einblendungen auf einen neu geschnittenen Clip umlegen.

Der Grund: Whisper ist nicht deterministisch. Neu transkribieren heisst
wuerfeln - zweimal ist dabei schon eine abgenommene Anpassung verlorengegangen
("meaningful for you?" in EINER Einblendung, die geheilten Woerter ohne
Dauer). Wenn am Clip nur Stellen herausgeschnitten werden, muss gar nicht neu
transkribiert werden: die Zeiten lassen sich rechnen.

    python3 video/cues_umlegen.py alt.json neu.json \
        --versatz 0.3833 --kopf-bis 3.0 --kopf-versatz 0.4 \
        --raus schnitte.json

`--versatz` gilt fuer alles hinter dem Kopfstueck, `--kopf-versatz` davor.
`--raus` ist die Liste der entfernten Stellen in der ALTEN Zeitrechnung,
jede mit "von" und "bis" - dasselbe Format, das video/pausen_waehlen.py
ausgibt.
"""
import argparse
import json
from pathlib import Path


def abbilden(t, kopf_bis, kopf_versatz, versatz, raus):
    if t <= kopf_bis:
        return t + kopf_versatz
    weg = 0.0
    for s in raus:
        if s["bis"] <= t:
            weg += s["bis"] - s["von"]
        elif s["von"] < t < s["bis"]:
            # Zeitpunkt liegt in einer herausgeschnittenen Stelle: an deren
            # Anfang klemmen, sonst liefe die Einblendung rueckwaerts.
            weg += t - s["von"]
    return t + versatz - weg


def main():
    p = argparse.ArgumentParser()
    p.add_argument("alt")
    p.add_argument("neu")
    p.add_argument("--versatz", type=float, default=0.0)
    p.add_argument("--kopf-bis", type=float, default=0.0)
    p.add_argument("--kopf-versatz", type=float, default=0.0)
    p.add_argument("--raus", default=None)
    a = p.parse_args()

    raus = json.loads(Path(a.raus).read_text(encoding="utf-8")) if a.raus else []
    raus.sort(key=lambda s: s["von"])
    cues = json.loads(Path(a.alt).read_text(encoding="utf-8"))

    def f(t):
        return round(abbilden(t, a.kopf_bis, a.kopf_versatz, a.versatz, raus), 4)

    beruehrt = 0
    for c in cues:
        for schluessel in ("start", "end"):
            c[schluessel] = f(c[schluessel])
        for w in c.get("woerter") or []:
            vor = (w["start"], w["end"])
            w["start"], w["end"] = f(w["start"]), f(w["end"])
            if w["end"] - w["start"] < 0.01 < vor[1] - vor[0]:
                beruehrt += 1

    Path(a.neu).write_text(json.dumps(cues, ensure_ascii=False, indent=1),
                           encoding="utf-8")
    weg = sum(s["bis"] - s["von"] for s in raus)
    print(f"{len(cues)} Einblendungen umgelegt · {len(raus)} Stellen raus "
          f"({weg:.2f} s) · letzte Einblendung endet bei {cues[-1]['end']:.2f} s")
    if beruehrt:
        print(f"ACHTUNG: {beruehrt} Woerter wurden von einem Schnitt beschnitten "
              f"- ein Schnitt liegt nicht in einer Pause.")


if __name__ == "__main__":
    main()
