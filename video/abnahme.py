#!/usr/bin/env python3
"""Abnahme eines fertigen Shorts — bevor er an Yannick geht.

Sein Einwand vom 22.10.2026: *„Ich verstehe nicht, warum hier immer wieder
dieselben Fehler passieren bei unterschiedlichen Agenten."* Die Antwort ist
unangenehm einfach: es gab keine Liste. Jeder hat sich das Schwierige
gemerkt und das Selbstverstaendliche vergessen — Outro, Logogroesse,
Tonquelle.

Geprueft wird, was sich messen laesst. Was nur das Auge sieht, steht am
Ende als Liste da und wird nicht als „bestanden" ausgegeben.

    python3 video/abnahme.py short.mp4 [--srt short.srt] [--outro marke/ynb-outro-9-16.mp4]

Rueckgabe 1, sobald eine Pruefung fehlschlaegt.
"""
import argparse, os, subprocess, sys

HIER = os.path.dirname(os.path.abspath(__file__))


def ff(args):
    return subprocess.run(args, capture_output=True, text=True).stdout.strip()


def probe(pfad, eintrag, strom=None):
    cmd = ["ffprobe", "-v", "error"]
    if strom:
        cmd += ["-select_streams", strom]
    cmd += ["-show_entries", eintrag, "-of", "csv=p=0", pfad]
    return ff(cmd)


def bild(pfad, t, ziel, breite=96):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(t),
                    "-i", pfad, "-frames:v", "1", "-vf", f"scale={breite}:-1",
                    ziel], check=True)


def abstand(a, b):
    """Mittlere absolute Differenz zweier Bilder, 0..255."""
    from PIL import Image
    ia, ib = Image.open(a).convert("L"), Image.open(b).convert("L")
    if ia.size != ib.size:
        ib = ib.resize(ia.size)
    da, db = list(ia.tobytes()), list(ib.tobytes())
    return sum(abs(x - y) for x, y in zip(da, db)) / len(da)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("short")
    p.add_argument("--srt", default=None)
    p.add_argument("--outro", default=os.path.join(HIER, "marke", "ynb-outro-9-16.mp4"))
    p.add_argument("--tmp", default="/tmp")
    a = p.parse_args()

    fehler = []

    def pruef(name, ok, text):
        print(f"  {'ok  ' if ok else 'FEHLT'}  {name}: {text}")
        if not ok:
            fehler.append(name)

    print(f"Abnahme {os.path.basename(a.short)}")

    groesse = probe(a.short, "stream=width,height", "v")
    pruef("Format", groesse.replace(" ", "") == "1080,1920", groesse or "nicht lesbar")

    rate = probe(a.short, "stream=sample_rate", "a")
    pruef("Tonquelle", rate == "48000",
          f"{rate} Hz" + ("" if rate == "48000"
                          else "  <- 44100 Hz heisst Kameramikrofon statt Mischung"))

    dauer = float(probe(a.short, "format=duration") or 0)
    pruef("Laufzeit", 0 < dauer <= 180,
          f"{dauer:.1f}s" + ("" if dauer <= 180 else "  <- ueber dem Shorts-Limit"))

    # Outro: das letzte Bild des Shorts gegen das letzte Bild des Outros
    if os.path.exists(a.outro):
        od = float(probe(a.outro, "format=duration") or 0)
        s_bild = os.path.join(a.tmp, "_ab_s.png")
        o_bild = os.path.join(a.tmp, "_ab_o.png")
        bild(a.short, max(dauer - 0.4, 0), s_bild)
        bild(a.outro, max(od - 0.4, 0), o_bild)
        d = abstand(s_bild, o_bild)
        pruef("Outro", d < 12, f"Abstand zum Outro-Schlussbild {d:.1f} (unter 12 = da)")
    else:
        pruef("Outro", False, f"Referenz fehlt: {a.outro}")

    if a.srt:
        n = sum(1 for z in open(a.srt, encoding="utf-8") if "-->" in z)
        pruef("Untertitel", n > 0, f"{n} Einblendungen")
        orts = subprocess.run([sys.executable, os.path.join(HIER, "ortscheck.py"), a.srt],
                              capture_output=True, text=True)
        pruef("Ortscheck", orts.returncode == 0,
              "sauber" if orts.returncode == 0 else orts.stdout.strip().splitlines()[-1])
    else:
        pruef("Untertitel", False, "keine .srt uebergeben (--srt)")

    print("\n  Mit dem Auge, nicht gemessen:")
    for z in ("Logo gross genug und an seiner Stelle",
              "Untertitel unter der Lippe, nicht auf dem Kinn",
              "Anfang auf einer Wortgrenze, Schluss auf einem Satzende",
              "Ton angehoert, nicht nur die Pegel angesehen"):
        print(f"    [ ] {z}")

    if fehler:
        print(f"\n{len(fehler)} Pruefung(en) fehlgeschlagen: {', '.join(fehler)}")
        return 1
    print("\nAlles Messbare bestanden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
