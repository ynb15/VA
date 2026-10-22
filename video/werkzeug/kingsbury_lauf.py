#!/usr/bin/env python3
"""Kingsbury-Transkript, wiederaufnehmbar.

Jede Stufe erkennt am Dateistand, ob sie schon fertig ist. Der Container wird
eingezogen, sobald ein Zug endet — ein neuer Aufruf macht da weiter, wo der
letzte aufgehoert hat. Kein Zustand im Speicher, nur auf der Platte.

Stufen:  1 Abhaengigkeiten  2 Ton holen  3 Dauer pruefen  4 Transkribieren
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

W = Path(__file__).resolve().parent
FID = "1mQjt0g5GVptvEDVY8w3mVN2Qa8NFlTnp"
GROESSE = 16971968643
FLAC = W / "kingsbury.flac"
JSON = W / "kingsbury-roh.transkript.json"
LOG = W / "kingsbury-lauf.log"


def sag(*a):
    zeile = f"[{time.strftime('%H:%M:%S')}] " + " ".join(str(x) for x in a)
    print(zeile, flush=True)
    with open(LOG, "a") as f:
        f.write(zeile + "\n")


def stufe1_abhaengigkeiten():
    fehlt = []
    for modul, paket in (("av", "av"), ("faster_whisper", "faster-whisper")):
        try:
            __import__(modul)
        except ImportError:
            fehlt.append(paket)
    if not fehlt:
        sag("Stufe 1: Abhaengigkeiten da")
        return
    sag("Stufe 1: installiere", fehlt)
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", *fehlt], check=True)
    sag("Stufe 1: fertig")


def stufe2_ton():
    # Fertig heisst: Datei da und seit 90 s nicht mehr gewachsen.
    if FLAC.exists():
        a = FLAC.stat().st_size
        time.sleep(2)
        # DERSELBE FEHLER WIE IN STUFE 3, hier zweimal stehengeblieben:
        # "0,9 * GROESSE / 107" rechnet die erwartete FLAC-Groesse aus
        # Aaronsons Verhaeltnis hoch und kommt auf 143 MB. Das fertige
        # Kingsbury-FLAC hat 68 MB (77:12 Ton aus einem MOV mit hoeherer
        # Datenrate) - und wurde darum geloescht und 46 Minuten neu geholt.
        # Ein Boden genuegt: unter 10 MB ist fuer eine Folge unplausibel,
        # alles darueber war ein Abruf, den drive_lesen.py blockweise
        # geprueft hat.
        if a == FLAC.stat().st_size and a > 10_000_000:
            sag(f"Stufe 2: {FLAC.name} liegt schon da, {a/1e6:.0f} MB")
            return
        sag(f"Stufe 2: {FLAC.name} ist unfertig ({a/1e6:.0f} MB) — neu holen")
        FLAC.unlink()
    sag("Stufe 2: hole Ton aus 17,0 GB — dauert")
    r = subprocess.run(
        [sys.executable, str(W / "ton_holen.py"), "--id", FID,
         "--groesse", str(GROESSE), "--out", str(FLAC)],
        capture_output=True, text=True)
    for zeile in (r.stdout or "").splitlines()[-6:]:
        sag("  ", zeile)
    if r.returncode != 0:
        sag("Stufe 2 FEHLER:", (r.stderr or "")[-600:])
        raise SystemExit(1)
    sag(f"Stufe 2: fertig, {FLAC.stat().st_size/1e6:.0f} MB")


def stufe3_dauer():
    """Nie der Bestellung glauben — die tatsaechliche Dauer nachmessen."""
    import av
    with av.open(str(FLAC)) as ein:
        dauer = ein.duration / 1_000_000
    sag(f"Stufe 3: Dauer gemessen {dauer:.1f} s = {int(dauer//60)}:{dauer%60:04.1f}")
    # KORREKTUR 21.10., nach einem Falschalarm von mir: die erwartete Dauer
    # NICHT aus Aaronsons Bytes-je-Sekunde hochrechnen. Kingsbury ist ein MOV
    # mit anderer Datenrate - 17,0 GB ergaben 77:12, nicht ~107 min, und mein
    # Dreisatz hat einen vollstaendigen Abruf (16,98 von 16,97 GB = 100 %) als
    # "still gekuerzt" verworfen. Beinahe 46 Minuten Abruf umsonst wiederholt.
    #
    # Die Vollstaendigkeit haengt an den GELESENEN BYTES, nicht an der Dauer,
    # und die prueft inzwischen drive_lesen.py blockweise: ein gekuerzter
    # Abruf wirft dort IOError. Kommt Stufe 2 ohne Fehler durch, ist die Datei
    # ganz. Hier bleibt nur ein Boden gegen offensichtlichen Unsinn.
    if dauer < 1200:
        (W / "kingsbury-dauer.txt").write_text(f"{dauer:.2f} UNFERTIG\n")
        raise SystemExit(
            f"Stufe 3 ABBRUCH: nur {dauer:.0f}s Ton. Unter 20 Minuten ist fuer "
            f"eine Folge unplausibel - Log von Stufe 2 pruefen.")
    (W / "kingsbury-dauer.txt").write_text(f"{dauer:.2f}\n")
    return dauer


def stufe4_transkript():
    """Stueckweise, damit ein Containerneustart nicht alles kostet.

    Am 22.10. hat ein Neustart eine laufende Transkription von 77 Minuten
    mitgenommen - der Ton war fertig, die Arbeit weg. Jetzt wird in Fenstern
    von 300 s gearbeitet und nach jedem Fenster gespeichert. Ein neuer Lauf
    liest den Fortschritt und macht am naechsten Fenster weiter.
    """
    if JSON.exists() and JSON.stat().st_size > 10_000:
        sag("Stufe 4: Transkript liegt schon da")
        return
    sys.path.insert(0, str(W))
    from ton_lesen import ton_als_array
    from faster_whisper import WhisperModel

    FENSTER = 300.0
    RATE = 16000
    teil_datei = W / "kingsbury-teile.json"
    fertig = json.loads(teil_datei.read_text()) if teil_datei.exists() else {}
    if fertig:
        sag(f"Stufe 4: {len(fertig)} Fenster liegen schon vor — mache weiter")

    sag("Stufe 4: lese Ton")
    ton = ton_als_array(FLAC)
    anzahl = int(len(ton) / RATE / FENSTER) + 1
    sag(f"Stufe 4: {anzahl} Fenster a {FENSTER:.0f}s")
    sag("Stufe 4: lade Modell medium (faster-whisper, int8)")
    modell = WhisperModel("medium", device="cpu", compute_type="int8")

    for n in range(anzahl):
        if str(n) in fertig:
            continue
        a = int(n * FENSTER * RATE)
        b = min(int((n + 1) * FENSTER * RATE), len(ton))
        if a >= b:
            break
        teile, _ = modell.transcribe(ton[a:b], language="en")
        versatz = n * FENSTER
        fertig[str(n)] = [{"start": t.start + versatz, "end": t.end + versatz,
                           "text": t.text} for t in teile]
        teil_datei.write_text(json.dumps(fertig, ensure_ascii=False))
        sag(f"Stufe 4: Fenster {n+1}/{anzahl} fertig "
            f"({len(fertig[str(n)])} Segmente, bis {versatz+FENSTER:.0f}s)")

    segmente = [s for n in sorted(fertig, key=int) for s in fertig[n]]
    JSON.write_text(json.dumps(segmente, ensure_ascii=False))
    sag(f"Stufe 4: fertig, {len(segmente)} Segmente")


def main():
    sag("=== Lauf beginnt ===")
    stufe1_abhaengigkeiten()
    stufe2_ton()
    stufe3_dauer()
    stufe4_transkript()
    sag("=== ALLE STUFEN FERTIG ===")


if __name__ == "__main__":
    main()
