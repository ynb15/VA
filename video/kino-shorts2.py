#!/usr/bin/env python3
"""Kino-Schicht fuer Shorts II — bewegte Schrift und Fotoblitze.

Seine Ansage vom 16.11.: *„ich moechte, dass sich die Schrift veraendert,
dass da Fotoblitze mit drin sind. Das soll eines der besten Shorts auf
YouTube sein."*

Zwei Dinge, die `shorts-render.py` nicht kann:

  * **Schrift, die sich bewegt.** Jede Einblendung setzt vergroessert ein
    und faellt in 90 ms auf ihre Groesse zurueck. Auf gesetzten
    Schlagwoertern ist der Sprung groesser und dauert laenger.
  * **Fotoblitze.** Ein bis zwei Bilder nahezu weiss, danach ein kurzer
    Abfall — gesetzt auf die Schnitte in die B-Roll und auf Schlagwoerter.

**`shorts-render.py` gehoert Shorts I und wird nicht angefasst.** Die
Untertitel-Logik (Whisper, Korrekturen, Packen, Lippen, Stilzeile,
Zwei-Ebenen-Gewicht) wird aus ihm IMPORTIERT, damit beide Werkzeuge
dieselben Einblendungen erzeugen. Aendert Shorts I den Stil, aendert er
sich hier mit.

Ablauf:
  1. `shorts-render.py` baut das Bild OHNE Untertitel (Plan, B-Roll,
     Look, Logo, Outro, Tempo).
  2. Dieses Werkzeug rechnet die Einblendungen auf der Vorlage (Tempo 1,0),
     schreibt sie als bewegte ASS und brennt sie zusammen mit den Blitzen
     auf das fertige Bild.
"""

import argparse, importlib.util, json, os, subprocess, sys
from pathlib import Path

HIER = Path(__file__).resolve().parent


def renderer_laden():
    """shorts-render.py als Bibliothek — der Bindestrich verbietet `import`."""
    pfad = HIER / "shorts-render.py"
    if not pfad.exists():
        raise SystemExit(f"{pfad} fehlt — ohne den Renderer geht es nicht.")
    spec = importlib.util.spec_from_file_location("shorts_render", pfad)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SR = renderer_laden()


# ---------------------------------------------------------------- Blitze

def blitz_kette(zeiten, hoehe=0.95, abfall=0.055, dauer=0.20):
    """Fotoblitze als Helligkeitsausdruck fuer `eq`.

    Ein echter Blitz ist kein Rechteck: er steigt in einem Bild an und
    faellt exponentiell. `exp(-(t-T)/abfall)` gibt bei 30 Bildern/s nach
    einem Bild noch 55 %, nach zweien 30 %, nach dreien 17 % — das liest
    sich als Blitz und nicht als Fehler im Band.

    `eval=frame` ist noetig, sonst wertet ffmpeg den Ausdruck einmal aus
    und der Blitz steht das ganze Short ueber im Bild.
    """
    if not zeiten:
        return None
    # `max(0,t-T)` ist nicht Kosmetik: ohne die Klammer rechnet ffmpeg fuer
    # Zeiten WEIT VOR einem Blitz `exp(+1164)`, das ist inf, und inf*0 ist
    # NaN. Ein einziger Blitz am Ende des Shorts faerbt damit alles davor
    # schwarzrot. Gefunden am 16.11. an genau diesem Bild.
    teile = [f"{hoehe}*exp(-max(0" + chr(92) + f",t-{t:.4f})/{abfall})"
             f"*between(t,{t:.4f},{t + dauer:.4f})"
             for t in sorted(zeiten)]
    return "eq=brightness='" + "+".join(teile) + "':eval=frame"


# ------------------------------------------------------------ bewegte ASS

def ass_kino(cues, pfad, tempo=1.0, schlagworte=(), pop=1.14, pop_stark=1.28,
             zeit_pop=150, zeit_stark=190, tiefer=0, gross=False,
             groesse=92, rand=40, schrift="Inter Display Black", kursiv=True,
             kontur=0, schatten=2, matt="&HB4B4B4&", hell_bord=2):
    """Wie `SR.build_ass`, aber die erste Zeile je Einblendung poppt auf.

    Warum nur die erste: der Renderer gibt JE WORT eine eigene Dialogzeile
    aus, damit das gesprochene Wort gelb wird. Bekaeme jede dieser Zeilen
    die Animation, zuckte die Schrift bei jedem Wort. Die Animation gehoert
    an den Einsatz der Einblendung, die Hervorhebung wandert danach ruhig
    durch.

    Beide Ebenen (Kontur und Gewichts-Nachzug) bekommen denselben
    Animationskopf — sonst laufen sie auseinander und die Schrift franst.
    """
    """Williamson-Stil, an seinen drei Referenz-Shorts ausgemessen (20.10.):
    Kleinschreibung, KEINE schwarze Kontur, kein Gelb, zwei Woerter je
    Einblendung, und das gesprochene Wort wird ueber HELLIGKEIT UND
    STRICHSTAERKE markiert, nicht ueber Farbe (gemessen: 245,3 gegen 187,5
    mittlere Helligkeit, 24,6 gegen 18,0 Pixel je Spalte).

    Kursiv auf seine Ansage vom 17.11.: *„eine viel artistischere Schrift.
    Geschwungen, kursiv."* Die gemessene Referenz steht aufrecht — das
    gehoert in die Uebergabe, nicht in eine stille Entscheidung.
    """
    W, H = SR.W, SR.H
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, ScaleX, ScaleY, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{schrift},{groesse},{SR.WEISS},&H00000000,&H80000000,0,{1 if kursiv else 0},100,100,1,{kontur},{schatten},2,{rand},{rand},{marginv_fix(rand)},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    sw = {s.strip().upper() for s in schlagworte if s.strip()}

    # Die Einflugrichtungen wechseln reihum. Dass sie wechseln ist der
    # Punkt — seine Ansage vom 17.11.: „bei Chris fliegt die Schrift
    # herum, die ist nicht statisch." Eine Einblendung, die immer aus
    # derselben Ecke kommt, liest sich nach zwei Wiederholungen wieder
    # als statisch.
    RICHTUNGEN = [(-78, 34), (78, 34), (0, 66), (-58, -46), (58, -46), (0, -62)]

    def anim(i, stark, x, y):
        """Einflug: Versatz, Drehung und Groesse laufen zusammen auf null.

        `\\move` ersetzt `\\pos` — beide zugleich ignoriert libass
        stillschweigend, und die Zeile stuende dann fest.
        """
        dx, dy = RICHTUNGEN[i % len(RICHTUNGEN)]
        ms = zeit_stark if stark else zeit_pop
        f = pop_stark if stark else pop
        rz = (6 if i % 2 == 0 else -6) * (1.6 if stark else 1.0)
        return (f"{{\\an8\\move({x + dx},{y + dy},{x},{y},0,{ms})"
                f"\\fscx{100 * f:.0f}\\fscy{100 * f:.0f}\\frz{rz:.1f}"
                f"\\alpha&HA0&"
                f"\\t(0,{ms},\\fscx100\\fscy100\\frz0\\alpha&H00&)}}")

    for nr, c in enumerate(cues):
        woerter = [w for w in (c.get("woerter") or [])
                   if w["t"].strip() and w["end"] > c["start"] and w["start"] < c["end"]]
        roh = [SR._anzeige(w["t"], gross) for w in woerter]
        roh = [w for w in roh if w]
        if not roh:
            roh = [SR._anzeige(t, gross) for t in (c.get("text") or "").split()]
            roh = [t for t in roh if t]
            if not roh:
                continue
        lippe = c.get("lippe")
        px, py = W // 2, (int(lippe) + tiefer) if lippe is not None else H // 2
        kopf_pos = f"{{\\an8\\pos({px},{py})}}"
        # Vergleich in Grossbuchstaben: seit dem Williamson-Stil steht der
        # Text klein im Bild, die Schlagwortliste kommt aber gross.
        stark = any(w.upper() in sw for w in roh)

        def bauen(hell=None):
            """Aktivwort weiss und dicker, die anderen abgedunkelt.

            Das Dickerwerden kommt ueber `\\bord` in der TEXTFARBE, nicht
            ueber eine zweite Schriftschnitt-Groesse: so bleibt die Zeile
            auf einer Grundlinie und nur die Strichstaerke aendert sich,
            genau wie in der Referenz gemessen.
            """
            teile = []
            for k, t in enumerate(roh):
                if k == hell:
                    teile.append(f"{{\\c{SR.WEISS_I}\\3c{SR.WEISS_I}"
                                 f"\\bord{hell_bord}}}{t}")
                else:
                    teile.append(f"{{\\c{matt}\\3c{matt}\\bord0}}{t}")
            return " ".join(teile)

        def zeile(von, bis, hell, mit_anim):
            t = 1.0 if c.get("fertigzeit") else tempo
            v, b = SR.ass_time(von / t), SR.ass_time(bis / t)
            kopf = anim(nr, stark, px, py) if mit_anim else kopf_pos
            lines.append(f"Dialogue: 0,{v},{b},Cap,,0,0,0,,{kopf}{bauen(hell)}")

        if not woerter:
            zeile(c["start"], c["end"], None, True)
            continue
        for i, w in enumerate(woerter):
            von = max(w["start"], c["start"]) if i else c["start"]
            bis = (min(woerter[i + 1]["start"], c["end"])
                   if i + 1 < len(woerter) else c["end"])
            if bis - von <= 0.02:
                continue
            zeile(von, bis, i, i == 0)

    Path(pfad).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


def marginv_fix(rand):
    """Die Lippe im Kopf schlaegt MarginV; der Wert steht nur der Form halber."""
    return 320


# ------------------------------------------------------------------ Lauf

def main():
    ap = argparse.ArgumentParser(
        description="Bewegte Schrift und Fotoblitze auf ein fertiges Short.")
    ap.add_argument("--bild", required=True,
                    help="Ausgabe von shorts-render.py OHNE Untertitel")
    ap.add_argument("--vorlage", required=True,
                    help="die geschnittene Vorlage (Tempo 1,0), fuer die Wortzeiten")
    ap.add_argument("--plan", required=True, help="derselbe Plan wie beim Rendern")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tempo", type=float, default=1.0)
    ap.add_argument("--model", default="medium")
    ap.add_argument("--lang", default=None)
    ap.add_argument("--worte", type=int, default=2,
                    help="Williamson setzt ZWEI Woerter je Einblendung")
    ap.add_argument("--pause", type=float, default=0.45)
    ap.add_argument("--korrekturen", default=None)
    ap.add_argument("--schlagworte", default="",
                    help="Woerter, auf denen die Schrift staerker aufpoppt, "
                         "mit Komma getrennt")
    ap.add_argument("--blitze", default="",
                    help="Zeitpunkte im FERTIGEN Bild, Sekunden, mit Komma")
    ap.add_argument("--blitz-hoehe", type=float, default=0.95)
    ap.add_argument("--blitz-abfall", type=float, default=0.055)
    ap.add_argument("--srt-out", default=None)
    ap.add_argument("--crf", type=int, default=20)
    ap.add_argument("--schrift", default="Inter Display Black")
    ap.add_argument("--schriftgroesse", type=int, default=92)
    ap.add_argument("--aufrecht", action="store_true",
                    help="nicht kursiv setzen (die gemessene Referenz steht aufrecht)")
    ap.add_argument("--versalien", action="store_true",
                    help="GROSSBUCHSTABEN statt der gemessenen Kleinschreibung")
    a = ap.parse_args()

    plan = json.loads(Path(a.plan).read_text(encoding="utf-8"))
    schnitte = plan["einstellungen"] if isinstance(plan, dict) else plan
    _, lippen = SR.plan_graph(schnitte)

    paare = SR.korrekturen_lesen(a.korrekturen)
    cues, lang = SR.whisper_cues(a.vorlage, a.model, a.lang, worte=a.worte,
                                 paare=paare, pause=a.pause)
    print(f"  Transkript: {len(cues)} Einblendungen, Sprache {lang}")
    # Die SRT wird VOR dem Lippen-Teiler geschrieben. `cues_an_lippen`
    # teilt eine Einblendung, die ueber einen Einstellungswechsel laeuft,
    # in zwei Teile mit demselben Text — im Bild richtig, in der Strichliste
    # steht der Text dann zweimal ("EXPERIENCES BUT EXPERIENCES BUT").
    if a.srt_out:
        n = SR.cues_als_srt(cues, a.srt_out, tempo=a.tempo)
        print(f"  {n} Zeilen nach {a.srt_out}")

    if lippen:
        cues = SR.cues_an_lippen(cues, lippen)
        print(f"  Lippen {sorted({l for _, _, l in lippen if l})}")

    ass = str(Path(a.out).with_suffix(".kino.ass"))
    sw = [s for s in a.schlagworte.split(",") if s.strip()]
    n = ass_kino(cues, ass, tempo=a.tempo, schlagworte=sw,
                 schrift=a.schrift, groesse=a.schriftgroesse,
                 kursiv=not a.aufrecht, gross=a.versalien)
    print(f"  {n} Dialogzeilen, {len(sw)} Schlagwoerter: {', '.join(sw) or '—'}")

    zeiten = [float(x) for x in a.blitze.split(",") if x.strip()]
    kette = [f"subtitles={ass}"]
    bl = blitz_kette(zeiten, a.blitz_hoehe, a.blitz_abfall)
    if bl:
        kette.append(bl)
        print(f"  {len(zeiten)} Fotoblitze bei {', '.join('%.2f' % t for t in zeiten)}")

    cmd = [SR.FFMPEG, "-y", "-i", a.bild, "-vf", ",".join(kette),
           "-r", "30", "-c:v", "libx264", "-preset", "medium",
           "-crf", str(a.crf), "-pix_fmt", "yuv420p", "-profile:v", "high",
           "-c:a", "copy", "-movflags", "+faststart", a.out]
    SR.run(cmd)
    mb = os.path.getsize(a.out) / 1e6
    print(f"  {a.out} — {SR.W}x{SR.H}, {mb:.1f} MB")


if __name__ == "__main__":
    main()
