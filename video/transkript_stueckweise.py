#!/usr/bin/env python3
"""Transkript einer langen Aufnahme — stueckweise und wiederaufnehmbar.

    python3 video/transkript_stueckweise.py --ton ton.flac --model medium \
            --out video/transkripte/strassman-roh.transkript.md

Warum nicht `transkript_lokal.py`: das laeuft in einem Zug durch. Bei zwei
Stunden Ton sind das Stunden Rechenzeit, und dieser Container wird zwischen
den Zuegen eingesammelt. Ein Abbruch nach neunzig Minuten liefert dann
nichts — nicht einmal die neunzig Minuten.

Hier wird der Ton in Fenster zerlegt, jedes Fenster einzeln transkribiert
und **nach jedem Fenster** der Stand auf die Platte geschrieben. Ein zweiter
Aufruf mit denselben Angaben setzt dort fort, wo der erste aufgehoert hat.

Die Fenstergrenzen liegen NICHT auf runden Minuten, sondern auf der
leisesten Stelle in einem Suchbereich darum herum. Ein Schnitt mitten im
Wort kostet sonst an jeder Grenze ein halbes Wort auf beiden Seiten, und
bei zwoelf Grenzen sind das zwoelf kaputte Saetze. Die Grenzen werden
einmal bestimmt und im Standfile festgehalten, damit ein zweiter Lauf
dieselben benutzt.
"""
import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
RATE = 16000


def ton_laden(pfad):
    """16 kHz Mono float32 — genau das, was das Modell sonst selbst baut.

    Den Umweg ueber ffmpeg braucht es, weil faster-whisper PyAV mit
    `metadata_errors` aufruft, das die hier installierte PyAV-Fassung nicht
    kennt. Steht genauso in transkript_lokal.py und shorts-render.py.
    """
    roh = subprocess.run([FFMPEG, "-nostdin", "-v", "quiet", "-i", str(pfad),
                          "-f", "f32le", "-ac", "1", "-ar", str(RATE), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype=np.float32)


def grenzen_finden(ton, fenster, suche=25.0, ruhe=0.30):
    """Fenstergrenzen auf die leiseste Stelle in der Naehe legen."""
    schritt = int(0.02 * RATE)                       # 20-ms-Rahmen
    n = len(ton) // schritt
    pegel = np.sqrt((ton[:n * schritt].reshape(n, schritt) ** 2).mean(1))
    breit = max(1, int(ruhe / 0.02))
    # gleitendes Mittel: gesucht ist eine ruhige STRECKE, kein einzelner Rahmen
    kern = np.ones(breit) / breit
    geglaettet = np.convolve(pegel, kern, mode="same")

    grenzen = [0.0]
    dauer = len(ton) / RATE
    ziel = fenster
    while ziel < dauer - suche:
        a = int(max(0, ziel - suche) / 0.02)
        b = int(min(dauer, ziel + suche) / 0.02)
        i = a + int(np.argmin(geglaettet[a:b]))
        grenzen.append(round(i * 0.02, 2))
        ziel = grenzen[-1] + fenster
    grenzen.append(round(dauer, 2))
    return grenzen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ton", required=True)
    ap.add_argument("--model", default="medium")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--titel", default=None)
    ap.add_argument("--fenster", type=float, default=600.0,
                    help="Soll-Laenge eines Stuecks in Sekunden")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    out = Path(a.out)
    stand_pfad = out.with_suffix(".fortschritt.json")

    print("  Ton wird gelesen ...", flush=True)
    ton = ton_laden(a.ton)
    dauer = len(ton) / RATE
    print(f"  {dauer:.1f} s ({dauer / 60:.1f} min) Ton", flush=True)

    if stand_pfad.exists():
        stand = json.loads(stand_pfad.read_text(encoding="utf-8"))
        if abs(stand["dauer"] - dauer) > 1.0 or stand["modell"] != a.model:
            raise SystemExit(
                f"Der Stand in {stand_pfad} gehoert zu anderem Ton oder einem "
                f"anderen Modell ({stand['dauer']:.1f} s / {stand['modell']}). "
                f"Loeschen oder anderen --out waehlen.")
        print(f"  Stand gefunden: {len(stand['stuecke'])} von "
              f"{len(stand['grenzen']) - 1} Stuecken fertig", flush=True)
    else:
        stand = {"ton": str(a.ton), "dauer": dauer, "modell": a.model,
                 "grenzen": grenzen_finden(ton, a.fenster), "stuecke": {}}
        stand_pfad.write_text(json.dumps(stand, ensure_ascii=False, indent=1),
                              encoding="utf-8")
        print(f"  {len(stand['grenzen']) - 1} Stuecke, Grenzen auf den "
              f"leisesten Stellen", flush=True)

    grenzen = stand["grenzen"]
    offen = [i for i in range(len(grenzen) - 1) if str(i) not in stand["stuecke"]]
    if offen:
        from faster_whisper import WhisperModel
        modell = WhisperModel(a.model, device="cpu", compute_type="int8",
                              cpu_threads=4)
    sprache = None
    for i in offen:
        von, bis = grenzen[i], grenzen[i + 1]
        segs, info = modell.transcribe(
            ton[int(von * RATE):int(bis * RATE)],
            language=a.lang, vad_filter=True, condition_on_previous_text=False)
        stueck = [{"start": round(s.start + von, 2),
                   "end": round(s.end + von, 2),
                   "text": s.text.strip()} for s in segs]
        sprache = info.language
        stand["stuecke"][str(i)] = stueck
        stand["sprache"] = sprache
        stand_pfad.write_text(json.dumps(stand, ensure_ascii=False, indent=1),
                              encoding="utf-8")
        schreiben(out, stand, a)
        print(f"  Stueck {i + 1}/{len(grenzen) - 1} "
              f"({von / 60:.1f}-{bis / 60:.1f} min): "
              f"{len(stueck)} Segmente, gesichert", flush=True)

    n, fehlend = schreiben(out, stand, a)
    print(f"{out} — {n} Segmente, {stand['dauer'] / 60:.1f} min"
          + (f", ABER {fehlend} Stuecke fehlen noch" if fehlend else ""))


def schreiben(out, stand, a):
    """Transkript aus dem Stand zusammensetzen — auch unfertig.

    Wird nach JEDEM Stueck aufgerufen, nicht erst am Ende. Sonst liegt
    waehrend der zweieinhalb Stunden Rechenzeit nur das Standfile da, und
    wer hineinsehen will, muss JSON lesen. Fehlende Stuecke stehen als
    Luecke drin, damit niemand ein halbes Transkript fuer ein ganzes haelt.
    """
    grenzen = stand["grenzen"]
    segmente, luecken = [], []
    for i in range(len(grenzen) - 1):
        if str(i) in stand["stuecke"]:
            segmente += stand["stuecke"][str(i)]
        else:
            luecken.append((grenzen[i], grenzen[i + 1]))
    out.with_suffix(".json").write_text(
        json.dumps(segmente, ensure_ascii=False, indent=1), encoding="utf-8")

    dauer = stand["dauer"]
    sprache = stand.get("sprache", a.lang)
    zeilen = [f"# {a.titel or out.stem}", "",
              f"**Dauer** {dauer:.0f} s ({int(dauer // 60)}:{int(dauer % 60):02d}) · "
              f"**Sprache** {sprache} · **Modell** {a.model}", "",
              "Quelle: eigenes Transkript aus dem Rohton, Zeiten in "
              "**Rohzeit**.", "",
              f"In {len(grenzen) - 1} Stuecken gerechnet; die Grenzen liegen "
              f"auf Sprechpausen.", ""]
    if luecken:
        zeilen += [f"**UNFERTIG — {len(luecken)} von {len(grenzen) - 1} "
                   f"Stuecken fehlen noch:** "
                   + ", ".join(f"{v / 60:.1f}–{b / 60:.1f} min"
                               for v, b in luecken), ""]
    zeilen += [
              "**Ohne Sprecherzuordnung.** Die Aufnahme liegt als eine "
              "Mischung vor, nicht als getrennte Spuren. Wer spricht, steht "
              "hier deshalb nicht; lieber keine Angabe als eine erfundene.",
              "", "---", ""]
    for s in segmente:
        t = int(s["start"])
        zeilen.append(f"**[{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}]** "
                      f"{s['text']}")
        zeilen.append("")
    out.write_text("\n".join(zeilen), encoding="utf-8")
    return len(segmente), len(luecken)


if __name__ == "__main__":
    main()
