#!/usr/bin/env python3
"""Einen Clip aus Quellstuecken zusammensetzen - Bild und Ton getrennt.

Warum getrennt: an einer Naht, die mitten in einer Einstellung liegt, ist
jeder Bildschnitt ein Sprung. Unsichtbar wird er, wenn der Bildschnitt auf
einen Kamerawechsel faellt und der Ton darueber weiterlaeuft (J-Schnitt).
Dafuer muessen Bild und Ton verschiedene Schnittpunkte haben duerfen.

Zwei Regeln sind fest eingebaut, beide aus seinen Befunden:

* **Keine Bildblende innerhalb derselben Einstellung.** Eine Blende von
  0,13 s hat am 22.10.2026 zwei Momente desselben Gesichts ineinander
  geblendet - sein Befund: "einfach richtig schlecht geschnitten". Bild wird
  hier immer hart geschnitten.
* **20-ms-Tonblenden an jeder Naht.** Ohne sie knackt es. Gemessen: an einer
  harten Tonnaht sprang das Signal um 0,13 (-17,7 dBFS), mit Blende liegt die
  Naht bei -85 dB.

Der Plan ist eine JSON-Datei und zugleich das Protokoll des Schnitts:

    {"quelle": "src2.mp4",
     "bild": [[0.600, 3.600], [8.8667, 15.0]],
     "ton":  [[0.600, 4.000], [9.2667, 15.0]],
     "tonblende_s": 0.02}

Bild- und Tonsumme muessen gleich lang sein, sonst laeuft die Lippensynchronitaet
auseinander; das wird geprueft, nicht geglaubt.

    python3 video/schnitt_bauen.py plan.json ziel.mp4
"""
import json
import subprocess
import sys
from pathlib import Path


def summe(stuecke):
    return sum(b - a for a, b in stuecke)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    plan = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    ziel = sys.argv[2]
    quelle = plan["quelle"]
    bild, ton = plan["bild"], plan["ton"]
    blende = plan.get("tonblende_s", 0.02)

    db, dt = summe(bild), summe(ton)
    if abs(db - dt) > 0.002:
        sys.exit(f"Bild {db:.4f} s und Ton {dt:.4f} s sind verschieden lang - "
                 f"das laeuft auseinander. Plan korrigieren.")

    # Jede Bildgrenze muss auf einem Bild liegen, und die herausgenommene
    # Laenge muss eine GANZE Zahl von Bildern sein. Am 26.10.2026 teuer
    # gelernt: 3,29 s sind 98,7 Bilder. Der Schnitt selbst sah sauber aus,
    # aber jede Einstellungsgrenze DAHINTER lag danach zwischen zwei Bildern,
    # und der Renderer gab dem Grenzbild den Ausschnitt der falschen
    # Einstellung - an vier Grenzen standen wieder zwei Bildspruenge statt
    # einem. Genau der Fehler, den er am 24.10. dreimal gemeldet hat.
    bilder = plan.get("bilder_je_sekunde", 30)
    schief = []
    for a, b in bild:
        for t in (a, b):
            if abs(t * bilder - round(t * bilder)) > 0.01:
                schief.append(t)
    if abs(db * bilder - round(db * bilder)) > 0.01:
        schief.append(db)
    if schief:
        sys.exit("Diese Zeiten liegen nicht auf einem Bild (bei "
                 f"{bilder} Bildern/s): "
                 + ", ".join(f"{t:.4f} = Bild {t * bilder:.2f}" for t in schief)
                 + "\nDas faellt am Schnitt selbst nicht auf, verschiebt aber "
                   "jede Einstellungsgrenze dahinter zwischen zwei Bilder. "
                   "Auf ein Vielfaches von 1/%d runden." % bilder)

    teile, enden = [], []
    for i, (a, b) in enumerate(bild):
        teile.append(f"[0:v]trim={a:.4f}:{b:.4f},setpts=PTS-STARTPTS[v{i}]")
    for i, (a, b) in enumerate(ton):
        d = b - a
        f = min(blende, d / 3)
        # Blende am Anfang nur, wenn ein Stueck davor war; am Ende nur, wenn
        # eines folgt - sonst schneidet man sich den Ein- und Ausstieg ab.
        kette = [f"[0:a]atrim={a:.4f}:{b:.4f}", "asetpts=PTS-STARTPTS"]
        if i > 0:
            kette.append(f"afade=t=in:st=0:d={f:.4f}")
        if i < len(ton) - 1:
            kette.append(f"afade=t=out:st={d - f:.4f}:d={f:.4f}")
        teile.append(",".join(kette) + f"[a{i}]")
        enden.append(d)

    v = "".join(f"[v{i}]" for i in range(len(bild)))
    a = "".join(f"[a{i}]" for i in range(len(ton)))
    teile.append(f"{v}concat=n={len(bild)}:v=1:a=0[vv]")
    teile.append(f"{a}concat=n={len(ton)}:v=0:a=1[aa]")

    befehl = ["ffmpeg", "-nostdin", "-v", "error", "-stats", "-i", quelle,
              "-filter_complex", ";".join(teile),
              "-map", "[vv]", "-map", "[aa]",
              "-c:v", "libx264", "-preset", "medium", "-crf", "16",
              "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
              ziel, "-y"]
    print(f"Bild {db:.4f} s in {len(bild)} Stuecken · "
          f"Ton {dt:.4f} s in {len(ton)} Stuecken · Blende {blende * 1000:.0f} ms")
    subprocess.run(befehl, check=True)
    print(f"-> {ziel}")


if __name__ == "__main__":
    main()
