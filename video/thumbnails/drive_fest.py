#!/usr/bin/env python3
"""Wie DriveDatei, aber jeder Block wird geprueft bevor er in den Puffer geht.

Der Leser im Repo nimmt `r.content` ohne Blick auf Statuscode oder Laenge. Gibt
Drive unter Last eine Fehlerseite (403/429) zurueck, landet HTML als "Daten" im
Puffer und der Demuxer bricht mit InvalidData ab — nicht reproduzierbar, weil es
von der Tagesform abhaengt. Hier wird 206 + content-range + Laenge geprueft und
bei Abweichung mit wachsender Wartezeit neu angefragt.
"""
import os, re, time
import requests

BLOCK = 8 << 20


class FesteDriveDatei:
    def __init__(self, url, groesse=None, cache_mb=768, url_neu=None,
                 sitzung=None):
        """url_neu: optionaler Aufruf, der eine frische URL liefert.

        Die Download-URL von Drive traegt ein uuid-Token, das nach einiger Zeit
        ablaeuft. Danach beantwortet Drive die Bereichsanfrage mit 200 und der
        ganzen Datei statt mit 206 — bei einer 4-GB-Datei ist das kein
        brauchbarer Rueckfall. Mit `url_neu` holt der Leser sich stattdessen
        ein frisches Token und macht weiter; lange Durchlaeufe brechen sonst
        mittendrin ab.
        """
        self.url = url
        self.url_neu = url_neu
        self.erneuert = 0
        # Dieselbe Sitzung wie die Virenscan-Bestaetigung benutzen. Die
        # Bestaetigung setzt ein Cookie; ohne das beantwortet Drive die
        # Bereichsanfrage mit 200 und der ganzen Datei statt mit 206.
        self.s = sitzung if sitzung is not None else requests.Session()
        self.pos = 0
        self.blocks = {}
        self.reihenfolge = []
        self.max_blocks = max(8, (cache_mb << 20) // BLOCK)
        self.gelesen = 0
        self.anfragen = 0
        self.wiederholt = 0
        self.groesse = groesse if groesse is not None else self._groesse()

    def _groesse(self):
        """Groesse aus content-range holen, nicht aus HEAD.

        Drive antwortet auf HEAD dieser Download-URL unzuverlaessig mit
        `content-length: 0`. Dann wird die Datei als leer behandelt und der
        Demuxer bricht mit InvalidData ab — genau der Fehler, der hier zuerst
        auftrat. Eine Bereichsanfrage ueber ein einzelnes Byte gibt die
        Gesamtgroesse dagegen immer im content-range zurueck.
        """
        r = self.s.get(self.url, timeout=60, headers={"Range": "bytes=0-0"},
                       allow_redirects=True)
        m = re.match(r"bytes 0-0/(\d+)", r.headers.get("content-range", ""))
        if not m:
            raise IOError(f"keine Groesse: status={r.status_code} "
                          f"content-range={r.headers.get('content-range')!r}")
        return int(m.group(1))

    def _block(self, nr):
        if nr in self.blocks:
            return self.blocks[nr]
        anfang = nr * BLOCK
        ende = min(anfang + BLOCK, self.groesse) - 1
        erwartet = ende - anfang + 1
        letzter = None
        for versuch in range(8):
            try:
                # stream=True: erst Kopfzeilen pruefen, Koerper nur bei 206
                # lesen. Ohne das laedt eine 200-Antwort die ganze Datei (hier
                # 4 GB) in den Speicher, bevor sie verworfen wird.
                r = self.s.get(self.url, timeout=180, stream=True,
                               headers={"Range": f"bytes={anfang}-{ende}"})
                try:
                    if r.status_code != 206:
                        if self.url_neu is not None and self.erneuert < 8:
                            self.url = self.url_neu()
                            self.erneuert += 1
                        raise IOError(f"Status {r.status_code} statt 206")
                    cr = r.headers.get("content-range", "")
                    if not cr.startswith(f"bytes {anfang}-{ende}/"):
                        raise IOError(f"content-range {cr!r} passt nicht")
                    daten = r.raw.read(erwartet, decode_content=True)
                finally:
                    r.close()
                if len(daten) != erwartet:
                    raise IOError(f"{len(daten)} statt {erwartet} Bytes")
                break
            except Exception as e:
                letzter = e
                self.wiederholt += 1
                if versuch == 7:
                    raise IOError(f"Block {nr} nach 8 Versuchen: {letzter}")
                time.sleep(min(60, 2.0 * (2 ** versuch)))
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
        teile, offen = [], n
        while offen > 0:
            b = self._block(self.pos // BLOCK)
            innen = self.pos % BLOCK
            stueck = b[innen:innen + offen]
            if not stueck:
                break
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
        return (f"{self.anfragen} Bereichsanfragen, {self.gelesen/1048576:.1f} MB"
                + (f", {self.wiederholt} Wiederholungen" if self.wiederholt else "")
                + (f", {self.erneuert}x Token erneuert" if self.erneuert else ""))
