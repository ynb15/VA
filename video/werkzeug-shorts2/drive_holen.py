#!/usr/bin/env python3
"""Eine Drive-Datei wiederaufnehmbar holen — Stueck fuer Stueck, mit Pruefung.

    python3 drive_holen.py <drive-id> <bytes> <zieldatei>

Warum eigenes Werkzeug: `ton_holen.py` braucht PyAV, und PyAV ist in diesem
Container nicht installiert (ffmpeg 6.1.1 ist da). Dieser Weg holt die Datei
per Bereichsanfrage und laesst das Tonziehen ffmpeg machen.

Wiederaufnehmbar, weil Container eingezogen werden (Lernkanal, 21.10.2026:
`nohup` hilft nicht): bei jedem Start wird die vorhandene Zieldatei gemessen
und ab ihrer Laenge weitergeholt. Abbrechen und neu starten kostet nichts.

Die Laenge ist die Wahrheit, nicht der Statuscode: Drive liefert
"Quota exceeded" als HTTP 200 mit ~2 kB HTML (Lernkanal, 21.10.2026).
Deshalb bricht jedes Stueck ab, das kuerzer zurueckkommt als angefordert.
"""
import os
import re
import sys
import time
import urllib.parse

import requests

STUECK = 32 * 1024 * 1024
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


def holen(file_id, groesse, ziel):
    url = bestaetigte_url(file_id)
    t0 = time.time()
    while True:
        da = os.path.getsize(ziel) if os.path.exists(ziel) else 0
        if da >= groesse:
            break
        bis = min(da + STUECK, groesse) - 1
        r = SITZUNG.get(url, headers={"Range": f"bytes={da}-{bis}"}, timeout=300)
        erwartet = bis - da + 1
        if len(r.content) != erwartet:
            kopf = r.content[:300].decode("utf-8", "replace")
            raise IOError(
                f"{len(r.content)} Bytes statt {erwartet} bei Byte {da} "
                f"(HTTP {r.status_code}). Tageslimit oder keine Freigabe. "
                f"Anfang: {kopf[:200]!r}")
        with open(ziel, "ab") as f:
            f.write(r.content)
        neu = da + len(r.content)
        print(f"  {neu / 1e9:.2f} / {groesse / 1e9:.2f} GB "
              f"({100 * neu / groesse:.1f} %), "
              f"{(time.time() - t0) / 60:.1f} min", flush=True)
    print(f"fertig: {ziel} — {groesse / 1e9:.2f} GB, "
          f"{(time.time() - t0) / 60:.1f} min")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        raise SystemExit(2)
    holen(sys.argv[1], int(sys.argv[2]), sys.argv[3])
