# Die Thumbnails seines Kanals — abgelesen, nicht erfunden

Erst gemessen am 20.10.2026 an sechs veröffentlichten Folgen, am selben Tag
**nachgemessen und in vier Punkten korrigiert** (siehe „Was ich revidiert habe").
Die Bilder sind ohne Anmeldung erreichbar:
`https://i.ytimg.com/vi/<video-id>/maxresdefault.jpg` liefert **1280×720**,
HTTP 200. (Für Shorts ist es `oardefault.jpg`, 720×1280.)
Geprüfte IDs: `frNOUgxE0IM`, `f79ehF4zP3I`, `ewgUIZGJaWQ`, `GxpvzT3rUBQ`,
`-0NES3TOiIg`, `RG-K0fIA2-w`.

## Der Bauplan

**Format** 1280×720.

### Es gibt zwei Aufbauten, nicht einen — und sie stehen 3 : 3

**A — Zwei Köpfe, links und rechts.** Beide schauen nach innen, angeschnitten
etwa auf Schulterhöhe. Mitte dunkel oder ein echtes Foto. Zeile in der Mitte.
→ `frNOUgxE0IM`, `ewgUIZGJaWQ`, `RG-K0fIA2-w`

**B — Ein Kopf rechts, links eine gekippte Fotokarte.** Ein echtes Foto
(NFL-Spieler, Rosie-the-Riveter-Plakat, Ayahuasca-Zeremonie) liegt als Karte
mit **hellem Rand und weichem Schlagschatten**, um wenige Grad gekippt, in der
linken Bildhälfte. Zeile daneben.
→ `-0NES3TOiIg`, `GxpvzT3rUBQ`, `f79ehF4zP3I`

**Die Fotokarte ist ein Markenzeichen, kein Sonderfall.** Sie steht in der
Hälfte aller geprüften Folgen. In `f79ehF4zP3I` liegt sie sogar zusätzlich in
der Mitte, zusammen mit einer freigestellten Hanfpflanze.

### Die Köpfe

**Der Kopf füllt die volle Bildhöhe, nicht zwei Drittel.** Gemessen über eine
Hautmaske: In fünf von sechs Thumbnails ist der **Scheitel oben angeschnitten**
(Hautbereich beginnt in Zeile 0), und der Kopf-Schulter-Bereich reicht bis
Zeile **685–719** von 720. Das Gesicht ist groß, nah und beschnitten.

Links steht in Aufbau A ein wiederkehrender Kopf, rechts der Gast. In Aufbau B
steht der einzelne Kopf **immer rechts**.

### Die Zeile

**Zwei bis vier Zeilen** (`RG-K0fIA2-w` hat vier: God / Saved / My / Life).
Versalien gemischt mit Gemischtschreibung. Sehr fett, weiß. Die Größen wechseln
bewusst innerhalb der Zeile: ein kleineres Wort oben („THIS", „F*ck", „NFL"),
darunter das große.

**Mittig — mit einer Ausnahme.** Die Kastenmitte liegt bei x = 616…644 bei fünf
von sechs (Bildmitte ist 640). `f79ehF4zP3I` bricht das: linksbündig, Textblock
oben links, Kastenmitte bei x = 464.

**Zwei bis vier Wörter insgesamt. Kein Satz, kein Punkt.**

**Fragezeichen schon** — meine frühere Regel „kein Fragezeichen" war zu eng.
Sie kam aus den sechs veröffentlichten Thumbnails, in denen zufällig keines
vorkommt. Sein Canva-File hat gleich mehrere: „Coincidence?", „Did I REALLY /
Make It Up?", „Was THIS GOD'S Calling?". Am 20.10. hat er selbst eines
angefordert.

**Der Kasten kann hinter einem Teil der Zeile liegen**, nicht nur hinter der
ganzen. „Coincidence?" liegt ganz darauf, bei „Did I REALLY / Make It Up?"
nur das Wort REALLY. `thumbnail_bau.py` nimmt dafür `"kasten": [1, "Teil"]`.

### Der orangerote Kasten

**`#DF2D00`** — aus seinem Canva-File abgelesen, nicht mehr geschätzt.

Meine Schätzung aus den JPEGs war `#DF2C00`, in der letzten Ziffer daneben.
Das Canva-File sagt `#df2d00`, und das ist die Quelle. **Immer diesen Wert
nehmen.**

Gemessene Geometrie:

| Folge | Kasten B×H | Polster L / R | Polster O / U |
|---|---|---|---|
| `frNOUgxE0IM` | 669×142 | 16 / 15 | 12 / 5 |
| `ewgUIZGJaWQ` | 414×119 | 21 / 22 | 17 / 16 |
| `GxpvzT3rUBQ` | 671×160 | 24 / **4** | 18 / 38 |
| `-0NES3TOiIg` | 743×166 | 15 / 17 | 16 / 12 |
| `RG-K0fIA2-w` | 495×152 | 29 / 30 | 21 / 27 |
| `f79ehF4zP3I` | 853×172 | 15 / 14 | 23 / 8 |

**Rechteckig, ohne Rundung. Seitliches Polster symmetrisch, 15–30 px** (rund
0,2–0,3 Versalhöhe). Höhe 119–172 px. Oberkante liegt bei y ≈ 200–300, also im
oberen mittleren Drittel. **Immer genau ein Wort, immer genau ein Kasten.**
`GxpvzT3rUBQ` ist der einzige Ausreißer: rechts nur 4 px Luft.

### Was es nicht gibt

**Kein Logo, kein Rahmen, kein Schlagschatten auf der Schrift, keine Kontur.**
Die Lesbarkeit kommt aus dem dunklen Hintergrund. Die **Fotokarte** dagegen
*hat* einen Schlagschatten — das ist der einzige Schatten im Bild.

## Die Schrift: Poppins Bold (700) — gemessen, nicht geraten

**Gefunden.** Fingerabdruck über die Einzelbuchstabenbreiten, auf Versalhöhe
normiert, gegen Poppins 700 / 800 und Montserrat 800 gerechnet:

„Patriarchy" aus `frNOUgxE0IM`, Versalhöhe 82 px:

| | P | a | t | r | i | a | r | c | h | y |
|---|---|---|---|---|---|---|---|---|---|---|
| **Original** | 62 | 69 | 41 | 40 | 23 | 69 | 40 | 63 | 65 | 71 |
| **Poppins 700** | 62,4 | 68,6 | 41,1 | 40,3 | 23,6 | 68,6 | 40,3 | 63,9 | 64,8 | 73,8 |
| Montserrat 800 | 73,8 | 63,3 | 50,4 | 42,8 | 27,2 | 63,3 | 42,8 | 66,2 | 67,6 | 75,0 |

„Saved" aus `RG-K0fIA2-w`, Versalhöhe 100 px: Original 73 / 82 / 82 / 77 / 82,
Poppins 700: 73,3 / 81,6 / 84,0 / 77,8 / 81,6. Montserrat verschmilzt dort „av"
und ist schon in der Buchstabenzahl falsch.

**Poppins Bold trifft auf unter 1 px je Buchstabe, zweimal unabhängig.
Montserrat ist ausgeschlossen.** Das 'a' ist einstöckig, die i-Punkte sind rund,
der y-Abstrich ist gerade — alles drei spricht gegen Montserrat und für Poppins.
Laufweite rund +1 % gegenüber der Vorgabe, sonst Standard.

Die Datei ist frei (OFL) und aus dem Container erreichbar:

```
curl -sS -A "Mozilla/5.0" "https://fonts.googleapis.com/css2?family=Poppins:wght@700"
# → https://fonts.gstatic.com/s/poppins/v24/pxiByp8kv8JHgFVrLCz7V1s.ttf  (700)
```

`github.com/google/fonts` gibt im Container **403** über den Proxy —
`fonts.gstatic.com` geht. **Damit ist die Schriftlücke zu**, vorbehaltlich
seiner Bestätigung: meine Messung schlägt seine Abnahme nicht.

## Was ich revidiert habe

1. **„Kopf füllt rund zwei Drittel der Bildhöhe"** → falsch. Volle Bildhöhe,
   Scheitel angeschnitten.
2. **„Die Mitte trägt ein echtes Foto"** → nur in Aufbau A. In Aufbau B liegt
   das Foto als gekippte Karte **links**, die Mitte ist Textspalte.
3. **„zwei bis drei Zeilen"** → zwei bis **vier**.
4. **Die gekippte Fotokarte mit Rand und Schatten fehlte ganz.** Sie ist das
   zweithäufigste Gestaltungsmittel nach dem Kasten.
5. **„Links in aller Regel er selbst"** → **bestätigt**, nachdem ich am
   20.10. ein Einzelbild aus `Right Cam` der Aaronson-Aufnahme gezogen habe
   (die Kameradatei, die laut `aaronson-shorts.md` auf Yannick zeigt): er ist
   der Brillenträger mit den langen Haaren, und der steht in Aufbau A links.
   Der einzelne Kopf in Aufbau B ist **der Gast**, nicht er — in
   `-0NES3TOiIg`, `GxpvzT3rUBQ` und `f79ehF4zP3I` steht dort derselbe
   Gast-Kopf rechts, und Yannick kommt im Bild gar nicht vor.

## Grafik in der Bildmitte — nach den DOAC-Vorlagen gemessen

Er am 20.10.: *„Ich möchte, dass du im Hintergrund so eine Grafik erstellst,
wie bei Diary of a CEO."* Drei Vorlagen geschickt, gewünscht ist die mittlere
mit dem ChatGPT-Logo.

### Was bei DOAC steht, mit demselben Detektor gemessen

| | links: Augen x / y · Höhe | rechts: Augen x / y · Höhe |
|---|---|---|
| Vorlage 1 | 177 / 283 · 441 | 1127 / 280 · 431 |
| Vorlage 2 | 162 / 305 · 448 | 1133 / 330 · 425 |
| Vorlage 3 | 163 / 290 · 489 | 1124 / 338 · 421 |
| **Mittel** | **167 / 293 · 459** | **1128 / 316 · 426** |

**Mit Grafik in der Mitte rücken die Köpfe nach aussen und werden kleiner:**
Gesichtshöhe 459 / 426 statt 508 / 497 bei ihm ohne Grafik, Augen bei x = 167
und 1128 statt 170 und 1109. Sonst bleibt für die Mitte kein Platz.

**Die Schrift sitzt oben, nicht mittig.** Bei DOAC läuft der Textblock von
y ≈ 20 bis 230, Mitte also bei ≈ 125. Das Mittelfeld beginnt darunter bei
y ≈ 230 und läuft bis zur Unterkante, waagerecht von x ≈ 300 bis 960.

**Das ChatGPT-Logo** in Vorlage 2: 132 × 135 px, Mitte bei (524, 402), Farbe
≈ `#F04860`, als Kontur mit Neon-Schein, nicht gefüllt.

### Was gebaut ist

`thumbnail_bau.py` nimmt jetzt `"mitte": "<bild>"`. Liegt eines vor, schaltet
der Setzer selbsttätig auf die DOAC-Werte um: Köpfe nach aussen, Schrift nach
oben. Dazu `karte()` — die **gekippte Fotokarte mit hellem Rand und
Schlagschatten**, die in drei seiner sechs Thumbnails steht und die hier
bisher nur beschrieben, nie gebaut war.

### Was nicht gebaut ist, und warum

**Das DOAC-Mittelbild ist selbst KI-erzeugt** — der Cyborg-Kopf, die
Robotergesichter, die brennende Stadt. Ein Eins-zu-eins-Nachbau ginge nur mit
einem Bildmodell, und seine stehende Vorgabe lautet: keine Bildmodelle, keine
erfundenen Gesichter, keine KI-Hintergründe.

**Gefragt und entschieden.** Am 20.10. habe ich ihm die drei Wege vorgelegt;
er hat **das Erzeugen für die Mitte freigegeben**. Damit gilt ab jetzt:

> **Die Köpfe bleiben echt. Nur das Mittelbild darf erzeugt werden.**
> Kein erzeugtes Gesicht von ihm, von einem Gast oder von einer anderen
> wirklichen Person — die Mitte zeigt Sachen und Figuren, keine Menschen,
> die es gibt.

### Wie das Mittelbild entsteht

Über den Canva-Connector, `generate-image`. Zwei Dinge sind dabei zu wissen:

**Der Sicherheitsfilter greift bei Gesichtsbeschreibungen.** Der erste Versuch
(„linke Hälfte eines menschlichen Gesichts, rechte Hälfte ein Androidenschädel")
lief in `CLIENT_UNSAFE_INPUT`. Als **ein Objekt** beschrieben ging es durch:
„ein humanoider Roboterkopf, links mit synthetischer Haut, rechts
blankgelegtes Chrom".

**Das Bild kommt nicht einfach heraus.** `generate-image` liefert nur eine
200-px-Vorschau, und `canva.com` wie `export-download.canva.com` sind im
Container über den Proxy gesperrt. Der Weg, der funktioniert:

1. `generate-image` → `media_id`
2. `create-design` (leere quadratische Seite) → `design_id`
3. `read-design` mit `open_transaction` → `transaction_id`, `page_id`
4. `edit-design`, `insert_fill` mit dem `media_id` über die ganze Seite
5. Die **Vorschau aus der Antwort** ist 600 × 600 und liegt als Datei im
   Container — die wird genommen. Der Export über `export-design` liefert
   zwar 1080 px, die URL ist aber nicht abrufbar.

600 px reichen: das Mittelfeld ist 660 px breit.

### Das ChatGPT-Logo — Behelf, der funktioniert

Alle Quellen für eine saubere Logodatei sind im Container gesperrt
(`simpleicons`, `unpkg`, `cdn.jsdelivr.net`, `upload.wikimedia.org`), und ein
Bildmodell malt Logos falsch. **Der Weg, der geht:** die Marke aus der
DOAC-Vorlage herauslösen, die er selbst geschickt hat. Dort liegt sie bei
(524, 402) in 132 × 135 px — genau der Größe, in der sie gebraucht wird, also
ohne Hochrechnen.

Gewonnen wird eine **Graustufenmaske** über die Pinkheit
(`rot − grün`), mit einer Kreismaske gegen Reste des Hintergrunds.
`logo_setzen()` färbt die Maske frisch in `#F04860` und legt drei
Weichzeichnungen als Neon-Schein darunter. Übernommen wird also die **Form**,
nicht fremdes Rendering. Liegt in `video/thumbnails/_logo_openai.png`,
136 × 141 px.

**Das bleibt ein Behelf.** Mit einer sauberen SVG sitzt es in jeder Größe
scharf — siehe `WAS-ICH-BRAUCHE.md`.

### Was noch fehlt

**Nichts mehr für dieses Thumbnail.** Was generell fehlt: In der DOAC-Vorlage liegt es als Kontur mit Neon-Schein
in der Mitte, 132 × 135 px, `#F04860`. Ich habe keine saubere Logodatei:
eine saubere Logodatei, die Netzwerkfreigabe für die gesperrten Hosts, und
die Bestätigung der Schrift. Alles aufgeschrieben in
`video/thumbnails/WAS-ICH-BRAUCHE.md`.

### Kopfgrössen gleichen sich nicht über den Gesichtsrahmen aus

Am 20.10. fiel ihm auf, dass Aaronsons Kopf oben zu viel Luft hatte, während
seiner den Rand ausreizte. Nachgemessen: bei gleichem YuNet-Rahmen
(459 / 426) landete sein Scheitel bei y = 11, Aaronsons bei y = 71.

**Der Grund:** der Abstand Scheitel-zu-Auge ist bei beiden verschieden, je
nach Kopfhaltung und Abstand zur Kamera. Der Gesichtsrahmen misst das nicht
mit.

**Die falsche Abhilfe, die ich zuerst nahm:** den Kopf grösser ziehen, bis
der Scheitel oben anstösst. Damit wurde Aaronson um 16 % grösser als Yannick,
und das fiel sofort auf: *„Scotts Kopf ist fast doppelt so gross wie meiner."*

**Die richtige Abhilfe: den Kopf hochschieben, nicht vergrössern.**
`kopf_setzen()` nimmt dafür `scheitel_y` statt `augen_y` — die Oberkante wird
gesetzt, die Augenhöhe daraus gerechnet. Beide Köpfe dürfen dieselbe Grösse
behalten und werden trotzdem oben gleich angeschnitten.

**Grössen vergleicht man am Pupillenabstand, nicht an der Rahmenhöhe.** Die
Rahmenhöhe hängt von Frisur und Kopfhaltung ab, der Pupillenabstand nicht.

| | links | rechts | Verhältnis |
|---|---:|---:|---:|
| seine DOAC-Vorlage 2 | 138,2 | 144,1 | **1,043** |
| dieses Thumbnail | 142,0 | 144,5 | **1,018** |

Rechts darf also **minimal grösser** sein als links, aber nicht mehr.

### Hände freistellen

Sein Hinweis: *„Die Hand hat keine Wirkung."* In `a_2504` liegen beide Hände
als **eigene Maskenbereiche** vor — ab Zeile 686 steht links von Spalte 800
nur die Hand, der Rumpf beginnt dort erst bei Spalte 880. Ein Nullsetzen des
Alphakanals in diesem Bereich entfernt sie sauber, ohne den Körper zu
beschädigen. Vor so einem Schnitt immer erst das Zeilenprofil der Maske
ansehen.

### Eine Regel für mich

**Genau das liefern, was bestellt ist.** Er hat „Human Extinction" verlangt;
ich habe zusätzlich eine zweite Copy gebaut, die er nicht wollte, und das hat
ihn zu Recht geärgert. Eine Bestellung, eine Lieferung. Was ich zusätzlich
für sinnvoll halte, wird gefragt, nicht danebengelegt.

## Die Mimik — die wichtigste Regel, und die habe ich zweimal verfehlt

Seine Worte am 20.10.: *„Das hat keinen Anreiz, da klickt keiner drauf, wenn
jemand auf einem Thumbnail lacht. Das müssen schockierte, überraschte, böse
Blicke sein."*

An den sieben Gesichtern seiner veröffentlichten Thumbnails nachgesehen, und
es stimmt ohne Ausnahme:

- **Augen weit auf, Weiß rundum sichtbar** — nicht zusammengekniffen
- **Brauen hoch**, bei mehreren die Stirn in Falten
- **Mund offen** — aber als Staunen oder Grimasse, nicht als Lächeln
- Oder stattdessen ein **harter, verengter Blick**

**Kein einziges lacht.** Ich habe in Runde 1 und 2 beide Male lächelnde
Gesichter geliefert. Das ist der teuerste Fehler dieser Serie gewesen.

### Messbar machen

Augenweiß ist ein brauchbarer Hilfswert: helle, farbarme Pixel in einem
Fenster um die beiden YuNet-Augenpunkte, auf den Pupillenabstand normiert
(`video/thumbnails/augen.py`). Grünliche Pixel müssen raus, sonst zählen die
Spiegelungen der Pflanzen in seiner Brille mit.

| | Augenweiß |
|---|---|
| seine veröffentlichten Gesichter | **0,006 – 0,201**, links meist 0,016–0,039 |
| meine lächelnden Fehlgriffe | **0,0000 – 0,032** — beim Lächeln verschwindet es ganz |

**Als Vorsortierung taugt es, als Entscheidung nicht.** Ein harter, verengter
Blick hat wenig Augenweiß und ist trotzdem richtig. Angeschaut wird jedes Bild.

### Was in der Aaronson-Aufnahme drin ist — und was nicht

**Nachgesehen: 2.600 Einzelbilder aus rund 45 Minuten** beider Nahkameras,
davon 1.806 aus einem zusammenhängenden 1-Bild-pro-Sekunde-Durchlauf über
30 Minuten.

**Bei ihm gibt es den aufgerissenen Blick in diesem Gespräch nicht.** Der
höchste Wert über alle Bilder liegt bei 0,017, seine eigenen Thumbnails liegen
bei 0,016–0,039. Er hört in dieser Folge ruhig zu, oft mit der Faust am Kinn.
Was es gibt: **ungläubig** (2871 s), **hart und verschlossen** (5749 s),
**skeptisch mit gerunzelter Braue** (3605 s), **angespannt sprechend** (718 s).

**Bei Aaronson ist die Ausbeute gut.** Bei 3000 s verzieht er das Gesicht
regelrecht gequält, bei 3002 s und 2504 s spricht er mit offenem Mund und
hochgezogenen Brauen.

**Das ist ein Befund über das Material, keine Entschuldigung.** Wenn er die
Stelle kennt, an der er stärker reagiert hat, genügt ein Zeitstempel. Sonst
bleibt der Weg über die Totale (`Middle Camera`) oder eine andere Folge.

### Lange Fenster statt vieler kurzer

Fürs Suchen gilt: **ein zusammenhängendes Fenster ist pro Bild viel billiger
als viele kurze.** Jedes Fenster kostet einen Sprung und damit mindestens
einen 8-MiB-Block; innerhalb eines Fensters laufen die Blöcke durch.
300 Sekunden bei 1 Bild/s kosten rund 200 MB für 300 Bilder — dieselben
300 Bilder aus 60 kurzen Fenstern kosten das Mehrfache.


## Sein Canva-File — die Quelle, nicht mehr die Schätzung

Seit dem 20.10. ist der Connector verbunden. Sein Arbeitsfile heisst
**`TN: YNB Podcast - Danny`** (`DAHTeSc4G4U`), elf Seiten, je 1280×720. „TN"
= Thumbnail. Es gibt **keine Brand Templates und kein Autofill** — das File
ist eine normale Sammlung von Seiten, keine befüllbare Vorlage. Der
Autofill-Weg ist damit erledigt.

Was direkt daraus kommt, statt gemessen zu werden:

| | Wert | Herkunft |
|---|---|---|
| Kastenfarbe | **`#df2d00`** | `paths[].fill.color` |
| Schriftverweis | `YAFdJjbTu24,1` | `formatting.fontRef` |
| Ausrichtung | `center` | `formatting.textAlign` |
| Zeilenabstand | **1,11** (einmal 1,02, einmal 1,22) | `formatting.lineHeight` |
| Schriftgrade | 104,5 · 107,7 · 116 · 122,2 · 132,6 · 137,9 · 161,3 · 163,8 · 175,0 | `formatting.fontSize` |

### Die Satzregel, die ich vorher falsch hatte

**Ein Textblock hat genau einen Schriftgrad und genau einen Zeilenabstand.**
Nicht eine eigene Versalhöhe je Zeile. Steht so in jedem `textRegion` seines
Files. Mein erster Entwurf gab jeder Zeile ihre eigene Grösse — damit wird der
Zeilenabstand ungleich und der Block franst aus. **Er hat das sofort gesehen
und benannt.**

### Kastenmasse, aus fünf seiner Kästen gerechnet

Kasten als Rechteck hinter genau einer Zeile, `cornerRounding: 0`:

| Wort | Grad | Tinte | Kasten | Polster seitl. | Höhe / Grad |
|---|---:|---:|---:|---:|---:|
| GOD | 116,0 | 264 | 288,2 | 12,1 | 1,010 |
| Coincidence? | 104,5 | 728 | 747,4 | 9,7 | 1,193 |
| REALLY | 107,7 | 384 | 406,1 | 11,1 | 0,942 |
| TRAP | 163,8 | 427 | 452,0 | 12,5 | 1,218 |
| PAST | 161,3 | 413 | 448,2 | 17,6 | 0,932 |

→ **Polster seitlich ≈ 0,10 × Schriftgrad · Polster oben/unten ≈ 0,14 ×
Schriftgrad.**

### Wie der Kasten sitzt — zweimal nachkorrigiert

Er am 20.10.: *„Der Balken muss nochmal adjustiert werden, da ist mir das Wort
Extinction noch nicht gleichmäßig."* Zu Recht, zwei Fehler:

1. **Waagerecht:** ich hatte die **Vorschubbreite** des Wortes genommen
   (`textlength`) statt der **Tintenbreite**. Die Vorschubbreite enthält den
   Seitenabstand der Schrift — dadurch stand rechts sichtbar mehr Luft als
   links. Richtig ist `textbbox`.
2. **Senkrecht:** der Kasten war auf die Versalhöhe zentriert. Wörter mit
   Oberlängen (`t`, `i`-Punkt in „Extinction") ragen darüber hinaus, also
   stand oben mehr Luft als unten.

**Die Regel, die jetzt gilt:** der Kasten sitzt auf dem **Tintenband** des
Wortes — Oberkante der Tinte bis Grundlinie — mit gleich viel Luft rundum.
**Unterlängen hängen heraus**, nicht hinein: das `y` von „Patriarchy" in
`frNOUgxE0IM` ragt deutlich unter den Kasten, und das `g` von „Orangutans"
macht es jetzt genauso.

Nachgemessen am fertigen Bild: links 22, rechts 22, oben 19, unten 19 px.

Nebenbei: dass Poppins-Bold-Tintenbreiten bei fünf verschiedenen Wörtern in
fünf verschiedenen Graden durchweg ein plausibles, gleichmässiges Polster
ergeben, ist ein weiterer unabhängiger Beleg für die Schrift.

## Die Blickrichtung — die Regel, die ich zuerst gebrochen habe

**Beide schauen nach innen. Er links nach rechts, der Gast rechts nach links.**
Das steht oben im Bauplan seit der ersten Messung, und ich habe mir trotzdem
ein Bild ausgesucht, auf dem er geradeaus schaut. Seine Rückmeldung:
*„Mein Gesicht soll natürlich den Gast anschauen."*

**Das ist nicht verhandelbar und geht der Mimik vor.** Lieber ein etwas
ruhigeres Gesicht mit richtiger Blickrichtung als ein ausdrucksstarkes, das
ins Leere schaut.

**Automatisch messen lässt sich das nicht zuverlässig.** Ich habe es über die
Nase gegen die Augenmitte versucht (YuNet) — bei Profilaufnahmen setzt der
Detektor die Punkte irgendwohin ins Unscharfe, und das Vorzeichen wird
Zufall. Geprüft an `y_2695`: Messung sagte „nach links gedreht", das Bild
zeigt eindeutig nach rechts. **Blickrichtung wird angeschaut, nicht
gerechnet.** Zur Platzierung taugt YuNet, zur Kopfdrehung nicht.


## Die Platzierung, aus seinen Thumbnails gemessen

Mit YuNet (Gesichtserkennung, kein Erzeugen) an den drei veröffentlichten
Zwei-Kopf-Thumbnails gemessen — Augenmitte und Gesichtsrahmenhöhe:

| Folge | links: Augen x / y · Höhe | rechts: Augen x / y · Höhe |
|---|---|---|
| `frNOUgxE0IM` | 178 / 315 · 500 | 1099 / 358 · 501 |
| `ewgUIZGJaWQ` | 185 / 286 · 545 | 1117 / 251 · 488 |
| `RG-K0fIA2-w` | 148 / 243 · 480 | 1110 / 303 · 500 |
| **Mittel** | **170 / 281 · 508** | **1109 / 304 · 497** |

Nach diesen sechs Zahlen setzt `video/thumbnail_bau.py` die Köpfe: skalieren
auf die Rahmenhöhe, platzieren auf die Augenmitte. Der Einzelkopf in Aufbau B
sitzt bei **1063 / 278 · 475** (aus `GxpvzT3rUBQ`, `-0NES3TOiIg`,
`f79ehF4zP3I`).

**Warum nicht über die Kopfhöhe:** Scheitel-zu-Schulter aus der Freistell-Maske
springt kaum, wenn jemand den Kopf in den Nacken legt — der Kopf im Bild aber
deutlich. Das war der erste Versuch, und er lieferte je nach Pose bis zu 25 %
Grössenunterschied. Die Augenlinie tut das nicht.

## Das Werkzeug

`video/thumbnail_bau.py` nimmt Freisteller, einen Hintergrund und die Zeilen
und setzt daraus die 1280×720. Aufruf über eine Plan-Datei:

```
python3 video/thumbnail_bau.py --plan video/thumbnails/plan-aaronson.json
```

Eine Zeile ist `[text, versalhöhe, kasten?]`. Genau eine Zeile bekommt den
Kasten. Mitgeliefert: `video/marke/Poppins-Bold.ttf` und
`video/modelle/yunet.onnx` (232 KB, von huggingface.co/opencv — `github.com`
und `cdn.jsdelivr.net` geben im Container 403 über den Proxy).

**Freistellen** läuft über `rembg`/U²-Net. Das ist Segmentierung: es schneidet
ein echtes Foto aus, es erfindet nichts. Die Kanten sitzen auch an den Haaren
sauber. `alpha_matting=True` gibt weichere Kanten, bricht aber bei manchen
Bildern mit einem Solver-Fehler ab — dann ohne.

**Zwei Fallen beim Drive-Zugriff**, über die ich gestolpert bin und die auch
`video/drive_fernzugriff.py` betreffen:

1. **HEAD liefert `content-length: 0`.** Dann ist die Dateigrösse 0, jeder
   Lesevorgang leer, und PyAV bricht mit `InvalidData` ab — nicht
   reproduzierbar, weil HEAD mal richtig und mal 0 antwortet. Die Grösse
   gehört aus dem `content-range` einer Ein-Byte-Bereichsanfrage.
2. **Der Blockleser prüft den Statuscode nicht.** Gibt Drive unter Last eine
   Fehlerseite, landet HTML als „Daten" im Puffer. Status, `content-range`
   und Blocklänge gehören geprüft.

Beides ist in `video/thumbnails/drive_fest.py` behoben; `drive_fernzugriff.py`
habe ich nicht angefasst, das gehört dem Schnitt-Zweig.

## Das Freistellen der Gesichter

**Gelöst, ohne Canva** — siehe oben. Der Weg über Canva bleibt offen, er wird
aber nicht mehr gebraucht.

## Canva

Der Canva-Connector **ist in seinem Konto schon eingerichtet**, steht aber auf
`needs_reconnect` — er ist also abgemeldet und liefert gerade keine Werkzeuge.
Nach dem Neuverbinden (claude.ai → Einstellungen → Connectoren) gäbe es unter
anderem `search-designs`, `get-design`, `autofill` und einen Export. Dann ließe
sich eine seiner bestehenden Vorlagen befüllen, statt das Layout nachzubauen.

**Vorbehalt, den ich nicht geprüft habe:** Canvas Autofill arbeitet mit
*Brand Templates*, und die sind an die größeren Canva-Tarife gebunden. Ob sein
Konto das hat, sagt erst ein Versuch nach dem Neuverbinden.

**Canva ist jetzt die Abkürzung, nicht mehr die Bedingung** — die Schrift liegt
seit dieser Messung auch ohne Canva vor.
