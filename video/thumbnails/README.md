# Aaronson-Thumbnails — erste Runde, 20.10.2026

Vier Fassungen zur Auswahl. **Nichts davon ist veröffentlicht**, nichts ist
hochgeladen. Er entscheidet.

## Woher die Bilder kommen

Alles sind echte Einzelbilder aus der Aufnahme vom 21.08.2026. Kein Bildmodell,
keine erfundenen Gesichter, kein erzeugter Hintergrund.

| | Quelle | Rohzeit | was da passiert |
|---|---|---|---|
| **Yannick** | `Right Cam` | **88:23,5** (5303,50 s) | hochgezogene Brauen, offener Mund — Reaktion |
| | | **88:22** (5302,00 s) | dasselbe, Brauen härter |
| | | **44:56** (2695,97 s) | echtes Lachen, Profil |
| **Aaronson** | `Left Camera` | **45:01,5** (2701,50 s) | offener Mund, Augen weit — beim Ilya-Satz |
| | | **96:36,5** (5796,47 s) | grosses Lachen, Brauen hoch |
| | | **01:35,5** (95,47 s) | warmes Lachen |
| **Hintergrund** | `Middle Camera` | **45:02** (2702,00 s) | der echte Raum, auf 8 % abgedunkelt und weichgezeichnet |

Kamerazeit = Rohzeit = Transkriptzeit (beide Dateien laufen 6136 s, das
Transkript 6134 s).

## Die vier Fassungen

| Datei | Zeile | Kasten auf | woher die Zeile |
|---|---|---|---|
| `aaronson-1-works-too-well.jpg` | AI / **Works** / Too Well | Works | „It's not that it doesn't work. **It's that it does work.**" (96:28) |
| `aaronson-2-orangutans.jpg` | We're The / **Orangutans** | Orangutans | „At some point it will be to us as we are to orangutans." (60:40) |
| `aaronson-3-broke-math.jpg` | AI Just / **Broke** / Math | Broke | „The unit distance conjecture … was falsified by an OpenAI model." (58:03) |
| `aaronson-4-love-humanity.jpg` | Make AI / **Love** / Humanity | Love | Ilyas Frage: „what is the mathematical definition of what it means for the AI to love humanity?" (44:46) |

**Nummer 1 ist meine Empfehlung.** Sie trägt den stärksten Satz der Folge, und
die beiden Gesichter arbeiten gegeneinander: er ernst und angespannt, Aaronson
offen und lachend.

**Nummer 3 nimmt sich die meiste Freiheit.** „Broke Math" ist zugespitzt — er
sagt, ein Modell habe *eine Vermutung widerlegt*, nicht die Mathematik
kaputtgemacht. Wenn Dir das zu weit geht, ist die Fassung raus.

## Nachgemessen gegen den Bauplan

| | Vorgabe aus seinen Folgen | diese vier |
|---|---|---|
| Format | 1280×720 | 1280×720 ✓ |
| Kastenfarbe | `#DF2C00` | `#DF2C01` (JPEG-Rundung) ✓ |
| Kastenbreite | 414–853 | 382–785 ✓ |
| Kastenhöhe | 119–172 | 126–151 ✓ |
| Kastenmitte x | 616–644 (Bildmitte 640) | 639,5–640 ✓ |
| Augen links | 170 / 281 | gesetzt ✓ |
| Augen rechts | 1109 / 304 | gesetzt ✓ |
| Kästen im Bild | genau einer | genau einer ✓ |
| Kontur / Schatten auf der Schrift | keine | keine ✓ |

Dateigrösse 154–168 KB, YouTube erlaubt 2 MB.

## Was ich noch nicht weiss

- **Ob Poppins Bold wirklich Deine Schrift ist.** Gemessen passt sie auf unter
  1 px je Buchstabe, zweimal unabhängig. Bestätigen musst Du.
- **Ob Dir die Mimik-Auswahl taugt.** Ich habe 321 Einzelbilder an 17 Stellen
  gezogen und durchgesehen; die sechs oben sind meine Auswahl, nicht die
  einzige mögliche. Sag, wenn Du einen anderen Moment willst — Zeitstempel
  genügt, dann hole ich das Bild.
- **Ob der Hintergrund so bleiben soll.** Gerade ist es der eigene Raum, stark
  abgedunkelt. In `ewgUIZGJaWQ` steht in der Mitte stattdessen ein echtes
  Sachfoto. Für diese Folge wäre das etwas aus der Quantenrechnerei — aber
  dafür bräuchte ich ein Bild, das Du freigibst.

## Neu bauen

```
python3 video/thumbnail_bau.py --plan video/thumbnails/plan-aaronson.json
```

Die Freisteller liegen in `_freisteller/`, der Hintergrund als
`_hintergrund.jpg`. Zeilen ändern geht in der Plan-Datei, ohne die
Einzelbilder neu zu holen.
