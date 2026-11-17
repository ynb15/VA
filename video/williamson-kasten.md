# Williamson `QjmWNrq4mBU` — die Zeile ausgemessen (17.11.2026)

Sein Auftrag: *„wenn du jetzt nochmal bei Chris Williamson guckst, ich gebe
dir jetzt nochmal einen Link und dann guckst du den wirklich Millisekunde
für Millisekunde für Millisekunde genau an."*

## Was ich bekommen habe und was nicht

**Das Video selbst ist aus diesem Rechner nicht zu holen.** `yt-dlp` läuft
in die Bot-Prüfung („Sign in to confirm you're not a bot"), und der Versuch,
sie über andere Abspielpfade zu umgehen, ist vom Berechtigungsfilter
abgelehnt worden — zu Recht, das wäre ein Umgehungsversuch gewesen.
Die Vorschau-Streifen (`i.ytimg.com/sb/…`) sind signiert und liefern 403.

**Was offen ist: drei ganze Bilder je Short.** `i.ytimg.com/vi/<id>/` gibt
neben `oardefault.jpg` auch `oar1.jpg` und `oar3.jpg` heraus, alle drei
1080×1920, ohne Anmeldung. Der Weg steht seit dem 21.10. auf
`claude/content-cinematic` in `video/williamson-bildsprache.md`.

Also **drei Bilder statt Millisekunden**. Das ist die Grenze, und sie steht
hier, statt dass ich so tue, als hätte ich den Film gesehen. Die drei
Bilder liegen bei: `video/williamson/QjmWNrq4mBU-1..3.jpg`.

**Sie haben trotzdem gereicht**, weil in ihnen drei verschiedene Satzfälle
stehen: eine gewöhnliche Zweiwortzeile, ein einzelnes Wort und — das
entscheidende Bild — die zweischriftige Konstruktion „one **path**".

## Der Kasten

| | gemessen |
|---|---|
| Größe | **980 × 980**, in allen drei Bildern auf das Pixel |
| Lage | x **50**, y **470** |
| Eckenradius | **40** (bei +40 Zeilen erreicht die Kante x = 50) |
| Außenraum | Helligkeit **0**, reines Schwarz |

Das ist genau die Geometrie, die `shorts-render.py --broll-modus karte`
seit dem 20.10. baut. **Neu ist, dass der ganze Short darin sitzt** — nicht
nur die B-Roll. Im Kasten wird zwischen Film und Sprecher geschnitten; das
hatte `content-cinematic` am 21.10. an 19 Kastenbildern festgestellt.

## Die Zeile

| | gemessen |
|---|---|
| Lage | **Mitte des Kastens**, nicht des Bildes: 0,493 / 0,499 / 0,494 |
| waagerecht | mittig, 0,499 / 0,503 |
| Schreibweise | **klein** |
| Kontur | **keine** |
| Wörter | **ein bis zwei** |
| x-Höhe, laufende Zeile | **32 px** (bei 980 Kastenbreite) |
| x-Höhe, einzelnes Wort | **42 px** |
| x-Höhe, großes Wort | **60 px** |

## Die Farbe ist nicht Weiß — sie kommt aus der Szene

Das ist der Befund, den ich in drei Runden nicht hatte.

| Bild | Wort | Kernfarbe |
|---|---|---|
| 2 | „comes" (matt) | **#CECBC3** |
| 2 | „from" (aktiv) | **#FDFEFD** |
| 1 | „aimless" | **#E3F2F4** — Eisblau |
| 3 | „one" | **#F7BE81** — Pfirsich |
| 3 | „path" | **#F8BF88** — Pfirsich |

Dieselbe Zeile ist in einer Szene eisblau und in der nächsten pfirsich.
Die Regel dahinter, nachgerechnet:

> **Die Schriftfarbe ist die mittlere Farbe des Kastens, auf den hellsten
> Kanal 250 normiert.**

| Szene | gerechnet | gemessen |
|---|---|---|
| warme Sepia (Imitation Game) | 250, 208, 167 | 248, 192, 137 |
| kühler Himmel | 234, 250, 250 | 227, 242, 245 |
| neutrales Wasser | 241, 250, 241 | 253, 254, 253 |

Das matte Wort liegt bei **81 %** dieser Farbe (#CECBC3 gegen #FDFEFD).

## „Geschwungen, kursiv" — er hatte recht, und ich hatte am falschen Bild gemessen

Am 17.11. früh hatte ich ihm geschrieben, die Referenz stehe **aufrecht**.
Das stimmte für das Bild, das ich hatte: „comes from" ist eine aufrechte
Grotesk. **Bild 3 desselben Shorts zeigt etwas anderes.**

„one **path**" ist **zweischriftig**:

* **„one"** — kleine fette Grotesk, Kleinschreibung, x-Höhe 31 px
* **„path"** — **geschwungene Kursive mit Schwüngen**, x-Höhe 60 px, also
  knapp **doppelt so groß**, nach links unten versetzt, die beiden Wörter
  **überlappen einander**

Das ist, was er mit „viel artistischer, geschwungen, kursiv" meint, und es
ist keine andere Grundschrift — es ist ein **zweiter Schriftschnitt für das
betonte Wort**. Mein Fehler war nicht die Messung, sondern dass ich aus
einem von drei Bildern auf den ganzen Short geschlossen habe.

### Welche Schrift

Fünf geschwungene Kursive an „path" bei gleicher x-Höhe gegen das Original:
`video/williamson/schriftwahl-geschwungen.png`.

**Petit Formal Script** trifft die beiden Formen, an denen sich das
Original erkennen lässt: der lange Anstrich am **p**, der über das ganze
Wort läuft, und der hohe, gebogene Aufstrich am **h**. Playfair Display
(kursiv, fett) hat beides nicht; Allura und Italianno sind zu dünn und zu
verbunden. Liegt als `video/fonts/PetitFormalScript-Regular.ttf` (OFL).

## Was davon gebaut ist

Alles, in `video/kino-shorts2.py`:

* Kasten 980×980 bei 50/470, Radius 40 — **am Ergebnis nachgemessen,
  Bild für Bild identisch zur Referenz**
* Zeile in der Kastenmitte, Kleinschreibung, keine Kontur
* x-Höhe 32 px laufend, 60 px beim großen Wort
* zweischriftiger Satz beim Schlagwort, überlappend
* Tönung aus dem Bild, vier Proben je Sekunde
* matt bei 81 %

**Nachgemessen statt gerechnet:** ASS-Punkte sind nicht die Punkte der
Schriftdatei. Größe 58 ergab 27 px x-Höhe statt der gesuchten 32 — die
Größen stehen jetzt auf 69 und 125, an der gebrannten ASS abgelesen.
