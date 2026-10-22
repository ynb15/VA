#!/usr/bin/env python3
"""Legt das Musikbett unter einen fertigen Short - gleiche Kette wie der Renderer.

    python3 musik_drunter.py <video.mp4> <musik.mp3> <stamm> <ab-sekunde> <dB-unter> ...
                             [--blende-ein SEKUNDEN]

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
    argv = list(ARGV)
    # Seine Rueckmeldung vom 22.10. zu "In This Shirt": "der Song, der muss
    # schon frueher losgehen. Die ersten paar Sekunden, da ist fast gar keine
    # Musik." Nachgemessen war nicht die Blende schuld, sondern der Songanfang
    # (0-2 s liegen 4-6 dB unter dem Rest). Trotzdem gehoert die Blende
    # einstellbar: 0,3 s sind am Anfang eines Shorts hoerbar.
    blende_ein = 0.3
    if "--blende-ein" in argv:
        i = argv.index("--blende-ein")
        blende_ein = float(argv[i + 1])
        del argv[i:i + 2]
    video, musik, stamm = argv[1], argv[2], argv[3]
    ab_s = float(argv[4])          # wo im Song das Bett anfaengt
    abstaende = [float(x) for x in argv[5:]]
    # Seine Ansage vom 21.10.: "die Musik auf jeden Fall viel lauter, und die
    # muss auch schon frueher starten -- da, wo ich die Frage stelle, ist gar
    # keine Musik." Also kurze Blende statt 1,5 s, und sanfteres Wegdruecken
    # (ratio 4 statt 8), damit das Bett unter der Stimme stehen bleibt,
    # statt zu verschwinden.
    ratio = 4
    laenge = dauer(video)
    stimme_db = sr.mittlerer_pegel(video, dauer=laenge)
    # Den Pegel des Betts an der Stelle messen, die auch benutzt wird. Von
    # 0:00 gemessen faellt er zu niedrig aus: die ersten 15 s von "Daylight"
    # sind 7-10 dB leiser als der Hauptteil, und genau daher kam sein
    # Eindruck "unter der Frage ist gar keine Musik".
    schnipsel = f"{stamm}-bettprobe.wav"
    subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                    "-ss", str(ab_s), "-t", f"{laenge:.2f}", "-i", musik,
                    schnipsel], check=True)
    bett_db = sr.mittlerer_pegel(schnipsel, dauer=laenge)
    print(f"Stimme {stimme_db:.1f} dB · Bett ab {int(ab_s)//60}:{int(ab_s)%60:02d} "
          f"{bett_db:.1f} dB · Laenge {laenge:.2f} s")
    for ab in abstaende:
        db = round(stimme_db - bett_db - ab, 1)
        out = f"{stamm}-{int(ab)}db.mp4"
        bett = (f"[1:a]atrim=start={ab_s},asetpts=PTS-STARTPTS,"
                f"aloop=loop=-1:size=2000000000,volume={db}dB,"
                f"afade=t=in:st=0:d={blende_ein},atrim=0:{laenge:.2f},"
                f"afade=t=out:st={max(laenge - 2.0, 0):.2f}:d=2.0[bett]")
        graph = ("[0:a]asplit=2[st1][st2];" + bett +
                 f";[bett][st2]sidechaincompress=threshold=0.04:ratio={ratio}:"
                 "attack=15:release=250[duck];"
                 "[st1][duck]amix=inputs=2:normalize=0:dropout_transition=0[amix]")
        subprocess.run([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                        "-i", video, "-i", musik, "-filter_complex", graph,
                        "-map", "0:v", "-map", "[amix]", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", out], check=True)
        print(f"  {ab:>4.0f} dB unter der Stimme  ->  Bett {db:+.1f} dB  ->  {out}")


if __name__ == "__main__":
    main()
