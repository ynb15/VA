# Aaronson-Thumbnails — erste Runde, 20.10.2026

Vier Fassungen zur Auswahl. **Nichts davon ist veröffentlicht**, nichts ist
hochgeladen. Er entscheidet.

## Woher die Bilder kommen

Alles sind echte Einzelbilder aus der Aufnahme vom 21.08.2026. Kein Bildmodell,
keine erfundenen Gesichter, kein erzeugter Hintergrund.

| | Quelle | Rohzeit | was da passiert |
|---|---|---|---|
| **Yannick** | `Right Cam` | **01:33** (92,97 s) | Dreiviertel nach rechts, offenes Lächeln, beide Augen sichtbar |
| | | **01:33,5** (93,47 s) | dasselbe, Mund weiter offen |
| | | **44:56** (2695,97 s) | echtes Lachen, stärker im Profil |
| **Aaronson** | `Left Camera` | **45:01,5** (2701,50 s) | offener Mund, Augen weit — beim Ilya-Satz |
| | | **45:03,5** (2703,50 s) | spricht, Augen engagiert |
| | | **96:36,5** (5796,47 s) | grosses Lachen, Brauen hoch |
| | | **01:35,5** (95,47 s) | warmes Lachen |

**Alle sechs schauen nach innen** — er nach rechts, Aaronson nach links.
Das war die erste Runde nicht so, und es war der schwerste Fehler darin.
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

**Nummer 1 ist meine Empfehlung.** Sie trägt den stärksten Satz der Folge.

**Nummer 3 ist die wärmste** — beide lachen und schauen sich an. Wenn Nummer 1
Dir zu frontal ist, ist 3 die Alternative, die am meisten nach Gespräch
aussieht.

**Nummer 3 nimmt sich die meiste Freiheit.** „Broke Math" ist zugespitzt — er
sagt, ein Modell habe *eine Vermutung widerlegt*, nicht die Mathematik
kaputtgemacht. Wenn Dir das zu weit geht, ist die Fassung raus.

## Nachgemessen gegen den Bauplan

| | Vorgabe aus seinen Folgen | diese vier |
|---|---|---|
| Format | 1280×720 | 1280×720 ✓ |
| Kastenfarbe | `#DF2D00` (aus seinem Canva-File) | `#DF2D00` ✓ |
| Kastenbreite | 414–853 | 376–780 ✓ |
| Kastenhöhe | 119–172 | 123–162 ✓ |
| Kastenmitte x | 616–644 (Bildmitte 640) | 639,5 ✓ |
| Blockmitte y | ~360 (Bildmitte) | auf 360 gesetzt ✓ |
| Schriftgrad je Block | einer, 104–175 | einer, 121–160 ✓ |
| Zeilenabstand | 1,11 × Grad, gleichmässig | 1,11, gleichmässig ✓ |
| Blick | beide nach innen | beide nach innen ✓ |
| Augen links | 170 / 281 | gesetzt ✓ |
| Augen rechts | 1109 / 304 | gesetzt ✓ |
| Kästen im Bild | genau einer | genau einer ✓ |
| Kontur / Schatten auf der Schrift | keine | keine ✓ |

Dateigrösse 154–168 KB, YouTube erlaubt 2 MB.

## Was in Runde 1 falsch war

Seine drei Punkte, alle berechtigt:

1. **Blickrichtung.** Ich hatte ihn mit einem fast frontalen Bild gesetzt, auf
   dem er an Aaronson vorbeischaut. Jetzt schauen beide nach innen.
2. **Copy nicht zentral.** Der Block sass bei y≈323 statt auf der Bildmitte.
   Jetzt auf 360, wie bei seinen eigenen drei Zwei-Kopf-Thumbnails gemessen.
3. **Zeilenabstand ungleich.** Ich hatte jeder Zeile eine eigene Versalhöhe
   gegeben. Sein Canva-File zeigt: ein Grad, ein Zeilenabstand je Block.

## Was ich noch nicht weiss

- **Ob Poppins Bold wirklich Deine Schrift ist.** Gemessen passt sie auf unter
  1 px je Buchstabe, zweimal unabhängig; dazu ergeben ihre Tintenbreiten in
  Deinem Canva-File bei fünf Wörtern ein gleichmässiges Kastenpolster. Dein
  File nennt die Schrift nur als `YAFdJjbTu24,1`, nicht im Klartext —
  **den Namen kannst nur Du bestätigen.**
- **Ob Dir die Mimik-Auswahl taugt.** Ich habe 324 Einzelbilder an 17 Stellen
  gezogen und durchgesehen; die oben sind meine Auswahl, nicht die
  einzige mögliche. Innerhalb der Bilder mit richtiger Blickrichtung ist die
  Auswahl deutlich kleiner als ich zuerst dachte — die ausdrucksstärksten
  Momente sind oft genau die, in denen einer von Euch in die Kamera schaut. Sag, wenn Du einen anderen Moment willst — Zeitstempel
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
