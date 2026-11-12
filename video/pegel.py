import subprocess, re, sys, pathlib, json
import imageio_ffmpeg
F = imageio_ffmpeg.get_ffmpeg_exe()
FP = "ffprobe"
ZIEL = -14.23        # mein eigenes abgenommenes Craig-Ubuntu-Short
OUTRO = 4.208333
DECKE = -0.5          # Spitze darf nicht darueber

def dauer(p):
    return float(subprocess.run([FP,"-v","error","-show_entries","format=duration",
                                 "-of","default=nw=1:nk=1",p],capture_output=True,
                                text=True).stdout.strip())

def messen(p, bis):
    r = subprocess.run([F,"-nostdin","-hide_banner","-t",f"{bis:.3f}","-i",p,
                        "-af","loudnorm=print_format=json","-f","null","-"],
                       capture_output=True, text=True).stderr
    m = re.findall(r"\{[^{}]*input_i[^{}]*\}", r, re.S)
    d = json.loads(m[-1])
    return float(d["input_i"]), float(d["input_tp"])

def angleichen(p, ziel_datei, haupt, gain):
    f = (f"[0:a]asplit=2[a1][a2];"
         f"[a1]atrim=0:{haupt:.3f},asetpts=PTS-STARTPTS,volume={gain:.2f}dB[m];"
         f"[a2]atrim={haupt:.3f},asetpts=PTS-STARTPTS[o];"
         f"[m][o]concat=n=2:v=0:a=1[aout]")
    subprocess.run([F,"-nostdin","-v","error","-i",p,"-filter_complex",f,
                    "-map","0:v","-c:v","copy","-map","[aout]","-c:a","aac",
                    "-b:a","192k","-ar","48000","-movflags","+faststart",
                    ziel_datei,"-y"], check=True)

zeilen = []
for ordner, ziel in ((sys.argv[1], sys.argv[2]),):
    pathlib.Path(ziel).mkdir(parents=True, exist_ok=True)
    for p in sorted(pathlib.Path(ordner).glob("*.mp4")):
        D = dauer(str(p)); haupt = D - OUTRO
        lufs, tp = messen(str(p), haupt)
        gain = ZIEL - lufs
        kopf = DECKE - tp
        gekappt = gain > kopf
        if gekappt: gain = kopf
        aus = str(pathlib.Path(ziel) / p.name.replace(".mp4", " (angeglichen).mp4"))
        angleichen(str(p), aus, haupt, gain)
        l2, tp2 = messen(aus, haupt)
        with open(sys.argv[3], "a") as f:
            f.write(f"| {p.stem.replace(chr(34),chr(39))} | {lufs:.1f} | {gain:+.2f} | {l2:.1f} | {tp:.1f} | {tp2:.1f} | {'nein' if gekappt else 'ja'} |\n")
        print(f"{p.stem[-22:]:<24} {lufs:6.1f} {gain:+6.2f} -> {l2:6.1f} LUFS, Spitze {tp2:6.1f}" + ("  GEKAPPT" if gekappt else ""), flush=True)
