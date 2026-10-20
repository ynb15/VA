# B-Roll-Shorts — die drei Referenzen, ausgemessen

**Von ihm am 20.10.2026 geschickt**, mit der Ansage: „die wie ich mir
vorstelle, wie sie idealerweise aussehen sollen. Also quasi mit B-Rolls, aus
Film unterlegt, und das würde ich gerne so umsetzen."

| Kennung | Titel | Kanal |
|---|---|---|
| `VWGWkfmJCq8` | Take The Time To Enjoy Your Life | **Chris Williamson** (`@ChrisWillx`) |
| `QjmWNrq4mBU` | A Man Must Have A Quest | Chris Williamson |
| `71g-MIALgKk` | Why You Need To Just Work | Chris Williamson |

**Es sind nicht seine eigenen Shorts** — das ist eine fremde Referenz, kein
Rückblick auf den eigenen Kanal. Titel und Kanal über den oEmbed-Endpunkt
geholt (`youtube.com/oembed`, HTTP 200 ohne Anmeldung).

---

## Was ich sehen konnte, und was nicht

**Die Watch-Seite ist zu.** `yt-dlp` auf alle drei Kennungen:
*„Sign in to confirm you're not a bot."* Also **keine Aufrufzahlen, keine
Dauer, keine automatischen Untertitel** — der Weg, der am 19.10. noch für den
eigenen Kanal funktionierte, ist für diese drei nicht offen.

**Die Vorschaubilder gehen.** `i.ytimg.com/vi/<id>/oardefault.jpg` liefert je
**ein** Einzelbild im Hochformat **1080×1920**, HTTP 200, ohne Anmeldung.
`maxresdefault` und `hq720` zeigen dieselbe Szene im Querformat, `frame0` ein
kleines Bild vom Anfang.

**Die Grenze dieser Messung gehört dazu: ein Bild je Short.** Was daraus
*nicht* abzulesen ist — und was deshalb unten auch nicht behauptet wird:
wie oft und wie lange B-Roll läuft, ob hart geschnitten oder geblendet wird,
ob der Ton unter der B-Roll abgesenkt ist, ob die B-Roll stummgeschaltet ist.
**Dafür bräuchte es den Schnitt, und an den komme ich nicht.**

---

## Die Geometrie — gemessen, nicht geschätzt

Verfahren: schwarze Ränder über die Zeilen-/Spaltenmaxima der Helligkeit
abgegrenzt (Schwelle 28), Schriftzeile über neutralweiße Pixel
(Minimalkanal > 200, Kanalspreizung < 22).

### Zwei Zustände, und sie sind klar getrennt

| | **Sprecherbild** (`VWGWkfmJCq8`) | **B-Roll** (`QjmWNrq4mBU`, `71g-MIALgKk`) |
|---|---|---|
| Bildfläche | **randlos 1080×1920** | **980×980 Kasten auf Schwarz** |
| Kasten x | — | **50–1029** (Rand 50 px je Seite) |
| Kasten y | — | **470–1449** (oben 470, unten 470 — exakt mittig) |
| Seitenverhältnis | 0,562 (9:16) | **1,000 — quadratisch** |
| Höhenanteil | 1,000 | **0,510** |
| Ecken | — | **gerundet** |
| Umfeld | — | **reines Schwarz**, keine Unschärfe, keine Verdopplung |

**Beide B-Roll-Shorts haben exakt dieselben Werte** — 50/470/980/980, auf das
Pixel gleich. Das ist kein Zufallsschnitt, das ist eine feste Vorlage.

**Der Film wird also nicht ins Hochformat gezwungen.** Er läuft als
quadratischer Ausschnitt in der Bildmitte, der Rest ist schwarz. Das ist der
Grund, warum eine Kinoeinstellung darin nicht zerschnitten aussieht.

### Die Schrift

| | Sprecherbild | B-Roll |
|---|---|---|
| Text im Bild | `would it` | `comes from` |
| Zeilenhöhe | 55 px | 49 px |
| Zeilenbreite | 282 px | 372 px |
| Mitte der Zeile | **0,610** der Bildhöhe | **0,496** der Bildhöhe |
| Ausrichtung | **links**, Rand 119 px | **mittig**, Rand 356 / 352 px |
| Farbe | weiß | weiß |
| Kontur | **keine sichtbare** | keine sichtbare |
| Schreibweise | **Kleinschreibung** | Kleinschreibung |
| Wörter | **zwei** | **zwei** |

**Das Aktivwort wird über Helligkeit und Strichstärke markiert, nicht über
Farbe.** Im B-Roll-Bild getrennt ausgemessen:

| Wort | mittlere Helligkeit | Pixel je Spalte |
|---|---:|---:|
| `comes` | 187,5 | 18,0 |
| `from` | **245,3** | **24,6** |

Also: das gerade gesprochene Wort ist **heller und fetter**, das vorige steht
abgedunkelt daneben. **Kein Gelb in keinem der drei Bilder.**

---

## Wo das von seinem eigenen Look abweicht

Sein Stand nach acht Runden am Sutcliffe-Short gegen die Referenz:

| | sein Look (abgenommen 20.10.) | die Referenz |
|---|---|---|
| Schreibweise | **VERSALIEN** | **Kleinschreibung** |
| Aktivwort | **gelb** `#FFD530` | **heller + fetter weiß** |
| Kontur | **dick schwarz** + Schatten | keine sichtbare |
| Zeile | **0,65** der Höhe, mittig | 0,50 (B-Roll) / 0,61 links (Sprecher) |
| Wörter je Einblendung | **genau drei** | **zwei** |
| Bild | randlos 9:16, warmer Look, Vignette | Sprecher randlos, B-Roll 980² auf Schwarz |
| Logo | 700 px bei 0,877 | **in keinem der drei Bilder** |

**Das ist kein Detail, das ist die Hälfte der Gestaltung.** „So umsetzen"
heißt entweder *B-Roll in seinen Look einbauen* oder *den Look wechseln*.
Das ist Geschmack, also seine Entscheidung — hier steht nur, dass die beiden
Dinge nicht dasselbe sind. **Nicht stillschweigend das eine für das andere
nehmen.**

---

## Woher das Filmmaterial NICHT kommt

**Aus dem Netz hole ich es nicht.** Zwei Gründe, der zweite ist der härtere.

**1. Es ist technisch zu.** Am 20.10. gegen 13:00 gemessen, alle über den
Egress-Proxy, alle `connect_rejected` (Gateway antwortet 403 auf CONNECT):

```
archive.org · pixabay.com · www.pexels.com · videos.pexels.com
mixkit.co · coverr.co · videvo.net · commons.wikimedia.org
upload.wikimedia.org · cdn.pixabay.com
```

**Auch die freien und gemeinfreien Quellen.** Das ist dieselbe Wand wie bei
der Musik am 20.10. (`freepd.com`, `musopen.org`, `incompetech.com`).

**2. Und selbst wenn sie offen wären: die drei Referenzen unterlegen
Handelsproduktionen** — Spielfilm- und Serienmaterial. Dasselbe Argument wie
bei der Spotify-Liste gilt hier unverändert: ein Content-ID-Anspruch träfe
**seinen** Kanal, nicht meinen. Dass große Kanäle damit durchkommen, ändert
nichts daran, wo der Anspruch landet. **Ob er das für seinen Kanal eingeht,
ist seine Entscheidung** — aber das Material besorgen tue ich nicht.

## Woher es kommen kann

1. **Sein eigenes Material.** Das ist der Weg, der nichts kostet und nichts
   riskiert: AfrikaBurn, Kapstadt, die Reiseaufnahmen, das Rohmaterial der
   Folgen selbst. Auf seinem Kanal liegen dafür schon Belege
   (`10 Life Lessons I Learned at AfrikaBurn`, `Living My Dream Life in Cape
   Town`). **Und es ist unverwechselbar seins**, was gekaufte Stockbilder nie
   sind.
2. **Lizenziertes Stockmaterial**, das er selbst herunterlädt (Artgrid,
   Storyblocks und dergleichen) und in den Drive-Eingang legt.
3. **Filmausschnitte**, wenn er sie trotz Punkt 2 oben will — dann legt er
   sie selbst in den Eingang. Entscheidung und Material kommen von ihm.

In allen drei Fällen ist der Ablauf derselbe: **Datei in den Drive-Eingang,
Mechanik von hier.**

---

## Was gebaut werden muss

In `video/shorts-render.py` gibt es **keinen Schalter für B-Roll** — geprüft
an der Argumentliste. Was fehlt:

- `--broll zeit:zeit=datei[,…]` — eine Schnittliste in Clipzeit
- den quadratischen Kasten **980×980 auf x=50, y=470**, gerundete Ecken,
  schwarzes Umfeld, Quelle mittig beschnitten
- **die Stimme läuft durch.** Die B-Roll liegt im Bild, nicht im Ton; ihr
  eigener Ton wird verworfen (anders geht es auch gar nicht, sonst reden
  zwei gleichzeitig)
- Untertitel laufen über die B-Roll weiter, auf ihrer Höhe
- Logo und Look: **offen, bis er sich entschieden hat** — in den drei
  Referenzen ist auf der B-Roll kein Logo und kein warmer Look zu sehen

**Was ich nicht aus den Bildern ableiten kann und deshalb von ihm brauche:**
wie lang eine B-Roll-Einstellung steht und wie oft sie kommt. Aus einem
Einzelbild je Short ist das nicht zu holen. Vorschlag zum Einstieg, als
Vorschlag gekennzeichnet: **2–4 s je Einstellung, nur dort, wo der Satz ein
Bild hergibt** — und dann an seiner Korrektur nachgezogen, wie alles andere.

---

## Gebaut und nachgemessen (20.10.2026)

`--broll von:bis=datei[,von:bis=datei]` steht in `video/shorts-render.py`.
Zeiten in **Clipzeit**, wie bei `--stumm`.

**Die Kette hängt hinter dem Look und vor den Untertiteln.** Begründung:
in der Referenz sieht die B-Roll aus wie Film, nicht wie sein Studio — sie
soll also nicht durch die warme Gradation laufen. Die Einblendungen sollen
aber darauf stehen, und das tun sie.

**Zwei Dinge je Fenster, und das zweite ist das, was es überhaupt erst wie
die Referenz aussehen lässt:** die Karte wird darübergelegt **und der Grund
wird schwarz** (`lutyuv` mit Zeitfenster). Ohne das Abdunkeln säße die Karte
mitten im weiterredenden Sprecher.

### Am fertigen Bild gemessen, nicht am Vorhaben

| | Referenz | mein Ergebnis |
|---|---|---|
| Kasten x | 50–1029 (980 px) | **50–1029 (980 px)** |
| Kasten y | 470–1449 (980 px) | **470–1449 (980 px)** |
| Seitenverhältnis | 1,000 | **1,000** |
| außerhalb | schwarz | **maximale Helligkeit 0,0** |
| außerhalb des Fensters | randlos 9:16 | **x 0–1079, y 0–1919** |

**Der Ton ist nicht angefasst.** Dieselbe Quelle einmal mit und einmal ohne
`--broll` gerechnet, beide auf 16-kHz-Mono dekodiert:
**abtastwertgenau gleich bis 10,967 s von 11,008 s.** Danach weichen
437 Werte ab, der größte um **9 von 32768** — 88 dB unter dem Signal. Das ist
der Schwanz des AAC-Enkoders, kein Eingriff. `-an` hält den Ton der B-Roll
von vornherein draußen, damit nie zwei Stimmen laufen.

**Rechenzeit:** 11 s Short mit 3,2 s B-Roll in **18,6 s**. Ohne B-Roll sind
es 6,9 s. Die runden Ecken kommen aus `geq`, das je Pixel rechnet — das sind
die rund 12 Sekunden Unterschied. Fällt das je ins Gewicht, wird die Maske
einmal als Bild erzeugt und mit `alphamerge` aufgelegt; gebraucht wurde es
bisher nicht.

### Dabei aufgefallen: `--srt` rendert keine Untertitel

**Ein Fehler, der schon vorher drinstand und nichts mit B-Roll zu tun hat.**
In `build_ass` fiel jede Einblendung ohne Wortzeiten vor dem dafür
vorgesehenen Zweig heraus — und aus `--srt` kommen Einblendungen immer ohne
Wortzeiten. Ergebnis: `--srt clip.srt` rechnete einen Short **ohne einen
einzigen Untertitel, ohne eine Zeile Warnung.** Der Weg steht so in
`video/README.md`.

Behoben: ohne Wortzeiten steht die Zeile als Ganzes im Bild. **Das gelbe
Aktivwort gibt es auf diesem Weg nicht** — dafür braucht es Wortzeiten, also
`--auto-captions`. Wer den vollen Look will, nimmt den.

### Was noch offen ist, und von ihm abhängt

- **Wie lang eine Einstellung steht und wie oft sie kommt.** Aus einem
  Einzelbild je Referenz nicht zu holen. Vorschlag 2–4 s, dann an seiner
  Korrektur nachgezogen.
- **Logo während der B-Roll.** Steht jetzt weiter im Bild, unterhalb der
  Karte auf dem schwarzen Grund. In den drei Referenzen ist keines zu sehen.
  Ein Zeitfenster am Logo-Overlay wäre ein Einzeiler — **nicht ungefragt
  geändert.**
- **Übergang.** Zur Zeit harter Schnitt in die Karte und heraus. Ob die
  Referenz blendet, ist aus Einzelbildern nicht zu sehen.

---

## Korrektur vom 20.10., noch am selben Abend: Vollbild, nicht Karte

**„Ich will's Vollbild lassen. Ich habe dir gesagt, lass meinen Stil. Das
Einzige, was ich von Chris Williamson kopieren möchte, sind die filmischen
B-Rolls."**

Er hat recht, und der Fehler ist sauber zu benennen: **ich habe Williamsons
Rahmen für den Inhalt gehalten.** Der 980er Kasten auf Schwarz ist *dessen*
Handschrift — genauso eine Stilentscheidung wie Kleinschreibung und weißes
Aktivwort, die ich beide richtig als fremd erkannt hatte. Beim Kasten habe
ich es nicht getan, weil er sich so sauber messen ließ. **Dass etwas gut
messbar ist, macht es nicht zum Inhalt.**

`--broll-modus vollbild` ist jetzt die Vorgabe: B-Roll füllt 1080×1920 wie
jede andere Einstellung seiner Shorts. Gemessen am Ergebnis: **Inhalt
x 0–1079, y 0–1919, schwarze Ränder null auf allen vier Seiten.** Untertitel
und Logo liegen darüber wie gehabt.

Die Karte bleibt als `--broll-modus karte`, weil sie gebaut und belegt ist —
sie steht nur nicht mehr im Weg.

**Der Preis des randlosen Wegs, und er gehört dazu:** aus einem 16:9-Film
bleiben im 9:16-Fenster **31,6 % der Breite** übrig. Was links und rechts
steht, ist weg — genau deshalb nimmt Williamson die Karte. Dagegen hilft
`--broll-fokus 0..1`, das den Ausschnitt waagrecht dorthin schiebt, wo das
Motiv steht, wie `--focus` beim Hauptbild. **Bei der Auswahl der Clips zählt
das:** eine Einstellung, deren Motiv mittig steht, überlebt den Beschnitt;
eine Totale mit zwei Leuten an den Rändern nicht.

---

## Erster echter Lauf: Craig Makhosi über *Into the Wild* (20.10.2026)

Er hat zwei Dateien in den Drive gelegt und damit genau das getan, worum ich
gebeten hatte.

| | |
|---|---|
| **Podcast** | „YNB Podcast - Craig Makhosi - Ubuntu(1).mp4" · 1,04 GB · **3:58,65** · 3840×2160, HEVC, 30 fps — ein bereits geschnittener Ausschnitt, nicht die ganze Folge |
| **B-Roll** | „YNB Podcast: Into The Wild" · 274 MB · **2:24,83** · 1206×2622 mit Drehmatrix, zeigt also **2622×1206 quer** |

Beide über `drive.usercontent.google.com` geladen — **1,04 GB in 7 s**. Der
Konnektor hätte das nicht gekonnt (base64), der Bereichsleser aus
`drive_fernzugriff.py` kann es.

### Was die B-Roll-Datei wirklich ist

**Eine Bildschirmaufnahme des Kinotrailers aus dem YouTube-Player.** Nicht
der Film. Im Bild stehen: die Seitenflächen der Webseite, schwarze
Letterbox-Balken, der **SUBSCRIBE-Knopf**, und in den ersten zwei Sekunden
sogar die **Bedienleiste des Players** (Rücksprungpfeil, Fortschrittsbalken).

Das nutzbare Filmbild liegt bei **x 244–2396, y 144–1056 → 2153×913**.
Gemessen über die Bewegung zwischen sieben Bildern: was sich ändert, ist
Film; was steht, ist Oberfläche.

**Die Folge für die Auflösung, und sie ist die wichtigste Zahl hier:**

| Weg | echte Pixel | auf 1080×1920 |
|---|---|---|
| 9:16 herausschneiden | **513×913** | **2,10× hochskaliert** |
| quadratisch (Modus `unschaerfe` / `karte`) | **913×913** | **1,18×** |

**Ein 9:16-Ausschnitt verwirft 76 % der Bildbreite und muss das Übrige
vervierfachen.** Neben 4K-Podcastmaterial sieht das weich aus. Deshalb ist
für diese Quelle `--broll-modus unschaerfe` gebaut worden: der Film steht
quadratisch und fast unskaliert scharf in der Mitte, dahinter füllt er sich
selbst vergrößert und unscharf das Hochformat. **Randlos wie verlangt, ohne
den Beschnitt zu bezahlen.**

### Vier Anläufe, die Einstellungen zu finden — und warum drei scheiterten

Das ist der eigentliche Lerninhalt dieses Laufs.

**1. Eigene Schnitterkennung über Bildänderung (4 Bilder/s, Schwelle 0,35):**
fand 14 Einstellungen. **Falsch.** Sie verschmolz Einstellungen, die einander
ähnlich sehen — eine angebliche „10,4 s lange Einstellung" bei 47 s enthielt
in Wahrheit ein halbes Dutzend.

**2. Dieselbe Erkennung auf der normalisierten Datei:** besser, aber immer
noch zu grob.

**3. `ffmpeg`s eigene Szenenerkennung (`select='gt(scene,0.18)'`):**
**130 Schnitte** statt 14 — eine völlig andere Größenordnung, und die
richtige. Trotzdem lagen die geschnittenen Stücke daneben.

**4. Dicht abgetastet und angesehen (2 Bilder/s, Streifen mit Zeitmarke):**
erst das hat es gelöst. **Der Trailer blendet über, statt zu schneiden** —
und eine Szenenerkennung sieht eine Überblendung nicht, weil sich das Bild
langsam ändert. Deshalb landete jeder automatisch gesetzte Anfang mitten in
einer Blende, in der zwei Bilder übereinanderliegen.

**REGEL: Ein Trailer ist kein Film.** Er ist in 1–2-Sekunden-Stücken
geschnitten und hält sie mit Blenden zusammen. Für B-Roll heißt das: die
sauberen Strecken sind **kurz** (hier durchweg 0,9–1,9 s), und sie müssen
**angesehen** werden, nicht errechnet. Ein Kontaktabzug der Mittelpunkte
genügt dafür nicht — es braucht Anfang, Mitte und Ende jedes Stücks, sonst
sieht man den Blendenrest nicht.

**REGEL: Variable Bildrate macht Zeitmarken unzuverlässig.** Die Datei meldet
„29,70 fps bei 60 tbr". Einmal auf feste 30 fps umgerechnet
(`fps=30`, `-g 30`), und alle Zeiten stimmen. Das vorher zu tun hätte mir
zwei der vier Anläufe erspart.

### Zwei Fehler im eigenen Werkzeug, dabei behoben

**`faster-whisper` brach ab** (`TypeError: open() got an unexpected keyword
argument 'metadata_errors'`): es ruft PyAV mit einem Argument auf, das die
hier installierte PyAV-Fassung nicht kennt. **Der Ton wird jetzt selbst über
ffmpeg dekodiert** (16 kHz Mono float32) und als Feld übergeben — derselbe
Weg, den der Rest der Datei ohnehin geht.

**`ffmpeg` frisst `stdin`.** Eine Schleife, die ihre Liste aus einem
Here-Dokument las, verlor nach dem ersten Durchlauf alle weiteren Zeilen.
`-nostdin` gehört in jeden ffmpeg-Aufruf innerhalb einer Schleife.

---

## Seine Korrektur, 20.10. abends: zu kurz und zu wenig Inhalt

**„Die B-Rolls, die sind gefühlt nur eine Sekunde da, die müssen viel länger
laufen. So ist es gerade richtig disruptiv, es stört. Und da fehlt auch die
Hälfte des Inhalts. Du hast viel zu viel rausgeschnitten."**

Beides richtig, und beides geht auf **denselben** Denkfehler zurück.

### Der Fehler: ich habe nach schnittfreien Einstellungen gesucht

Ich hatte mir selbst die Regel gegeben, eine B-Roll dürfe „keinen Schnitt
drin" haben. Für einen **einzelnen Einspieler** stimmt das. Für einen
Trailer ist es die falsche Frage: der ist in 1–2-Sekunden-Stücken geschnitten,
also fand ich nur 1–2-Sekunden-Stücke — und genau die hat er als störend
empfunden.

**Richtig ist, durchgehende Strecken zu nehmen, mitsamt den Schnitten des
Trailers.** Die Schnitte sind dann kein Mangel, sondern das, was es nach
Film aussehen lässt. Nicht „eine Einstellung", sondern **ein Block**.

### Was im Trailer wirklich frei ist — gesichtet, nicht gerechnet

Vier Versuche, die Schrift automatisch zu finden, sind gescheitert; der
letzte maß an einer bekannten Schriftstelle (`jon krakauer`) **0,0000** und
an einer bekannt sauberen (`anhalter`) **0,0064** — also genau verkehrt
herum. Die Trailerschrift ist dünn, halbdurchsichtig und wandert; kein
Schwellenwert trennt sie vom Bild.

**Gelöst durch Hinsehen:** der ganze Trailer als Kontaktabzug, ein Bild je
Sekunde, 145 Stück auf drei Blättern.

| Schrift im Bild | |
|---|---|
| 0,0–3,0 | Bedienleiste des Players |
| 5,0–7,5 | Paramount / RiverRoad |
| 57,9–60,6 | „from writer-director sean penn" |
| 80,7–83,6 | „based on the best-seller by jon krakauer" |
| 87,9–90,6 | „inspired by the true story" |
| 113,6–115,9 | „take a journey" |
| 122,9–124,9 | „into the beauty" |
| 127,8–129,0 | „into the danger" |
| 134,9–138,9 | Titel „into the WILD" |

**Dazwischen 121,5 von 144,8 Sekunden frei**, in Strecken bis **50,4 s**.
Material war also nie das Problem — meine Suche war es.

**REGEL: Wenn die Automatik dreimal falsch liegt, ist es ein Blättchen-Problem,
kein Schwellenwert-Problem.** Ein Kontaktabzug über die ganze Länge kostet
eine Minute und beantwortet die Frage endgültig.

### Der Inhalt: die Stelle war halb so lang wie das Thema

Erste Fassung 76:06–115:35 (39,3 s roh). **Die Passage über *Into the Wild*
beginnt in Wahrheit bei 22:80** — mit „Everyone used to say I looked just
like the dude" — und läuft bis zum Ubuntu-Satz bei 118:00.

Neu: **22,80–118,00 = 95,2 s roh → 79,3 s bei Tempo 1,2.** Darin steckt, was
vorher fehlte: dass er das Buch an der Uni las · „happiness is only real when
shared" · *„that made his death worth it"* · *„he went and lived what we were
fantasizing about"* · der Austausch über Buch und Film · und erst dann die
Selbst-Initiation und Ubuntu.

### Die sieben Blöcke

| Block | im Short | Dauer | Trailer | worauf |
|---|---|---|---|---|
| A | 16,6–22,2 | 5,6 s | 108,5 | „that made his death worth it" |
| B | 22,9–31,1 | 8,2 s | 17,0 | „he went and lived what we were fantasizing about" |
| C | 48,7–54,5 | 5,8 s | 90,8 | „the book goes even deeper" |
| D | 54,9–58,5 | 3,6 s | 84,0 | „Christopher McCandless, Alex Supertramp" |
| E | 64,0–71,1 | 7,1 s | 61,0 | „cutting ties with my mother, my father" |
| F | 77,3–83,5 | 6,2 s | 98,8 | „going into the wilderness" |
| G | 84,2–89,2 | 5,0 s | 116,2 | „relationships are what make life meaningful" |

Zusammen **41,5 s von 95,2 s Clipzeit, also 44 %.** Vorher waren es sechs
Einspieler von je 0,9–1,9 s.

### Nebenbei: die Unschärfe war der Flaschenhals

`gblur=sigma=42` auf 1080×1920 war der Grund, warum ein 33-Sekunden-Short
**25 Minuten** brauchte. Jetzt wird auf ein Viertel verkleinert, mit
`sigma=11` weichgezeichnet und wieder vergrößert — bei einer so starken
Weichzeichnung sieht man keinen Unterschied, und es kostet ein Sechzehntel.
