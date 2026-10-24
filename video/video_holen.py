#!/usr/bin/env python3
"""Ein Bild-und-Ton-Fenster aus einer grossen Drive-Datei holen.

    python3 video/video_holen.py --id <drive-id> --groesse <bytes> \
            --von 16 --bis 90 --out fenster.mp4

Das Gegenstueck zu `ton_holen.py`: dort geht es um die ganze Tonspur, hier
um ein kurzes Fenster mit Bild. Die Pakete werden **kopiert**, nicht neu
kodiert — das haelt die geholten Bytes bei dem, was das Fenster wirklich
braucht, und kostet keine Rechenzeit.

Zwei Dinge, die hier eingebaut sind, weil sie schon Material gekostet haben:

* **Vorlauf bis zum Schluesselbild.** Beim Kopieren von Paketen kann nur an
  einem Schluesselbild angefangen werden. Das Fenster beginnt darum frueher,
  und die Datei traegt in `<out>.json`, ab welcher Sekunde der Quelle sie
  wirklich laeuft. Der genaue Schnitt passiert danach lokal — da kostet er
  nichts mehr.
* **Zeiten auf Null.** Die Pakete behalten in der Quelle ihre absoluten
  Zeitstempel. Wird das uebernommen, sucht jedes spaetere Werkzeug an der
  falschen Stelle (am 22.10. einmal passiert). Hier faengt die Datei bei 0 an.
"""
import argparse, json, os, sys, time
from pathlib import Path

import av

sys.path.insert(0, str(Path(__file__).resolve().parent))
from drive_fernzugriff import DriveDatei, bestaetigte_url


def holen(file_id, ziel, von, bis, groesse=None, melden=10.0):
    quelle = DriveDatei(bestaetigte_url(file_id), groesse=groesse)
    ein = av.open(quelle)
    v_ein = next(s for s in ein.streams if s.type == "video")
    a_ein = next((s for s in ein.streams if s.type == "audio"), None)

    # Vor den Fensteranfang springen; der Demuxer landet auf dem letzten
    # Schluesselbild davor.
    ein.seek(int(max(0.0, von - 0.5) / v_ein.time_base), stream=v_ein)

    aus = av.open(str(ziel), "w")
    v_aus = aus.add_stream_from_template(v_ein)
    a_aus = aus.add_stream_from_template(a_ein) if a_ein else None

    wanne = {v_ein: v_aus}
    if a_ein:
        wanne[a_ein] = a_aus

    anfang = None            # Quellzeit des ersten uebernommenen Pakets
    t0 = zuletzt = time.time()
    letzte = 0.0
    for p in ein.demux(list(wanne)):
        if p.dts is None:
            continue
        t = float(p.pts if p.pts is not None else p.dts) * float(p.time_base)
        if t > bis:
            if p.stream is v_ein:
                break
            continue
        if anfang is None:
            if p.stream is not v_ein or not p.is_keyframe:
                continue
            anfang = t
        versatz = int(anfang / float(p.time_base))
        p.pts = (p.pts - versatz) if p.pts is not None else None
        p.dts = p.dts - versatz
        p.stream = wanne[p.stream]
        aus.mux(p)
        letzte = t
        if time.time() - zuletzt > melden:
            zuletzt = time.time()
            print(f"  {t - anfang:.0f}s im Fenster, "
                  f"{(time.time() - t0) / 60:.1f} min", flush=True)

    aus.close()
    ein.close()
    if anfang is None:
        print("FEHLER: kein Schluesselbild im Fenster gefunden")
        return None
    Path(str(ziel) + ".json").write_text(json.dumps(
        {"quelle": file_id, "laeuft_ab": anfang, "bis": letzte,
         "angefragt_von": von, "angefragt_bis": bis,
         "vorlauf": round(von - anfang, 3)}, indent=1), encoding="utf-8")
    print(f"{ziel} — laeuft ab Quellzeit {anfang:.3f}s "
          f"(Vorlauf {von - anfang:.3f}s), bis {letzte:.3f}s, "
          f"{os.path.getsize(ziel) / 1e6:.1f} MB")
    return anfang


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--groesse", type=int, default=None)
    ap.add_argument("--von", type=float, required=True)
    ap.add_argument("--bis", type=float, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    return 0 if holen(a.id, a.out, a.von, a.bis, a.groesse) is not None else 1


if __name__ == "__main__":
    sys.exit(main())
