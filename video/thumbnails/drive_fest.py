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
    def __init__(self, url, groesse=None, cache_mb=768):
        self.url = url
        self.s = requests.Session()
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
        for versuch in range(6):
            try:
                r = self.s.get(self.url, timeout=180,
                               headers={"Range": f"bytes={anfang}-{ende}"})
                if r.status_code != 206:
                    raise IOError(f"Status {r.status_code} statt 206")
                cr = r.headers.get("content-range", "")
                if not cr.startswith(f"bytes {anfang}-{ende}/"):
                    raise IOError(f"content-range {cr!r} passt nicht")
                if len(r.content) != erwartet:
                    raise IOError(f"{len(r.content)} statt {erwartet} Bytes")
                daten = r.content
                break
            except Exception as e:
                letzter = e
                self.wiederholt += 1
                if versuch == 5:
                    raise IOError(f"Block {nr} nach 6 Versuchen: {letzter}")
                time.sleep(1.5 * (2 ** versuch))
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
                + (f", {self.wiederholt} Wiederholungen" if self.wiederholt else ""))
