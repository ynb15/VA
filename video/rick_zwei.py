#!/usr/bin/env python3
"""Rick Strassman zweimal rechnen: mit seinen „you know"s und ohne.

Sein Auftrag vom 21.10.: „dann gib mir doch mal jetzt nochmal die Vision.
Einmal, mit seinen 16 You-Knows und einmal ohne."

**Wiederaufnehmbar.** Der Container wird eingezogen, sobald ein Zug endet;
ein laufender Prozess stirbt mit ihm, die Dateien bleiben. Darum erkennt
dieses Skript am Dateistand, was schon fertig ist, macht nur den naechsten
offenen Schritt und laesst sich beliebig oft neu starten.

  python3 video/rick_zwei.py [--ordner ...]
"""
import argparse, json, os, subprocess, sys, time

HIER = os.path.dirname(os.path.abspath(__file__))
# Der Ausschnitt und die Lippenhoehe sind an seiner Folge ausgemessen
# (Webcam, 21.10.): Kasten im 1920er Quellbild, Zeile auf 965 im
# Ausgabebild — nicht die 70 % aus dem Preset, die gelten nur, wenn
# nichts gemessen ist.
KASTEN, LIPPE = "780:14:528:939", 965
TEMPO = 1.15


def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}]", *a, flush=True)


def dauer(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", p]).decode().strip())


def fertig(p, mindest=1_000_000):
    return os.path.exists(p) and os.path.getsize(p) > mindest


def plan_schreiben(quelle, ziel):
    plan = {"quelle": quelle, "groesse": [1920, 1080],
            "einstellungen": [{"layout": "einzel", "kasten": KASTEN,
                               "lippe": LIPPE, "start": 0.0,
                               "ende": round(dauer(quelle), 2), "tot": False}]}
    with open(ziel, "w") as f:
        json.dump(plan, f, indent=1)
    return ziel


def rendern(quelle, ziel, srt_out, logo):
    plan = plan_schreiben(quelle, ziel.replace(".mp4", "_plan.json"))
    cmd = [sys.executable, os.path.join(HIER, "shorts-render.py"),
           "--src", quelle, "--out", ziel, "--plan", plan,
           "--auto-captions", "--model", "medium", "--lang", "en",
           "--tempo", str(TEMPO), "--srt-out", srt_out,
           "--korrekturen", os.path.join(HIER, "korrekturen.txt")]
    if logo and os.path.exists(logo):
        cmd += ["--logo", logo]
    log("rendere", os.path.basename(ziel))
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ordner", required=True, help="Arbeitsordner mit rick4_mit.mp4")
    ap.add_argument("--logo", default=os.path.join(HIER, "marke", "ynb-logo-weiss.png"))
    a = ap.parse_args()
    o = a.ordner

    mit = os.path.join(o, "rick4_mit.mp4")
    ohne = os.path.join(o, "rick4_ohne.mp4")
    if not fertig(mit):
        sys.exit(f"fehlt: {mit}")

    # 1) Fuellwoerter wortweise entfernen
    if not fertig(ohne):
        log("entferne Fuellwoerter aus rick4_mit.mp4")
        subprocess.run([sys.executable, os.path.join(HIER, "fuellwoerter.py"),
                        "--clip", mit, "--out", ohne], check=True)
    else:
        log("rick4_ohne.mp4 liegt schon da")
    log(f"Laengen: mit {dauer(mit):.1f}s, ohne {dauer(ohne):.1f}s, "
        f"fertig bei Tempo {TEMPO}: {dauer(mit)/TEMPO:.1f}s / {dauer(ohne)/TEMPO:.1f}s")

    # 2) beide Fassungen rendern
    for quelle, name in ((mit, "07-rick-mit"), (ohne, "07-rick-ohne")):
        ziel = os.path.join(o, f"{name}.mp4")
        if fertig(ziel):
            log(f"{name}.mp4 liegt schon da")
            continue
        rendern(quelle, ziel, os.path.join(o, f"{name}.srt"), a.logo)

    log("fertig:", ", ".join(sorted(f for f in os.listdir(o)
                                    if f.startswith("07-rick"))))


if __name__ == "__main__":
    main()
