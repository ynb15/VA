#!/usr/bin/env python3
"""Laufzeit einer Drive-Videodatei lesen, ohne sie zu laden.

Drive beantwortet Bereichsanfragen. Die Laufzeit steht im `mvhd`-Atom im
`moov`-Container — bei den Exporten aus diesem Schnittplatz liegt `moov` am
Dateiende. Also: letzte 8 MiB holen, `mvhd` suchen, fertig.

Gemessen am 21.10.2026: 8 MiB statt 895 MB, Antwort in Sekunden.

    python3 laufzeit.py <drive-file-id> <dateigroesse-in-bytes>

Die Dateigroesse liefert das Drive-Metadatum (`fileSize`). Die Datei muss im
Drive link-freigegeben sein ("anyone with the link") — sonst kommt HTML statt
Bytes zurueck, und das sagt das Skript auch.
"""
import re
import struct
import sys
import urllib.parse

import requests

SITZUNG = requests.Session()


def bestaetigte_url(file_id):
    """Drive schiebt bei grossen Dateien eine Virenscan-Warnung davor."""
    start = f"https://drive.usercontent.google.com/download?id={file_id}&export=download"
    r = SITZUNG.get(start, timeout=60, stream=True)
    kopf = r.raw.read(200_000).decode("utf-8", "replace")
    r.close()
    if "Virus scan warning" not in kopf:
        return start
    m = re.search(r'<form[^>]*action="([^"]+)"[^>]*>(.*?)</form>', kopf, re.S)
    if not m:
        raise RuntimeError("Warnseite ohne Formular — Link-Freigabe pruefen")
    felder = dict(re.findall(r'name="([^"]+)"\s+value="([^"]*)"', m.group(2)))
    return m.group(1).replace("&amp;", "&") + "?" + urllib.parse.urlencode(felder)


def mvhd_dauer(block):
    """-> Sekunden, oder None wenn kein mvhd im Block."""
    i = block.find(b"mvhd")
    if i < 0:
        return None
    o = i + 4
    version = block[o]
    if version == 0:
        timescale, dauer = struct.unpack(">II", block[o + 12:o + 20])
    else:
        timescale, dauer = struct.unpack(">IQ", block[o + 20:o + 32])
    return dauer / timescale


def laufzeit(file_id, groesse):
    url = bestaetigte_url(file_id)
    # Erst vorne (faststart), dann hinten, dann weiter hinten.
    versuche = [(0, 4), ("ende", 8), ("ende", 32)]
    for wo, mb in versuche:
        spanne = (f"bytes=0-{mb * 1024 * 1024}" if wo == 0
                  else f"bytes={groesse - mb * 1024 * 1024}-{groesse - 1}")
        r = SITZUNG.get(url, headers={"Range": spanne}, timeout=180)
        if b"<html" in r.content[:200].lower():
            raise RuntimeError("HTML statt Bytes — Datei ist nicht link-freigegeben")
        sek = mvhd_dauer(r.content)
        if sek is not None:
            return sek
    raise RuntimeError("kein mvhd gefunden — vorne 4 MiB und hinten 32 MiB geprueft")


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(2)
    sek = laufzeit(sys.argv[1], int(sys.argv[2]))
    print(f"{sek:.1f} s = {int(sek // 60)}:{sek % 60:04.1f}")
    print()
    print("Timestamps daraus:  veroeffentlicht = (Rohzeit - Vorlauf) / Tempo")
    print("Tempo = Rohdauer / (Laufzeit + abgeschnittenes Ende)")


if __name__ == "__main__":
    main()
