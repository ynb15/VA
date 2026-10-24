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
import argparse, os, re, subprocess, sys

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()

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

    # Dateiname, seine Ansage vom 22.10.: „YNB Podcast und dann der Name und
    # dann halt ein Stichwort zu dem Inhalt". Das Stichwort ist EIN Wort und
    # sagt, welche Stelle es ist. Nebenfassungen in Klammern dahinter, damit
    # der Grundname gleich bleibt.
    name = os.path.basename(a.short)
    passt = re.match(r"^YNB Podcast .+? \S+( \(.+\))?\.(mp4|mov)$", name)
    pruef("Dateiname", bool(passt),
          name if passt else f"{name}  <- erwartet: "
          f"YNB Podcast <Gast> <Stichwort>.mp4")

    # Musikbett. Vier Sperrmeldungen an einem Tag, drei Titel, auch ein
    # Klaviercover — die Sperre haengt an der Komposition, nicht an der
    # Aufnahme. Ein durchlaufendes Bett haelt die Laengengrenze nie ein.
    # Messbar ist es am Pegel in den Sprechpausen: in den sauberen Fassungen
    # liegen 12 bis 20 Prozent aller 20-ms-Fenster unter -55 dB, unter einem
    # Bett faellt der Boden dort nie hin. Das Outro bleibt aussen vor, es
    # hat seinen eigenen Ton.
    bis = max(dauer - 4.5, 1.0)
    roh = subprocess.run([FF, "-nostdin", "-v", "quiet", "-t", f"{bis:.2f}",
                          "-i", a.short, "-f", "f32le", "-ac", "1",
                          "-ar", "16000", "-"], capture_output=True).stdout
    if roh:
        import numpy as np
        t = np.frombuffer(roh, dtype=np.float32)
        f = t[:len(t) // 320 * 320].reshape(-1, 320)
        pegel = 20 * np.log10(np.maximum(np.sqrt((f ** 2).mean(axis=1)), 1e-9))
        boden = float(np.percentile(pegel, 1))
        # Nicht der Anteil leiser Fenster, sondern wie tief es in den
        # Sprechpausen ueberhaupt wird. Nachgemessen: saubere Fassungen
        # liegen im leisesten Prozent bei -78 bis -89 dB. Mit einem
        # untergelegten Bett bei -58 — und das war ein absichtlich leises
        # Testbett; ein hoerbares liegt bei -30 bis -40. Der Anteil unter
        # -55 dB taugte dafuer nicht: er fiel von 13,6 auf 11,3 Prozent und
        # haette das Bett durchgelassen.
        # Der Pegel allein sagt nicht, WAS da leise liegt. Am 24.10. fiel
        # ein Short mit -64,7 dB durch, ein anderer aus derselben Folge kam
        # mit -65,4 dB durch — der Unterschied war, dass in dem einen 45
        # Sekunden ohne Sprechpause geredet wird. Darum wird zusaetzlich
        # berichtet, wie der leise Boden klingt: die spektrale Flachheit der
        # leisesten Fenster. Raumton ist breitbandig, ein Musikbett ist
        # tonal. Das ist eine ANGABE, kein Freispruch: das Urteil bleibt am
        # Pegel, und im Zweifel entscheidet sein Ohr.
        leise = f[pegel <= float(np.percentile(pegel, 3))]
        flach = float("nan")
        if len(leise):
            S = np.abs(np.fft.rfft(leise * np.hanning(320), axis=1)) ** 2 + 1e-20
            S = S.mean(axis=0)[1:]
            flach = float(np.exp(np.log(S).mean()) / S.mean())
        pruef("Kein Musikbett", boden <= -65.0,
              f"leisestes Prozent bei {boden:.1f} dB, Flachheit {flach:.3f}"
              + ("" if boden <= -65.0 else "  <- zu laut fuer Raumton; "
                 "Flachheit deutlich unter den sauberen Fassungen "
                 "(0,077-0,089) hiesse zusaetzlich tonal"))
    else:
        pruef("Kein Musikbett", False, "Tonspur nicht lesbar")

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
        ortspfad = os.path.join(HIER, "ortscheck.py")
        if not os.path.exists(ortspfad):
            # Shorts II hat genau hier einen IndexError gesehen: liegt
            # ortscheck.py nicht daneben, lief der Aufruf ins Leere, stdout
            # blieb leer, und `.splitlines()[-1]` griff auf eine leere Liste.
            # Eine fehlende Pruefung darf die Abnahme nicht abstuerzen
            # lassen — sie muss sagen, dass sie fehlt.
            pruef("Ortscheck", False, f"ortscheck.py fehlt neben {os.path.basename(__file__)}")
        else:
            orts = subprocess.run([sys.executable, ortspfad, a.srt],
                                  capture_output=True, text=True)
            meldung = (orts.stdout.strip().splitlines() or
                       orts.stderr.strip().splitlines() or ["ohne Ausgabe"])[-1]
            pruef("Ortscheck", orts.returncode == 0,
                  "sauber" if orts.returncode == 0 else meldung)
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
