#!/usr/bin/env python3
"""Sein Outro hinten anhaengen - gehoert hinter JEDEN Short.

Seine Ansage vom 22.10.2026: *„du vergisst jetzt schon wieder mein Outro.
Wo ist mein Outro? Das gehoert hinter jedes Short."* Es stand als Flag im
Renderer (`--outro`), wurde aber nie gesetzt.

Warum als eigener Schritt und nicht ueber `--outro`: das Musikbett kommt im
Renderer VOR dem Outro in die Kette, bei uns aber erst nach dem Rendern
(`musik_drunter.py`, spart das zweite Transkribieren). Haengt man das Outro
schon beim Rendern an, liegt das Bett hinterher auch darueber. Also:
rendern, Bett drunter, danach das Outro.

    python3 video/outro_anhaengen.py <haupt.mp4> <outro.mov> <ausgabe.mp4> [--kopie]

`--kopie` rechnet den Hauptteil NICHT neu durch: es wird nur das Outro auf
dieselben Werte kodiert und danach aneinandergehaengt, das Bild des
Hauptteils kopiert. Der Ton wird trotzdem neu kodiert, in einem Stueck ueber
beide Teile - AAC haengt an jeden Abschnitt Vor- und Nachlauf, und beim
blossen Kopieren sitzt genau das als Luecke oder Knacken an der Naht.

Warum das ueberhaupt gebaut wurde: seit dem 24.10. liegt die Ausgabe auf
2160x3840. Dieser Schritt kodierte den ganzen Short ein zweites Mal - bei 4K
sind das rund 25 Minuten und eine zweite Generation Qualitaetsverlust fuer
4,21 Sekunden Outro. Mit `--kopie` dauert es eine Minute, und der Hauptteil
bleibt Bit fuer Bit der gerenderte.

Das Outro behaelt seinen eigenen Ton und bekommt weder Look noch Logo noch
Untertitel - genauso wie im Renderer. Es wird auf die Bildgroesse des
Hauptteils und auf 30 Bilder gebracht, falls es abweicht.

Die Groesse wird am Hauptteil GEMESSEN und nicht mehr fest auf 1080x1920
gesetzt: seit dem 24.10.2026 liefert der Renderer 2160x3840, und ein fester
Wert hier haette den fertigen Short wieder auf ein Viertel der Pixel
gerechnet. Auch der zweite Durchgang laeuft jetzt auf `-preset medium -crf
18` statt `veryfast`: dieser Schritt rechnet den ganzen Short ein zweites
Mal durch, und `veryfast` hat dabei mehr weggeworfen als noetig.
"""
import os
import re
import subprocess
import sys

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def bildgroesse(pfad):
    """Bildgroesse des Hauptteils lesen - danach richtet sich alles andere."""
    r = subprocess.run([FF, "-hide_banner", "-i", pfad],
                       capture_output=True, text=True)
    for zeile in r.stderr.splitlines():
        if " Video:" in zeile:
            m = re.search(r"\b(\d{2,5})x(\d{2,5})\b", zeile)
            if m:
                return int(m.group(1)), int(m.group(2))
    raise SystemExit(f"Konnte die Bildgroesse von {pfad} nicht lesen.")


def outro_anpassen(outro, W, H, ziel):
    """Das Outro allein auf die Werte des Hauptteils bringen."""
    graph = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
             f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,"
             f"format=yuv420p[v]")
    subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                    "-i", outro, "-filter_complex", graph, "-map", "[v]",
                    "-map", "0:a",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-ac", "2", ziel], check=True)


def anhaengen_kopie(haupt, outro, ziel, W, H):
    """Bild kopieren, Ton in einem Stueck neu kodieren."""
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        o = f"{td}/outro.mp4"
        outro_anpassen(outro, W, H, o)
        liste = f"{td}/liste.txt"
        with open(liste, "w", encoding="utf-8") as f:
            for teil in (haupt, o):
                f.write("file '" + os.path.abspath(teil).replace("'", "'\\''") + "'\n")
        subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                        "-f", "concat", "-safe", "0", "-i", liste,
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-ar", "48000", "-ac", "2",
                        "-movflags", "+faststart", ziel], check=True)


def dauer(p):
    r = subprocess.run([FF, "-hide_banner", "-i", p], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def bericht(haupt, outro, ziel, W, H, wie):
    soll = dauer(haupt) + dauer(outro)
    ist = dauer(ziel)
    print(f"  {dauer(haupt):.2f} s + {dauer(outro):.2f} s Outro "
          f"= {ist:.2f} s, {W}x{H} ({wie})  ->  {ziel}")
    if abs(ist - soll) > 0.1:
        print(f"  ACHTUNG: erwartet waren {soll:.2f} s, es sind {ist:.2f} s — "
              f"{ist - soll:+.2f} s. Die Naht pruefen.")


def main():
    argv = sys.argv[1:]
    kopie = "--kopie" in argv
    if kopie:
        argv.remove("--kopie")
    if len(argv) != 3:
        sys.exit(__doc__)
    haupt, outro, ziel = argv
    W, H = bildgroesse(haupt)
    if kopie:
        anhaengen_kopie(haupt, outro, ziel, W, H)
        bericht(haupt, outro, ziel, W, H, "Bild kopiert, Ton neu")
        return
    graph = (
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,format=yuv420p[v0];"
        f"[0:a]aformat=sample_fmts=fltp:sample_rates=48000:"
        f"channel_layouts=stereo[a0];"
        f"[1:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,format=yuv420p[v1];"
        f"[1:a]aformat=sample_fmts=fltp:sample_rates=48000:"
        f"channel_layouts=stereo[a1];"
        f"[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]"
    )
    subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                    "-i", haupt, "-i", outro, "-filter_complex", graph,
                    "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "192k", ziel], check=True)

    bericht(haupt, outro, ziel, W, H, "alles neu kodiert")


if __name__ == "__main__":
    main()
