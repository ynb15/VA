#!/usr/bin/env python3
"""Schneidet aus einer Langfassung einen vertikalen Short mit eingebrannten
Untertiteln. Kein GPU, kein Dienst, kein Upload — nur ffmpeg.

  python3 shorts-render.py --src folge.mp4 --start 00:12:04 --end 00:12:48 \
        --out short.mp4 --focus 0.5 --auto-captions

Ohne --auto-captions wird eine .srt erwartet (--srt), deren Zeiten sich auf
den Clip beziehen, nicht auf die Langfassung.

Drei Dinge, die aus der ersten Runde am Sutcliffe-Master gelernt sind
(19.10.2026, seine Rueckmeldung):

* `--tempo` — die veroeffentlichte Folge laeuft schneller als der Master, weil
  er den Podcast beim Export beschleunigt. Ein Short aus dem Master klingt
  ohne diesen Faktor langsamer als alles andere auf dem Kanal. Ton ueber
  `atempo`, Bild ueber `setpts`, die Untertitelzeiten werden mitgeteilt.
* Untertitel an der LIPPE statt am unteren Rand. Der Plan aus
  `bildausschnitt.py` gibt je Einstellung eine Lippenhoehe; jede Einblendung
  wird am Einstellungswechsel geteilt und einzeln mit `\\pos` gesetzt, damit
  sie dem Sprecher folgt. Fester Wert fuer den Einzelschnitt: `--lippe`.
* Tote Einstellungen (`"tot": true` im Plan) zeigen nur den Tisch. Ihr Bild
  wird NICHT gezeigt, sondern mit dem letzten Bild der vorhergehenden
  Einstellung ueberbrueckt (`tpad=clone`). Der Ton laeuft dabei
  unveraendert weiter — deshalb werden Bild- und Tonspur getrennt
  zusammengesetzt, und deshalb bleiben die Untertitelzeiten gueltig.
  Verworfen: den toten Abschnitt samt Ton herausschneiden. Das zerreisst den
  Satz, der darueber laeuft, und verschiebt alle folgenden Zeiten.
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


def build_ass(cues, path, highlight="&H0030D5FF&", marginv=320, tempo=1.0):
    """cues: [{'start','end','text', 'lippe'?}] -> ASS.

    Mit `lippe` sitzt die Zeile per \\pos mit Oberkante an dieser Hoehe,
    ohne sie am unteren Rand (marginv). `tempo` rechnet die Zeiten auf die
    beschleunigte Fassung um.
    """
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
        if not txt:
            continue
        style = "Hit" if c.get("hit") else "Cap"
        if c.get("lippe") is not None:
            txt = f"{{\\an8\\pos({W // 2},{int(c['lippe'])})}}" + txt
        lines.append(
            f"Dialogue: 0,{ass_time(c['start'] / tempo)},"
            f"{ass_time(c['end'] / tempo)},{style},,0,0,0,,{txt}"
        )
    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


def cues_an_lippen(cues, lippen):
    """Jede Einblendung an den Einstellungsgrenzen teilen und setzen.

    `lippen`: [(start, ende, lippe)] in Clipsekunden. Eine Einblendung, die
    ueber einen Kameraschnitt laeuft, wird zweimal ausgegeben — derselbe Text,
    an zwei Hoehen. Das ist gewollt: die Zeile springt mit der Kamera mit,
    statt eine Einstellung lang neben dem Mund zu stehen.
    """
    raus = []
    for c in cues:
        teile = []
        for von, bis, lippe in lippen:
            a, b = max(c["start"], von), min(c["end"], bis)
            if b - a > 0.08:
                teile.append({**c, "start": a, "end": b, "lippe": lippe})
        raus.extend(teile or [c])
    return raus


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


def _ausschnitt(spec, ziel_h, marke):
    x, y, b, h = (int(v) for v in spec.split(":"))
    return (f"crop={b}:{h}:{x}:{y},scale={W}:{ziel_h}:flags=lanczos,setsar=1")


def plan_graph(schnitte):
    """Filtergraph fuer einen Plan: Bild ohne tote Einstellungen, Ton vollstaendig.

    Rueckgabe: (teile, lippen). `lippen` ordnet jedem Zeitabschnitt des Clips
    die Lippenhoehe zu, die dort tatsaechlich im Bild ist — fuer eine
    ueberbrueckte Einstellung ist das die Hoehe des stehenden Bildes.
    """
    lebend = [i for i, s in enumerate(schnitte) if not s.get("tot")]
    if not lebend:
        raise SystemExit("Alle Einstellungen sind als tot markiert.")

    # Welche toten Abschnitte haengen vor/hinter welcher lebenden Einstellung?
    vorlauf = {i: 0.0 for i in lebend}
    nachlauf = {i: 0.0 for i in lebend}
    letzte_lebende = None
    for i, s in enumerate(schnitte):
        dauer = s["ende"] - s["start"]
        if s.get("tot"):
            if letzte_lebende is None:
                vorlauf[lebend[0]] += dauer
            else:
                nachlauf[letzte_lebende] += dauer
        else:
            letzte_lebende = i

    teile, vmarken, amarken = [], [], []
    for i, s in enumerate(schnitte):
        von, bis = s["start"], s["ende"]
        teile.append(f"[0:a]atrim={von}:{bis},asetpts=PTS-STARTPTS[a{i}]")
        amarken.append(f"[a{i}]")
        if s.get("tot"):
            continue
        if s.get("layout") == "stapel":
            for seite, marke in (("oben", f"o{i}"), ("unten", f"u{i}")):
                teile.append(f"[0:v]trim={von}:{bis},setpts=PTS-STARTPTS,"
                             + _ausschnitt(s[seite], H // 2, marke)
                             + f"[{marke}]")
            teile.append(f"[o{i}][u{i}]vstack=inputs=2[s{i}]")
        else:
            teile.append(f"[0:v]trim={von}:{bis},setpts=PTS-STARTPTS,"
                         + _ausschnitt(s["kasten"], H, f"s{i}") + f"[s{i}]")
        pad = []
        if vorlauf[i] > 0.01:
            pad.append(f"start_mode=clone:start_duration={vorlauf[i]:.3f}")
        if nachlauf[i] > 0.01:
            pad.append(f"stop_mode=clone:stop_duration={nachlauf[i]:.3f}")
        if pad:
            teile.append(f"[s{i}]tpad={':'.join(pad)},setpts=PTS-STARTPTS[v{i}]")
        else:
            teile.append(f"[s{i}]null[v{i}]")
        vmarken.append(f"[v{i}]")

    teile.append("".join(vmarken) + f"concat=n={len(vmarken)}:v=1:a=0[vcat]")
    teile.append("".join(amarken) + f"concat=n={len(amarken)}:v=0:a=1[acat]")

    # Lippenhoehen ueber die Zeit: tote Abschnitte erben die Hoehe des Bildes,
    # das sie ueberbrueckt.
    lippen, zuletzt = [], None
    for s in schnitte:
        if not s.get("tot"):
            zuletzt = s.get("lippe")
        lippen.append((s["start"], s["ende"], zuletzt))
    if lippen and lippen[0][2] is None:          # toter Vorlauf am Anfang
        erste = next((l for _, _, l in lippen if l is not None), None)
        lippen = [(a, b, l if l is not None else erste) for a, b, l in lippen]
    return teile, lippen


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
                         "Setzt je Einstellung Ausschnitt, Lippe und tote Stellen.")
    ap.add_argument("--marginv", type=int, default=None,
                    help="Abstand der Untertitel vom unteren Rand (ohne Lippe)")
    ap.add_argument("--lippe", type=int, default=None,
                    help="Feste Untertitelhoehe im Ausgabebild (0..1920), "
                         "Oberkante der Zeile. Schlaegt --marginv.")
    ap.add_argument("--tempo", type=float, default=1.0,
                    help="Beschleunigung wie in der veroeffentlichten Folge "
                         "(gemessen 1.0575). 1.0 = unveraendert.")
    a = ap.parse_args()

    if not 0.5 <= a.tempo <= 2.0:
        raise SystemExit("--tempo muss zwischen 0.5 und 2.0 liegen (atempo).")

    t0 = tc(a.start)
    dur = (tc(a.end) - t0) if a.end else None
    sw, sh = probe_size(a.src)
    lippen = None

    if a.plan:
        daten = json.loads(Path(a.plan).read_text(encoding="utf-8"))
        schnitte = daten["einstellungen"]
        graph, lippen = plan_graph(schnitte)
        tot = [s for s in schnitte if s.get("tot")]
        if tot:
            summe = sum(s["ende"] - s["start"] for s in tot)
            print(f"  {len(tot)} tote Einstellung(en), {summe:.1f}s, "
                  f"mit Standbild ueberbrueckt")
        marginv = a.marginv if a.marginv is not None else 150
        t0, dur = 0.0, None
        v_quelle, a_quelle = "[vcat]", "[acat]"
    elif a.layout == "stapel":
        if not (a.oben and a.unten):
            raise SystemExit("--layout stapel braucht --oben und --unten")
        graph = [f"[0:v]{_ausschnitt(a.oben, H // 2, 'o')}[o]",
                 f"[0:v]{_ausschnitt(a.unten, H // 2, 'u')}[u]",
                 "[o][u]vstack=inputs=2[vcat]"]
        marginv = a.marginv if a.marginv is not None else 150
        v_quelle, a_quelle = "[vcat]", "0:a?"
    else:
        cw = min(sw, int(sh * 9 / 16))
        cx = int((sw - cw) * min(max(a.focus, 0.0), 1.0))
        graph = [f"[0:v]crop={cw}:{sh}:{cx}:0,"
                 f"scale={W}:{H}:flags=lanczos,setsar=1[vcat]"]
        marginv = a.marginv if a.marginv is not None else 320
        v_quelle, a_quelle = "[vcat]", "0:a?"

    if a.tempo != 1.0:
        graph.append(f"{v_quelle}setpts=PTS/{a.tempo}[vt]")
        v_quelle = "[vt]"
        if a_quelle.startswith("["):
            graph.append(f"{a_quelle}atempo={a.tempo}[at]")
        else:
            graph.append(f"[{a_quelle.rstrip('?')}]atempo={a.tempo}[at]")
        a_quelle = "[at]"

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

        letzte = v_quelle
        if cues:
            if lippen:
                cues = cues_an_lippen(cues, lippen)
                print(f"  Untertitel an der Lippe: {len(cues)} Zeilen, "
                      f"Hoehen {sorted({l for _,_,l in lippen if l})}")
            elif a.lippe is not None:
                cues = [{**c, "lippe": a.lippe} for c in cues]
            ass = os.path.join(td, "cap.ass")
            build_ass(cues, ass, marginv=marginv, tempo=a.tempo)
            graph.append(f"{v_quelle}subtitles="
                         + ass.replace(":", r"\:") + "[vout]")
            letzte = "[vout]"

        cmd = [FFMPEG, "-y"]
        if not a.plan:
            cmd += ["-ss", str(t0)]
        cmd += ["-i", a.src]
        if dur and not a.plan:
            cmd += ["-t", str(dur)]
        cmd += ["-filter_complex", ";".join(graph),
                "-map", letzte, "-map", a_quelle,
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
