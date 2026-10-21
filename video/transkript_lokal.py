#!/usr/bin/env python3
"""Transkript einer lokalen Tondatei, mit Zeitmarken und Sprecherzuordnung.

    python3 video/transkript_lokal.py --ton roh_mix.flac --model medium \
            --spuren spur1.mp3 spur2.mp3 spur4.mp3 \
            --namen Aaronson Yannick Raum \
            --out video/transkripte/aaronson.transkript.md

Fuer veroeffentlichte Folgen gibt es `yt-transkript.py` — das holt die
automatischen Untertitel und kostet nichts. Dieses Werkzeug ist fuer
Material, das noch nicht online steht.

Die Sprecherzuordnung kommt NICHT aus einem Diarisierungsmodell, sondern
aus den Einzelspuren: wer gerade spricht, ist auf seinem eigenen Mikrofon
am lautesten. Jede Spur wird dafuer zuerst auf ihren eigenen Sprechpegel
normiert, sonst gewinnt immer die lauteste Aufnahme. Ohne `--spuren`
bleibt die Zuordnung weg.
"""
import argparse
import json
import sys
import subprocess
from pathlib import Path

import numpy as np
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def huelle(pfad, rate=100):
    """Lautstaerkeverlauf in dB, `rate` Werte je Sekunde."""
    roh = subprocess.run(
        [FFMPEG, "-nostdin", "-v", "error", "-i", str(pfad),
         "-ac", "1", "-ar", str(rate * 10), "-f", "s16le", "-"],
        capture_output=True).stdout
    a = np.frombuffer(roh, dtype=np.int16).astype(np.float32) / 32768
    n = len(a) // 10
    e = np.sqrt((a[:n * 10].reshape(n, 10) ** 2).mean(1)) + 1e-9
    return 20 * np.log10(e)


def trennt_die_spuren(segmente, h, rate=100, mindest_spreizung=4.0):
    """Taugen diese Spuren ueberhaupt zur Sprecherzuordnung?

    Zwei Lavaliers trennen Sprecher, weil das Verhaeltnis der Pegel kippt,
    je nachdem wer spricht. Drei Mikrofone, die denselben Raum aufnehmen,
    tun das nicht — ihr Verhaeltnis bleibt konstant, nur die Verstaerkung
    ist anders eingestellt.

    Geprueft wird deshalb die **Spreizung des Pegelverhaeltnisses** je
    Spurpaar ueber alle Segmente (Quartilsabstand). Kippt das Verhaeltnis
    nie, traegt es keine Information ueber den Sprecher, und eine Zuordnung
    daraus waere erfunden.

    Am Aaronson-Material vom 21.08.2026 gemessen: Quartilsabstand 2,4 dB
    (Spur 4 gegen 1) und 2,3 dB (Spur 2 gegen 1), beide Verteilungen
    eingipflig. Die drei mp3 sind drei Mikrofone im selben Raum mit rund
    -17 und -7 dB Versatz, keine getrennten Ansteckmikrofone.
    """
    paare = []
    for i in range(1, len(h)):
        d = []
        for seg in segmente:
            a, b = int(seg["start"] * rate), int(seg["end"] * rate)
            if b - a < rate * 0.8 or b > min(len(h[0]), len(h[i])):
                continue
            d.append(np.percentile(h[i][a:b], 80) - np.percentile(h[0][a:b], 80))
        if not d:
            continue
        d = np.array(d)
        paare.append(float(np.percentile(d, 75) - np.percentile(d, 25)))
    return (max(paare) if paare else 0.0), mindest_spreizung


def sprecher_zuordnen(segmente, spuren, namen, rate=100):
    """Je Segment die Spur mit dem hoechsten Pegel ueber ihrem eigenen Mittel.

    Der Bezug ist das 75. Perzentil der jeweiligen Spur — ihr Sprechpegel.
    Dadurch zaehlt der Abstand zum eigenen Normal, nicht die absolute
    Lautstaerke; sonst gewaenne eine heiss ausgesteuerte Aufnahme immer.

    Vorher wird geprueft, ob die Spuren ueberhaupt trennen. Tun sie es
    nicht, bleibt die Zuordnung weg — **lieber kein Sprechername als ein
    erfundener.** Der erste Lauf am Aaronson-Material hat Namen vergeben,
    die reines Rauschen waren, und sie sahen im Transkript genauso
    verlaesslich aus wie echte.
    """
    h = [huelle(p, rate) for p in spuren]
    spreizung, mindest = trennt_die_spuren(segmente, h, rate)
    if spreizung < mindest:
        print(f"  KEINE Sprecherzuordnung: die Spuren trennen nicht "
              f"(groesste Spreizung {spreizung:.1f} dB, gebraucht "
              f"{mindest:.0f} dB). Das sind Mikrofone im selben Raum, "
              f"keine getrennten Ansteckmikrofone.")
        return segmente, False
    print(f"  Sprecherzuordnung aus den Spuren (Spreizung {spreizung:.1f} dB)")
    bezug = [np.percentile(x, 75) for x in h]
    for seg in segmente:
        a, b = int(seg["start"] * rate), int(seg["end"] * rate)
        if b <= a:
            continue
        werte = [float(np.percentile(x[a:b], 80) - r) if b <= len(x) else -99
                 for x, r in zip(h, bezug)]
        i = int(np.argmax(werte))
        zweiter = sorted(werte)[-2] if len(werte) > 1 else -99
        seg["sprecher"] = namen[i]
        seg["abstand"] = round(werte[i] - zweiter, 1)
    return segmente, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ton", required=True)
    ap.add_argument("--model", default="medium")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--titel", default=None)
    ap.add_argument("--spuren", nargs="*", default=None)
    ap.add_argument("--namen", nargs="*", default=None)
    ap.add_argument("--out", required=True)
    # Zuschaltbar, nicht Vorgabe: ohne diesen Schalter verhaelt sich das
    # Werkzeug genau wie bisher. Der Stimmabdruck ordnet die Abschnitte ueber
    # die Aehnlichkeit zu seiner Stimme zu — er ist in jeder Folge, also muss
    # nur eine Klasse gelernt werden. Gemessen am 21.10.2026 folgenweise an
    # 93 handbeschrifteten Abschnitten: 89 % entschieden, davon 100 % richtig,
    # 11 % verweigert. Was unsicher ist, bekommt "?" statt eines Namens.
    ap.add_argument("--stimmabdruck", default=None, metavar="TONDATEI",
                    help="Sprecher ueber den Stimmabdruck zuordnen. Braucht "
                         "die Mediendatei, aus der der Ton stammt.")
    a = ap.parse_args()

    from faster_whisper import WhisperModel
    m = WhisperModel(a.model, device="cpu", compute_type="int8", cpu_threads=4)
    segs, info = m.transcribe(a.ton, language=a.lang, vad_filter=True,
                              condition_on_previous_text=False)
    segmente = []
    for s in segs:
        segmente.append({"start": s.start, "end": s.end, "text": s.text.strip()})
        if len(segmente) % 200 == 0:
            print(f"  {s.end / 60:.0f} min, {len(segmente)} Segmente", flush=True)

    # Erst sichern, dann zuordnen: das Transkript kostet eine Stunde, die
    # Zuordnung Sekunden. Wer die Spuren spaeter anders benennt, laesst nur
    # den zweiten Schritt neu laufen.
    roh = Path(a.out).with_suffix(".json")
    roh.write_text(json.dumps(segmente, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"  Segmente gesichert: {roh}")

    zugeordnet = abdruck = False
    if a.stimmabdruck:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import stimmabdruck as sa
        segmente = sa.kennzeichnen_liste(segmente, a.stimmabdruck)
        abdruck = True
    if a.spuren:
        namen = a.namen or [Path(p).stem for p in a.spuren]
        segmente, zugeordnet = sprecher_zuordnen(segmente, a.spuren, namen)

    dauer = segmente[-1]["end"] if segmente else 0
    zeilen = [f"# {a.titel or Path(a.ton).stem}", "",
              f"**Dauer** {dauer:.0f} s ({int(dauer // 60)}:{int(dauer % 60):02d}) · "
              f"**Sprache** {info.language} · **Modell** {a.model}", "",
              "Quelle: eigenes Transkript aus dem Rohton, Zeiten in **Rohzeit**.", ""]
    if abdruck:
        n = {x: sum(1 for z in segmente if z.get("sprecher") == x)
             for x in ("YNB", "Gast", "?")}
        zeilen += [f"Sprecher ueber den **Stimmabdruck**: Aehnlichkeit jedes "
                   f"Abschnitts zu seiner Stimme (Kosinus, ECAPA-TDNN). Ab "
                   f"{sa.AB_YNB} ist es er, unter {sa.AB_GAST} der Gast, "
                   f"dazwischen steht **?** — dort wird nicht geraten. "
                   f"Hier: {n['YNB']} YNB, {n['Gast']} Gast, {n['?']} offen "
                   f"({100 * n['?'] / max(1, len(segmente)):.0f} %).", ""]
    if zugeordnet:
        zeilen += ["Sprecher aus den Einzelspuren: wer spricht, ist auf seinem "
                   "Mikrofon am lautesten. Der Wert in Klammern ist der Abstand "
                   "zur zweitlautesten Spur in dB — unter 2 dB ist die "
                   "Zuordnung unsicher.", ""]
    elif a.spuren:
        zeilen += ["**Ohne Sprecherzuordnung.** Die mitgegebenen Spuren trennen "
                   "die Sprecher nicht — es sind Mikrofone im selben Raum mit "
                   "unterschiedlicher Verstaerkung, nicht getrennte "
                   "Ansteckmikrofone. Wer spricht, steht hier deshalb nicht; "
                   "lieber keine Angabe als eine erfundene.", ""]
    zeilen.append("---")
    zeilen.append("")
    for s in segmente:
        t = int(s["start"])
        marke = f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"
        if "sprecher" in s and "abstand" in s:
            zeilen.append(f"**[{marke}] {s['sprecher']}** ({s['abstand']:+.1f}) "
                          f"{s['text']}")
        elif "sprecher" in s:
            c = s.get("aehnlichkeit")
            zeilen.append(f"**[{marke}] {s['sprecher']}**"
                          + (f" ({c:+.2f})" if c is not None else "")
                          + f" {s['text']}")
        else:
            zeilen.append(f"**[{marke}]** {s['text']}")
        zeilen.append("")
    Path(a.out).write_text("\n".join(zeilen), encoding="utf-8")
    print(f"{a.out} — {len(segmente)} Segmente, {dauer / 60:.1f} min")


if __name__ == "__main__":
    main()
