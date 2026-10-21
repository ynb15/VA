# Eine Folge veröffentlichen — was ich liefere, wenn Du es sagst

**Dein Auftrag, 21.10.2026:** *„dass ich dir einfach sage, ich will jetzt den
Podcast mit Kyle oder mit Matt oder mit Rick veröffentlichen und dass du dann
genau weißt, was du mir dann zu liefern hast."*

Also: **Du sagst einen Satz. Ich liefere die Liste unten.** Ohne Rückfragen,
außer bei den zwei Dingen unter „Was ich von Dir brauche" — und auch die frage
ich nicht vorher ab, sondern liefere alles andere und sage dazu, was fehlt.

---

## Das Paket — acht Stücke

| # | Stück | Form |
|---|---|---|
| 1 | **Beschreibung der Folge** | `.txt`, nur die Beschreibung, ein Rutsch Kopieren |
| 2 | **15 Titel** | nach Deinen belegten Formen gruppiert, mit einer Empfehlung |
| 3 | **15 Thumbnail-Zeilen** | 2–4 Wörter, Kasten markiert, mit einer Empfehlung |
| 4 | **Tags** | ~20, als eine Zeile zum Einsetzen |
| 5 | **Angepinnter Kommentar zur Folge** | die Fundraiser-Variante |
| 6 | **Angepinnte Kommentare für jeden Clip** | Anrede + Teaser + Link zur Folge |
| 7 | **Beschreibungen für jeden Clip** | Deine Clip-Form mit der Doppelformel |
| ~~8~~ | ~~Beschreibungen für die Shorts~~ | **gestrichen am 21.10.** — s. unten |

Dazu, ungefragt, wenn mir beim Transkript etwas auffällt: **die drei bis fünf
stärksten Stellen für Clips**, mit Zeitmarke. Kein Konzept, eine Liste.

### Stück 8 ist gestrichen — Short-Beschreibungen

Von ihm am 21.10.2026: *„Ich finde halt die Short-Beschreibung, die ist jetzt
nicht wirklich relevant."*

**Mein Befund dazu war richtig gemessen** — 39 von 39 Shorts haben keine
Beschreibung, und ich hatte ihn als größten einzelnen SEO-Posten des Kanals
gemeldet. **Er hat ihn gehört und anders entschieden.** Die Streichung steht
hier, damit sie niemand als Lücke wieder aufmacht. Die anderen sieben Stücke
bleiben unverändert.

---

## Der Kalender — seit 21.10.2026

Zwei Podcasts im Monat, Hauptfolge **samstags**, dazu täglich ein Content-Stück.
Der Plan liegt auf Alfreds Branch (`plan/README.md`, `plan/kalender.md`,
`plan/ABLAUF.md`); **mein Stichtag ist T−6, der Text.**

| Folge | Veröffentlichung | mein Stichtag |
|---|---|---|
| **Kyle Kingsbury** | Sa 31.10. | **So 25.10.** |
| Scott Aaronson | Sa 14.11. | So 08.11. |
| David Sutcliffe | Sa 28.11. | So 22.11. |
| Matt Defina | Sa 12.12. | So 06.12. |
| Ken Stern | Sa 19.12. | So 13.12. |

**Die Vorlaufkette:** T−10 Transkript · T−8 Auswahl · **T−6 Text (ich)** ·
T−5 Bild · T−3 Shorts · T−2 Paket bei ihm.

**Was das für mich heißt:** das Transkript ist meine Eingangsvoraussetzung und
kommt vom Shorts-Assistenten. **Liegt es an meinem Stichtag nicht vor, melde ich
das, statt zu warten** — Titel und Thumbnail-Copy kann ich aus dem Prep-Doc
bauen, Beschreibung und Timestamps nicht.

---

## Der Ablauf, den ich selbst gehe

### 1. Sein Prep-Doc lesen — **immer zuerst**
Drive: `YNB Podcast: In Progress` → `00 YNB Podcast: <Name>` → das Dokument
`09 YNB Podcast: <Name>`.

Dort stehen **seine eigenen** Titel- und Thumbnail-Ideen, seine Fragenliste, die
Zitate, die ihn interessieren, und seine Inspo-Links. Bei Aaronson waren das
fünf Titel und zwei Thumbnail-Zeilen. **Das ist der Ausgangspunkt, nicht mein
eigener Einfall.** Wer das überspringt, erfindet neben ihm her.

Ebenfalls dort: `YNB Podcast: Promo` (`1qtpoKKjhESeoJHEwYYxkvKLBPYihgXnLDpxDkn8U6e4`)
— der GoFundMe-Text, und darin **seine eigene Gast-Formel** („quantum physicist
& OpenAI insider Prof. Scott Aaronson"). Die nehme ich wörtlich.

### 2. Die Laufzeit der finalen Datei messen
```
python3 video/werkzeug/laufzeit.py <drive-file-id> <fileSize>
```
Liest nur das Dateiende (8 MiB statt 895 MB). Die Datei muss im Drive
link-freigegeben sein.

### 3. Den Versatz rechnen, nicht annehmen
```
veröffentlicht = (Rohzeit − Vorlauf) ÷ Tempo
```
- **Vorlauf** = was vorne abgeschnitten ist. Bei Aaronson 12,2 s, gemessen über
  Lautstärkeverläufe an elf Stellen.
- **Tempo** = sein Export-Faktor, **im Schnitt 1,1** (seine Angabe, 21.10.).
- **Fundraiser-Einschub** = rund 3 Minuten. **Wo er sitzt, entscheidet alles:**
  am Ende verschiebt er nichts, in der Mitte verschiebt er jedes Kapitel danach.

**Die Probe, die das ohne Nachfragen klärt:** Rohdauer, Laufzeit und Vorlauf
gegeneinander rechnen. Bleibt ein Rest von ~3 Minuten übrig, den das
abgeschnittene Ende nicht erklärt, sitzt der Einschub **in der Mitte** — dann
muss ich ihn im Ton suchen. Geht die Rechnung ohne Rest auf, sitzt er am Ende.

**Was dazu gemessen ist (21.10.):** bei Danny (`20260831`) ist der Fundraiser
das **letzte Kapitel** — `1:15:22 Help me bring Man's Search for Meaning to
life`, und danach laufen 3:32 bis zum Ende der Folge. Bei Sutcliffe
(`20260930`) liegen 4:30 hinter dem letzten Kapitel, unbenannt. **Beides passt
auf einen Einschub am Schluss.** Ein Mid-Roll ist in keiner der 16 Folgen mit
Timestamps belegt — aber „nicht belegt" ist nicht „ausgeschlossen", und bei
drei Minuten Versatz prüfe ich das je Folge neu.

### 4. Timestamps bauen
Aus dem Transkript, in **veröffentlichter Zeit**. Rund 20 Kapitel, seine
Kapitelsprache: konkret, oft erste Person, oft ein Zitat. Letztes Kapitel fast
immer `What makes life meaningful?`. Wenn der Fundraiser am Ende sitzt, bekommt
er ein eigenes letztes Kapitel — so wie bei Danny.

### 5. Entwerfen, nach den Mustern
- Beschreibung: `youtube/beschreibungen.md`
- Angepinnte Kommentare: `youtube/clip-kommentar.md`
- Thumbnail-Regeln: `video/thumbnails.md`
- Seine Stimme: `voice/german-register.md`, `voice/en-podcast-outreach.md`

### 6. Ablegen und sagen, was fehlt
`drafts/<name>/` — die `.txt` nur mit dem Einsetztext, daneben eine
`LIESMICH.md` mit Begründungen und den offenen Punkten.

### 7. Nichts senden
Kein Upload, kein Pinnen, keine Antwort in seinem Namen. **Seine Regel vom
21.10.: Agenten entwerfen.**

---

## Der Aufbau der Beschreibung — von ihm am 21.10. festgelegt

```
Absatz 1   eine catchy, provokative Frage
Absatz 2   den Gast vorstellen
Absatz 3   den Inhalt anteasern
           maximal 5 Bullet Points, einzeilig
           An unfiltered, deeply human conversation about …
           Get in touch with <Vorname>:
           Here's the timestamps:
           Prefer listening on the go? …
```

**Absatz 3 und 4 der alten Form (die Wende, die Nerven-Passage) gehören nicht
hinein** — ausdrücklich von ihm, 21.10. Was dort stünde, geht in Absatz 3 oder
in ein Kapitel.

---

## Was ich von Dir brauche — zwei Zahlen und drei Links

Immer dieselben. Wenn sie fehlen, liefere ich trotzdem und markiere die Lücke.

1. **Die Laufzeit des fertigen Uploads** — oder die finale Datei link-freigegeben
   im Drive, dann messe ich sie selbst.
2. **Wo der Fundraiser-Einschub sitzt**, falls er nicht am Ende sitzt.
3. **Gast-Links** und, falls vorhanden, sein YouTube-`@handle`. Ich erfinde
   keinen.
4. **Spotify- und Apple-Episodenlink.**
5. **Die Schriftdatei**, falls Thumbnails gebaut werden sollen — die fehlt im
   Container seit dem 20.10.

---

## Die harten Grenzen, damit sie nicht jedes Mal neu verhandelt werden

- **In YouTube schreiben geht nicht.** Kein Connector, kein OAuth. Lesen ohne
  Anmeldung ja (Titel, Abrufe, Beschreibungen, Kommentare, Thumbnails), schreiben
  nein. Dafür braucht es die YouTube Data API v3 mit einem OAuth-Client auf
  `youtube.force-ssl` — das Google-Cloud-Projekt vom 19./20.10.
- **Drive und Trello: lesen ja, schreiben nein.** Notion schreiben ja.
- **Die Mediendaten eines veröffentlichten Videos** sind nicht abrufbar (403).
  Thumbnails und automatische Untertitel schon.
- **Zwei Zahlen sind Messwerte, keine Bewertung:** Abrufe und Abos. Die berichte
  ich nackt und ohne Deutung.

---

## Die kommenden Folgen, aus dem Drive gelesen (21.10.2026)

In `YNB Podcast: In Progress`:

| Ordner | angelegt |
|---|---|
| `00 YNB Podcast: Scott Aaronson` | 27.08. |
| `00 YNB Podcast: Rick Strassman` | 29.09. |
| `00 YNB Podcast: Matt Defina` | 04.09. |
| `00 YNB Podcast: Logan Gonzalez` | 10.10. |
| `00 YNB Podcast: Ken Stern` | 15.09. |

**„Kyle" ist dort nicht dabei.** In `voice/blindtest/` steht ein Kyle als
Mail-Korrespondenz, kein Podcast-Ordner. Wenn Du „Kyle" sagst, frage ich
einmal nach, wer gemeint ist — das ist der eine Fall, in dem Raten teurer wäre
als die Frage.
