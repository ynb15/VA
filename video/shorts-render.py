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

Aus der sechsten Runde (20.10.2026, „der Ton ist irgendwie anders“):

* `--laut` — der Master kommt ungemastert aus der Kamera und liegt bei
  -31 LUFS. Shorts laufen bei etwa -14 LUFS. Ohne Angleichung klingt ein
  Short aus dem Master duenn und fern neben allem anderen auf dem Kanal,
  und das Outro (-24,9 LUFS) springt am Ende um 6,5 LU nach oben. Die
  Kette normalisiert Hauptteil und Outro auf dasselbe Ziel, bevor sie
  aneinandergesetzt werden.
* `--dehnung rubberband` statt `atempo`. Gemessen an derselben Passage hebt
  `atempo=1.2` die spektrale Flachheit um 8 % und die Energie ueber 6 kHz um
  11 % — das ist die Rauhheit, die WSOLA beim Zusammensetzen erzeugt.
  `rubberband` bleibt darunter.
"""
import argparse, json, os, re, subprocess, sys, tempfile
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1080, 1920
HIER = Path(__file__).resolve().parent

# --- Sein Preset ----------------------------------------------------------
# Alles unter dieser Linie kommt aus dem Ordner "YNB Shorts Preset", den er
# am 21.10.2026 uebergeben hat: „ist jetzt der Filter und die Schrift, die
# wir bisher fuer meine Shorts verwendet haben". Das sind seine Werte, nicht
# meine Messung — wo sie sich unterscheiden, gelten seine.
FONT_ORDNER = HIER / "fonts"
LUT_VORGABE = HIER / "luts" / "ynb_look.png"


def _schrift_waehlen():
    """Eveleth, wenn sie in fonts/ liegt, sonst Inter Black als Ersatz.

    Eveleth ist das Original aus CapCut und laesst sich nicht aus dem
    Programm holen. Legt er die Datei in fonts/, wird sie genommen und das
    Nachziehen unten entfaellt.
    """
    try:
        dateien = sorted(d for d in FONT_ORDNER.iterdir()
                         if d.suffix.lower() in (".otf", ".ttf"))
    except OSError:
        dateien = []
    if not dateien:
        return None, "DejaVu Sans", False
    d = (next((x for x in dateien if "eveleth" in x.name.lower()), None)
         or next((x for x in dateien if "inter" in x.name.lower()), dateien[0]))
    name = d.stem.replace("-", " ")
    try:
        from PIL import ImageFont
        fam, stil = ImageFont.truetype(str(d), 40).getname()
        name = fam if stil.lower() in ("regular", "normal") else f"{fam} {stil}"
    except Exception:
        pass
    return d, name, "eveleth" not in d.name.lower()


FONT_DATEI, FONT, FONT_ERSATZ = _schrift_waehlen()
# Inter Black ist schmaler und leichter als Eveleth. Sein Preset zieht den
# Ersatz darum auf 112 % Breite und legt 2 px Strich in der Textfarbe nach.
SCALE_X = 112 if FONT_ERSATZ else 100
FETTER = 2 if FONT_ERSATZ else 0
GROESSE = 82               # seine Schriftgroesse (vorher hier 78)
KONTUR = 8                 # schwarze Kontur ringsum
MAX_BREITE = int(W * 0.72)  # die Zeile wird nie breiter, Rand bleibt frei
LIPPE_VORGABE = int(H * 0.70)   # Mitte der Zeile, wenn die Lippe nicht feststeht
GELB = "&H003AF1F9&"       # #F9F13A, sein Gelb aus dem Preset (ABGR)
WEISS = "&H00FFFFFF&"
GELB_I, WEISS_I = "&H3AF1F9&", "&HFFFFFF&"   # dieselben Farben als \\c im Text
# Ohne LUT: die Annaeherung aus seinem Preset (dunkel, entsaettigt, kuehl —
# der Oppenheimer-Filter). `--look warm` haelt die aeltere Annaeherung
# bereit, die ich an seinen Vorschaubildern abgelesen hatte.
LOOK_PRESET = ("eq=contrast=1.12:saturation=0.78:gamma=0.92:brightness=-0.03,"
               "colorbalance=rs=-0.04:gs=0.02:bs=0.06:rm=0.03:gm=0.0:bm=-0.02,"
               "vignette=PI/4.2")
LOOK = ("eq=contrast=1.14:brightness=-0.02:saturation=1.16,"
        "colorbalance=rs=0.04:gs=0.01:bs=-0.05:rm=0.03:bm=-0.03,"
        "vignette=PI/4.5")
# B-Roll-Karte, ausgemessen an den drei Referenz-Shorts (20.10.2026):
# quadratisch 980x980 auf x=50/y=470 im 1080x1920-Bild, also 50 px Rand
# seitlich und senkrecht exakt mittig; Ecken auf 40 px gerundet; ringsum
# reines Schwarz. Beide B-Roll-Bilder stimmen darin aufs Pixel ueberein.
BROLL_SEITE, BROLL_RADIUS = 980, 40


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


def srt_time(t):
    h, rem = divmod(max(t, 0), 3600)
    m, sec = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{sec:06.3f}".replace(".", ",")


def cues_als_srt(cues, pfad, tempo=1.0, gross=True):
    """Dieselben Einblendungen als .srt, in der Zeit des fertigen Videos.

    Gebraucht fuer den Weg über einen Schnittplatz: CapCut Desktop liest
    .srt (Untertitel → Untertitel hinzufügen) und legt jede Zeile als
    eigenen Textblock auf die Spur. Die Gruppierung zu drei Wörtern und die
    Korrekturen stecken dann schon drin — nur Schrift und Farbe setzt er
    dort selbst.
    """
    zeilen = []
    for i, c in enumerate(cues, 1):
        # Einblendungen aus --srt haben keine Wortzeiten. Vorher griff diese
        # Zeile blind auf c["woerter"] zu, und `--srt` zusammen mit
        # `--srt-out` brach mit einem KeyError ab.
        if c.get("woerter"):
            text = " ".join(_anzeige(w["t"], gross) for w in c["woerter"])
        else:
            text = " ".join(_anzeige(t, gross) for t in (c.get("text") or "").split())
        # Wer schon in der Zeit des fertigen Videos steht, wird nicht noch
        # einmal durch das Tempo geteilt.
        teiler = 1.0 if c.get("fertigzeit") else tempo
        zeilen.append(f"{i}\n{srt_time(c['start'] / teiler)} --> "
                      f"{srt_time(c['end'] / teiler)}\n{text}\n")
    Path(pfad).write_text("\n".join(zeilen), encoding="utf-8")
    return len(cues)


SATZZEICHEN = ".,!;:\u2026"
# Das Fragezeichen bleibt stehen — seine Ansage vom 21.10.: die Frage soll
# „in einer Einblendung mit einem Fragezeichen" stehen. Am 20.10. hatte er
# das Gegenteil gesagt („wirkt total fehl am Platz"); die juengere Ansage
# gilt. Punkt, Komma und Ausrufezeichen fallen weiter weg.
# Eine Einblendung, die auf ein Fragezeichen endet, darf breiter werden als
# die uebrigen: `MEANINGFUL TO YOU?` misst bei 82 px 884 px und passt nicht
# in die 72 Prozent des Presets. Lieber diese eine Zeile 84 Prozent breit
# als sie zu teilen oder kleiner zu setzen — dass eine Einblendung kleiner
# gesetzt ist als die davor, war sein Einwand vom 20.10.
FRAGE_BREITE = int(W * 0.84)


def _anzeige(wort, gross):
    """Wort, wie es im Bild steht: ohne schliessendes Satzzeichen.

    Sein Einwand vom 20.10.: „du hast an zwei, drei Stellen noch einen Punkt
    gemacht und ein Fragezeichen, das wirkt total fehl am Platz." Stimmt —
    in Shorts steht kein Satzzeichen. Fuer die TRENNUNG braucht das Werkzeug
    den Punkt aber weiterhin, deshalb faellt er erst hier weg und nicht
    schon im Transkript. Apostrophe bleiben: IT'S, THERE'S.
    """
    w = wort.rstrip(SATZZEICHEN)
    return w.upper() if gross else w


def _ist_frage(woerter):
    """Endet die Einblendung auf einem Fragezeichen?"""
    return bool(woerter) and str(woerter[-1].get("t", "")).rstrip().endswith("?")


_FONT_CACHE = {}


def _font(groesse=None):
    from PIL import ImageFont
    g = int(groesse or GROESSE)
    if g not in _FONT_CACHE:
        _FONT_CACHE[g] = ImageFont.truetype(str(FONT_DATEI), g)
    return _FONT_CACHE[g]


def _libass_faktor(groesse=None):
    """Wieviel kleiner libass setzt, als die Schriftgroesse vermuten laesst.

    libass legt die Schriftgroesse nicht auf das Geviert, sondern auf
    Oberlaenge plus Unterlaenge der Schrift. Inter Black meldet zusammen
    1,21 Geviert, also steht die Zeile nur auf 0,826 der Groesse, mit der
    PIL rechnet. Nachgemessen am gerenderten Bild: `WHAT MAKES LIFE` ist
    bei 82 px 643 px breit, PIL sagt 776 — Verhaeltnis 0,829, der Wert aus
    den Metriken 0,826. Ohne diese Korrektur misst der Umbruch 21 % zu
    breit und teilt Dreier, die laengst passen.
    """
    g = int(groesse or GROESSE)
    try:
        auf, ab = _font(g).getmetrics()
        return g / (auf + ab) if auf + ab else 1.0
    except Exception:
        return 1.0


def _breite_px(text, groesse=None, kontur=True):
    """Textbreite im Ausgabebild, in Pixel.

    Seit die Schriftdatei selbst in fonts/ liegt, wird mit ihr gemessen:
    Vorschub aus der Datei, der libass-Faktor oben, die Dehnung auf
    SCALE_X Prozent und die Kontur ringsum. Fehlt die Datei oder PIL,
    bleibt die alte Schaetzung in Geviert als Notnagel — die war an
    DejaVu Sans Bold ausgezaehlt und passt zu einer anderen Schrift nur
    ungefaehr.
    """
    g = int(groesse or GROESSE)
    try:
        roh = _font(g).getlength(text) * _libass_faktor(g)
    except Exception:
        roh = _breite_em(text) * g
    return roh * SCALE_X / 100 + (2 * (KONTUR + FETTER) if kontur else 0)


def _breite_em(text):
    """Notnagel: Textbreite in Geviert, an DejaVu Sans Bold ausgezaehlt.

    Gemessen wurde, indem Probezeilen in genau dem Stil gerendert und die
    weissen Pixel gezaehlt wurden: `COMPLETELY SUPPRESS` ist 11,59 Geviert
    breit, `MMM` 0,80 je Zeichen, `III` 0,27. Mit geschaetzten Werten lagen
    zwei Einblendungen daneben und brachen auf zwei Zeilen um.
    """
    b = 0.0
    for c in text:
        if c == " ":
            b += 0.30
        elif c in "IJl'\u2019":
            b += 0.27
        elif c in "MW":
            b += 0.80
        else:
            b += 0.61
    return b


def _rundes_rechteck(breite, hoehe, radius):
    """Abgerundetes Rechteck als ASS-Zeichenbefehl, Ursprung oben links.

    Warum nicht als PNG mit `overlay`: ein Standbild als zweiter Eingang hat
    nur einen Zeitstempel, und `fade` bewertet den — die Einblendung kam
    deshalb mit Alpha 0 heraus und blieb unsichtbar. Als Zeichenbefehl im
    Untertitelstrom bekommt das Feld dieselbe Zeitachse wie die Schrift,
    `\\fad` wirkt darauf, und es braucht keinen zweiten Eingang.
    ASS kann runde Ecken nur so — `BorderStyle=3` gibt scharfe.
    """
    b, h, r = int(breite), int(hoehe), int(radius)
    r = max(0, min(r, b // 2, h // 2))
    return (f"m {r} 0 l {b - r} 0 b {b} 0 {b} 0 {b} {r} "
            f"l {b} {h - r} b {b} {h} {b} {h} {b - r} {h} "
            f"l {r} {h} b 0 {h} 0 {h} 0 {h - r} "
            f"l 0 {r} b 0 0 0 0 {r} 0")


def kopfzeile_ass(text, pfad, dauer, groesse=96, hoehe_anteil=0.68,
                  dunkel=True, polster=(44, 28), radius=26,
                  zeilenabstand=1.18, einblenden=(260, 340)):
    """Kopfzeile ueber die ersten Sekunden, nach Modern-Wisdom-Vorbild.

    Ein Feld mit runden Ecken, darauf zwei bis drei Woerter. Bei Williamson
    ist das Feld weiss und die Schrift schwarz; **er hat es am 21.10.
    umgekehrt bestellt** — schwarzes Feld, weisse Schrift. `dunkel=False`
    dreht es auf das Original.

    Die Feldbreite kommt aus der **gemessenen** Textbreite, mit derselben
    Schrift und demselben libass-Faktor wie die Untertitel, aber ohne die
    Kontur — das Feld traegt keine. `|` im Text trennt Zeilen; ohne Trenner
    wird nicht umbrochen, weil eine Kopfzeile, die von selbst umbricht,
    unvorhersehbar aussieht.

    Rueckgabe: (Feldbreite, Feldhoehe) — nur zum Berichten.
    """
    zeilen = [t.strip() for t in text.split("|") if t.strip()]
    if not zeilen:
        raise SystemExit("--kopfzeile ist leer")
    px, py = polster
    breite = int(round(max(_breite_px(z, groesse, kontur=False)
                           for z in zeilen) + 2 * px))
    hoehe = int(round(len(zeilen) * groesse * zeilenabstand + 2 * py))

    mitte_y = hoehe_anteil * H
    x0 = int(round((W - breite) / 2))
    y0 = int(round(mitte_y - hoehe / 2))

    feld = "&H00000000" if dunkel else "&H00FFFFFF"
    schrift = "&H00FFFFFF" if dunkel else "&H00000000"
    ein, aus = einblenden

    kopf = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, ScaleX, ScaleY, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Feld,{FONT},{groesse},{feld},&H00000000,&H00000000,0,0,100,100,1,0,0,7,0,0,0,1
Style: Kopf,{FONT},{groesse},{schrift},&H00000000,&H00000000,0,0,{SCALE_X},100,1,0,0,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    bis = ass_time(dauer)
    zeilen_aus = [
        f"Dialogue: 0,{ass_time(0)},{bis},Feld,,0,0,0,,"
        f"{{\\an7\\pos({x0},{y0})\\bord0\\shad0\\fad({ein},{aus})\\p1}}"
        + _rundes_rechteck(breite, hoehe, radius) + "{\\p0}"
    ]
    abstand = groesse * zeilenabstand
    erste = mitte_y - (len(zeilen) - 1) * abstand / 2
    for i, z in enumerate(zeilen):
        y = int(round(erste + i * abstand))
        zeilen_aus.append(
            f"Dialogue: 1,{ass_time(0)},{bis},Kopf,,0,0,0,,"
            f"{{\\an5\\pos({W // 2},{y})\\bord0\\shad0"
            f"\\fad({ein},{aus})}}{z}")
    Path(pfad).write_text(kopf + "\n".join(zeilen_aus) + "\n", encoding="utf-8")
    return breite, hoehe


def build_ass(cues, path, marginv=320, tempo=1.0, tiefer=0, gross=True,
              groesse=GROESSE, rand=40):
    """cues -> ASS mit wortweiser Hervorhebung.

    Abgelesen an seinen veroeffentlichten Shorts: GROSSBUCHSTABEN, fetter
    Serifenloser, dicke schwarze Kontur, und das gerade gesprochene Wort in
    Gelb. Dafuer wird je Wort eine eigene Zeile ausgegeben, die alle Woerter
    der Einblendung zeigt und nur eines einfaerbt.

    **Eine Schriftgroesse fuer alle.** Dass eine einzelne Einblendung kleiner
    gesetzt ist als die davor, faellt auf — sein Einwand vom 20.10. Dass die
    Zeile passt, erledigt das Packen in `_packen`: zu breite Einblendungen
    werden geteilt, nicht verkleinert.
    """
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, ScaleX, ScaleY, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{FONT},{groesse},{WEISS},&H00000000,&H00000000,0,0,{SCALE_X},100,1,{KONTUR},3,2,{rand},{rand},{marginv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    nutzbar = W - 2 * rand

    def zeile(von, bis, bauen, lippe, fs, fertig_zeit=False):
        """Eine Einblendung ausgeben.

        Layer 0 ist die Zeile mit schwarzer Kontur. Solange Inter Black als
        Ersatz fuer Eveleth laeuft, kommt Layer 1 darueber und zieht jeden
        Buchstaben in seiner eigenen Farbe nach — so holt sein Preset das
        fehlende Gewicht. Mit der echten Eveleth faellt der Layer weg.
        """
        kopf = ""
        if lippe is not None:
            kopf = f"{{\\an8\\pos({W // 2},{int(lippe) + tiefer})}}"
        if fs != groesse:
            kopf += f"{{\\fs{fs}}}"
        t = 1.0 if fertig_zeit else tempo
        von_s, bis_s = ass_time(von / t), ass_time(bis / t)
        lines.append(f"Dialogue: 0,{von_s},{bis_s},Cap,,0,0,0,,"
                     f"{kopf}{bauen(False)}")
        if FETTER:
            lines.append(f"Dialogue: 1,{von_s},{bis_s},Cap,,0,0,0,,"
                         f"{kopf}{{\\bord{FETTER}}}{bauen(True)}")

    for c in cues:
        woerter = [w for w in (c.get("woerter") or [])
                   if w["t"].strip() and w["end"] > c["start"] and w["start"] < c["end"]]
        roh = [_anzeige(w["t"], gross) for w in woerter]
        roh = [w for w in roh if w]
        if not roh:
            # Einblendungen ohne Wortzeiten — so kommen sie aus --srt — haben
            # kein `woerter`. Dann gibt es nichts hervorzuheben, aber die
            # Zeile gehoert trotzdem ins Bild. Vorher fiel sie genau hier
            # heraus, und --srt rechnete einen Short ohne einen einzigen
            # Untertitel, ohne eine Zeile Warnung.
            roh = [_anzeige(t, gross) for t in (c.get("text") or "").split()]
            roh = [t for t in roh if t]
            if not roh:
                continue
        fs = groesse

        def bauen(kontur, hell=None):
            teile = []
            for k, t in enumerate(roh):
                f = GELB_I if k == hell else WEISS_I
                nach = f"\\3c{f}" if kontur else ""
                teile.append(f"{{\\c{f}{nach}}}{t}")
            return " ".join(teile)

        if not woerter:
            zeile(c["start"], c["end"], bauen, c.get("lippe"), fs,
                  c.get("fertigzeit", False))
            continue
        for i, w in enumerate(woerter):
            von = max(w["start"], c["start"]) if i else c["start"]
            bis = min(woerter[i + 1]["start"], c["end"]) if i + 1 < len(woerter) else c["end"]
            if bis - von <= 0.02:
                continue
            zeile(von, bis, lambda kontur, i=i: bauen(kontur, i),
                  c.get("lippe"), fs, c.get("fertigzeit", False))

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
            if not falsch:
                continue
            if falsch.startswith("~"):
                # Muster statt fester Schreibweise: Whisper buchstabiert
                # denselben Namen von Lauf zu Lauf anders — `endotades`,
                # `endotates`, `endate`. Eine Liste jagt dem ewig hinterher.
                paare[re.compile(falsch[1:], re.I)] = richtig.split()
            else:
                paare[tuple(falsch.lower().split())] = richtig.split()
    return paare


def _kern(wort):
    """Wortkern fuer den Vergleich: alles Nichtalphanumerische aussen weg.

    Whisper liefert Bindestriche als eigene Vorsilbe (`hyper` + `-masculinity`).
    Mit einem festen Satzzeichenstreifen blieb der Bindestrich stehen und die
    Korrektur griff nicht — `CALLED THE HYPER` stand im Bild.
    """
    return re.sub(r"^[^0-9A-Za-z]+|[^0-9A-Za-z]+$", "", wort).lower()


def korrekturen_anwenden(woerter, paare):
    """Wortfolgen ersetzen, Satzzeichen des letzten Wortes bleiben stehen.

    Arbeitet auf der flachen Wortliste VOR der Gruppierung, damit eine
    Korrektur auch ueber eine Einblendungsgrenze hinweg greift.
    """
    if not paare:
        return woerter
    muster = {k: v for k, v in paare.items() if hasattr(k, "search")}
    feste = {k: v for k, v in paare.items() if not hasattr(k, "search")}
    maxlen = max((len(k) for k in feste), default=1)
    raus, i = [], 0
    while i < len(woerter):
        treffer = None
        for n in range(min(maxlen, len(woerter) - i), 0, -1):
            schluessel = tuple(_kern(w["t"]) for w in woerter[i:i + n])
            if schluessel in feste:
                treffer = (n, feste[schluessel])
                break
        if not treffer:
            kern = _kern(woerter[i]["t"])
            for re_k, ersatz in muster.items():
                if kern and re_k.fullmatch(kern):
                    treffer = (1, ersatz)
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


def srt_to_cues(srt_path, offset=0.0, fertigzeit=True):
    """Eine .srt einlesen.

    `fertigzeit=True`: die Zeiten stehen schon in der Zeit des fertigen
    Videos — so kommen sie aus `--srt-out` zurueck. Dann darf das Tempo
    nicht noch einmal hineingerechnet werden. Eine .srt, die zur
    ungeschnittenen Quelle gehoert, wird mit `fertigzeit=False` gelesen.
    """
    cues, block = [], []
    for raw in Path(srt_path).read_text(encoding="utf-8").splitlines() + [""]:
        if raw.strip():
            block.append(raw)
            continue
        if len(block) >= 2:
            times = next(l for l in block if "-->" in l)
            a, b = [t.strip().replace(",", ".") for t in times.split("-->")]
            text = " ".join(block[block.index(times) + 1:])
            cues.append({"start": tc(a) - offset, "end": tc(b) - offset,
                         "text": text, "fertigzeit": fertigzeit})
        block = []
    return cues


def stillen_finden(clip, mindest=0.24, schwelle=-45.0):
    """Echte Sprechpausen aus dem Ton holen.

    Warum nicht aus Whisper: mit `word_timestamps` zieht es die Wortenden an
    den naechsten Wortanfang heran — die Luecke ist dann 0,00 s, auch wenn in
    Wahrheit eine Viertelsekunde Stille liegt. Und die Zeichensetzung faellt
    mal weg (`strength` statt `strength.`), die Abschnittsgrenzen ebenso.
    Gemessen am Pegel ist die Pause dagegen eindeutig: an der Stelle, an der
    `expression of strength` in `most men` ueberging, liegen 0,24 s bei
    -59 dB. Genau dort gehoert der Schnitt in der Zeile hin.
    """
    import tempfile as tf
    with tf.TemporaryDirectory() as td:
        roh = os.path.join(td, "ton.raw")
        run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-i", clip,
             "-ac", "1", "-ar", "16000", "-f", "s16le", roh])
        import numpy as np
        a = np.fromfile(roh, dtype="<i2").astype(float) / 32768
    import numpy as np
    fenster = 320                      # 20 ms
    n = len(a) // fenster
    if n < 2:
        return []
    rms = np.sqrt((a[:n * fenster].reshape(n, fenster) ** 2).mean(axis=1))
    db = 20 * np.log10(np.maximum(rms, 1e-6))
    leise = db < schwelle
    stillen, start = [], None
    for i, ist in enumerate(leise):
        if ist and start is None:
            start = i
        elif not ist and start is not None:
            if (i - start) * 0.02 >= mindest:
                stillen.append((start * 0.02, i * 0.02))
            start = None
    if start is not None and (n - start) * 0.02 >= mindest:
        stillen.append((start * 0.02, n * 0.02))
    return stillen


def _packen(woerter, worte, max_px):
    """Woerter einer Strecke zu Einblendungen packen.

    Zwei Schranken: hoechstens `worte` Woerter, und die Zeile muss bei
    EINER Schriftgroesse auf EINE Zeile passen. Sein Einwand vom 20.10.:
    `CALLED THE HYPERMASCULINITY` kleiner zu setzen als den Rest faellt auf.
    Also wird die Einblendung geteilt, nicht die Schrift verkleinert —
    `CALLED THE` und `HYPERMASCULINITY` stehen beide gross da.
    """
    gruppen, akt = [], []
    for w in woerter:
        kand = akt + [w]
        text = " ".join(_anzeige(x["t"], True) for x in kand)
        schranke = FRAGE_BREITE if _ist_frage(kand) else max_px
        if akt and (len(kand) > worte or _breite_px(text) > schranke):
            gruppen.append(akt)
            akt = [w]
        else:
            akt = kand
    if akt:
        gruppen.append(akt)
    # Ein einzelnes Wort am Ende holt sich eines vom Vorgaenger, solange der
    # dabei nicht selbst zu einem einzelnen wird und die Zeile passt.
    if len(gruppen) >= 2 and len(gruppen[-1]) == 1 and len(gruppen[-2]) >= 3:
        kand = gruppen[-2][-1:] + gruppen[-1]
        text = " ".join(_anzeige(x["t"], True) for x in kand)
        if _breite_px(text) <= (FRAGE_BREITE if _ist_frage(kand) else max_px):
            gruppen[-2] = gruppen[-2][:-1]
            gruppen[-1] = kand
    return gruppen


def whisper_cues(clip, model_size="small", lang=None, worte=3, paare=None,
                 pause=0.45, max_px=MAX_BREITE):
    """Wortgenaue Zeiten fuer den bereits geschnittenen Clip.

    `worte` ist die Zahl der Woerter je Einblendung — drei, sein Wunsch vom
    20.10. Eine Einblendung aus einem einzigen Wort wandert zum Nachbarn.

    **Eine Einblendung laeuft nie ueber eine Satzgrenze.** Das war sein
    zweiter Einwand: wenn der letzte Satz endet und der naechste anfaengt,
    standen beide Teile in derselben Zeile und der Schnitt war im Bild nicht
    zu sehen. Getrennt wird an zwei Stellen: am Satzzeichen — und an einer
    **Sprechpause ueber `pause` Sekunden**, weil die Zeichensetzung des
    Modells unzuverlaessig ist, die Pause aber nicht.
    """
    from faster_whisper import WhisperModel
    import numpy as np
    # Den Ton selbst dekodieren statt faster-whisper die Datei geben:
    # es ruft PyAV mit `metadata_errors` auf, das die hier installierte
    # PyAV-Fassung nicht kennt (TypeError). Ueber ffmpeg ist es ohnehin
    # derselbe Weg, den der Rest dieser Datei geht — 16 kHz Mono float32,
    # genau das, was das Modell erwartet.
    roh = subprocess.run([FFMPEG, "-nostdin", "-v", "quiet", "-i", clip,
                          "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    ton = np.frombuffer(roh, dtype=np.float32)
    m = WhisperModel(model_size, device="cpu", compute_type="int8")
    # condition_on_previous_text=False: der Decoder nimmt sonst den vorher
    # erkannten Text als Vorlage und unterdrueckt Wiederholungen. Rick sagt
    # „you know" im Sekundentakt — gemessen am selben 80-s-Fenster von
    # rick5_mit: mit Vorlage 170 Woerter und 0x „you know", ohne Vorlage 188
    # Woerter und 7x. Eine ganze Fassung verlor so 90 Woerter, und die
    # Untertitel waren lueckenhaft, ohne dass irgendetwas davon meldete.
    segments, info = m.transcribe(ton, language=lang, word_timestamps=True,
                                  vad_filter=True,
                                  condition_on_previous_text=False)
    # Der Abschnitt, aus dem ein Wort stammt, wird mitgefuehrt: Whisper
    # trennt Saetze zuverlaessiger ueber seine eigenen Abschnitte als ueber
    # die Satzzeichen, die es setzt. `too afraid to touch.` und `This is why`
    # standen in getrennten Abschnitten — und trotzdem in einer Zeile, weil
    # der Punkt fehlte und die Pause zu kurz war.
    flach = [{"t": w.word.strip(), "start": w.start, "end": w.end, "seg": i}
             for i, s in enumerate(segments) for w in (s.words or [])
             if w.word.strip()]
    # Whisper liefert eine Nachsilbe mit Bindestrich als eigenes Wort:
    # `self` + `-initiation`. Zusammengesetzt mit Leerzeichen steht dann
    # `SELF -INITIATION` im Bild. Derselbe Fallstrick wie bei
    # `hyper` + `-masculinity` am 20.10. Hier zusammenziehen, vor den
    # Korrekturen — sonst findet die Liste das ganze Wort nicht.
    gezogen = []
    for w in flach:
        if (gezogen and w["t"].startswith("-") and len(w["t"]) > 1
                and gezogen[-1]["seg"] == w["seg"]):
            gezogen[-1] = {**gezogen[-1], "t": gezogen[-1]["t"] + w["t"],
                           "end": w["end"]}
        else:
            gezogen.append(w)
    flach = korrekturen_anwenden(gezogen, paare)

    # Pausen aus dem Ton: sie markieren die Satzgrenzen, die Whisper
    # verschluckt. Jede Stille schliesst das Wort ab, das vor ihr beginnt.
    nach_stille = set()
    for von, bis in stillen_finden(clip):
        kandidaten = [i for i, w in enumerate(flach) if w["start"] < von]
        if kandidaten:
            nach_stille.add(kandidaten[-1])

    cues, buf = [], []

    def schliessen(buf, grund):
        cues.append({"start": buf[0]["start"], "end": buf[-1]["end"],
                     "text": " ".join(w["t"] for w in buf),
                     "woerter": list(buf), "grund": grund})

    for i, w in enumerate(flach):
        buf.append(w)
        naechstes = flach[i + 1] if i + 1 < len(flach) else None
        luecke = (naechstes["start"] - w["end"]) if naechstes else 99
        if w["t"].endswith((".", "?", "!", "…")):
            grund = "satz"
        elif i in nach_stille:
            grund = "stille"
        elif naechstes and naechstes.get("seg") != w.get("seg"):
            grund = "abschnitt"
        elif luecke > pause:
            grund = "pause"
        elif len(buf) >= worte:
            grund = "voll"
        else:
            grund = None
        if grund:
            schliessen(buf, grund)
            buf = []
    if buf:
        schliessen(buf, "satz")

    # Drei Woerter heisst drei, nicht „meistens drei". In der Fassung davor
    # wanderte ein einzelnes Wort zum Nachbarn und machte daraus vier. Statt
    # zu verschieben werden die Woerter einer durchgehenden Strecke neu
    # aufgeteilt: vier Woerter werden 2+2, sieben werden 3+2+2. Ein Wort steht
    # nur dann allein, wenn die Strecke selbst nur aus einem besteht.
    # Eine „Strecke" endet an einer echten Grenze — Satzende, Abschnitt oder
    # Atempause. Ueber die hinweg wird nichts umverteilt.
    laeufe, aktuell = [], []
    for c in cues:
        aktuell.append(c)
        if c["grund"] != "voll":
            laeufe.append(aktuell)
            aktuell = []
    if aktuell:
        laeufe.append(aktuell)

    # Eine Strecke aus einem einzigen Wort gibt eine Einblendung aus einem
    # einzigen Wort — `LIKE` stand so im Bild. Sie wird mit dem Nachbarn
    # zusammengelegt, aber nur ueber eine Atempause hinweg: ueber ein Satzende
    # oder einen Abschnittswechsel wandert weiterhin nichts. Eine Strecke,
    # deren letzte Grenze auf „voll" steht, ist offen und nimmt die naechste auf.
    geglaettet = []
    for lauf in laeufe:
        laenge = sum(len(c["woerter"]) for c in lauf)
        offen = bool(geglaettet) and geglaettet[-1][-1]["grund"] == "voll"
        if offen:
            geglaettet[-1].extend(lauf)
        elif (laenge == 1 and geglaettet
              and geglaettet[-1][-1]["grund"] in ("pause", "stille")):
            geglaettet[-1][-1]["grund"] = "voll"
            geglaettet[-1].extend(lauf)
        elif laenge == 1 and lauf[-1]["grund"] in ("pause", "stille"):
            lauf[-1]["grund"] = "voll"      # nimmt die naechste Strecke auf
            geglaettet.append(lauf)
        else:
            geglaettet.append(lauf)
    laeufe = geglaettet

    zusammen = []
    for lauf in laeufe:
        teile = _packen([w for c in lauf for w in c["woerter"]], worte, max_px)
        for k, teil in enumerate(teile):
            # Innerhalb einer Strecke steht die naechste Einblendung sofort da,
            # damit es nicht zwischen jedem Dreier kurz schwarz wird.
            ende = teile[k + 1][0]["start"] if k + 1 < len(teile) else teil[-1]["end"]
            zusammen.append({"start": teil[0]["start"], "end": ende,
                             "text": " ".join(w["t"] for w in teil),
                             "woerter": teil,
                             "grund": lauf[-1]["grund"] if k + 1 == len(teile) else "voll"})
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


def lautheit(datei, dauer=None):
    """Integrierte Lautheit (LUFS) und wahre Spitze (dBTP) nach EBU R128.

    `volumedetect` taugt dafuer nicht: es misst den quadratischen Mittelwert
    ueber alles, Pausen eingerechnet. Fuer die Frage \u201eklingt das so laut wie
    seine anderen Shorts\u201c zaehlt die gegatete Lautheit.
    """
    cmd = [FFMPEG, "-hide_banner"]
    if dauer:
        cmd += ["-t", str(dauer)]
    cmd += ["-i", datei, "-af", "ebur128=peak=true", "-f", "null", os.devnull]
    p = subprocess.run(cmd, capture_output=True, text=True)
    lufs = spitze = None
    for zeile in p.stderr.splitlines():
        t = zeile.strip()
        if t.startswith("I:") and "LUFS" in t:
            lufs = float(t.split()[1])
        elif t.startswith("Peak:") and "dBFS" in t:
            spitze = float(t.split()[1])
    return lufs, spitze


def lautheit_kette(ziel):
    """Filterkette, die Sprache auf `ziel` LUFS bringt.

    Vor dem `loudnorm` steht ein milder Kompressor: aus -31 LUFS auf -14 sind
    17 dB, und die will man nicht allein ueber den Begrenzer holen. Gemessen
    schrumpft die Dynamik dabei nur von 32,7 auf 30,4 dB, es pumpt also
    nicht. Danach ein Begrenzer gegen einzelne Spitzen.
    """
    return ("highpass=f=80,"
            "acompressor=threshold=-26dB:ratio=3:attack=5:release=150:makeup=1,"
            f"loudnorm=I={ziel}:TP=-1.5:LRA=9,"
            "alimiter=limit=-1dB:level=disabled")


def _logo_kasten(pfad):
    """(x, y, breite, hoehe) des sichtbaren Teils eines PNG mit Alphakanal.

    Rueckgabe None, wenn die Datei randlos ist oder sich nicht lesen laesst —
    dann wird nicht zugeschnitten.
    """
    try:
        from PIL import Image
        im = Image.open(pfad).convert("RGBA")
        bb = im.getchannel("A").getbbox()
    except Exception:
        return None
    if not bb:
        return None
    x0, y0, x1, y1 = bb
    if (x1 - x0) >= im.size[0] * 0.98 and (y1 - y0) >= im.size[1] * 0.98:
        return None
    return x0, y0, x1 - x0, y1 - y0


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


def broll_lesen(spec):
    """'12.4:15.8=clip.mp4,20:23=zweit.mp4' -> [(von, bis, datei), ...].

    Zeiten in Clipzeit, wie bei --stumm: das ist die Zeit, in der er die
    Stelle im Transkript sieht. Auf die Zeit des fertigen Bildes gerechnet
    wird erst dort, wo der Filter wirklich haengt.
    """
    stuecke = []
    for teil in spec.split(","):
        teil = teil.strip()
        if not teil:
            continue
        zeit, _, datei = teil.partition("=")
        if not datei:
            raise SystemExit(f"--broll: '{teil}' hat keine Datei "
                             f"(Form: von:bis=datei)")
        try:
            von, bis = (float(x) for x in zeit.split(":"))
        except ValueError:
            raise SystemExit(f"--broll: '{zeit}' ist kein Zeitpaar von:bis")
        if bis <= von:
            raise SystemExit(f"--broll: {von}:{bis} endet nicht nach dem Anfang")
        if not Path(datei).is_file():
            raise SystemExit(f"--broll: {datei} gibt es nicht")
        stuecke.append((von, bis, datei))
    stuecke.sort(key=lambda s: s[0])
    for (v1, b1, _), (v2, b2, _) in zip(stuecke, stuecke[1:]):
        if v2 < b1:
            raise SystemExit(f"--broll: {v1}:{b1} und {v2}:{b2} ueberlappen")
    return stuecke


def _ecken_alpha(seite, radius):
    """geq-Ausdruck fuer die Alphamaske einer Karte mit runden Ecken.

    Abstand zur naechsten Ecke nur dort messen, wo man ueberhaupt im
    Eckviertel ist — sonst ist dx=dy=0 und die Flaeche bleibt voll deckend.
    Der halbe Pixel Weichheit nimmt die Treppe aus dem Bogen.
    """
    r = radius
    dx = f"max(max({r}-X,X-({seite}-1-{r})),0)"
    dy = f"max(max({r}-Y,Y-({seite}-1-{r})),0)"
    return f"clip(({r}-sqrt(pow({dx},2)+pow({dy},2))+0.5)*255,0,255)"


def broll_graph(stuecke, quelle, tempo, modus, seite, radius, fokus,
                erste_eingabe):
    """B-Roll ueber das Bild legen — randlos oder als Karte.

    **Vorgabe ist randlos**, weil das sein Bild ist: 1080x1920 gefuellt, wie
    jede andere Einstellung seiner Shorts auch. Die quadratische Karte auf
    Schwarz ist Williamsons Rahmen, nicht seiner — sie bleibt als `--broll-
    modus karte` erhalten, weil sie ausgemessen und gebaut ist, steht aber
    nicht mehr im Weg.

    Preis des randlosen Wegs, und der gehoert dazu: aus einem 16:9-Film
    bleiben im 9:16-Fenster **31,6 % der Breite** uebrig. Was links und
    rechts steht, ist weg. Deshalb `--broll-fokus`, das den Ausschnitt waag-
    recht schiebt — wie `--focus` beim Hauptbild.

    `tempo` rechnet die Clipzeit auf die Zeit des fertigen Bildes um, weil
    dieser Filter hinter `setpts` haengt. Das ist genau der Fehler, der am
    20.10. die Stummschaltung acht Sekunden zu spaet greifen liess.
    """
    fenster = [(von / tempo, bis / tempo) for von, bis, _ in stuecke]
    teile, letzte = [], quelle

    if modus == "karte":
        # Nur hier wird der Grund schwarz: die Karte deckt das Bild nicht ab,
        # ohne das Abdunkeln saehe man ihn ringsherum weiterreden.
        bed = "+".join(f"between(t,{a:.3f},{b:.3f})" for a, b in fenster)
        teile.append(f"{quelle}lutyuv=y=0:u=128:v=128:enable='{bed}'[bgrund]")
        letzte = "[bgrund]"

    alpha = _ecken_alpha(seite, radius)
    for i, (a, b) in enumerate(fenster):
        k = erste_eingabe + i
        kopf = (f"[{k}:v]trim=0:{b - a:.3f},setpts=PTS-STARTPTS+{a:.3f}/TB,")
        if modus == "karte":
            teile.append(
                kopf
                + f"scale={seite}:{seite}:force_original_aspect_ratio=increase,"
                f"crop={seite}:{seite},fps=30,setsar=1,format=rgba,"
                f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='{alpha}'[bk{i}]")
            x, y = (W - seite) // 2, (H - seite) // 2
        elif modus == "unschaerfe":
            # Randlos, aber nichts wird beschnitten: der Film laeuft in voller
            # Breite scharf in der Mitte, dahinter steht er vergroessert und
            # unscharf und fuellt das Bild. Fuer Quellen, bei denen ein
            # 9:16-Ausschnitt zu wenig echte Pixel uebrig laesst — beim
            # Into-the-Wild-Trailer waeren es 513 von 2153.
            # Der scharfe Teil ist quadratisch, nicht in voller Breite: ein
            # 2,36:1-Trailer waere ueber die ganze Breite nur 458 von 1920
            # Pixeln hoch, also ein duenner Streifen. Quadratisch geschnitten
            # steht er bei 1080x1080 — aus 913 echten Pixeln, also Faktor
            # 1,18 statt 2,10 beim 9:16-Ausschnitt.
            f = min(max(fokus, 0.0), 1.0)
            teile.append(kopf + f"fps=30,setsar=1,split=2[bg{i}][fg{i}]")
            # Erst klein rechnen, dann unscharf, dann wieder gross: eine
            # starke Weichzeichnung sieht danach genauso aus und kostet ein
            # Sechzehntel. Bei 1080x1920 war `gblur=sigma=42` der Grund,
            # warum ein 33-Sekunden-Short 25 Minuten brauchte.
            teile.append(
                f"[bg{i}]scale={W}:{H}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H},scale={W // 4}:{H // 4},gblur=sigma=11,"
                f"scale={W}:{H}:flags=bilinear,eq=brightness=-0.16[bgu{i}]")
            teile.append(
                f"[fg{i}]crop='min(iw,ih)':'min(iw,ih)':'(iw-min(iw,ih))*{f}':"
                f"'(ih-min(iw,ih))/2',scale={W}:{W}[fgs{i}]")
            teile.append(f"[bgu{i}][fgs{i}]overlay=0:(H-h)/2[bk{i}]")
            x, y = 0, 0
        else:
            # Randlos: auf Hoehe bringen, dann das 9:16-Fenster waagrecht
            # dorthin schieben, wo das Motiv steht.
            teile.append(
                kopf
                + f"scale={W}:{H}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H}:(iw-{W})*{min(max(fokus, 0.0), 1.0)}:(ih-{H})/2,"
                f"fps=30,setsar=1[bk{i}]")
            x, y = 0, 0
        teile.append(f"{letzte}[bk{i}]overlay={x}:{y}:"
                     f"enable='between(t,{a:.3f},{b:.3f})'[bo{i}]")
        letzte = f"[bo{i}]"
    return teile, letzte, fenster


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
    # 1,15 ist seine Ansage vom 21.10.: „dass wir die Shorts allesamt auf
    # 1,15-facher Geschwindigkeit laufen lassen". Davor war 1,2 von Hand
    # mitgegeben; seine Folgen selbst laufen auf 1,1.
    ap.add_argument("--tempo", type=float, default=1.15,
                    help="Beschleunigung. Seine Folgen laufen auf 1.1, fuer "
                         "Shorts will er 1.2. 1.0 = unveraendert.")
    ap.add_argument("--worte", type=int, default=3,
                    help="Woerter je Einblendung (sein Wunsch: 3)")
    ap.add_argument("--tiefer", type=int, default=0,
                    help="Pixel, um die die Zeile zusaetzlich nach unten "
                         "rueckt; der Plan setzt die Hoehe schon unter die Lippe")
    ap.add_argument("--schriftgroesse", type=int, default=GROESSE,
                    help=f"Vorgabe {GROESSE} aus seinem Preset")
    ap.add_argument("--korrekturen", default="video/korrekturen.txt",
                    help="Liste falsch -> richtig fuer die Untertitel")
    ap.add_argument("--pause", type=float, default=0.45,
                    help="Sprechpause in Sekunden, ab der eine Einblendung "
                         "endet (Satzgrenze ohne Satzzeichen)")
    ap.add_argument("--logo", default=None,
                    help="PNG mit Transparenz, wird unten mittig eingeblendet")
    ap.add_argument("--logo-breite", type=int, default=int(W * 0.28),
                    help="Vorgabe 28 %% der Bildbreite, aus seinem Preset")
    ap.add_argument("--logo-alpha", type=float, default=1.0)
    ap.add_argument("--logo-hoehe", type=float, default=0.87,
                    help="Anteil der Bildhoehe, auf dem das Logo sitzt "
                         "(Vorgabe 0.87 aus seinem Preset)")
    ap.add_argument("--kopfzeile", default=None,
                    help="Schlagzeile ueber die ersten Sekunden, wie bei "
                         "Modern Wisdom. `|` trennt Zeilen. Beispiel: "
                         "\"Is AI safe?\"")
    ap.add_argument("--kopfzeile-dauer", type=float, default=4.5,
                    help="Sekunden im fertigen Video (Vorgabe 4.5)")
    ap.add_argument("--kopfzeile-groesse", type=int, default=96)
    ap.add_argument("--kopfzeile-hoehe", type=float, default=0.68,
                    help="Mitte des Feldes als Anteil der Bildhoehe")
    ap.add_argument("--kopfzeile-hell", action="store_true",
                    help="weisses Feld mit schwarzer Schrift, wie bei Modern "
                         "Wisdom. Vorgabe ist umgekehrt: schwarzes Feld, "
                         "weisse Schrift — so hat er es am 21.10. bestellt.")
    ap.add_argument("--musik", default=None,
                    help="Musikbett; wird geloopt, ein- und ausgeblendet und "
                         "unter der Stimme abgesenkt")
    ap.add_argument("--musik-db", type=float, default=None,
                    help="fester Pegel des Betts; ohne Angabe wird er aus "
                         "Stimme und Bett gemessen")
    ap.add_argument("--musik-unter", type=float, default=8.0,
                    help="dB, die das Bett unter der Stimme liegt")
    ap.add_argument("--srt-out", default=None,
                    help="Einblendungen zusaetzlich als .srt ablegen, in der "
                         "Zeit des fertigen Videos. Fuer den Weg ueber einen "
                         "Schnittplatz: CapCut Desktop liest .srt.")
    ap.add_argument("--dehnung", choices=("atempo", "rubberband"),
                    default="atempo",
                    help="Verfahren fuer --tempo. atempo (WSOLA) ist messbar "
                         "rauher, aber es ist der Klang, den er abgenommen "
                         "hat. rubberband nur bewusst einschalten.")
    ap.add_argument("--laut", default="aus",
                    help="Ziellautheit in LUFS fuer Hauptteil UND Outro, "
                         "'aus' laesst den Pegel wie er ist (Vorgabe). Der "
                         "Master liegt bei -31 LUFS, Shorts laufen bei etwa "
                         "-14 — aber die Angleichung hebt den Rauschboden um "
                         "18 dB, und genau das hat er am 20.10. abgelehnt.")
    ap.add_argument("--stumm", default=None,
                    help="Zeitfenster im Clip, die stumm geschaltet werden, "
                         "z. B. 49.50:49.98,12.1:12.4 — fuer Zwischenrufe des "
                         "Gegenuebers, die den Fluss stoeren")
    ap.add_argument("--outro", default=None,
                    help="Clip, der hinten angehaengt wird; wird auf 1080x1920 "
                         "und 30 Bilder gebracht, bekommt aber weder Look noch "
                         "Logo noch Untertitel")
    ap.add_argument("--klein", action="store_true",
                    help="keine Grossbuchstaben (sein Kanal nutzt Versalien)")
    ap.add_argument("--broll", default=None,
                    help="B-Roll als Karte: 'von:bis=datei[,von:bis=datei]', "
                         "Zeiten in Clipzeit wie bei --stumm. Der Ton der "
                         "B-Roll wird verworfen, die Stimme laeuft durch.")
    ap.add_argument("--broll-modus",
                    choices=["vollbild", "unschaerfe", "karte"],
                    default="vollbild",
                    help="vollbild: 9:16 aus der B-Roll geschnitten. "
                         "unschaerfe: Film scharf in voller Breite, dahinter "
                         "er selbst vergroessert und unscharf — nichts wird "
                         "beschnitten. karte: Williamsons Quadrat auf Schwarz.")
    ap.add_argument("--broll-fokus", type=float, default=0.5,
                    help="0..1 schiebt das 9:16-Fenster waagrecht durch die "
                         "B-Roll — aus 16:9 bleiben nur 31,6 %% der Breite")
    ap.add_argument("--broll-seite", type=int, default=BROLL_SEITE,
                    help=f"nur bei --broll-modus karte: Kantenlaenge "
                         f"(Vorgabe {BROLL_SEITE}, an der Referenz gemessen)")
    ap.add_argument("--broll-radius", type=int, default=BROLL_RADIUS,
                    help=f"nur bei --broll-modus karte: Eckradius "
                         f"(Vorgabe {BROLL_RADIUS})")
    ap.add_argument("--look", choices=["preset", "warm", "aus"],
                    default="preset",
                    help="preset = sein CapCut-Filter als LUT (--lut), sonst "
                         "die Annaeherung aus seinem Preset. warm = die "
                         "aeltere Annaeherung von seinen Vorschaubildern.")
    ap.add_argument("--lut", default=str(LUT_VORGABE),
                    help="Hald-CLUT-PNG mit seinem Filter. Liegt sie nicht "
                         "da, laeuft die Annaeherung und es steht in der "
                         "Ausgabe.")
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

    if a.stumm:
        # Ein kurzes „Yeah" des Gegenuebers zwischen zwei Saetzen bricht den
        # Fluss. Stummschalten statt herausschneiden: das Bild laeuft weiter,
        # der Schnitt bleibt ruhig, und die Pause war ohnehin da.
        fenster = []
        for teil in a.stumm.split(","):
            von, bis = (float(x) for x in teil.split(":"))
            fenster.append(f"between(t,{von},{bis})")
        quelle = a_quelle if a_quelle.startswith("[") else f"[{a_quelle.rstrip('?')}]"
        graph.append(f"{quelle}volume=enable='{'+'.join(fenster)}':volume=0[astumm]")
        a_quelle = "[astumm]"
        print(f"  {len(fenster)} Fenster stummgeschaltet (vor dem Tempo, "
              f"also in Clipzeit)")

    if a.tempo != 1.0:
        graph.append(f"{v_quelle}setpts=PTS/{a.tempo}[vt]")
        v_quelle = "[vt]"
        if a.dehnung == "rubberband":
            dehner = (f"rubberband=tempo={a.tempo}:transients=crisp"
                      ":pitchq=quality")
        else:
            dehner = f"atempo={a.tempo}"
        ein = a_quelle if a_quelle.startswith("[") else f"[{a_quelle.rstrip('?')}]"
        graph.append(f"{ein}{dehner}[at]")
        a_quelle = "[at]"
        print(f"  Tempo {a.tempo}x ueber {a.dehnung}")

    if a.look != "aus":
        lut = a.lut if (a.look == "preset" and a.lut
                        and os.path.exists(a.lut)) else None
        if lut:
            # haldclut traegt seinen CapCut-Filter Pixel fuer Pixel auf,
            # die Vignette kommt wie im Preset hinterher.
            graph.append(f"movie={lut}[clut]")
            graph.append(f"{v_quelle}[clut]haldclut,vignette=PI/6[vlook]")
            print(f"  Look: LUT {lut}")
        else:
            graph.append(f"{v_quelle}"
                         f"{LOOK_PRESET if a.look == 'preset' else LOOK}"
                         f"[vlook]")
            print("  Look: Annaeherung"
                  + (f" (LUT {a.lut} fehlt)" if a.look == "preset" else " warm"))
        v_quelle = "[vlook]"

    # B-Roll kommt HINTER den Look und VOR die Untertitel: der Film soll
    # nicht durch seine warme Gradation laufen (in der Referenz sieht die
    # B-Roll aus wie Film, nicht wie sein Studio), die Einblendungen sollen
    # aber darauf stehen.
    broll = broll_lesen(a.broll) if a.broll else []
    if broll:
        graph_b, v_quelle, fenster_b = broll_graph(
            broll, v_quelle, a.tempo, a.broll_modus, a.broll_seite,
            a.broll_radius, a.broll_fokus, 1)
        graph += graph_b
        for (von, bis, datei), (fa, fb) in zip(broll, fenster_b):
            print(f"  B-Roll {von:.2f}-{bis:.2f} Clipzeit "
                  f"-> {fa:.2f}-{fb:.2f} im Bild ({fb - fa:.2f}s): "
                  f"{os.path.basename(datei)}")
        if a.broll_modus == "karte":
            print(f"  Karte {a.broll_seite}x{a.broll_seite} auf "
                  f"x={(W - a.broll_seite) // 2}/"
                  f"y={(H - a.broll_seite) // 2}, "
                  f"Radius {a.broll_radius}, Grund schwarz")
        else:
            print(f"  randlos {W}x{H}, Fokus {a.broll_fokus:.2f}")

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

        if cues and a.srt_out:
            n = cues_als_srt(cues, a.srt_out, tempo=a.tempo, gross=not a.klein)
            print(f"  {n} Zeilen nach {a.srt_out}")

        letzte = v_quelle
        if cues:
            if lippen:
                cues = cues_an_lippen(cues, lippen)
                print(f"  Untertitel an der Lippe: {len(cues)} Zeilen, "
                      f"Hoehen {sorted({l for _,_,l in lippen if l})}")
            elif a.lippe is not None:
                cues = [{**c, "lippe": a.lippe} for c in cues]
            elif a.marginv is None:
                # Steht die Lippe nicht fest, sitzt die Zeilenmitte auf
                # 70 % der Bildhoehe — der Wert aus seinem Preset. \an8
                # haengt die Zeile an der Oberkante auf, darum die halbe
                # Schriftgroesse abziehen. --marginv schlaegt das.
                oben = LIPPE_VORGABE - a.schriftgroesse // 2
                cues = [{**c, "lippe": oben} for c in cues]
            ass = os.path.join(td, "cap.ass")
            build_ass(cues, ass, marginv=marginv, tempo=a.tempo,
                      tiefer=a.tiefer, gross=not a.klein,
                      groesse=a.schriftgroesse)
            print(f"  {a.worte} Woerter je Einblendung, "
                  f"{'VERSALIEN' if not a.klein else 'gemischt'}, "
                  f"{a.tiefer} px unter der Lippe, Look: {a.look}")
            filt = "subtitles=" + ass.replace(":", r"\:")
            if FONT_DATEI:
                filt += ":fontsdir=" + str(FONT_ORDNER).replace(":", r"\:")
            graph.append(f"{v_quelle}{filt}[vout]")
            letzte = "[vout]"

        cmd = [FFMPEG, "-y"]
        if not a.plan:
            cmd += ["-ss", str(t0)]
            # `-t` MUSS vor das `-i` der Quelle. ffmpeg ordnet Optionen der
            # naechsten Datei zu: stand es dahinter und folgte noch ein
            # Eingang (Logo, B-Roll), band es an DESSEN Eingang und
            # begrenzte gar nichts. Am 22.10. kam so ein Short heraus, der
            # bis zum Ende der Quelle lief — 54 s statt 45 s — und am
            # Standbild nichts davon zeigte.
            if dur:
                cmd += ["-t", str(dur)]
        cmd += ["-i", a.src]
        naechste = 1
        for _, _, datei in broll:
            # Nur das Bild wird gebraucht; -an haelt den Ton der B-Roll
            # von vornherein draussen, damit nie zwei Stimmen laufen.
            cmd += ["-an", "-i", datei]
            naechste += 1

        if a.kopfzeile:
            kopf_ass = os.path.join(td, "kopf.ass")
            kb, kh = kopfzeile_ass(
                a.kopfzeile, kopf_ass, a.kopfzeile_dauer,
                groesse=a.kopfzeile_groesse,
                hoehe_anteil=a.kopfzeile_hoehe,
                dunkel=not a.kopfzeile_hell)
            filt = "subtitles=" + kopf_ass.replace(":", r"\:")
            if FONT_DATEI:
                filt += ":fontsdir=" + str(FONT_ORDNER).replace(":", r"\:")
            graph.append(f"{letzte}{filt}[vkopf]")
            letzte = "[vkopf]"
            print(f"  Kopfzeile {a.kopfzeile!r}: Feld {kb}x{kh} px, "
                  f"{a.kopfzeile_dauer}s, "
                  + ("weiss auf schwarz" if not a.kopfzeile_hell
                     else "schwarz auf weiss"))
            # Kopfzeile und Untertitel koennen sich treffen: das Feld sitzt
            # mittig auf 68 % der Hoehe, die Zeile ohne gemessene Lippe auf
            # 70 %. Das faellt am Code nicht auf, nur im Bild — also wird es
            # ausgerechnet und gesagt, statt es zu riskieren.
            feld_oben = a.kopfzeile_hoehe * H - kh / 2
            feld_unten = feld_oben + kh
            band = [(c["lippe"] + a.tiefer, c["lippe"] + a.tiefer + a.schriftgroesse)
                    for c in (cues or [])
                    if c.get("lippe") is not None
                    and c["start"] / a.tempo < a.kopfzeile_dauer]
            stoss = [b for b in band if b[0] < feld_unten and b[1] > feld_oben]
            if stoss:
                print(f"  ACHTUNG: Kopfzeile ({feld_oben:.0f}-{feld_unten:.0f} px) "
                      f"und Untertitel ({min(b[0] for b in stoss):.0f}-"
                      f"{max(b[1] for b in stoss):.0f} px) ueberlappen in den "
                      f"ersten {a.kopfzeile_dauer}s. --kopfzeile-hoehe "
                      f"verschieben oder die Kopfzeile kuerzer halten.")

        if a.logo:
            # Auf den sichtbaren Teil zuschneiden, BEVOR skaliert wird.
            # `marke/ynb-logo-weiss.png` ist 5224x2947 gross, die Marke darin
            # aber nur 1924 px breit — 36,8 Prozent. Wer die Datei auf 28
            # Prozent der Bildbreite skaliert, bekommt eine Marke von 111 px
            # statt der gemeinten 302. Genau das war sein Einwand vom 22.10.
            # („das Logo ist wieder mal zu klein"). `--logo-breite` meint ab
            # jetzt die Breite der MARKE, nicht die der Datei.
            kasten = _logo_kasten(a.logo)
            cmd += ["-i", a.logo]
            zuschnitt = (f"crop={kasten[2]}:{kasten[3]}:{kasten[0]}:{kasten[1]},"
                         if kasten else "")
            graph.append(f"[{naechste}:v]{zuschnitt}"
                         f"scale={a.logo_breite}:-1,format=rgba,"
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

        ziel = None if a.laut.strip().lower() == "aus" else float(a.laut)
        if ziel is not None:
            gemessen, spitze = lautheit(a.src, dauer=clip_laenge)
            if gemessen is not None:
                print(f"  Quelle {gemessen:.1f} LUFS, Spitze {spitze:.1f} dBFS"
                      f" -> {ziel:.1f} LUFS")
            stimme = a_quelle if a_quelle.startswith("[") else f"[{a_quelle.rstrip('?')}]"
            graph.append(f"{stimme}{lautheit_kette(ziel)}[alaut]")
            a_quelle = "[alaut]"

        if a.outro:
            cmd += ["-i", a.outro]
            graph.append(f"[{naechste}:v]scale={W}:{H}:"
                         f"force_original_aspect_ratio=decrease,"
                         f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,"
                         f"format=yuv420p[ov]")
            outro_ton = (f"[{naechste}:a]aformat=sample_fmts=fltp:"
                         f"sample_rates=48000:channel_layouts=stereo")
            if ziel is not None:
                # Das Outro liegt bei -24,9 LUFS, der angeglichene Hauptteil
                # bei -14. Ohne diesen Schritt springt der Ton am Uebergang.
                outro_ton += "," + lautheit_kette(ziel)
            graph.append(outro_ton + "[oa]")
            stimme = a_quelle if a_quelle.startswith("[") else f"[{a_quelle.rstrip('?')}]"
            graph.append(f"{letzte}format=yuv420p[vm]")
            graph.append(f"{stimme}aformat=sample_fmts=fltp:sample_rates=48000:"
                         f"channel_layouts=stereo[am]")
            graph.append("[vm][am][ov][oa]concat=n=2:v=1:a=1[vend][aend]")
            letzte, a_quelle = "[vend]", "[aend]"
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
