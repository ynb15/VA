#!/usr/bin/env python3
"""Die Einstellungsgrenzen eines Plans Bild fuer Bild nachmessen.

    python3 video/schnittgrenzen.py clip.mp4 plan.json [--aus plan_genau.json]

Warum das sein muss, steht in `lernen/content-gastauftritte.md` zum 24.10.:
`bildausschnitt.py` SCHAETZT die Grenzen (es tastet den Clip in Schritten ab)
und lag beim Hypermaskulinitaets-Short dreimal um ein Bild daneben — 19,03
statt 19,0000. Der Renderer schneidet mit `trim`, und `trim=0:19.03` nimmt
alles *kleiner als* 19,03; das Bild bei 19,0000 gehoert schon zur neuen
Einstellung, bekam aber den Ausschnitt der alten. Ein Bild, 128 px daneben —
im fertigen Short das Zittern, das er dreimal gemeldet hat.

Dieses Werkzeug sucht um jede Grenze herum das Bildpaar mit dem groessten
Unterschied und setzt die Grenze auf den Zeitstempel des ERSTEN Bildes der
neuen Einstellung. Dazu wird der Ruhepegel der Umgebung mitgemessen: liegt
der groesste Unterschied nicht deutlich darueber, ist an dieser Stelle gar
kein Kamerawechsel, und die Grenze bleibt, wie sie war (mit Hinweis).
"""
import argparse
import json

import av
import numpy as np


def bilder_um(pfad, mitte, fenster=0.6):
    """Alle Bilder in [mitte-fenster, mitte+fenster] als kleine Graubilder."""
    c = av.open(pfad)
    v = c.streams.video[0]
    von, bis = max(mitte - fenster, 0.0), mitte + fenster
    c.seek(int(max(von - 1.0, 0) / float(v.time_base)), stream=v)
    raus = []
    for f in c.decode(v):
        t = float(f.pts * v.time_base)
        if t > bis:
            break
        if t < von:
            continue
        g = f.to_ndarray(format="gray")
        raus.append((t, g[::8, ::8].astype(np.float32)))
    c.close()
    return raus


def grenze_messen(pfad, mitte, fenster=0.6, faktor=4.0):
    """Rueckgabe: (zeit, groesster_unterschied, ruhepegel) oder (None, ...)."""
    folge = bilder_um(pfad, mitte, fenster)
    if len(folge) < 3:
        return None, 0.0, 0.0
    unterschiede = [(folge[i + 1][0], float(np.abs(folge[i + 1][1] - folge[i][1]).mean()))
                    for i in range(len(folge) - 1)]
    werte = sorted(u for _, u in unterschiede)
    ruhe = float(np.median(werte[:max(len(werte) - 2, 1)]))
    zeit, groesster = max(unterschiede, key=lambda x: x[1])
    if groesster < max(faktor * ruhe, 2.0):
        return None, groesster, ruhe
    return zeit, groesster, ruhe


def main():
    p = argparse.ArgumentParser()
    p.add_argument("clip")
    p.add_argument("plan")
    p.add_argument("--aus", default=None, help="Vorgabe: den Plan ersetzen")
    p.add_argument("--fenster", type=float, default=0.6,
                   help="Suchbereich um jede Grenze, in Sekunden")
    a = p.parse_args()

    plan = json.loads(open(a.plan, encoding="utf-8").read())
    e = plan["einstellungen"]
    geaendert = 0
    for i in range(1, len(e)):
        alt = e[i]["start"]
        neu, gross, ruhe = grenze_messen(a.clip, alt, a.fenster)
        if neu is None:
            print(f"  Grenze {alt:8.4f}  KEIN Kamerawechsel gefunden "
                  f"(groesster Unterschied {gross:.2f}, Ruhepegel {ruhe:.2f}) "
                  f"— bleibt stehen")
            continue
        print(f"  Grenze {alt:8.4f}  ->  {neu:8.4f}  "
              f"({(neu - alt) * 30:+.1f} Bilder, Unterschied {gross:.1f} "
              f"gegen Ruhepegel {ruhe:.2f})")
        if abs(neu - alt) > 1e-6:
            geaendert += 1
        e[i - 1]["ende"] = neu
        e[i]["start"] = neu
    ziel = a.aus or a.plan
    open(ziel, "w", encoding="utf-8").write(json.dumps(plan, indent=1))
    print(f"  {geaendert} von {max(len(e) - 1, 0)} Grenzen verschoben  ->  {ziel}")


if __name__ == "__main__":
    main()
