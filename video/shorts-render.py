#!/usr/bin/env python3
"""Schneidet aus einer Langfassung einen vertikalen Short mit eingebrannten
Untertiteln. Kein GPU, kein Dienst, kein Upload — nur ffmpeg.

  python3 shorts-render.py --src folge.mp4 --start 00:12:04 --end 00:12:48 \
        --out short.mp4 --focus 0.5 --auto-captions

Ohne --auto-captions wird eine .srt erwartet (--srt), deren Zeiten sich auf
den Clip beziehen, nicht auf die Langfassung.
"""
import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1080, 1920
FONT = "DejaVu Sans"


def tc(s):
    """'00:12:04' oder '724' oder '12:04.5' -> Sekunden."""
    if isinstance(s, (int, float)):
        return float(s)
    parts = str(s).split(":")
    return sum(float(p) * 60 ** i for i, p in enumerate(reversed(parts)))


def ass_time(t):
    h, rem = divmod(max(t, 0), 3600)
    m, sec = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{sec:05.2f}"


def build_ass(cues, path, highlight="&H0030D5FF&", marginv=320):
    """cues: [{'start':s,'end':s,'text':str}] -> ASS mit grossem Fliesstext unten."""
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{FONT},86,&H00FFFFFF,&H00000000,&H00000000,-1,0,1,7,3,2,90,90,{marginv},1
Style: Hit,{FONT},86,{highlight},&H00000000,&H00000000,-1,0,1,7,3,2,90,90,{marginv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for c in cues:
        txt = c["text"].strip().replace("\n", "\\N")
        style = "Hit" if c.get("hit") else "Cap"
        lines.append(
            f"Dialogue: 0,{ass_time(c['start'])},{ass_time(c['end'])},{style},,0,0,0,,{txt}"
        )
    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


def srt_to_cues(srt_path, offset=0.0):
    cues, block = [], []
    for raw in Path(srt_path).read_text(encoding="utf-8").splitlines() + [""]:
        if raw.strip():
            block.append(raw)
            continue
        if len(block) >= 2:
            times = next(l for l in block if "-->" in l)
            a, b = [t.strip().replace(",", ".") for t in times.split("-->")]
            text = " ".join(block[block.index(times) + 1:])
            cues.append({"start": tc(a) - offset, "end": tc(b) - offset, "text": text})
        block = []
    return cues


def whisper_cues(clip, model_size="small", lang=None, group=4):
    """Wortgenaue Zeiten fuer den bereits geschnittenen Clip."""
    from faster_whisper import WhisperModel
    m = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = m.transcribe(clip, language=lang, word_timestamps=True,
                                  vad_filter=True)
    words = [w for s in segments for w in (s.words or [])]
    cues, buf = [], []
    for w in words:
        buf.append(w)
        if len(buf) >= group or w.word.strip().endswith((".", "?", "!", "…")):
            cues.append({"start": buf[0].start, "end": buf[-1].end,
                         "text": " ".join(x.word.strip() for x in buf)})
            buf = []
    if buf:
        cues.append({"start": buf[0].start, "end": buf[-1].end,
                     "text": " ".join(x.word.strip() for x in buf)})
    return cues, info.language


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.stderr.write(p.stderr[-3000:])
        raise SystemExit(f"ffmpeg brach ab ({p.returncode})")
    return p


def probe_size(src):
    out = run([FFMPEG, "-hide_banner", "-i", src]).stderr if False else None
    p = subprocess.run([FFMPEG, "-hide_banner", "-i", src],
                       capture_output=True, text=True)
    for line in p.stderr.splitlines():
        if " Video:" in line:
            for tok in line.split(","):
                tok = tok.strip().split(" ")[0]
                if "x" in tok and tok.replace("x", "").isdigit():
                    w, h = tok.split("x")
                    return int(w), int(h)
    raise SystemExit("Konnte die Bildgroesse nicht lesen.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--start", default="0")
    ap.add_argument("--end", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--srt", default=None)
    ap.add_argument("--auto-captions", action="store_true")
    ap.add_argument("--model", default="small")
    ap.add_argument("--lang", default=None)
    ap.add_argument("--focus", type=float, default=0.5,
                    help="0..1 — wo im Breitbild der Ausschnitt sitzt (0.5 = Mitte)")
    ap.add_argument("--crf", type=int, default=20)
    ap.add_argument("--layout", choices=["einzel", "stapel"], default="einzel",
                    help="stapel = zwei Ausschnitte uebereinander (Zweier-Shot)")
    ap.add_argument("--oben", default=None, help="x:y:b:h im Quellbild, obere Haelfte")
    ap.add_argument("--unten", default=None, help="x:y:b:h im Quellbild, untere Haelfte")
    ap.add_argument("--plan", default=None,
                    help="JSON aus bildausschnitt.py; Zeiten relativ zu --src. "
                         "Setzt je Einstellung einen eigenen Ausschnitt.")
    ap.add_argument("--marginv", type=int, default=None,
                    help="Abstand der Untertitel vom unteren Rand")
    a = ap.parse_args()

    t0 = tc(a.start)
    dur = (tc(a.end) - t0) if a.end else None
    sw, sh = probe_size(a.src)

    if a.plan:
        daten = json.loads(Path(a.plan).read_text(encoding="utf-8"))
        schnitte = daten["einstellungen"]
        teile, marken = [], []
        for i, sc in enumerate(schnitte):
            von, bis = sc["start"], sc["ende"]
            if sc.get("layout") == "stapel":
                for seite, marke in (("oben", f"o{i}"), ("unten", f"u{i}")):
                    x, y, b, h = (int(v) for v in sc[seite].split(":"))
                    teile.append(f"[0:v]trim={von}:{bis},setpts=PTS-STARTPTS,"
                                 f"crop={b}:{h}:{x}:{y},scale={W}:{H // 2}:"
                                 f"flags=lanczos,setsar=1[{marke}]")
                teile.append(f"[o{i}][u{i}]vstack=inputs=2[v{i}]")
            else:
                x, y, b, h = (int(v) for v in sc["kasten"].split(":"))
                teile.append(f"[0:v]trim={von}:{bis},setpts=PTS-STARTPTS,"
                             f"crop={b}:{h}:{x}:{y},scale={W}:{H}:"
                             f"flags=lanczos,setsar=1[v{i}]")
            teile.append(f"[0:a]atrim={von}:{bis},asetpts=PTS-STARTPTS[a{i}]")
            marken.append(f"[v{i}][a{i}]")
        teile.append("".join(marken) + f"concat=n={len(schnitte)}:v=1:a=1[v][aout]")
        graph = teile
        marginv = a.marginv if a.marginv is not None else 150
        t0, dur = 0.0, None
    elif a.layout == "stapel":
        if not (a.oben and a.unten):
            raise SystemExit("--layout stapel braucht --oben und --unten")
        def teil(spec, marke):
            x, y, b, h = (int(v) for v in spec.split(":"))
            return (f"[0:v]crop={b}:{h}:{x}:{y},"
                    f"scale={W}:{H // 2}:flags=lanczos,setsar=1[{marke}]")
        graph = [teil(a.oben, "o"), teil(a.unten, "u"), "[o][u]vstack=inputs=2[v]"]
        marginv = a.marginv if a.marginv is not None else 150
    else:
        cw = min(sw, int(sh * 9 / 16))
        cx = int((sw - cw) * min(max(a.focus, 0.0), 1.0))
        graph = [f"[0:v]crop={cw}:{sh}:{cx}:0,"
                 f"scale={W}:{H}:flags=lanczos,setsar=1[v]"]
        marginv = a.marginv if a.marginv is not None else 320

    with tempfile.TemporaryDirectory() as td:
        cues = None
        if a.auto_captions:
            raw = os.path.join(td, "clip.mp4")
            cut = [FFMPEG, "-y", "-ss", str(t0), "-i", a.src]
            if dur:
                cut += ["-t", str(dur)]
            run(cut + ["-c", "copy", raw])
            cues, lang = whisper_cues(raw, a.model, a.lang)
            print(f"  Transkript: {len(cues)} Einblendungen, Sprache {lang}")
        elif a.srt:
            cues = srt_to_cues(a.srt)

        letzte = "[v]"
        if cues:
            ass = os.path.join(td, "cap.ass")
            build_ass(cues, ass, marginv=marginv)
            graph.append("[v]subtitles=" + ass.replace(":", r"\:") + "[vout]")
            letzte = "[vout]"

        cmd = [FFMPEG, "-y"]
        if not a.plan:
            cmd += ["-ss", str(t0)]
        cmd += ["-i", a.src]
        if dur and not a.plan:
            cmd += ["-t", str(dur)]
        tonspur = "[aout]" if a.plan else "0:a?"
        cmd += ["-filter_complex", ";".join(graph), "-map", letzte, "-map", tonspur,
                "-r", "30",
                "-c:v", "libx264", "-preset", "medium", "-crf", str(a.crf),
                "-pix_fmt", "yuv420p", "-profile:v", "high",
                "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
                "-movflags", "+faststart", a.out]
        run(cmd)

    mb = os.path.getsize(a.out) / 1e6
    print(f"  {a.out} — {W}x{H}, {mb:.1f} MB")


if __name__ == "__main__":
    main()
