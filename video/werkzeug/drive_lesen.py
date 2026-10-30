#!/usr/bin/env python3
"""Eine Drive-Datei als virtuelle lokale Datei öffnen.

Grosse Dateien (hier 18,6 GB) kann der Container nicht laden. Drive beantwortet
aber Bereichsanfragen (`accept-ranges: bytes`), und PyAV nimmt ein
dateiähnliches Objekt — also holt diese Klasse nur die Bytes, die der Demuxer
wirklich liest. Gemessen am 19.10.2026: ein 60-Sekunden-Fenster kostet rund
170 MB statt 18,6 GB.

Die Datei muss im Drive link-freigegeben sein ("anyone with the link").
"""
import os
import re
import time
import urllib.parse

import requests

# Gemessen am 19.10.2026: eine einzelne grosse Bereichsanfrage laeuft mit
# 12,8 MB/s. Mit urllib brach das auf unter 1 MB/s ein, weil pro Block ein
# neuer TLS-Handschlag aufgebaut wurde. Darum requests.Session (keep-alive)
# und grosse Bloecke.
BLOCK = 8 << 20  # 8 MiB
SITZUNG = requests.Session()


def bestaetigte_url(file_id):
    """Drive schiebt bei grossen Dateien eine Virenscan-Warnung davor.

    Die Warnseite enthaelt ein Formular mit einem uuid-Token; erst damit
    liefert der Server die Bytes. Diese Funktion holt das Token.
    """
    start = f"https://drive.usercontent.google.com/download?id={file_id}&export=download"
    r = SITZUNG.get(start, timeout=60, stream=True)
    kopf = r.raw.read(200_000).decode("utf-8", "replace")
    r.close()
    if "Virus scan warning" not in kopf:
        return start  # kleine Datei, direkt
    m = re.search(r'<form[^>]*action="([^"]+)"[^>]*>(.*?)</form>', kopf, re.S)
    if not m:
        raise RuntimeError("Warnseite ohne Formular — Freigabe pruefen")
    felder = dict(re.findall(r'name="([^"]+)"\s+value="([^"]*)"', m.group(2)))
    return m.group(1).replace("&amp;", "&") + "?" + urllib.parse.urlencode(felder)


class AbrufGekuerzt(IOError):
    """Drive hat zu wenige Bytes geliefert — Tageslimit oder gekuerzter Abruf.

    Eigene Klasse, weil `except IOError` NICHT reicht: requests.RequestException
    erbt selbst von IOError. Am 30.10.2026 fing das `except IOError: raise`
    darum auch einen ChunkedEncodingError ab (Relay-Neustart, Code 1012) und
    riss den Lauf nach 218 MB ab, statt den Block zu wiederholen.
    Ein Verbindungsabbruch ist wiederholbar, ein erschoepftes Tageslimit nicht
    — die beiden muessen unterscheidbar bleiben.
    """


class DriveDatei:
    """read/seek/tell auf einer entfernten Datei, blockweise zwischengespeichert."""

    def __init__(self, url, groesse=None, cache_mb=512):
        self.url = url
        self.pos = 0
        self.blocks = {}
        self.reihenfolge = []
        self.max_blocks = max(8, (cache_mb * 1024 * 1024) // BLOCK)
        self.gelesen = 0
        self.anfragen = 0
        self.groesse = groesse if groesse is not None else self._groesse_abfragen()

    def _groesse_abfragen(self):
        r = SITZUNG.head(self.url, timeout=60, allow_redirects=True)
        return int(r.headers["content-length"])

    def _block(self, nr):
        if nr in self.blocks:
            return self.blocks[nr]
        anfang = nr * BLOCK
        ende = min(anfang + BLOCK, self.groesse) - 1
        erwartet = ende - anfang + 1
        daten = None
        for versuch in range(4):
            try:
                r = SITZUNG.get(self.url, timeout=180,
                                headers={"Range": f"bytes={anfang}-{ende}"})
                # DIE PRUEFUNG, DIE GEFEHLT HAT. Drive beantwortet ein
                # erschoepftes Tageslimit mit HTTP 200 und ~2 kB HTML, und
                # kuerzt Bereichsabrufe auch sonst still. Ohne Laengenpruefung
                # wird so eine Antwort zwischengespeichert, read() liefert zu
                # wenige Bytes, und der Demuxer liest das als Dateiende: der
                # Lauf meldet Erfolg mit einem Bruchteil des Tons.
                # Am 21.10.2026 zweimal passiert — 23:32 und 3:50 statt ~107 min.
                if len(r.content) == erwartet:
                    daten = r.content
                    break
                kopf = r.content[:200].decode("utf-8", "replace")
                if versuch == 3:
                    raise AbrufGekuerzt(
                        f"Block {nr}: {len(r.content)} statt {erwartet} Bytes "
                        f"(HTTP {r.status_code}). Tageslimit des Eigentuemers "
                        f"erschoepft oder Abruf gekuerzt. Anfang: {kopf!r}")
                time.sleep(2 ** versuch)
            except AbrufGekuerzt:
                raise
            except Exception:
                if versuch == 3:
                    raise
                time.sleep(2 ** versuch)
        if daten is None:
            raise AbrufGekuerzt(f"Block {nr}: nach vier Versuchen keine vollen Daten")
        self.anfragen += 1
        self.gelesen += len(daten)
        self.blocks[nr] = daten
        self.reihenfolge.append(nr)
        while len(self.reihenfolge) > self.max_blocks:
            self.blocks.pop(self.reihenfolge.pop(0), None)
        return daten

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.groesse - self.pos
        n = min(n, self.groesse - self.pos)
        teile = []
        offen = n
        while offen > 0:
            nr = self.pos // BLOCK
            innen = self.pos % BLOCK
            b = self._block(nr)
            stueck = b[innen:innen + offen]
            if not stueck:
                # Nie still kuerzen: ein kurzer read() ist fuer jeden Demuxer
                # ein Dateiende. Lieber laut abbrechen als halben Ton liefern.
                raise IOError(
                    f"read() bei Byte {self.pos} von {self.groesse}: Block {nr} "
                    f"liefert nichts mehr. Kein Dateiende — ein gekuerzter Abruf.")
            teile.append(stueck)
            self.pos += len(stueck)
            offen -= len(stueck)
        return b"".join(teile)

    def seek(self, pos, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self.pos = pos
        elif whence == os.SEEK_CUR:
            self.pos += pos
        else:
            self.pos = self.groesse + pos
        self.pos = max(0, min(self.pos, self.groesse))
        return self.pos

    def tell(self):
        return self.pos

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return False

    def close(self):
        self.blocks.clear()
        self.reihenfolge.clear()

    @property
    def bilanz(self):
        return f"{self.anfragen} Bereichsanfragen, {self.gelesen / 1048576:.1f} MB geladen"
