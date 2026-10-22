#!/usr/bin/env python3
"""Die Tonspur eines grossen Drive-Masters in Stuecken holen — wiederaufnehmbar.

Am 22.10.2026 starb ein Zug ueber einen 27-GB-Master nach fuenf Minuten:
der Container wurde eingezogen, der Proxy bekam einen neuen Port, und der
laufende Prozess lief ins Leere. Ein sequentieller Lauf ueber eine Stunde
ueberlebt das nie.

Hier wird je Stueck ein **eigener Prozess** gestartet — frischer Proxy,
frische Verbindung. Fertige Stuecke bleiben liegen und werden beim naechsten
Start uebersprungen. Am Ende werden sie zu einer FLAC zusammengefuegt.

    python3 video/ton_stueckweise.py --id <drive-id> --groesse <bytes> \
            --dauer 6150 --out ton.flac [--stueck 600]
"""
import argparse, os, subprocess, sys, time

HIER = os.path.dirname(os.path.abspath(__file__))


def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}]", *a, flush=True)


def laenge(pfad):
    try:
        return float(subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", pfad]).decode().strip())
    except Exception:
        return 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--groesse", type=int, default=None)
    ap.add_argument("--dauer", type=float, required=True,
                    help="Laufzeit der Folge in Sekunden (grob genuegt)")
    ap.add_argument("--stueck", type=float, default=600.0)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rate", type=int, default=16000)
    a = ap.parse_args()

    ordner = os.path.dirname(os.path.abspath(a.out))
    marke = os.path.splitext(os.path.basename(a.out))[0]
    teile, n = [], 0
    von = 0.0
    while von < a.dauer:
        bis = min(von + a.stueck, a.dauer)
        t = os.path.join(ordner, f"{marke}_t{n:03d}.flac")
        teile.append(t)
        soll = bis - von
        da = laenge(t)
        if da >= soll * 0.97:
            log(f"Stueck {n} liegt schon da ({da:.0f}s)")
        else:
            if os.path.exists(t):
                log(f"Stueck {n} unvollstaendig ({da:.0f}s statt {soll:.0f}s), neu")
                os.remove(t)
            log(f"Stueck {n}: {von:.0f}-{bis:.0f}s")
            r = subprocess.run(
                [sys.executable, os.path.join(HIER, "ton_holen.py"),
                 "--id", a.id, "--out", t, "--rate", str(a.rate),
                 "--von", str(von), "--bis", str(bis)]
                + (["--groesse", str(a.groesse)] if a.groesse else []))
            if r.returncode != 0 or laenge(t) < soll * 0.97:
                log(f"Stueck {n} fehlgeschlagen — beim naechsten Lauf erneut")
                return 1
        von, n = bis, n + 1

    liste = os.path.join(ordner, f"{marke}_teile.txt")
    with open(liste, "w") as f:
        for t in teile:
            f.write(f"file '{t}'\n")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "concat",
                    "-safe", "0", "-i", liste, "-c", "copy", a.out], check=True)
    log(f"fertig: {a.out} — {laenge(a.out) / 60:.1f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())
