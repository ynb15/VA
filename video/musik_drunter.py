#!/usr/bin/env python3
"""Legt das Musikbett unter einen fertigen Short - gleiche Kette wie der Renderer.

    python3 musik_drunter.py <video.mp4> <musik.mp3> <ausgabe-stamm> <dB-unter> ...

Je angegebenem Abstand entsteht eine Fassung. Der Pegel wird nicht geraten,
sondern aus Stimme und Bett gerechnet, genauso wie in `shorts-render.py`:
`db = stimme_db - bett_db - abstand`. Danach laeuft dieselbe Kette --
geloopt, 1,5 s eingeblendet, 2 s ausgeblendet, per `sidechaincompress` von
der Stimme weggedrueckt und mit `normalize=0` gemischt.

Kein `loudnorm`, kein Limiter: seine Ansage vom 20.10. gilt weiter.
"""
import importlib.util, subprocess, sys
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
# Argumente sichern, BEVOR shorts-render.py geladen wird: das Modul wertet
# beim Import sein eigenes argparse aus, darum wird sys.argv dafuer geleert.
ARGV = list(sys.argv)
spec = importlib.util.spec_from_file_location("sr", "/home/user/VA/video/shorts-render.py")
sr = importlib.util.module_from_spec(spec)
sys.argv = ["x"]
try:
    spec.loader.exec_module(sr)
except SystemExit:
    pass


def dauer(pfad):
    p = subprocess.run([FF, "-hide_banner", "-i", pfad], capture_output=True, text=True)
    import re
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", p.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def main():
    video, musik, stamm = ARGV[1], ARGV[2], ARGV[3]
    abstaende = [float(x) for x in ARGV[4:]]
    laenge = dauer(video)
    stimme_db = sr.mittlerer_pegel(video, dauer=laenge)
    bett_db = sr.mittlerer_pegel(musik, dauer=laenge)
    print(f"Stimme {stimme_db:.1f} dB · Bett {bett_db:.1f} dB · Laenge {laenge:.2f} s")
    for ab in abstaende:
        db = round(stimme_db - bett_db - ab, 1)
        out = f"{stamm}-{int(ab)}db.mp4"
        bett = (f"[1:a]aloop=loop=-1:size=2000000000,volume={db}dB,"
                f"afade=t=in:st=0:d=1.5,atrim=0:{laenge:.2f},"
                f"afade=t=out:st={max(laenge - 2.0, 0):.2f}:d=2.0[bett]")
        graph = ("[0:a]asplit=2[st1][st2];" + bett +
                 ";[bett][st2]sidechaincompress=threshold=0.04:ratio=8:"
                 "attack=15:release=350[duck];"
                 "[st1][duck]amix=inputs=2:normalize=0:dropout_transition=0[amix]")
        subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                        "-i", video, "-i", musik, "-filter_complex", graph,
                        "-map", "0:v", "-map", "[amix]", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", out], check=True)
        print(f"  {ab:>4.0f} dB unter der Stimme  ->  Bett {db:+.1f} dB  ->  {out}")


if __name__ == "__main__":
    main()
