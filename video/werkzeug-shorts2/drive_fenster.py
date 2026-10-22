#!/usr/bin/env python3
"""Aus einer grossen Drive-Videodatei ein Zeitfenster lesbar machen, ohne sie
zu laden — als Sparse-Datei mit echten Byte-Offsets.

    python3 drive_fenster.py <drive-id> <bytes> <von-s> <bis-s> <ziel.mp4>

Warum nicht `ffmpeg -ss ... -i <url>`: ffmpeg kommt in diesem Container ueber
den Egress-Proxy nicht an die Drive-URL heran ("Invalid data found when
processing input" nach 0,9 s), waehrend `curl` auf dieselbe URL sauber
HTTP 206 mit gueltigen mp4-Bytes liefert. Gemessen am Aaronson-Master,
22.10.2026.

Der Trick: die Datei hat `moov` vorn (faststart, am Dateianfang geprueft).
Also eine Datei der vollen Groesse anlegen — sparse, sie belegt nur, was
wirklich geschrieben wird —, den Kopf an Offset 0 schreiben und das
Byte-Fenster an seinen echten Offset. ffmpeg liest dann den Index aus `moov`,
springt in das Fenster und findet dort echte Bytes. Alles dazwischen wird nie
angefasst.

Das Fenster wird ueber die mittlere Datenrate geschaetzt und grosszuegig
gepolstert; bei variabler Rate ist das die einzige Unbekannte, deshalb meldet
das Skript, wie gross der Puffer war.
"""
import os
import re
import subprocess
import sys
import urllib.parse

import requests

SITZUNG = requests.Session()
KOPF_MB = 24
PUFFER_S = 90          # Sicherheitsabstand in Sekunden je Seite
STUECK = 16 * 1024 * 1024


def bestaetigte_url(file_id):
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


def hole(url, von, bis, ziel, offset):
    """Byte-Bereich [von, bis] an `offset` in `ziel` schreiben."""
    geholt = 0
    with open(ziel, "r+b") as f:
        pos = von
        while pos <= bis:
            ende = min(pos + STUECK - 1, bis)
            r = SITZUNG.get(url, headers={"Range": f"bytes={pos}-{ende}"},
                            timeout=300)
            erwartet = ende - pos + 1
            # Bei Drive ist die Laenge die Wahrheit, nicht der Statuscode:
            # "Quota exceeded" kommt als HTTP 200 mit ~2 kB HTML.
            if len(r.content) != erwartet:
                raise IOError(
                    f"{len(r.content)} statt {erwartet} Bytes bei {pos} "
                    f"(HTTP {r.status_code}) — Tageslimit oder keine Freigabe")
            f.seek(offset + (pos - von))
            f.write(r.content)
            geholt += len(r.content)
            pos = ende + 1
    return geholt


def main():
    fid, groesse, von_s, bis_s, ziel = sys.argv[1:6]
    groesse, von_s, bis_s = int(groesse), float(von_s), float(bis_s)
    url = bestaetigte_url(fid)

    with open(ziel, "wb") as f:
        f.truncate(groesse)                      # sparse

    kopf = min(KOPF_MB * 1024 * 1024, groesse) - 1
    g1 = hole(url, 0, kopf, ziel, 0)
    print(f"Kopf: {g1 / 1e6:.0f} MB", flush=True)

    # Dauer aus dem Kopf lesen, dann die mittlere Rate bestimmen.
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", ziel],
                       capture_output=True, text=True)
    dauer = float(p.stdout.strip() or 0) or (bis_s + PUFFER_S)
    rate = groesse / dauer
    a = max(0, int((von_s - PUFFER_S) * rate))
    b = min(groesse - 1, int((bis_s + PUFFER_S) * rate))
    g2 = hole(url, a, b, ziel, a)
    print(f"Fenster {von_s:.0f}-{bis_s:.0f} s -> Bytes {a}-{b} "
          f"({g2 / 1e6:.0f} MB, Puffer {PUFFER_S} s je Seite, "
          f"Rate {rate / 1e6:.2f} MB/s)")
    print(f"belegt auf der Platte: "
          f"{os.stat(ziel).st_blocks * 512 / 1e6:.0f} MB von {groesse / 1e9:.1f} GB")


if __name__ == "__main__":
    main()
