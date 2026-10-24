#!/usr/bin/env python3
"""Ein langes Transkript in Fenstern — wiederaufnehmbar.

Eine 86-Minuten-Folge braucht auf dieser CPU mehr als eine Stunde. Der
Container wird in dieser Zeit mehrfach eingezogen, und ein Lauf, der alles
im Speicher haelt, verliert dann alles. Darum: je Fenster ein **eigener
Prozess**, je Fenster eine eigene JSON auf der Platte. Fertige Fenster
werden beim naechsten Start uebersprungen.

    python3 video/transkript_stueckweise.py --ton logan.flac \
            --dauer 5159 --out logan.segmente.json [--fenster 600]

Der Unterprozess bekommt `--nur <n>` und schreibt genau ein Fenster.

Zwei Dinge, die in dieser Werkstatt schon Material gekostet haben und
hier festgeschrieben sind:

* `condition_on_previous_text=False`. Mit der Vorgabe True liess Whisper
  bei wiederholter Rede ganze Passagen fallen — 170 Woerter statt 188 im
  selben Fenster.
* Ueberlappung. Ein hartes Fenster schneidet mitten im Satz; das Modell
  hoert den Anfang nicht und raet. Jedes Fenster hoert `--rand` Sekunden
  vorher mit; Segmente, die vor dem eigentlichen Fensteranfang enden,
  werden verworfen.
"""
import argparse, json, os, subprocess, sys, time

HIER = os.path.dirname(os.path.abspath(__file__))


def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}]", *a, flush=True)


def ton_lesen(pfad, von, dauer):
    """Fenster als float32-Array, 16 kHz mono — dekodiert mit ffmpeg.

    Nicht die Datei an faster-whisper geben: dessen `decode_audio` ruft
    `av.open(..., metadata_errors=...)`, was die hier installierte PyAV
    nicht kennt (TypeError am 24.10.). Wer selbst dekodiert, haengt auch
    nicht an der Auslegung von `clip_timestamps`.
    """
    import numpy as np, imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    roh = subprocess.run(
        [ff, "-nostdin", "-v", "error", "-ss", f"{von:.3f}", "-t",
         f"{dauer:.3f}", "-i", pfad, "-ac", "1", "-ar", "16000",
         "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype="<f4").copy()


def ein_fenster(a):
    """Ein Fenster transkribieren und als JSON ablegen."""
    von = a.nur * a.fenster
    bis = min(von + a.fenster, a.dauer)
    rand = min(a.rand, von)
    ton = ton_lesen(a.ton, von - rand, (bis - von) + rand)
    if len(ton) < 16000:
        log(f"Fenster {a.nur}: nur {len(ton) / 16000:.1f}s Ton gelesen")
        return 1
    from faster_whisper import WhisperModel
    m = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=4)
    segs, _ = m.transcribe(
        ton, language=a.lang, vad_filter=True,
        condition_on_previous_text=False, word_timestamps=True)
    # Die Zeiten kommen ab Null des Fensters zurueck; hier auf Dateizeit
    # zurueckrechnen, einmal und an einer Stelle.
    null = von - rand
    raus = []
    for s in segs:
        if s.end + null + 1e-6 < von:   # liegt im Vorlauf, gehoert ins Fenster davor
            continue
        raus.append({"start": s.start + null, "end": s.end + null,
                     "text": s.text.strip(),
                     "woerter": [{"start": w.start + null, "end": w.end + null,
                                  "wort": w.word} for w in (s.words or [])]})
    ziel = f"{a.out}.f{a.nur:03d}"
    with open(ziel, "w", encoding="utf-8") as f:
        json.dump({"von": von, "bis": bis, "segmente": raus}, f,
                  ensure_ascii=False)
    log(f"Fenster {a.nur}: {von:.0f}-{bis:.0f}s, {len(raus)} Segmente")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ton", required=True)
    ap.add_argument("--dauer", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fenster", type=float, default=600.0)
    ap.add_argument("--rand", type=float, default=15.0)
    ap.add_argument("--model", default="medium")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--nur", type=int, default=None)
    a = ap.parse_args()

    if a.nur is not None:
        return ein_fenster(a)

    anzahl = int(a.dauer // a.fenster) + (1 if a.dauer % a.fenster else 0)
    for n in range(anzahl):
        ziel = f"{a.out}.f{n:03d}"
        if os.path.exists(ziel) and os.path.getsize(ziel) > 2:
            log(f"Fenster {n} liegt schon")
            continue
        r = subprocess.run([sys.executable, os.path.abspath(__file__),
                            "--ton", a.ton, "--dauer", str(a.dauer),
                            "--out", a.out, "--fenster", str(a.fenster),
                            "--rand", str(a.rand), "--model", a.model,
                            "--lang", a.lang, "--nur", str(n)])
        if r.returncode != 0 or not os.path.exists(ziel):
            log(f"Fenster {n} fehlgeschlagen — beim naechsten Lauf erneut")
            return 1

    # Zusammenfuegen. Die Zeiten sind schon absolut — `ein_fenster` rechnet
    # den Fensteranfang drauf, bevor es schreibt.
    alle, leer = [], []
    for n in range(anzahl):
        teil = json.load(open(f"{a.out}.f{n:03d}", encoding="utf-8"))
        if not teil["segmente"]:
            leer.append(n)
        alle += teil["segmente"]
    alle.sort(key=lambda s: s["start"])
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(alle, f, ensure_ascii=False, indent=1)

    woerter = sum(len(s["woerter"]) for s in alle)
    ende = alle[-1]["end"] if alle else 0
    log(f"fertig: {a.out} — {len(alle)} Segmente, {woerter} Woerter, "
        f"bis {ende / 60:.1f} min von {a.dauer / 60:.1f} min")
    if leer:
        log(f"WARNUNG: leere Fenster {leer} — dort wurde nichts erkannt")
    if ende < a.dauer - 120:
        log(f"FEHLER: Transkript endet {a.dauer - ende:.0f}s vor dem Ton")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
