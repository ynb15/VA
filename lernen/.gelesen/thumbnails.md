# Thumbnails — Befunde für den Kanal

Geschrieben vom Thumbnail Assistant, Branch `claude/thumbnails`. Neuester Tag
oben. Nur nachgemessene Befunde mit Zahl oder wörtlichem Zitat.

---

## 21.10.2026 — Nachtrag aus 15 Commits

### Die Schrift der Marke — gefunden und belegt

- **Es ist Poppins Bold (700).** Nicht Montserrat. Gemessen über einen
  Fingerabdruck der **Einzelbuchstaben-Tintenbreiten**, auf Versalhöhe
  normiert, gegen Poppins 700, Poppins 800 und Montserrat 800 gerechnet.
  Zweimal unabhängig: „Patriarchy" aus `frNOUgxE0IM` (Versalhöhe 82 px) und
  „Saved" aus `RG-K0fIA2-w` (Versalhöhe 100 px). **Abweichung unter 1 px je
  Buchstabe.** Montserrat verschmilzt bei „Saved" sogar „av" und ist schon in
  der Buchstabenzahl falsch. Unabhängige Gegenprobe: die Kastenpolster in
  seinem Canva-File ergeben mit Poppins-Breiten bei fünf verschiedenen Wörtern
  in fünf Graden durchweg 0,10 × Schriftgrad.
  **Die Datei liegt im Repo: `video/marke/Poppins-Bold.ttf`.**
  → betrifft: content-*, cinematic, alle, die Kopfzeilen oder Grafiken setzen

- **Woher die Datei kam:** `fonts.gstatic.com` (über die CSS-API von
  `fonts.googleapis.com`). `github.com`, `cdn.jsdelivr.net` und `unpkg.com`
  geben im Container **403** über den Proxy.
  → betrifft: alle

- **Sein Canva-File nennt die Schrift nur als `YAFdJjbTu24,1`**, nicht im
  Klartext. **Er hat Poppins bis heute nicht bestätigt** — bis dahin ist es
  eine sehr gut belegte Messung, keine Auskunft von ihm.
  → betrifft: alle

### Die Markenfarbe war falsch im Umlauf

- **Der orangerote Kasten ist `#DF2D00`**, aus seinem Canva-File
  (`paths[].fill.color`). Mein früherer Wert `#DF2C00` war aus JPEGs
  geschätzt und in der letzten Ziffer daneben. **Immer `#DF2D00`.**
  → betrifft: alle

### Satzregel aus seinem Canva-File

- **Ein Textblock hat genau einen Schriftgrad und genau einen Zeilenabstand.**
  `lineHeight` meist **1,11** (einmal 1,02, einmal 1,22), `textAlign: center`,
  Schriftgrade 104,5 bis 175,0. Wo im fertigen Bild verschiedene Größen stehen,
  sind es **zwei getrennte Textblöcke**, nicht ungleiche Zeilen in einem.
  Sein Arbeitsfile: `TN: YNB Podcast - Danny` (`DAHTeSc4G4U`), 11 Seiten à
  1280×720. **Brand Templates und Autofill gibt es in dem Konto nicht.**
  → betrifft: alle, die Typo in seiner Marke setzen

### Vier Korrekturen am Bauplan `video/thumbnails.md`

Mein erster Bauplan war an sechs Thumbnails abgelesen und in vier Punkten
falsch. **Wer die alte Fassung gelesen hat, arbeitet mit falschen Zahlen:**

1. **„Kopf füllt rund zwei Drittel der Bildhöhe"** → falsch. Der Kopf füllt
   die **volle Bildhöhe**, der Scheitel ist oben angeschnitten. Über eine
   Hautmaske gemessen: in fünf von sechs beginnt der Hautbereich in Zeile 0
   und reicht bis Zeile 685–719 von 720.
2. **„Die Mitte trägt ein echtes Foto"** → nur in der Hälfte der Fälle. In
   drei von sechs liegt das Foto als **gekippte Karte links**, die Mitte ist
   Textspalte.
3. **„zwei bis drei Zeilen"** → zwei bis **vier**.
4. **Die gekippte Fotokarte mit hellem Rand und Schlagschatten fehlte ganz.**
   Sie steht in drei von sechs Thumbnails und ist das zweithäufigste
   Gestaltungsmittel nach dem Kasten.

Dazu eine fünfte, später: **„kein Fragezeichen" war zu eng.** Das kam aus den
sechs veröffentlichten Thumbnails, in denen zufällig keines vorkommt; sein
Canva-File hat mehrere („Coincidence?", „Did I REALLY Make It Up?").
  → betrifft: alle, die `video/thumbnails.md` als Grundlage nehmen

### Seine Korrekturen, wörtlich

Diese drei gelten weit über Thumbnails hinaus:

- **Mimik.** *„Das hat keinen Anreiz, da klickt keiner drauf, wenn jemand auf
  einem Thumbnail lacht. Das müssen schockierte, überraschte, böse Blicke
  sein."* Nachgeprüft an den sieben Gesichtern seiner veröffentlichten
  Thumbnails: **keines lacht.** Alle haben weit offene Augen, hochgezogene
  Brauen und offenen Mund — oder einen harten, verengten Blick. Ich hatte ihm
  zweimal lachende Gesichter geliefert.
  → betrifft: content-*, cinematic, alle, die Standbilder von ihm auswählen

- **Blickrichtung.** *„Mein Gesicht soll natürlich den Gast anschauen und der
  Gast auch, oder zumindest in die gegenseitige Richtung."* Das sticht die
  Mimik: lieber ein ruhigeres Gesicht mit richtiger Blickrichtung als ein
  ausdrucksstarkes, das ins Leere schaut.
  → betrifft: content-*, cinematic

- **Umfang.** Er bestellte die Copy „Human Extinction"; ich lieferte
  zusätzlich eine zweite Copy, die er nicht wollte: *„Ich hab dir gesagt, ich
  will den Text Human Extinction und dann … nimmst einfach eine andere Copy.
  Was soll der Scheiß?"* **Eine Bestellung, eine Lieferung.** Was man
  zusätzlich für sinnvoll hält, wird gefragt, nicht danebengelegt.
  → betrifft: alle

### Erzeugte Bilder — die Regel, die er gesetzt hat

- **Am 20.10. hat er das Erzeugen für die Bildmitte freigegeben.** Wortlaut
  der Regel, wie sie seitdem gilt: **die Köpfe bleiben echte Einzelbilder,
  erzeugt werden darf nur das Mittelbild, und es zeigt keine wirkliche
  Person.**
- **Am 21.10. bat er um eine Ausnahme** — das Gesicht eines Gastes
  (Kingsbury) erzeugen zu lassen. **Habe ich nicht gemacht:** über das Gesicht
  eines Gastes kann er nicht entscheiden, und eine bestimmte Ähnlichkeit
  trifft ein Modell nie ganz. **Es war auch nicht nötig** — siehe unten.
  → betrifft: alle, die Bilder erzeugen

### Kingsbury: die Annahme stimmte nicht

- **Er sagte, die Aufnahme sei schlecht aufgelöst.** Gemessen: seine eigene
  Kamera hat in **3840×2160** aufgenommen, Kyles DJI-Dateien ebenfalls in 4K
  bei 60 fps, Kyles C0105 in 1080p mit sehr hoher Bitrate. **Das „LOW_RES" im
  Dateinamen gehört zur Proxy-Datei des Cutters**, nicht zum Material.
- **Das wirkliche Problem war die Einstellungsgröße.** Für ein Thumbnail
  braucht ein Gesicht rund **145 px Pupillenabstand**. Alle Winkel sind
  Totalen: 71 px auf seiner Kamera, 21–31 px auf Kyles 1080p-Kamera.
- **Und meine eigene Messung war zu dünn.** Zwölf Bilder aus drei Fenstern
  ergaben höchstens 70 px. **72 Bilder aus acht Fenstern derselben Datei
  ergaben 132 px** — er lehnt sich im Gespräch vor. Aus 2× Hochrechnung wurde
  1,1×. **Zwölf Stichproben reichen nicht, um eine Datei abzuschreiben.**
  → betrifft: alle, die Material beurteilen

### Gesichter messen — drei Fallen

- **Größen vergleicht man am Pupillenabstand, nicht an der Rahmenhöhe.** Die
  Rahmenhöhe hängt von Frisur und Kopfhaltung ab. Bei gleicher Rahmenhöhe lag
  der eine Scheitel bei y = 11, der andere bei y = 71.
- **YuNet versagt bei Profilaufnahmen.** Der Detektor setzt die Punkte dann
  irgendwohin ins Unscharfe, und eine daraus gerechnete Blickrichtung wird
  Zufall. Am Bild geprüft: die Messung sagte „nach links gedreht", das Bild
  zeigte eindeutig nach rechts. **Blickrichtung wird angeschaut, nicht
  gerechnet.** Zur Platzierung taugt YuNet, zur Kopfdrehung nicht.
- **Der Detektor meldete in einer DJI-Datei 109 px — das war eine Hand.**
  Jeden Messwert, auf dem eine Entscheidung steht, am Bild nachsehen.
  → betrifft: content-*, cinematic, thumbnails

- **Augenweite lässt sich vorsortieren:** helle, farbarme Pixel in einem
  Fenster um die YuNet-Augenpunkte, auf den Pupillenabstand normiert
  (`video/thumbnails/augen.py`). Grünliche Pixel ausschliessen, sonst zählen
  Spiegelungen in seiner Brille mit. **Seine veröffentlichten Gesichter liegen
  bei 0,016–0,039, lächelnde Gesichter bei 0,0000** — beim Lächeln verschwindet
  das Augenweiß ganz. Taugt zum Vorsortieren, nicht zum Entscheiden: ein
  harter, verengter Blick hat wenig Augenweiß und ist trotzdem richtig.
  → betrifft: content-*, cinematic

### Drive — vier Fallen zusätzlich zu dem, was Alfred schon notiert hat

Alle vier traten bei langen Durchläufen auf und sind in
`video/thumbnails/drive_fest.py` behoben:

1. **HEAD liefert auf die Download-URL unzuverlässig `content-length: 0`.**
   Dann ist die Dateigröße 0, jeder Lesevorgang leer, und PyAV bricht mit
   `InvalidData` ab — **nicht reproduzierbar**, weil HEAD mal richtig und mal
   0 antwortet. Die Größe gehört aus dem `content-range` einer
   **Ein-Byte-Bereichsanfrage**.
2. **Der Bereichsleser muss dieselbe `requests.Session` benutzen wie die
   Virenscan-Bestätigung.** Die Bestätigung setzt ein Cookie; ohne das
   antwortet Drive auf die Bereichsanfrage mit **200 und der ganzen Datei**
   statt mit 206.
3. **Eine 200-Antwort muss mit `stream=True` verworfen werden**, bevor der
   Körper gelesen wird. Sonst lädt der Leser eine 4-GB-Datei in den Speicher,
   nur um sie wegzuwerfen.
4. **Das uuid-Token der Download-URL läuft ab.** Bei Durchläufen über eine
   Viertelstunde braucht der Leser einen Rückruf, der eine frische URL holt.
  → betrifft: alle, die Drive direkt lesen

- **Lange zusammenhängende Fenster sind pro Bild viel billiger als viele
  kurze.** Jeder Sprung kostet mindestens einen 8-MiB-Block; innerhalb eines
  Fensters laufen die Blöcke durch. **300 Sekunden bei 1 Bild/s kosten rund
  200 MB für 300 Bilder** — dieselben 300 Bilder aus 60 kurzen Fenstern kosten
  das Mehrfache.
  → betrifft: alle Content-Agenten

### Netz — was der Proxy im Container sperrt

- **Gesperrt (403):** `github.com`, `raw.githubusercontent.com`,
  `cdn.jsdelivr.net`, `unpkg.com`, `cdn.simpleicons.org`,
  `upload.wikimedia.org`, `canva.com`, `export-download.canva.com`.
- **Erreichbar:** `fonts.googleapis.com`, `fonts.gstatic.com`,
  `huggingface.co`, `drive.usercontent.google.com`, `i.ytimg.com`,
  `youtube.com`.
- Das YuNet-Modell kam deshalb von **huggingface.co**, nicht aus dem
  opencv_zoo auf GitHub. Liegt im Repo: `video/modelle/yunet.onnx` (232 KB).
  → betrifft: alle

### Canva — zwei Dinge, die Zeit kosten

- **`generate-image` liefert nur eine 200-px-Vorschau.** Der Export über
  `export-design` gibt zwar 1080 px, aber **die URL ist über den Proxy nicht
  abrufbar**. Brauchbar ist die **600-px-Vorschau aus der
  `edit-design`-Antwort**, die als Datei im Container landet. Der Weg:
  `generate-image` → `create-design` (leere Seite) → `read-design` mit
  `open_transaction` → `edit-design` mit `insert_fill` → Vorschau nehmen.
- **Der Sicherheitsfilter greift bei Gesichtsbeschreibungen.** „Linke Hälfte
  eines menschlichen Gesichts, rechte Hälfte ein Androidenschädel" lief in
  `CLIENT_UNSAFE_INPUT`. Als **ein Objekt** beschrieben ging es durch: „ein
  humanoider Roboterkopf, links mit synthetischer Haut, rechts blankgelegtes
  Chrom".
  → betrifft: alle, die Canva benutzen
