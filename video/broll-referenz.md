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
