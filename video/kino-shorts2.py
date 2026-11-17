#!/usr/bin/env python3
"""Kino-Schicht fuer Shorts II — Williamson-Kasten, zweischriftiger Satz,
bewegte Schrift und Fotoblitze.

**`shorts-render.py` gehoert Shorts I und wird nicht angefasst.** Die
Untertitel-Logik (Whisper, Korrekturen, Packen, Lippen) wird aus ihm
IMPORTIERT; dieses Werkzeug schreibt nur die ASS und baut das Bild um.

Ablauf:
  1. `shorts-render.py` baut das Bild OHNE Untertitel, OHNE Logo und
     OHNE Outro (Plan, B-Roll, Look, Tempo).
  2. Dieses Werkzeug schneidet daraus den Kasten, setzt Logo, Schrift
     und Blitze darauf.
  3. Das Outro wird danach angehaengt.

Alles, was hier an Zahlen steht, ist am Williamson-Short QjmWNrq4mBU
gemessen (17.11.), Datei fuer Datei in `video/williamson-kasten.md`.
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

# ---------------------------------------------------- gemessene Vorlage
# QjmWNrq4mBU, drei Zeitproben, 1080x1920:
#   Kasten 980x980 bei x=50 y=470, Eckenradius 40 (Aussenraum Helligkeit 0)
#   Schriftzeile: Mitte des KASTENS, nicht des Bildes (0,493 / 0,499 / 0,494)
#   x-Hoehe der laufenden Zeile 32 px, des grossen Wortes 60 px
#   matt gegen aktiv: #CECBC3 gegen #FDFEFD  -> Faktor 0,81
KASTEN_SEITE, KASTEN_X, KASTEN_OBEN, KASTEN_RADIUS = 980, 50, 470, 40
XH_INTER, XH_SKRIPT = 0.550, 0.600          # x-Hoehe je Punkt, gemessen
MATT_FAKTOR = 0.81

# Seine Ansage vom 17.11. abends: die Schrift soll SILBER sein, "was
# Edleres". Das schlaegt die Messung: bei Williamson ist die Zeile die
# mittlere Farbe der Szene. Silber bleibt Grundfarbe, die Szene mischt nur
# noch mit — sonst stuende die Zeile ueber warmem Material wieder pfirsich.
SILBER = (231, 238, 246)
SZENE_ANTEIL = 0.26

# Die Zeile wandert. Seine Ansage: die Position soll variieren, zentral
# "floatet das Ganze nicht". Der goldene Schnitt als Schrittweite sorgt
# dafuer, dass zwei aufeinanderfolgende Einblendungen weit auseinander
# landen statt zu benachbarten Plaetzen zu kriechen.
GOLDEN = 0.6180339887498949
WANDER_X, WANDER_Y = 150, 125
WANDER_X_STARK = 112          # das grosse Wort ist breiter, also enger gefuehrt


# ---------------------------------------------------------------- Blitze

def blitz_kette(zeiten, hoehe=0.95, abfall=0.055, dauer=0.20):
    """Fotoblitze als Helligkeitsausdruck fuer `eq`.

    `max(0,t-T)` ist noetig: ohne ihn ueberlaeuft `exp` weit VOR einem
    Blitz, `inf * 0` wird NaN und das ganze Band kippt.
    """
    if not zeiten:
        return None
    teile = [f"{hoehe}*exp(-max(0" + chr(92) + f",t-{t:.4f})/{abfall})"
             f"*between(t,{t:.4f},{t + dauer:.4f})" for t in sorted(zeiten)]
    return "eq=brightness='" + "+".join(teile) + "':eval=frame"


# ------------------------------------------------------------- Toenung

def kasten_toene(bild, y_off, seite=1080, takt=4):
    """Mittlere Farbe des Kastens je Zeitpunkt — die Grundlage der Toenung.

    Gemessen am Original: die Schriftfarbe IST die mittlere Farbe der
    Szene, auf den hellsten Kanal 250 normiert.
      warme Sepia-Szene  -> gemessen #F8BF88, gerechnet (250,208,167)
      kuehle Himmel-Szene-> gemessen #E3F2F4, gerechnet (234,250,250)
      neutrales Wasser   -> gemessen #FDFEFD, gerechnet (241,250,241)
    """
    cmd = [SR.FFMPEG, "-nostdin", "-v", "error", "-i", bild,
           "-vf", f"crop={seite}:{seite}:0:{y_off},scale=8:8,fps={takt}",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    roh = subprocess.run(cmd, capture_output=True).stdout
    n = len(roh) // (8 * 8 * 3)
    toene = []
    for i in range(n):
        b = roh[i * 192:(i + 1) * 192]
        r = sum(b[0::3]) / 64; g = sum(b[1::3]) / 64; bl = sum(b[2::3]) / 64
        m = max(r, g, bl, 1)
        szene = (r * 250 / m, g * 250 / m, bl * 250 / m)
        toene.append(tuple(
            min(255, SILBER[i] * (1 - SZENE_ANTEIL) + szene[i] * SZENE_ANTEIL)
            for i in range(3)))
    return toene, takt


def ass_farbe(rgb):
    r, g, b = (int(max(0, min(255, round(v)))) for v in rgb)
    return f"&H00{b:02X}{g:02X}{r:02X}&"


# ---------------------------------------------------------------- Satz

RICHTUNGEN = [(-46, 20), (46, 20), (0, 38), (-34, -27), (34, -27), (0, -36)]


def ass_kino(cues, pfad, tempo=1.0, schlagworte=(), toene=None, takt=4,
             groesse=69, groesse_stark=125, schrift="Inter Black",
             schrift_matt="Inter SemiBold", schrift_stark="Petit Formal Script",
             mitte_x=None, mitte_y=None, pop=1.12, pop_stark=1.22,
             zeit_pop=150, zeit_stark=200):
    """Der gemessene Williamson-Satz, Wort fuer Wort.

    Zwei Faelle:

    * **gewoehnliche Einblendung** — eine Zeile in der Mitte des Kastens,
      Kleinschreibung, keine Kontur. Das gesprochene Wort steht in
      `Inter Black` und voller Toenung, die uebrigen in `Inter SemiBold`
      und auf 81 % abgedunkelt (gemessen #FDFEFD gegen #CECBC3).
    * **Einblendung mit Schlagwort** — zwei Zeilen uebereinander, wie
      „one path" im Original: die gewoehnlichen Woerter klein und nach
      rechts oben versetzt, das Schlagwort gross in der geschwungenen
      Kursiven nach links unten, beide ueberlappend.

    Die Farbe kommt NICHT aus einer Konstante, sondern aus dem Bild: der
    Kasten wird vier Mal je Sekunde abgetastet, und die Schrift nimmt
    seine mittlere Farbe an. Genau das steht im Original — dieselbe
    Zeile ist in einer Szene eisblau und in der naechsten pfirsich.
    """
    W, H = SR.W, SR.H
    mitte_x = mitte_x if mitte_x is not None else KASTEN_X + KASTEN_SEITE // 2
    mitte_y = mitte_y if mitte_y is not None else KASTEN_OBEN + KASTEN_SEITE // 2
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, ScaleX, ScaleY, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{schrift},{groesse},&H00FFFFFF,&H00000000,&H64000000,0,0,100,100,1,0,2,5,30,30,30,1
Style: Gross,{schrift_stark},{groesse_stark},&H00FFFFFF,&H00000000,&H64000000,0,0,100,100,1,0,2,5,30,30,30,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    sw = {s.strip().upper() for s in schlagworte if s.strip()}

    def ton(t_aus):
        if not toene:
            return (250, 250, 250)
        i = min(len(toene) - 1, max(0, int(t_aus * takt)))
        return toene[i]

    def anim(i, stark, x, y, ms, f):
        """Einflug: Versatz, Drehung und Groesse laufen zusammen auf null.

        `\\move` ersetzt `\\pos` — beide zugleich ignoriert libass
        stillschweigend, und die Zeile stuende dann fest.
        """
        dx, dy = RICHTUNGEN[i % len(RICHTUNGEN)]
        rz = (5 if i % 2 == 0 else -5) * (1.8 if stark else 1.0)
        return (f"\\move({x + dx},{y + dy},{x},{y},0,{ms})"
                f"\\fscx{100 * f:.0f}\\fscy{100 * f:.0f}\\frz{rz:.1f}"
                f"\\alpha&HB0&"
                f"\\t(0,{ms},\\fscx100\\fscy100\\frz0\\alpha&H00&)")

    def zeit(x):
        return SR.ass_time(x / tempo)

    for nr, c in enumerate(cues):
        woerter = [w for w in (c.get("woerter") or [])
                   if w["t"].strip() and w["end"] > c["start"] and w["start"] < c["end"]]
        roh = [SR._anzeige(w["t"], False) for w in woerter]
        roh = [w for w in roh if w]
        if not roh:
            roh = [SR._anzeige(t, False) for t in (c.get("text") or "").split()]
            roh = [t for t in roh if t]
            if not roh:
                continue
            woerter = []
        k_index = next((i for i, w in enumerate(roh) if w.upper() in sw), None)
        # Zwei unabhaengige Folgen, damit die Zeile nicht auf einer Diagonalen
        # wandert: x laeuft mit dem goldenen Schnitt, y mit seinem Quadrat.
        wx = WANDER_X_STARK if k_index is not None else WANDER_X
        px = mitte_x + int(round((((nr + 1) * GOLDEN) % 1.0 - 0.5) * 2 * wx))
        py = mitte_y + int(round((((nr + 1) * GOLDEN * GOLDEN) % 1.0 - 0.5)
                                 * 2 * WANDER_Y))
        rgb = ton(c["start"] / tempo)
        voll = ass_farbe(rgb)
        matt = ass_farbe([v * MATT_FAKTOR for v in rgb])

        def satz(hell):
            """Eine Zeile, das aktive Wort heller und fetter."""
            teile = []
            for k, t in enumerate(roh):
                if k == hell:
                    teile.append(f"{{\\fn{schrift}\\c{voll}}}{t}")
                else:
                    teile.append(f"{{\\fn{schrift_matt}\\c{matt}}}{t}")
            return " ".join(teile)

        def ausgeben(von, bis, hell, mit_anim):
            v, b = zeit(von), zeit(bis)
            if k_index is None:
                kopf = ("{\\an5" + (anim(nr, False, px, py, zeit_pop, pop)
                                    if mit_anim else f"\\pos({px},{py})") + "}")
                lines.append(f"Dialogue: 0,{v},{b},Cap,,0,0,0,,{kopf}{satz(hell)}")
                return
            # Schlagwort-Fall: zwei Zeilen, wie „one path" im Original
            rest = " ".join(t for i, t in enumerate(roh) if i != k_index)
            ox, oy = px + 52, py - 46
            gx, gy = px - 32, py + 38
            if rest:
                hell_rest = (hell is not None and hell != k_index)
                f_rest = voll if hell_rest else matt
                s_rest = schrift if hell_rest else schrift_matt
                kopf = ("{\\an5" + (anim(nr, False, ox, oy, zeit_pop, pop)
                                    if mit_anim else f"\\pos({ox},{oy})") + "}")
                lines.append(f"Dialogue: 0,{v},{b},Cap,,0,0,0,,"
                             f"{kopf}{{\\fn{s_rest}\\c{f_rest}}}{rest}")
            kopf = ("{\\an5" + (anim(nr, True, gx, gy, zeit_stark, pop_stark)
                                if mit_anim else f"\\pos({gx},{gy})") + "}")
            lines.append(f"Dialogue: 1,{v},{b},Gross,,0,0,0,,"
                         f"{kopf}{{\\c{voll}}}{roh[k_index]}")

        if not woerter:
            ausgeben(c["start"], c["end"], None, True)
            continue
        for i, w in enumerate(woerter):
            von = max(w["start"], c["start"]) if i else c["start"]
            bis = (min(woerter[i + 1]["start"], c["end"])
                   if i + 1 < len(woerter) else c["end"])
            if bis - von <= 0.02:
                continue
            ausgeben(von, bis, i, i == 0)

    Path(pfad).write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return len(lines)


# ------------------------------------------------------------ Kastenmaske

def maske_bauen(pfad, seite=KASTEN_SEITE, radius=KASTEN_RADIUS):
    from PIL import Image, ImageDraw
    m = Image.new("L", (seite, seite), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, seite - 1, seite - 1],
                                        radius=radius, fill=255)
    m.save(pfad)
    return pfad


# ------------------------------------------------------------------ Lauf

def main():
    ap = argparse.ArgumentParser(
        description="Williamson-Kasten, bewegte Schrift und Fotoblitze.")
    ap.add_argument("--bild", required=True,
                    help="Ausgabe von shorts-render.py OHNE Untertitel/Logo/Outro")
    ap.add_argument("--vorlage", required=True,
                    help="die geschnittene Vorlage (Tempo 1,0), fuer die Wortzeiten")
    ap.add_argument("--plan", required=True, help="derselbe Plan wie beim Rendern")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tempo", type=float, default=1.0)
    ap.add_argument("--model", default="medium")
    ap.add_argument("--lang", default=None)
    ap.add_argument("--worte", type=int, default=2)
    ap.add_argument("--pause", type=float, default=0.45)
    ap.add_argument("--korrekturen", default=None)
    ap.add_argument("--schlagworte", default="")
    ap.add_argument("--blitze", default="")
    ap.add_argument("--blitz-hoehe", type=float, default=0.95)
    ap.add_argument("--blitz-abfall", type=float, default=0.055)
    ap.add_argument("--srt-out", default=None)
    ap.add_argument("--crf", type=int, default=20)
    ap.add_argument("--kasten-y", type=int, default=380,
                    help="welche 1080er Zeile des Vollbildes in den Kasten kommt")
    ap.add_argument("--logo", default=None)
    ap.add_argument("--logo-breite", type=int, default=300)
    ap.add_argument("--logo-oben", type=int, default=1520)
    # Nachgemessen an der gebrannten ASS, nicht gerechnet: ASS-Punkte sind
    # NICHT die Punkte der Schriftdatei. 58 ergab 27 px x-Hoehe, gebraucht
    # sind die gemessenen 32 -> 69. Beim grossen Wort 100 -> 48 px, noetig
    # sind 60 -> 125.
    ap.add_argument("--groesse", type=int, default=69)
    ap.add_argument("--groesse-stark", type=int, default=125)
    a = ap.parse_args()

    plan = json.loads(Path(a.plan).read_text(encoding="utf-8"))
    schnitte = plan["einstellungen"] if isinstance(plan, dict) else plan

    paare = SR.korrekturen_lesen(a.korrekturen)
    cues, lang = SR.whisper_cues(a.vorlage, a.model, a.lang, worte=a.worte,
                                 paare=paare, pause=a.pause)
    print(f"  Transkript: {len(cues)} Einblendungen, Sprache {lang}")
    if a.srt_out:
        n = SR.cues_als_srt(cues, a.srt_out, tempo=a.tempo)
        print(f"  {n} Zeilen nach {a.srt_out}")
    # Die Lippen des Plans gelten im Vollbild. Im Kasten steht die Zeile
    # IMMER in der Kastenmitte — gemessen 0,493 / 0,499 / 0,494.

    toene, takt = kasten_toene(a.bild, a.kasten_y)
    print(f"  Toenung: {len(toene)} Proben ({takt}/s), erste "
          f"{tuple(round(v) for v in toene[0]) if toene else '—'}")

    ass = str(Path(a.out).with_suffix(".kino.ass"))
    sw = [s for s in a.schlagworte.split(",") if s.strip()]
    n = ass_kino(cues, ass, tempo=a.tempo, schlagworte=sw, toene=toene, takt=takt,
                 groesse=a.groesse, groesse_stark=a.groesse_stark)
    print(f"  {n} Dialogzeilen, {len(sw)} Schlagwoerter: {', '.join(sw) or '—'}")

    maske = str(Path(a.out).with_suffix(".maske.png"))
    maske_bauen(maske)

    zeiten = [float(x) for x in a.blitze.split(",") if x.strip()]
    bl = blitz_kette(zeiten, a.blitz_hoehe, a.blitz_abfall)

    eing = ["-i", a.bild, "-i", maske]
    # Der Blitz gehoert IN den Kasten. Auf das ganze Bild gelegt hellt er
    # auch den schwarzen Rand auf — dann blitzt nicht die Szene, sondern
    # das Telefon. Deshalb sitzt er vor dem Zusammensetzen.
    kasten = (f"crop={SR.W}:{SR.W}:0:{a.kasten_y},"
              f"scale={KASTEN_SEITE}:{KASTEN_SEITE}:flags=lanczos")
    if bl:
        kasten += "," + bl
        print(f"  {len(zeiten)} Fotoblitze im Kasten bei "
              f"{', '.join('%.2f' % t for t in zeiten)}")
    g = ["[0:v]split=2[src][bgq]",
         "[bgq]drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill[bg]",
         f"[src]{kasten}[k]",
         "[1:v]format=gray[m]",
         "[k][m]alphamerge[ka]",
         f"[bg][ka]overlay={KASTEN_X}:{KASTEN_OBEN}[c1]"]
    letzte = "c1"
    if a.logo:
        eing += ["-i", a.logo]
        g.append(f"[2:v]scale={a.logo_breite}:-1[lg]")
        g.append(f"[{letzte}][lg]overlay=(W-w)/2:{a.logo_oben}[c2]")
        letzte = "c2"
    g.append(f"[{letzte}]subtitles={ass}[c3]")
    letzte = "c3"

    cmd = [SR.FFMPEG, "-y"] + eing + [
        "-filter_complex", ";".join(g), "-map", f"[{letzte}]", "-map", "0:a?",
        "-r", "30", "-c:v", "libx264", "-preset", "medium",
        "-crf", str(a.crf), "-pix_fmt", "yuv420p", "-profile:v", "high",
        "-c:a", "copy", "-movflags", "+faststart", a.out]
    SR.run(cmd)
    mb = os.path.getsize(a.out) / 1e6
    print(f"  {a.out} — {SR.W}x{SR.H}, {mb:.1f} MB")


if __name__ == "__main__":
    main()
