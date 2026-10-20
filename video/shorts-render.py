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
        text = " ".join(_anzeige(w["t"], gross) for w in c["woerter"])
        zeilen.append(f"{i}\n{srt_time(c['start'] / tempo)} --> "
                      f"{srt_time(c['end'] / tempo)}\n{text}\n")
    Path(pfad).write_text("\n".join(zeilen), encoding="utf-8")
    return len(cues)


SATZZEICHEN = ".,!?;:\u2026"
# Was im Bild wegfaellt: alles, was nur Satzbau ist. `?` und `!` bleiben.
STUMME_ZEICHEN = ".,;:\u2026"


def _anzeige(wort, gross):
    """Wort, wie es im Bild steht: ohne Punkt, aber mit Fragezeichen.

    Sein Einwand vom 20.10.: „du hast an zwei, drei Stellen noch einen Punkt
    gemacht und ein Fragezeichen, das wirkt total fehl am Platz." Also fielen
    erst alle Satzzeichen weg. Am selben Abend, am Aaronson-Short: „da wo ich
    die Frage stelle, how safe is AI, danach sollte ein Fragezeichen kommen."

    Beides stimmt, und es ist kein Widerspruch: **gestoert hat ihn ein
    Fragezeichen, das keine Frage war** — eines, das Whisper an eine Aussage
    gehaengt hatte. Ein echtes Fragezeichen traegt. Also faellt weiterhin
    alles weg, was nur Satzbau ist (`. , ; : …`), und `?` und `!` bleiben
    stehen. Sitzt eines falsch, ist das ein Hoerfehler und gehoert in
    `korrekturen.txt`, nicht in eine Regel, die alle Fragezeichen abraeumt.

    Fuer die TRENNUNG braucht das Werkzeug den Punkt weiterhin, deshalb
    faellt er erst hier weg und nicht schon im Transkript. Apostrophe
    bleiben: IT'S, THERE'S.
    """
    w = wort.rstrip(STUMME_ZEICHEN)
    return w.upper() if gross else w


def _breite_em(text):
    """Textbreite in Geviert — an DejaVu Sans Bold ausgemessen, nicht geraten.

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


def build_ass(cues, path, marginv=320, tempo=1.0, tiefer=0, gross=True,
              groesse=78, rand=40):
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
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{FONT},{groesse},{WEISS},&H00000000,&H00000000,-1,0,1,8,3,2,{rand},{rand},{marginv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    nutzbar = W - 2 * rand

    def zeile(von, bis, text, lippe, fs):
        kopf = ""
        if lippe is not None:
            kopf = f"{{\\an8\\pos({W // 2},{int(lippe) + tiefer})}}"
        if fs != groesse:
            kopf += f"{{\\fs{fs}}}"
        lines.append(f"Dialogue: 0,{ass_time(von / tempo)},{ass_time(bis / tempo)},"
                     f"Cap,,0,0,0,,{kopf}{text}")

    for c in cues:
        woerter = [w for w in (c.get("woerter") or [])
                   if w["t"].strip() and w["end"] > c["start"] and w["start"] < c["end"]]
        roh = [_anzeige(w["t"], gross) for w in woerter]
        roh = [w for w in roh if w]
        if not roh:
            continue
        fs = groesse
        if not woerter:
            zeile(c["start"], c["end"], " ".join(roh), c.get("lippe"), fs)
            continue
        for i, w in enumerate(woerter):
            von = max(w["start"], c["start"]) if i else c["start"]
            bis = min(woerter[i + 1]["start"], c["end"]) if i + 1 < len(woerter) else c["end"]
            if bis - von <= 0.02:
                continue
            teile = [f"{{\\c{GELB_I if k == i else WEISS_I}}}{t}"
                     for k, t in enumerate(roh)]
            zeile(von, bis, " ".join(teile), c.get("lippe"), fs)

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
        # Satzzeichen des Originals uebernehmen — ausser die Korrektur bringt
        # selbst eines mit. Sonst stuende dort "AI??", sobald Whisper das
        # Fragezeichen auch gesetzt hat, und ohne diese Regel haengt es davon
        # ab, wie der Lauf gerade ausgegangen ist.
        if ersatz and ersatz[-1][-1:] in ".,!?;:":
            schwanz = ""
        else:
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


def _packen(woerter, worte, max_em):
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
        if akt and (len(kand) > worte or _breite_em(text) > max_em):
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
        if _breite_em(text) <= max_em:
            gruppen[-2] = gruppen[-2][:-1]
            gruppen[-1] = kand
    return gruppen


def whisper_cues(clip, model_size="small", lang=None, worte=3, paare=None,
                 pause=0.45, max_em=11.8):
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
        teile = _packen([w for c in lauf for w in c["woerter"]], worte, max_em)
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
    ap.add_argument("--schriftgroesse", type=int, default=78)
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
