# Lernkanal — YouTube Manager

Schlüssel `youtube-manager`, Branch `claude/youtube-manager`.
Anhängen, neuester Eintrag oben. Protokoll: `lernen/KANAL.md` auf Alfreds Branch.

---

## 2026-10-21

### Die Kommentare sind erreichbar — der Irrtum, der Weg, der Preis

- **Der Irrtum war, einen Abbruch als Verbot zu lesen.** Am 20.10. stand in
  `video/youtube-kanal.md`, die Watch-Seite antworte mit *„Sign in to confirm
  you're not a bot"* — also seien Kommentare unerreichbar. Falsch. Die Sperre
  gilt den **Videoformaten**; `yt-dlp` gibt nur auf, *bevor* es den
  Kommentar-Endpunkt überhaupt anfragt. Mit `ignore_no_formats_error: True`
  läuft es weiter und die Kommentare kommen **vollständig**: bei jedem von 14
  geprüften Videos war die Zahl der geholten Kommentare gleich der von YouTube
  gemeldeten `comment_count`. Preis: rund 20 s pro Video, kein Schlüssel, kein
  OAuth. `yt-dlp` ist **nicht vorinstalliert** (`pip install yt-dlp`).
  **Die Regel dahinter: eine Fehlermeldung nennt, was *sie* verweigert, nicht
  was die Schnittstelle verweigert.** Wer die Sackgasse protokolliert, muss
  dazuschreiben, welcher Teilweg geprüft wurde — sonst erbt der nächste eine
  Grenze, die es nicht gibt.
  → betrifft: alle

### Das eigene Erzeugnis als fremdes Signal zählen

- **Seine eigenen angepinnten Kommentare liefen bei mir als „unbeantwortet".**
  Die Zählung „offene Community-Kommentare" nahm jeden Hauptkommentar ohne
  Uploader-Antwort — und sein eigener angepinnter Kommentar ist ein
  Hauptkommentar ohne Antwort. Bei `cMI3tsQp410` ergab das 3 statt 2.
  **Als Regel, nicht als Anekdote: vor jeder Zählung über eine Plattform die
  Zeile streichen, deren Urheber wir selbst sind** — eigene Kommentare, eigene
  Mails im Postausgang, eigene Commits, eigene Karten. Ein Arbeitsvorrat zählt
  nur, was von außen kam.
  → betrifft: alle

### Die Beschreibungen seines Kanals, an 77 Videos gezählt

- **39 von 39 Shorts haben keine Beschreibung.** 38 von 38 langen Videos haben
  eine. 16 haben Timestamps.
  → betrifft: head-of-content, content-*
- **0 von 77 Videos haben Tags.** Gegengeprüft an einem fremden Video über
  denselben Weg: acht Tags kamen zurück, die Auslesung funktioniert. **Die Null
  ist echt, kein Messfehler.**
  → betrifft: head-of-content, thumbnails
- **Seine wörtlichen Formeln**, mit Häufigkeit: `In this episode of Man's Search
  for Meaning, we go far past the highlight reel:` (4×) · `An unfiltered, deeply
  human conversation about …` (4×) · `Here's the timestamps:` (6×) ·
  `Prefer listening on the go? You can find this episode on:` (9×) ·
  `Subscribe for raw, in-person conversations with the wildest and most
  inspiring humans on the planet.` (9×) · `In this episode we explore:` /
  `Expect to learn:` vor Bullet-Blöcken (3×).
  → betrifft: head-of-content, content-*
- **Seine Selbstzensur ist Absicht, kein Tippfehler:** `suic*des` · `su*cide` ·
  `Pen*s` · `vɐgina` · `K*ll`. Ebenso **`wyld`/`wyldest`** (4×, neben `wildest`
  — er ist darin nicht konsistent, also ist beides seins). Nicht wegpolieren.
  → betrifft: alle
- **Angepinnte Kommentare, 14 Belege.** Anreden: `Howdy Savages!` 6× ·
  `Howdy Seekers!` 2× · `Hey Savages!` · `Howdy y'all!` · `Ladies and gents!` ·
  `Cheers ladies and gents,` · `Hey team!` · 2× keine. Der Rumpf ist immer
  `If this clip <moved you|touched you|sparked your curiosity>, the full
  conversation with <Vorname> goes even deeper into <Themen>: 👉 <Link>`.
  → betrifft: content-*, head-of-content

### Der Fundraiser-Einschub sitzt am Ende — soweit belegbar

- **Bei Danny (`20260831`) ist er das letzte Kapitel:** `1:15:22 Help me bring
  Man's Search for Meaning to life`, danach 3:32 bis zum Ende der 78:54-Folge.
  Bei Sutcliffe (`20260930`) liegen 4:30 unbenannt hinter dem letzten Kapitel.
  **Ein Mid-Roll ist in keiner der 16 Folgen mit Timestamps belegt.** Sitzt er am
  Ende, verschiebt er keinen Timestamp; sitzt er in der Mitte, verschiebt er
  jedes Kapitel danach um drei Minuten. **Je Folge prüfen, nicht annehmen.**
  → betrifft: content-*, head-of-content

### Laufzeit einer Drive-Videodatei: 8 MiB statt 895 MB

- **Die Laufzeit steht im `mvhd`-Atom**, bei den Exporten dieses Schnittplatzes
  am **Dateiende**. Letzte 8 MiB per Bereichsanfrage holen, `mvhd` suchen,
  `dauer/timescale` rechnen. `video/werkzeug/laufzeit.py`. Damit ist
  `Scott Aaronson AI God.mp4` als **3:44** gemessen — ein Clip, nicht die Folge,
  ohne 895 MB zu laden.
  **Vorne zuerst suchen, dann hinten:** bei `+faststart` liegt `moov` vorn, bei
  diesen Exporten hinten.
  → betrifft: alle
- **Alfreds Drive-Befund hat in diesem Werkzeug einen Fehler gefunden, bevor er
  auftrat.** „Quota exceeded" kommt als **HTTP 200** mit ~2 kB HTML. Meine erste
  Fassung prüfte nur, ob `<html` in den ersten 200 Bytes steht — eine
  Fehlerseite ohne Doctype am Anfang wäre durchgelaufen und `mvhd` hätte
  gefehlt, was als „kein mvhd gefunden" gemeldet worden wäre statt als
  Tageslimit. Jetzt zählt die **Blocklänge**: wer Megabytes anfordert und
  Kilobytes bekommt, hat eine Fehlerseite. **Bei Drive ist die Länge die
  Wahrheit, nicht der Statuscode.**
  → betrifft: alle

### Was ich vom Head of Content übernommen und an mir korrigiert habe

- **Ich hatte ihm 15 Titel gegeben, alle mit `(4K)` am Ende, und ihm empfohlen,
  den Gastnamen weglassen zu können.** Beides war aus seiner bisherigen Praxis
  abgeleitet statt gemessen. Die 438-Titel-Messung sagt: technischer Tag in 400
  Vorbildtiteln **einmal**, und der zweite Slot (`| <Name>`) kostet nichts,
  während er in 0 von 38 seiner Titel benutzt wird. **Fassung 2 ist umgebaut.**
  **Die Regel: „er macht es so" ist eine Beobachtung, keine Begründung.** Wenn
  ein anderer Agent dieselbe Sache gegen eine Außenreferenz gemessen hat, sticht
  seine Messung meine Nachahmung.
  → betrifft: alle

### Zur Zuständigkeit

- **Thumbnail-*Copy* hat er am 21.10. ausdrücklich bei mir bestellt**, zusammen
  mit den Titeln — die Thumbnail-*Bilder* liegen beim Thumbnail Assistant. Meine
  15 Zeilen doppeln die sechs schon gebauten (`AI/Works/Too Well`,
  `We're The/Orangutans`, `AI Just/Broke/Math`, `Make AI/Love/Humanity`,
  `OpenAI/Insider`, `Human/Extinction?`) **nicht**. Sie stehen in
  `drafts/aaronson/titel-und-thumbnail.md` und folgen `video/thumbnails.md`
  (2–4 Wörter, 2–3 Zeilen, genau ein Kasten `#DF2C00`).
  **Offener Widerspruch, den nur er entscheiden kann:** `thumbnails.md` sagt
  „kein Fragezeichen" (an sechs veröffentlichten gemessen), sein eigener Entwurf
  im Prep-Doc sagt `Human Extinction?!`, und das gebaute Thumbnail trägt
  `Human Extinction?`.
  → betrifft: thumbnails, head-of-content

### Sein Prep-Doc ist der Ausgangspunkt, nicht mein Einfall

- **In `00 YNB Podcast: <Name>` liegt je Folge ein Dokument `09 YNB Podcast:
  <Name>`** mit seinen eigenen Titel- und Thumbnail-Ideen, Fragenliste, Zitaten
  und Inspo-Links. Bei Aaronson waren das fünf Titel und zwei Thumbnail-Zeilen.
  Dazu `YNB Podcast: Promo` mit dem GoFundMe-Text und **seiner eigenen
  Gast-Formel** („quantum physicist & OpenAI insider Prof. Scott Aaronson").
  **Wer das überspringt, erfindet neben ihm her.**
  → betrifft: head-of-content, thumbnails, content-*
- **Die kommenden Folgen, aus `YNB Podcast: In Progress`:** Scott Aaronson,
  Rick Strassman, Matt Defina, Logan Gonzalez, Ken Stern. **Ein „Kyle" ist dort
  nicht** — er hat den Namen am 21.10. genannt, im Drive gibt es keinen Ordner
  dazu.
  → betrifft: alle
