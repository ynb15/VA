# Aaronson-Thumbnails — dritte Runde, 20.10.2026

Vier Fassungen zur Auswahl. **Nichts ist veröffentlicht, nichts hochgeladen.**

## Die Vorgabe dieser Runde

> „Das hat keinen Anreiz, da klickt keiner drauf, wenn jemand auf einem
> Thumbnail lacht. Das müssen schockierte, überraschte, böse Blicke sein."

Richtig, und an seinen eigenen Thumbnails nachgeprüft: **keines der sieben
Gesichter dort lacht.** Alle haben weit offene Augen, hochgezogene Brauen und
offenen Mund — oder einen harten, verengten Blick. In Runde 1 und 2 habe ich
beide Male lächelnde Gesichter geliefert.

## Woher die Bilder kommen

Echte Einzelbilder aus der Aufnahme vom 21.08.2026. Kein Bildmodell, nichts
erzeugt.

| | Quelle | Rohzeit | Mimik |
|---|---|---|---|
| **Yannick** | `Right Cam` | **47:51** (2871 s) | ungläubig, Mund offen, wacher Blick |
| | | **95:49** (5749 s) | hart, verschlossen, Mund zu |
| | | **11:58** (718 s) | angespannt sprechend |
| | | **60:05** (3605 s) | skeptisch, Braue gerunzelt |
| **Aaronson** | `Left Camera` | **50:00** (3000 s) | gequälte Grimasse, Brauen zusammen |
| | | **50:02** (3002 s) | spricht mit offenem Mund, intensiv |
| | | **41:44** (2504 s) | emphatisch, Brauen hoch |
| | | **98:24** (5904 s) | ernst, geschlossen |
| **Hintergrund** | `Middle Camera` | **45:02** (2702 s) | der echte Raum, auf 8 % abgedunkelt |

Alle acht schauen nach innen.

## Die vier Fassungen

| Datei | Zeile | Kasten | Paarung |
|---|---|---|---|
| `aaronson-1-works-too-well.jpg` | AI / **Works** / Too Well | Works | ungläubig ↔ gequält |
| `aaronson-2-orangutans.jpg` | We're The / **Orangutans** | Orangutans | hart ↔ intensiv |
| `aaronson-3-broke-math.jpg` | AI Just / **Broke** / Math | Broke | angespannt ↔ emphatisch |
| `aaronson-4-love-humanity.jpg` | Make AI / **Love** / Humanity | Love | skeptisch ↔ ernst |

**Nummer 1 ist meine Empfehlung**, danach Nummer 3.

## Was ich sagen muss, statt es zu verschweigen

**Den aufgerissenen Blick gibt es in dieser Aufnahme von Dir nicht.**

Durchgesehen: **2.600 Einzelbilder aus rund 45 Minuten** beider Nahkameras,
darunter ein zusammenhängender Durchlauf über 30 Minuten mit einem Bild je
Sekunde. Gemessen am Augenweiß liegt Dein höchster Wert bei **0,017**; auf
Deinen veröffentlichten Thumbnails liegst Du bei **0,016 bis 0,039**.

Du hörst in dieser Folge ruhig zu, oft mit der Faust am Kinn. Die vier oben
sind das härteste, was drin ist: ungläubig, hart, angespannt, skeptisch —
aber nicht schockiert.

**Bei Aaronson sieht es besser aus.** Bei 50:00 verzieht er das Gesicht
regelrecht gequält.

**Drei Wege, wenn Dir das nicht reicht:**
1. **Du nennst einen Zeitstempel**, an dem Du Dich stärker reagieren siehst.
   Dann hole ich das Bild in einer Minute.
2. **Ich suche die restlichen 57 Minuten ab**, die ich noch nicht gesehen
   habe. Das sind rund 4 GB Drive-Verkehr und etwa eine Stunde.
3. **Der Blick kommt nicht aus dem Gespräch.** Wenn Deine starken Thumbnail-
   Gesichter gestellt sind — direkt in die Kamera gespielt —, dann ist das
   eine Aufnahme von zwei Minuten vor oder nach dem Dreh und nichts, was
   sich aus diesem Material holen lässt. Sag mir, ob das so ist.

## Nachgemessen gegen den Bauplan

| | Vorgabe | diese vier |
|---|---|---|
| Format | 1280×720 | 1280×720 ✓ |
| Kastenfarbe | `#DF2D00` (sein Canva-File) | `#DF2D00` ✓ |
| Kastenmitte x | Bildmitte 640 | 639,5 ✓ |
| Blockmitte y | ~360 | 360 ✓ |
| Schriftgrad je Block | einer, 104–175 | einer, 121–160 ✓ |
| Zeilenabstand | 1,11 × Grad, gleichmässig | 1,11, gleichmässig ✓ |
| Blick | beide nach innen | beide nach innen ✓ |
| Mimik | kein Lächeln | kein Lächeln ✓ |

## Werkzeuge

```
# Einzelbilder holen — lange Fenster sind pro Bild viel billiger als kurze
python3 video/thumbnails/greifer.py --id <drive-id> --out ordner --fps 1 --fenster 3400:300

# nach Augenweite sortieren und als Kontaktbogen zeigen
python3 video/thumbnails/rang.py ordner y bogen.jpg 24

# setzen
python3 video/thumbnail_bau.py --plan video/thumbnails/plan-aaronson.json
```
