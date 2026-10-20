#!/usr/bin/env python3
"""Findet Kamerawechsel, die Lippenhoehe und tote Einstellungen — ohne OpenCV.

Die Studio-Schnitte wechseln mitten im Short zwischen Nahaufnahme und
Zweier-Shot. Ein fester 9:16-Ausschnitt trifft dann mal den Sprecher, mal eine
Zimmerpflanze. Dieses Modul zerlegt den Clip in Einstellungen und schlaegt je
Einstellung einen Ausschnitt vor, dazu zwei Angaben, die der Renderer braucht:

* `lippe` — die Hoehe des Mundes im AUSGABEBILD (0..1920). Untertitel gehoeren
  an die Lippe oder knapp darunter; das ist kein Geschmack, sondern der Grund,
  warum der Blick nicht zwischen Mund und Bildunterkante pendeln muss.
* `tot` — Einstellungen ohne Sprecher. Nach einem Kameraschnitt steht im
  Studiomaterial regelmaessig eine knappe Sekunde nur der Tisch im Bild. Der
  Ton laeuft weiter, das Bild ist leer. Solche Abschnitte werden markiert,
  damit der Renderer sie ueberbrueckt statt sie zu zeigen.

Das Signal ist BEWEGUNG, nicht Hautfarbe. Hauttoene wurden am 19.10.2026
verworfen: im warmen Studiolicht galten 26–48 % des Bildes als Haut, Holzregal
und Pflanzen eingeschlossen — das Profil trennte Sprecher und Kulisse nicht.
Bewegung trennt sie sauber: der Redner bewegt Kopf und Haende, die Kulisse
steht. Und sie trennt auch leer von belegt: ein Tisch bewegt sich gar nicht.

Die Lippenhoehe wird NICHT als bewegungsstaerkste Zeile genommen. Das war der
erste Versuch und er lag verlaesslich falsch: die staerkste Bewegung im
Gesicht sitzt an Augen und Brille, nicht am Mund — die Linie landete auf der
Stirn. Auch die Hautfarbe taugt nicht: das Hautband lief in das graue T-Shirt
und in die Tischplatte hinein und zog den Mund auf die Brust. Was haelt: die
OBERKANTE des bewegten Bereichs ist der Kopf, und der Mund liegt ein festes
Stueck darunter (`KOPF_MUND`, Anteil der Ausschnitthoehe). An vier
Nahaufnahmen geprueft: Streuung der Kopfoberkante 0,156–0,189.

Ein-/Zweier-Shot entscheidet das Werkzeug jetzt selbst, ueber die
Bewegungsmasse in der Bildmitte. Im Studio sitzen die beiden am Rand, der
Tisch steht dazwischen: in der Totale liegen rund 28 % der Bewegung in der
Mitte, in der Nahaufnahme 55–73 %. Unter `MITTE_SCHWELLE` wird gestapelt —
ein 9:16-Ausschnitt aus einer Totale zeigt sonst den Tisch.

    python3 video/bildausschnitt.py clip.mp4 --json plan.json
"""
import argparse
import json

import av
import numpy as np

ZIEL_V = 9 / 16
AUS_B, AUS_H = 1080, 1920
MITTE_SCHWELLE = 0.45       # darunter: Totale mit zwei Personen -> stapeln
KOPF_MUND = 0.44            # Abstand Kopfoberkante -> Mund, Anteil der Hoehe
LIPPE_BAND = (0.56, 0.66)   # enges Band: an vier geprueften Nahaufnahmen
                            # lag der Mund bei 0,595–0,629. Die Messung darf
                            # darin wandern, aber nicht daraus heraus — eine
                            # zu tief gelesene Kopfoberkante schob die Zeile
                            # sonst an den Hals (Short 2: 0,72).
STAPEL_H = 0.70             # Hoehe eines Stapelausschnitts, Anteil der Quelle
STAPEL_LIPPE = 0.70         # feste Zeilenhoehe im Stapel, Anteil der Haelfte
ZEILE_FEST = 0.65           # Zeilenhoehe bei grossem Kopf, Anteil der Hoehe
ZEILE_WEIT = 0.42           # Zeilenhoehe, wenn die Person klein im Bild steht
                            # Beim Zoom sitzt die Kopfoberkante bauartbedingt auf
                            # 10 % der Kastenhoehe — damit liegt der Mund immer
                            # bei rund 0,56 und das Kinn bei 0,73. Eine feste
                            # Zeile dazwischen ist genauer als jede Messung:
                            # die Schaetzung schwankte zwischen 0,56 und 0,66
                            # und landete mal unter dem Kinn, mal auf dem Mund.
KOPF_PROBEN = 25            # Proben (a 0,2 s) fuer die Messung der Kopfoberkante


def _graustufen_folge(pfad, breite=160, abstand=0.2):
    """Alle `abstand` Sekunden ein kleines Graubild."""
    c = av.open(pfad)
    v = next(s for s in c.streams if s.type == "video")
    klein, zeiten = [], []
    letzte = -1.0
    w = h = 0
    for frame in c.decode(v):
        t = float(frame.pts * v.time_base)
        if t - letzte < abstand:
            continue
        letzte = t
        img = frame.to_ndarray(format="rgb24")
        h, w, _ = img.shape
        schritt = max(1, w // breite)
        klein.append(img[::schritt, ::schritt].mean(axis=2))
        zeiten.append(t)
    c.close()
    return zeiten, klein, (w, h)


def schnitte_finden(zeiten, klein, anteil=0.45, mittel=25.0):
    """Grenzen zwischen Einstellungen.

    Nicht ueber die mittlere Bildaenderung allein — daran ist die erste
    Fassung gescheitert. Sutcliffe redet mit beiden Haenden; eine ausholende
    Geste hebt den Mittelwert auf 20–31 und erzeugte vier Schnitte, wo keiner
    war. Entscheidend ist der ANTEIL des Bildes, der sich aendert: beim
    echten Kameraschnitt wechselt auch der Hintergrund, gemessen 0,51–0,61;
    bei der groessten Handbewegung nur 0,19–0,35. Dazwischen liegt Luft.
    """
    grenzen = [0]
    for i in range(1, len(klein)):
        a, b = klein[i - 1], klein[i]
        n = min(a.shape[0], b.shape[0]), min(a.shape[1], b.shape[1])
        d = np.abs(a[:n[0], :n[1]] - b[:n[0], :n[1]])
        if float((d > 25).mean()) > anteil and d.mean() > mittel:
            grenzen.append(i)
    grenzen.append(len(klein))
    return grenzen


def bewegungskarte(bilder):
    """Mittlere zeitliche Aenderung je Bildpunkt innerhalb einer Einstellung."""
    if len(bilder) < 2:
        return np.zeros_like(bilder[0]) if bilder else np.zeros((1, 1))
    h = min(b.shape[0] for b in bilder)
    w = min(b.shape[1] for b in bilder)
    stapel = np.stack([b[:h, :w] for b in bilder])
    return np.abs(np.diff(stapel, axis=0)).mean(axis=0)


def _glatt(profil, teiler=12):
    k = max(3, len(profil) // teiler)
    return np.convolve(profil, np.ones(k) / k, mode="same")


def schwerpunkt(profil):
    """Spalte mit der groessten Bewegungsmasse, geglaettet."""
    if profil.max() <= 0:
        return len(profil) / 2
    return float(np.argmax(_glatt(profil)))


def kopfoberkante(karte, r0, r1, c0, c1, anteil=0.35):
    """Oberste Zeile mit nennenswerter Bewegung, als Anteil des Ausschnitts."""
    aus = karte[max(0, r0):max(r0 + 1, r1), max(0, c0):max(c0 + 1, c1)]
    if aus.size == 0:
        return None
    z = _glatt(aus.mean(axis=1), teiler=20)
    if z.max() <= 0:
        return None
    ueber = np.where(z > anteil * z.max())[0]
    return float(ueber[0]) / len(z) if len(ueber) else None


def lippe_aus_kopf(karte, kasten, sx, sy):
    """Lippenhoehe im Ausgabeausschnitt (0..1), aus der Kopfoberkante."""
    x, y, b, h = kasten
    oben = kopfoberkante(karte, int(y / sy), int((y + h) / sy),
                         int(x / sx), int((x + b) / sx))
    roh = (oben + KOPF_MUND) if oben is not None else 0.62
    return min(max(roh, LIPPE_BAND[0]), LIPPE_BAND[1])


def mittenmasse(spalten):
    """Anteil der Bewegung, der in der Bildmitte liegt."""
    g = _glatt(spalten)
    if g.sum() <= 0:
        return 1.0
    g = g / g.sum()
    n = len(g)
    return float(g[int(n * 0.35):int(n * 0.65)].sum())


def gipfel(spalten, von, bis):
    """Staerkste geglaettete Bewegungsspalte im Bereich [von, bis)."""
    g = _glatt(spalten)
    bereich = g[von:bis]
    return (von + int(np.argmax(bereich))) if len(bereich) else (von + bis) // 2


def stapelseite(karte, spalten, von, bis, qb, qh, sx, sy):
    """Ausschnitt fuer eine Haelfte des Stapels (9:8, damit nichts verzerrt).

    Waagerecht auf den Bewegungsgipfel der Seite, senkrecht an der gemessenen
    Kopfoberkante ausgerichtet — sonst steht ueber dem Kopf eine halbe
    Bildhoehe Wand.
    """
    bh = int(round(qh * STAPEL_H))
    bb = min(int(round(bh * (AUS_B / (AUS_H / 2)))), qb)
    x = max(0, min(int(round(gipfel(spalten, von, bis) * sx - bb / 2)), qb - bb))
    oben = kopfoberkante(karte, 0, karte.shape[0], int(x / sx), int((x + bb) / sx))
    kopf = (oben if oben is not None else 0.25) * qh
    y = int(max(0, min(kopf - 0.12 * qh, qh - bh)))
    return x, y, bb, bh


def _kasten(mitte_x, qb, qh, seitenverhaeltnis, zoom=1.0, kopf_oben=None):
    """Ausschnitt mit gegebenem Seitenverhaeltnis um mitte_x, im Bild gehalten.

    `zoom` > 1 zieht enger heran. Seine veroeffentlichten Shorts sind deutlich
    naeher dran als ein voller 1080er Ausschnitt: der Kopf fuellt dort rund
    zwei Drittel der Bildhoehe. `kopf_oben` (Anteil der Quellhoehe) setzt den
    Ausschnitt so, dass ueber dem Kopf ein Zehntel Luft bleibt.
    """
    bh = int(round(qh / max(zoom, 1.0)))
    bb = int(round(bh * seitenverhaeltnis))
    if bb > qb:
        bb = qb
        bh = int(round(bb / seitenverhaeltnis))
    x = int(round(mitte_x - bb / 2))
    x = max(0, min(x, qb - bb))
    if kopf_oben is None:
        y = max(0, (qh - bh) // 3)      # Koepfe sitzen im oberen Drittel
    else:
        y = int(round(kopf_oben * qh - 0.10 * bh))
    y = max(0, min(y, qh - bh))
    return x, y, bb, bh


def marke_meiden(kasten, marke, qb, qh):
    """Schiebt den Ausschnitt aus einem eingebrannten Logo heraus.

    Der Master traegt sein YNB-Logo schon unten links im Bild. In den
    Nahaufnahmen liegt es ausserhalb des 9:16-Ausschnitts, in der Totale
    nicht — dort stand es im fertigen Short neben dem Logo, das wir selbst
    darueberlegen. Erst nach oben ausweichen (das Bild bleibt auf der
    Person), erst wenn das nicht reicht, nach rechts.
    """
    if not marke:
        return kasten
    mx0, my0, mx1, my1 = marke
    x, y, bb, bh = kasten
    if x >= mx1 or x + bb <= mx0 or y >= my1 or y + bh <= my0:
        return kasten
    y_neu = my0 - bh
    if y_neu >= 0:
        return x, y_neu, bb, bh
    # Nach oben passt der Kasten nicht mehr — dann lieber ein Stueck enger
    # ziehen als zur Seite rutschen: zur Seite verliert man die Person aus
    # der Mitte, enger behaelt sie. Mehr als ein Viertel wird nicht gekuerzt.
    if my0 >= 0.75 * bh:
        bh_neu = int(my0)
        bb_neu = int(round(bh_neu * bb / bh))
        x_neu = max(0, min(x + (bb - bb_neu) // 2, qb - bb_neu))
        return x_neu, 0, bb_neu, bh_neu
    x_neu = mx1
    if x_neu + bb <= qb:
        return x_neu, y, bb, bh
    return kasten


def plan_bauen(pfad, mindestdauer=0.6, totanteil=0.28, lippe_versatz=0,
               abstand=0.2, zoom=1.0, kein_stapel=False,
               zeile_folgt=False, marke=None):
    zeiten, klein, (qb, qh) = _graustufen_folge(pfad, abstand=abstand)
    if len(klein) < 2:
        raise SystemExit("Zu wenige Bilder gelesen.")
    grenzen = schnitte_finden(zeiten, klein)
    sy = qh / klein[0].shape[0]
    sx = qb / klein[0].shape[1]

    roh = []
    for i in range(len(grenzen) - 1):
        a, b = grenzen[i], grenzen[i + 1]
        if b <= a:
            continue
        karte = bewegungskarte(klein[a:b])
        # Fuer die Kopfoberkante nur ein kurzes Fenster aus der Mitte der
        # Einstellung: ueber 20 Sekunden gemittelt verschwindet die schwache
        # Bewegung am Haaransatz unter der Schwelle, die Oberkante rutscht
        # nach unten und die Zeile landet am Hals. Gemessen an Short 2:
        # 0,28 statt 0,13. Das Mass muss so lang sein wie das, an dem
        # KOPF_MUND geeicht wurde — rund fuenf Sekunden.
        k = min(len(klein[a:b]), KOPF_PROBEN)
        m = a + max(0, (b - a - k) // 2)
        karte_kurz = bewegungskarte(klein[m:m + k])
        roh.append({"kurz": karte_kurz, "start": zeiten[a],
                    "ende": zeiten[b] if b < len(zeiten) else zeiten[-1] + abstand,
                    "karte": karte, "spalten": karte.mean(axis=0),
                    "masse": float(karte.mean()), "proben": b - a})

    # Bezug fuer "tot": der Mittelwert der langen Einstellungen. Kurze
    # Abschnitte haben zu wenige Differenzen, um den Bezug zu tragen.
    lang = [s["masse"] for s in roh if s["ende"] - s["start"] >= 1.5]
    bezug = float(np.median(lang)) if lang else float(np.median([s["masse"] for s in roh]))

    plan = []
    for s in roh:
        dauer = s["ende"] - s["start"]
        # Unter drei Proben gibt es zu wenige Differenzen, um leer von belegt
        # zu trennen — dann lieber zeigen als faelschlich ueberbruecken.
        tot = (s["proben"] >= 3 and bezug > 0
               and s["masse"] < totanteil * bezug)
        mitte = mittenmasse(s["spalten"])
        n = len(s["spalten"])
        if tot or kein_stapel or mitte >= MITTE_SCHWELLE:
            x = gipfel(s["spalten"], 0, n) * sx
            # Erst ueber den vollen Ausschnitt die Kopfoberkante messen, dann
            # den engeren Kasten darum legen — sonst sucht man den Kopf in
            # einem Fenster, das man erst kennt, wenn man den Kopf hat.
            grob = _kasten(x, qb, qh, ZIEL_V)
            oben = kopfoberkante(s["kurz"], 0, s["kurz"].shape[0],
                                 int(grob[0] / sx), int((grob[0] + grob[2]) / sx))
            kasten = _kasten(x, qb, qh, ZIEL_V, zoom=zoom,
                             kopf_oben=oben if zoom > 1.0 else None)
            kasten = marke_meiden(kasten, marke, qb, qh)
            # Die Zeile bleibt auf einer Hoehe, auch wenn die Kamera auf
            # die Totale wechselt — sein Wunsch vom 20.10.: „es kann auf der
            # gleichen Hoehe bleiben." Das Auge hat die Zeile dann immer am
            # selben Fleck, und genau das ist der Sinn der Sache.
            # Mit `zeile_folgt` richtet sie sich stattdessen danach, wie gross
            # die Person im Bild steht (Nahaufnahme 0,65, Totale 0,42).
            if zeile_folgt and mitte < MITTE_SCHWELLE:
                anteil = ZEILE_WEIT
            else:
                anteil = ZEILE_FEST
            if zoom > 1.0:
                hoehe = int(round(anteil * AUS_H))
            else:
                hoehe = int(round(lippe_aus_kopf(s["kurz"], kasten, sx, sy) * AUS_H))
            eintrag = {"layout": "einzel", "kasten": "%d:%d:%d:%d" % kasten,
                       "lippe": hoehe + lippe_versatz}
        else:
            # Totale: beide sitzen am Rand, der Tisch steht in der Mitte.
            links = stapelseite(s["kurz"], s["spalten"], 0, int(n * 0.45),
                                qb, qh, sx, sy)
            rechts = stapelseite(s["kurz"], s["spalten"], int(n * 0.55), n,
                                 qb, qh, sx, sy)
            x = gipfel(s["spalten"], 0, n) * sx
            # Im Stapel wird die Lippe NICHT gemessen. Welcher der beiden
            # gerade spricht, weiss das Werkzeug nicht, und eine gemessene
            # Hoehe landete im Versuch auf Yannicks Brille. Weil der
            # Ausschnitt die Kopfoberkante auf 12 % der Kastenhoehe setzt und
            # ein Kopf in der Totale hoechstens 45 % davon einnimmt, liegt das
            # Kinn immer ueber STAPEL_LIPPE — die Zeile deckt nie ein Gesicht.
            eintrag = {"layout": "stapel", "oben": "%d:%d:%d:%d" % links,
                       "unten": "%d:%d:%d:%d" % rechts,
                       "lippe": int(round(STAPEL_LIPPE * AUS_H / 2)) + lippe_versatz}
        if plan and not tot and not plan[-1]["tot"] and dauer < mindestdauer \
                and abs(x / qb - plan[-1]["bewegung_x"]) < 0.08:
            plan[-1]["ende"] = round(s["ende"], 2)   # gleiche Kadrierung: anhaengen
            continue
        eintrag.update(start=round(s["start"], 2), ende=round(s["ende"], 2),
                       tot=bool(tot), bewegung_x=round(x / qb, 3),
                       mitte=round(mitte, 2), masse=round(s["masse"], 2))
        plan.append(eintrag)

    # Ein angeschnittener Anfang (Trim mitten in der Bildgruppe) erzeugt eine
    # Einstellung von zwei Zehntelsekunden ohne Bewegung und mit geratenem
    # Ausschnitt. Sie faellt der naechsten zu, statt kurz Unsinn zu zeigen.
    while len(plan) > 1 and plan[0]["ende"] - plan[0]["start"] < mindestdauer:
        plan[1]["start"] = plan[0]["start"]
        plan.pop(0)
    while len(plan) > 1 and plan[-1]["ende"] - plan[-1]["start"] < mindestdauer:
        plan[-2]["ende"] = plan[-1]["ende"]
        plan.pop()
    return plan, (qb, qh), bezug


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("--json", default=None)
    ap.add_argument("--abstand", type=float, default=0.2)
    ap.add_argument("--totanteil", type=float, default=0.28,
                    help="Anteil der mittleren Bewegung, unter dem eine "
                         "Einstellung als leer gilt")
    ap.add_argument("--zeile-folgt", action="store_true",
                    help="Untertitelzeile der Bildgroesse folgen lassen statt "
                         "sie auf einer Hoehe zu halten")
    ap.add_argument("--kein-stapel", action="store_true",
                    help="auch Totalen auf eine Person beschneiden statt zu "
                         "stapeln — auf dem staerksten Bewegungsgipfel, also "
                         "auf dem, der gerade spricht und gestikuliert")
    ap.add_argument("--zoom", type=float, default=1.0,
                    help="enger heranziehen. Bewaehrt: 1.15. Seine veroeffentlichten Shorts wirken naeher (rund 1.35), aber dabei liegt die Kopfoberkante ausserhalb des Bildes und der Schrift bleiben nur 70 px zum Rand.")
    ap.add_argument("--lippe-versatz", type=int, default=0,
                    help="Pixel, um die die Untertitel zusaetzlich nach unten "
                         "ruecken")
    ap.add_argument("--marke", default=None,
                    help="x0,y0,x1,y1 eines schon eingebrannten Logos in der "
                         "Quelle; der Ausschnitt weicht ihm aus. Fuer den "
                         "Podcast-Master gemessen: 0,875,215,1080")
    a = ap.parse_args()
    marke = None
    if a.marke:
        marke = tuple(int(v) for v in a.marke.split(","))
        if len(marke) != 4:
            raise SystemExit("--marke braucht vier Werte: x0,y0,x1,y1")
    plan, groesse, bezug = plan_bauen(a.clip, totanteil=a.totanteil,
                                      lippe_versatz=a.lippe_versatz,
                                      abstand=a.abstand, zoom=a.zoom,
                                      kein_stapel=a.kein_stapel,
                                      zeile_folgt=a.zeile_folgt, marke=marke)
    print(f"Bezugsbewegung {bezug:.2f} · {len(plan)} Einstellungen")
    for p in plan:
        mark = "TOT " if p["tot"] else "    "
        wo = p.get("kasten") or f'{p["oben"]} + {p["unten"]}'
        print(f'{p["start"]:6.1f}–{p["ende"]:6.1f}  {mark}{p["layout"]:6} {wo:>26}'
              f'  Lippe {p["lippe"]:4}  Mitte {p["mitte"]:.2f}'
              f'  Bewegung {p["masse"]:5.2f}')
    if a.json:
        json.dump({"quelle": a.clip, "groesse": groesse,
                   "bezugsbewegung": round(bezug, 3), "einstellungen": plan},
                  open(a.json, "w"), indent=1)
        print(f'→ {a.json}')
