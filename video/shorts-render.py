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
GELB = "&H0030D5FF&"       # das Gelb seines Kanals, als Stilfarbe (ABGR)
WEISS = "&H00FFFFFF&"
GELB_I, WEISS_I = "&H30D5FF&", "&HFFFFFF&"   # dieselben Farben als \\c im Text
# Sein Look, abgelesen an den eigenen Shorts (Vorschaubilder, 20.10.2026):
# warm, kontrastreich, Hintergrund abgesoffen, deutliche Vignette.
LOOK = ("eq=contrast=1.14:brightness=-0.02:saturation=1.16,"
        "colorbalance=rs=0.04:gs=0.01:bs=-0.05:rm=0.03:bm=-0.03,"
        "vignette=PI/4.5")


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


def build_ass(cues, path, marginv=320, tempo=1.0, tiefer=0, gross=True,
              groesse=88):
    """cues -> ASS mit wortweiser Hervorhebung.

    Abgelesen an seinen veroeffentlichten Shorts: GROSSBUCHSTABEN, fetter
    Serifenloser, dicke schwarze Kontur, und das gerade gesprochene Wort in
    Gelb. Dafuer wird je Wort eine eigene Zeile ausgegeben, die alle Woerter
    der Einblendung zeigt und nur eines einfaerbt.

    `tiefer` schiebt die Zeile unter die Lippe — nicht darauf. Auch das ist
    an seinen Shorts abgelesen: die Zeile sitzt dort auf Bart- und Kinnhoehe,
    rund 0,70 der Bildhoehe.
    """
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{FONT},{groesse},{WEISS},&H00000000,&H00000000,-1,0,1,8,3,2,80,80,{marginv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []

    def zeile(von, bis, text, lippe):
        kopf = ""
        if lippe is not None:
            kopf = f"{{\\an8\\pos({W // 2},{int(lippe) + tiefer})}}"
        lines.append(f"Dialogue: 0,{ass_time(von / tempo)},{ass_time(bis / tempo)},"
                     f"Cap,,0,0,0,,{kopf}{text}")

    for c in cues:
        woerter = [w for w in (c.get("woerter") or [])
                   if w["t"].strip() and w["end"] > c["start"] and w["start"] < c["end"]]
        roh = [w["t"].strip() for w in woerter] or c["text"].split()
        roh = [w.upper() for w in roh] if gross else roh
        if not roh:
            continue
        if not woerter:
            zeile(c["start"], c["end"], " ".join(roh), c.get("lippe"))
            continue
        for i, w in enumerate(woerter):
            von = max(w["start"], c["start"]) if i else c["start"]
            bis = min(woerter[i + 1]["start"], c["end"]) if i + 1 < len(woerter) else c["end"]
            if bis - von <= 0.02:
                continue
            teile = [f"{{\\c{GELB_I if k == i else WEISS_I}}}{t}"
                     for k, t in enumerate(roh)]
            zeile(von, bis, " ".join(teile), c.get("lippe"))

    Path(path).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")


def korrekturen_lesen(pfad):
    """Korrekturen fuer eingebrannte Untertitel laden.

    Links darf eine Wortfolge stehen, nicht nur ein Wort: `for short` war in
    Wahrheit `fall short`, und das sieht man erst im Satz. Ein falsch
    verstandenes Wort steht nach dem Rendern fuer immer im Bild — die Liste
    ist billiger als jedes groessere Modell.
    """
    paare = {}
    if not pfad or not Path(pfad).exists():
        return paare
    for zeile in Path(pfad).read_text(encoding="utf-8").splitlines():
        zeile = zeile.split("#")[0].strip()
        if "->" in zeile:
            falsch, richtig = (t.strip() for t in zeile.split("->", 1))
            if falsch:
                paare[tuple(falsch.lower().split())] = richtig.split()
    return paare


def _kern(wort):
    return wort.strip(".,!?;:\"'\u2019\u201c\u201d").lower()


def korrekturen_anwenden(woerter, paare):
    """Wortfolgen ersetzen, Satzzeichen des letzten Wortes bleiben stehen.

    Arbeitet auf der flachen Wortliste VOR der Gruppierung, damit eine
    Korrektur auch ueber eine Einblendungsgrenze hinweg greift.
    """
    if not paare:
        return woerter
    maxlen = max(len(k) for k in paare)
    raus, i = [], 0
    while i < len(woerter):
        treffer = None
        for n in range(min(maxlen, len(woerter) - i), 0, -1):
            schluessel = tuple(_kern(w["t"]) for w in woerter[i:i + n])
            if schluessel in paare:
                treffer = (n, paare[schluessel])
                break
        if not treffer:
            raus.append(woerter[i]); i += 1
            continue
        n, ersatz = treffer
        gruppe = woerter[i:i + n]
        schwanz = gruppe[-1]["t"][len(gruppe[-1]["t"].rstrip(".,!?;:")):]
        von, bis = gruppe[0]["start"], gruppe[-1]["end"]
        schritt = (bis - von) / max(len(ersatz), 1)
        for k, t in enumerate(ersatz):
            raus.append({"t": t + (schwanz if k == len(ersatz) - 1 else ""),
                         "start": von + k * schritt,
                         "end": von + (k + 1) * schritt,
                         "seg": gruppe[0].get("seg")})
        i += n
    return raus


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


def whisper_cues(clip, model_size="small", lang=None, worte=3, paare=None,
                 pause=0.45):
    """Wortgenaue Zeiten fuer den bereits geschnittenen Clip.

    `worte` ist die Zahl der Woerter je Einblendung — drei, sein Wunsch vom
    20.10.

    **Eine Einblendung laeuft nie ueber eine Satzgrenze.** Das war sein
    zweiter Einwand: wenn der letzte Satz endet und der naechste anfaengt,
    standen beide Teile in derselben Zeile und der Schnitt war im Bild nicht
    zu sehen. Getrennt wird an zwei Stellen: am Satzzeichen — und an einer
    **Sprechpause ueber `pause` Sekunden**, weil die Zeichensetzung des
    Modells unzuverlaessig ist, die Pause aber nicht.
    """
    from faster_whisper import WhisperModel
    m = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = m.transcribe(clip, language=lang, word_timestamps=True,
                                  vad_filter=True)
    # Der Abschnitt, aus dem ein Wort stammt, wird mitgefuehrt: Whisper
    # trennt Saetze zuverlaessiger ueber seine eigenen Abschnitte als ueber
    # die Satzzeichen, die es setzt. `too afraid to touch.` und `This is why`
    # standen in getrennten Abschnitten — und trotzdem in einer Zeile, weil
    # der Punkt fehlte und die Pause zu kurz war.
    flach = [{"t": w.word.strip(), "start": w.start, "end": w.end, "seg": i}
             for i, s in enumerate(segments) for w in (s.words or [])
             if w.word.strip()]
    flach = korrekturen_anwenden(flach, paare)

    cues, buf, harte_grenze = [], [], False

    def schliessen(buf, hart):
        cues.append({"start": buf[0]["start"], "end": buf[-1]["end"],
                     "text": " ".join(w["t"] for w in buf),
                     "woerter": list(buf), "hart": hart})

    for i, w in enumerate(flach):
        buf.append(w)
        satzende = w["t"].endswith((".", "?", "!", "…"))
        naechstes = flach[i + 1] if i + 1 < len(flach) else None
        luecke = (naechstes["start"] - w["end"]) if naechstes else 99
        wechsel = bool(naechstes) and naechstes.get("seg") != w.get("seg")
        hart = satzende or wechsel or luecke > pause
        if hart or len(buf) >= worte:
            schliessen(buf, hart)
            buf = []
    if buf:
        schliessen(buf, True)

    # Eine Einblendung aus einem einzigen Wort liest sich wie ein Zucken. Sie
    # wandert zurueck — aber nur, wenn die vorhergehende nicht an einer
    # Satzgrenze endet. Sonst waere genau der Fehler wieder da.
    zusammen = []
    for c in cues:
        v = zusammen[-1] if zusammen else None
        if (v and not v["hart"] and len(c["woerter"]) == 1
                and len(v["woerter"]) < worte + 1):
            v["end"] = c["end"]
            v["text"] += " " + c["text"]
            v["woerter"] += c["woerter"]
            v["hart"] = c["hart"]
        else:
            zusammen.append(c)
    return zusammen, info.language


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.stderr.write(p.stderr[-3000:])
        raise SystemExit(f"ffmpeg brach ab ({p.returncode})")
    return p


def mittlerer_pegel(datei, dauer=None):
    """Mittlerer Pegel einer Tonspur in dB, ueber `volumedetect`.

    Gebraucht, weil ein fester Wert wie -16 dB nichts taugt: er ist absolut,
    die Quellen sind es nicht. Im ersten Versuch lag das Bett danach 14 dB
    unter der Stimme und war schlicht nicht zu hoeren — gemessen 0,1 dB
    Unterschied zwischen Mischung mit und ohne Musik.
    """
    cmd = [FFMPEG, "-hide_banner"]
    if dauer:
        cmd += ["-t", str(dauer)]
    cmd += ["-i", datei, "-af", "volumedetect", "-f", "null", os.devnull]
    p = subprocess.run(cmd, capture_output=True, text=True)
    for zeile in p.stderr.splitlines():
        if "mean_volume:" in zeile:
            return float(zeile.split("mean_volume:")[1].split("dB")[0])
    return None


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
                    help="Beschleunigung. Seine Folgen laufen auf 1.1, fuer "
                         "Shorts will er 1.2. 1.0 = unveraendert.")
    ap.add_argument("--worte", type=int, default=3,
                    help="Woerter je Einblendung (sein Wunsch: 3)")
    ap.add_argument("--tiefer", type=int, default=0,
                    help="Pixel, um die die Zeile zusaetzlich nach unten "
                         "rueckt; der Plan setzt die Hoehe schon unter die Lippe")
    ap.add_argument("--schriftgroesse", type=int, default=88)
    ap.add_argument("--korrekturen", default="video/korrekturen.txt",
                    help="Liste falsch -> richtig fuer die Untertitel")
    ap.add_argument("--pause", type=float, default=0.45,
                    help="Sprechpause in Sekunden, ab der eine Einblendung "
                         "endet (Satzgrenze ohne Satzzeichen)")
    ap.add_argument("--logo", default=None,
                    help="PNG mit Transparenz, wird unten mittig eingeblendet")
    ap.add_argument("--logo-breite", type=int, default=520)
    ap.add_argument("--logo-alpha", type=float, default=1.0)
    ap.add_argument("--logo-hoehe", type=float, default=0.845,
                    help="Anteil der Bildhoehe, auf dem das Logo sitzt")
    ap.add_argument("--musik", default=None,
                    help="Musikbett; wird geloopt, ein- und ausgeblendet und "
                         "unter der Stimme abgesenkt")
    ap.add_argument("--musik-db", type=float, default=None,
                    help="fester Pegel des Betts; ohne Angabe wird er aus "
                         "Stimme und Bett gemessen")
    ap.add_argument("--musik-unter", type=float, default=8.0,
                    help="dB, die das Bett unter der Stimme liegt")
    ap.add_argument("--klein", action="store_true",
                    help="keine Grossbuchstaben (sein Kanal nutzt Versalien)")
    ap.add_argument("--look", choices=["warm", "aus"], default="warm",
                    help="warm = der Grading seiner Shorts (Kontrast, warmer "
                         "Stich, Vignette), abgelesen an den Vorschaubildern")
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
        clip_laenge = schnitte[-1]["ende"] - schnitte[0]["start"]
        v_quelle, a_quelle = "[vcat]", "[acat]"
    elif a.layout == "stapel":
        if not (a.oben and a.unten):
            raise SystemExit("--layout stapel braucht --oben und --unten")
        clip_laenge = dur
        graph = [f"[0:v]{_ausschnitt(a.oben, H // 2, 'o')}[o]",
                 f"[0:v]{_ausschnitt(a.unten, H // 2, 'u')}[u]",
                 "[o][u]vstack=inputs=2[vcat]"]
        marginv = a.marginv if a.marginv is not None else 150
        v_quelle, a_quelle = "[vcat]", "0:a?"
    else:
        clip_laenge = dur
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

    if a.look == "warm":
        graph.append(f"{v_quelle}{LOOK}[vlook]")
        v_quelle = "[vlook]"

    with tempfile.TemporaryDirectory() as td:
        cues = None
        if a.auto_captions:
            raw = os.path.join(td, "clip.mp4")
            cut = [FFMPEG, "-y", "-ss", str(t0), "-i", a.src]
            if dur:
                cut += ["-t", str(dur)]
            run(cut + ["-c", "copy", raw])
            cues, lang = whisper_cues(raw, a.model, a.lang, worte=a.worte,
                                      paare=korrekturen_lesen(a.korrekturen),
                                      pause=a.pause)
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
            build_ass(cues, ass, marginv=marginv, tempo=a.tempo,
                      tiefer=a.tiefer, gross=not a.klein,
                      groesse=a.schriftgroesse)
            print(f"  {a.worte} Woerter je Einblendung, "
                  f"{'VERSALIEN' if not a.klein else 'gemischt'}, "
                  f"{a.tiefer} px unter der Lippe, Look: {a.look}")
            graph.append(f"{v_quelle}subtitles="
                         + ass.replace(":", r"\:") + "[vout]")
            letzte = "[vout]"

        cmd = [FFMPEG, "-y"]
        if not a.plan:
            cmd += ["-ss", str(t0)]
        cmd += ["-i", a.src]
        if dur and not a.plan:
            cmd += ["-t", str(dur)]
        naechste = 1

        if a.logo:
            cmd += ["-i", a.logo]
            graph.append(f"[{naechste}:v]scale={a.logo_breite}:-1,format=rgba,"
                         f"colorchannelmixer=aa={a.logo_alpha}[lg]")
            graph.append(f"{letzte}[lg]overlay=(W-w)/2:"
                         f"H*{a.logo_hoehe}-h/2[vlogo]")
            letzte = "[vlogo]"
            naechste += 1

        if a.musik:
            # Das Bett laeuft unter der Stimme und wird von ihr weggedrueckt
            # (sidechaincompress). Ohne das Wegdruecken frisst eine epische
            # Flaeche die Konsonanten.
            cmd += ["-i", a.musik]
            laenge = (clip_laenge / a.tempo) if clip_laenge else None
            db = a.musik_db
            if db is None:
                stimme_db = mittlerer_pegel(a.src, dauer=clip_laenge)
                bett_db = mittlerer_pegel(a.musik, dauer=laenge)
                if stimme_db is not None and bett_db is not None:
                    db = round(stimme_db - bett_db - a.musik_unter, 1)
                    print(f"  Musik: Stimme {stimme_db:.1f} dB, Bett "
                          f"{bett_db:.1f} dB -> {db:+.1f} dB "
                          f"({a.musik_unter:.0f} dB darunter)")
                else:
                    db = -16.0
            stimme = a_quelle if a_quelle.startswith("[") else f"[{a_quelle.rstrip('?')}]"
            graph.append(f"{stimme}asplit=2[st1][st2]")
            bett = (f"[{naechste}:a]aloop=loop=-1:size=2000000000,"
                    f"volume={db}dB,afade=t=in:st=0:d=1.5")
            if laenge:
                bett += f",atrim=0:{laenge:.2f},afade=t=out:st={max(laenge-2.0,0):.2f}:d=2.0"
            graph.append(bett + "[bett]")
            graph.append("[bett][st2]sidechaincompress=threshold=0.04:ratio=8:"
                         "attack=15:release=350[duck]")
            graph.append("[st1][duck]amix=inputs=2:normalize=0:"
                         "dropout_transition=0[amix]")
            a_quelle = "[amix]"
            naechste += 1

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
