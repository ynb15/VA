#!/usr/bin/env python3
"""Findet Kamerawechsel und die Position der Gesichter — ohne OpenCV.

Die Studio-Schnitte wechseln mitten im Short zwischen Nahaufnahme und
Zweier-Shot. Ein fester 9:16-Ausschnitt trifft dann mal den Sprecher, mal eine
Zimmerpflanze. Dieses Modul zerlegt den Clip in Einstellungen und schlaegt je
Einstellung einen Ausschnitt vor:

Das Signal ist BEWEGUNG, nicht Hautfarbe. Hauttoene wurden am 19.10.2026
verworfen: im warmen Studiolicht galten 26–48 % des Bildes als Haut, Holzregal
und Pflanzen eingeschlossen — das Profil trennte Sprecher und Kulisse nicht.
Bewegung trennt sie sauber: der Redner bewegt Kopf und Haende, die Kulisse steht.

Je Einstellung wird das Spaltenprofil der zeitlichen Abweichung gebildet und der
Schwerpunkt als Kopfposition genommen. Ob eine oder zwei Personen im Bild sind,
entscheidet das Werkzeug NICHT von sich aus — dafuer gibt es `--plan`, in dem
die Einstellung ueberschrieben werden kann. Automatische Einzel/Stapel-Erkennung
steht noch aus; lieber ein Feld zum Nachtragen als eine Zahl, die raet.

    python3 video/bildausschnitt.py clip.mp4 --json plan.json
"""
import argparse
import json

import av
import numpy as np

ZIEL_V = 9 / 16


def _graustufen_folge(pfad, breite=160):
    """Je Sekunde ein kleines Graubild plus ein Farbbild fuer die Hautsuche."""
    c = av.open(pfad)
    v = next(s for s in c.streams if s.type == "video")
    klein, farbe, zeiten = [], [], []
    letzte = -1.0
    for frame in c.decode(v):
        t = float(frame.pts * v.time_base)
        if t - letzte < 0.5:
            continue
        letzte = t
        img = frame.to_ndarray(format="rgb24")
        h, w, _ = img.shape
        schritt = max(1, w // breite)
        mini = img[::schritt, ::schritt]
        klein.append(mini.mean(axis=2))
        farbe.append(mini)
        zeiten.append(t)
    c.close()
    return zeiten, klein, farbe, (w, h)


def schnitte_finden(zeiten, klein, schwelle=18.0):
    """Grenzen zwischen Einstellungen ueber die mittlere Bildaenderung."""
    grenzen = [0]
    for i in range(1, len(klein)):
        a, b = klein[i - 1], klein[i]
        n = min(a.shape[0], b.shape[0]), min(a.shape[1], b.shape[1])
        d = np.abs(a[:n[0], :n[1]] - b[:n[0], :n[1]]).mean()
        if d > schwelle:
            grenzen.append(i)
    grenzen.append(len(klein))
    return grenzen


def bewegungsprofil(bilder):
    """Spaltenweise mittlere Aenderung ueber die Bilder einer Einstellung."""
    if len(bilder) < 2:
        return np.zeros(bilder[0].shape[1]) if bilder else np.zeros(1)
    h = min(b.shape[0] for b in bilder)
    w = min(b.shape[1] for b in bilder)
    stapel = np.stack([b[:h, :w] for b in bilder])
    return np.abs(np.diff(stapel, axis=0)).mean(axis=(0, 1))


def schwerpunkt(profil):
    """Spalte mit der groessten Bewegungsmasse, geglaettet."""
    if profil.max() <= 0:
        return len(profil) / 2
    k = max(3, len(profil) // 12)
    kern = np.ones(k) / k
    glatt = np.convolve(profil, kern, mode="same")
    return float(np.argmax(glatt))


def hautspalten(rgb):
    """Spaltenprofil der Hautpixel."""
    r, g, b = (rgb[..., i].astype(np.int16) for i in range(3))
    y = (0.299 * r + 0.587 * g + 0.114 * b)
    cb = 128 - 0.168736 * r - 0.331264 * g + 0.5 * b
    cr = 128 + 0.5 * r - 0.418688 * g - 0.081312 * b
    maske = (cb > 77) & (cb < 127) & (cr > 133) & (cr < 173) & (y > 40)
    return maske.sum(axis=0).astype(float), maske


def personen_finden(profil, mindestanteil=0.12):
    """Gipfel im Spaltenprofil zu Personen zusammenfassen."""
    if profil.max() <= 0:
        return []
    p = profil / profil.max()
    aktiv = p > mindestanteil
    gruppen, start = [], None
    for i, an in enumerate(aktiv):
        if an and start is None:
            start = i
        elif not an and start is not None:
            gruppen.append((start, i))
            start = None
    if start is not None:
        gruppen.append((start, len(aktiv)))
    # winzige Gruppen verwerfen, nach Masse sortieren
    gruppen = [g for g in gruppen if (g[1] - g[0]) >= max(3, len(p) * 0.04)]
    gruppen.sort(key=lambda g: profil[g[0]:g[1]].sum(), reverse=True)
    return gruppen[:2]


def plan_bauen(pfad, mindestdauer=1.2):
    zeiten, klein, farbe, (qb, qh) = _graustufen_folge(pfad)
    grenzen = schnitte_finden(zeiten, klein)
    mb = farbe[0].shape[1]           # Breite der Miniatur
    faktor = qb / mb
    plan = []
    for i in range(len(grenzen) - 1):
        a, b = grenzen[i], grenzen[i + 1]
        if b <= a:
            continue
        profil = bewegungsprofil(klein[a:b])
        start_t = zeiten[a]
        ende_t = zeiten[b] if b < len(zeiten) else zeiten[-1] + 1.0
        if ende_t - start_t < mindestdauer and plan:
            plan[-1]["ende"] = ende_t
            continue
        x = schwerpunkt(profil) * faktor
        plan.append({"start": round(start_t, 2), "ende": round(ende_t, 2),
                     "layout": "einzel", "kasten": _kasten(x, qb, qh, ZIEL_V),
                     "bewegung_x": round(x / qb, 3)})
    return plan, (qb, qh)


def _kasten(mitte_x, qb, qh, seitenverhaeltnis):
    """Ausschnitt mit gegebenem Seitenverhaeltnis um mitte_x, im Bild gehalten."""
    bh = qh
    bb = int(round(bh * seitenverhaeltnis))
    if bb > qb:
        bb = qb
        bh = int(round(bb / seitenverhaeltnis))
    x = int(round(mitte_x - bb / 2))
    x = max(0, min(x, qb - bb))
    y = max(0, (qh - bh) // 3)      # Koepfe sitzen im oberen Drittel
    return f"{x}:{y}:{bb}:{bh}"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    plan, groesse = plan_bauen(a.clip)
    for p in plan:
        rest = p.get("kasten") or f'{p["oben"]} / {p["unten"]}'
        print(f'{p["start"]:6.1f}–{p["ende"]:6.1f}  {p["layout"]:7} {rest}')
    if a.json:
        json.dump({"quelle": a.clip, "groesse": groesse, "einstellungen": plan},
                  open(a.json, "w"), indent=1)
        print(f'→ {a.json}')
