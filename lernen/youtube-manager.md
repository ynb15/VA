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

### Nachtrag 21.10., nachmittags — zur Arbeitsteilung mit dem Head of Content

- **Die 38 Beschreibungen sind schon gemessen. Er muss nur die 400 ziehen.**
  `video/titel-regeln.md` §H sagt, zu Beschreibungen sei nichts gemessen, weil
  `--flat-playlist` sie nicht liefert, und bietet an, „die 38 und die 400"
  nachzuziehen. **Die 38 liegen fertig in `youtube/beschreibungen.md`** —
  Bauplan, Häufigkeiten seiner wörtlichen Formeln, Selbstzensur, Timestamp-Form,
  und die zwei Nullen (39 Shorts ohne Beschreibung, 0 von 77 mit Tags). Der Weg
  dorthin steht in `video/youtube-kanal.md`: `getcomments` plus
  `ignore_no_formats_error`, rund 20 s je Video, kein Schlüssel.
  **Wer die 400 Vorbildbeschreibungen zieht, braucht denselben Schalter** — ohne
  ihn bricht `yt-dlp` an der Bot-Prüfung ab, bevor es die Beschreibung hat.
  → betrifft: head-of-content

- **Sein Widerspruch zwischen §B und §C, und wie ich ihn aufgelöst habe.**
  §B verlangt 45–65 Zeichen, §C zeigt als Vorbild einen DOAC-Titel mit **71**
  und einen mit **92**; DOACs Median ist 77,5. Beides gilt nicht gleichzeitig.
  Meine Auflösung: **die 45–65 auf Slot 1 beziehen**, den Teil vor dem `|`.
  Damit liegen 14 von 15 Aaronson-Titeln im Fenster und die vollen Titel bei
  65–79. **Das ist meine Entscheidung, nicht seine Regel** — falls er es anders
  meint, korrigiert er mich, und dann fällt der zweite Slot weg.
  → betrifft: head-of-content, thumbnails

- **Die Thumbnail-Regel, die meine 15 Zeilen schwächer macht, als sie sein
  müssten.** §G: die Copy wiederholt den Titel nicht, und **das Konfliktpaar ist
  seine Form** (`Patriarchy over Feminism`). Meine 15 waren fast alle
  Behauptungen. Fünf Paare nachgetragen (`QUANTUM to GOD`, `PARROT or GOD`,
  `HUMANS to ORANGUTANS`, `PHYSICS to PRAYER`, `MATH vs MEANING`).
  **Als Regel: wer Copy in zwei Feldern schreibt, muss prüfen, ob das zweite das
  erste wiederholt** — bei Titel und Thumbnail ist Arbeitsteilung die Form, nicht
  Redundanz.
  → betrifft: thumbnails, content-*

### Nachtrag 21.10., spät — zwei Zahlen aus dem Kanal waren falsch, von ihm korrigiert

- **„Mansons `…, Solved` ist ein Serienkunstgriff" — nein, es ist sein
  Podcastname.** Nachgeprüft: der Podcast heißt **„SOLVED with Mark Manson"**
  (Apple Podcasts, id1247526593). Dass `…, Solved` in 21 von 100 Titeln steht,
  ist derselbe Effekt wie „Jay Shetty" in 53 von 100 — **der Showname, keine
  Betonung und kein Format.** Yannick hat es sofort gesehen: *„Das ist sein
  Podcast. So heißt sein Podcast."*
  **Die Falle steht in `video/titel-regeln.md` §E selbst beschrieben** und wurde
  im gleichen Dokument ein zweites Mal betreten. **Regel: ein wiederkehrendes
  Titelwort ist erst ein Kunstgriff, wenn es nicht der Name der Show ist — und
  das kostet eine Suche, keine Messung.**
  → betrifft: head-of-content, youtube-manager, thumbnails

- **„Gastname hinten in 0 von 38" ist falsch. Es sind 3.** Nachgezählt an den
  38 Titeln: `– Millionaire Rob Paddock (8K)` · `- Nathan Maingard (8K)` ·
  `Why Kids Should Be Allowed Trans Surgery – Dr. Curtis Crane`. Ein vierter
  trägt den Namen in der Mitte (`77 y/o Techno DJ Rob Bennett`). **Vier von 38
  enthalten überhaupt einen Gastnamen.** Ich habe die Null zweimal an ihn
  weitergegeben, ohne sie nachzuzählen — **eine Zahl aus dem Kanal ist ein
  Befund, keine Messung; wer sie weitergibt, prüft sie an den eigenen Daten.**
  → betrifft: alle

- **Seine Namensregel, seit Jahren, wörtlich von ihm am 21.10.:** *„nur die
  Namen können wir nur verwenden, wenn die wirklich weltweit global bekannt
  sind."* Beispiele von ihm: Christopher Nolan, Donald Trump. Für alle anderen
  **die Rolle**, weil sie zieht: *„America's #1 Transgender Doctor hat natürlich
  viel mehr Pull, viel mehr Attraktivität als Curtis Crane."* Selbst bei Steven
  Bartlett wäre **„Diary of a CEO"** das stärkere Wort.
  **Damit ist die Empfehlung „der zweite Slot für den Gastnamen kostet nichts"
  gegenstandslos** — rechnerisch stimmt sie, aber sie füllt den Slot mit einem
  Namen, den niemand sucht. Der Name gehört in Beschreibung und Tags, nicht in
  den Titel. **Bekannt im eigenen Fach ist nicht global bekannt** (Scott
  Aaronson).
  → betrifft: head-of-content, thumbnails, content-*

- **Keine Schablone von einem Vorbildkanal.** Wörtlich: *„ich will die nicht
  kopieren. Oder so eine Schablone mir abschauen von Diary of a CEO, sondern
  eher das als Inspiration sehen. Und immer wieder punktuell entscheiden."*
  Konkret zur Dreier-Aufzählung: **dass DOAC sie nicht benutzt, ist kein Verbot
  für ihn.** Ich hatte sie in meiner Fassung 3 ganz gestrichen — das war
  Schablonendenken und ist zurückgenommen.
  **Regel: eine Messung an einem Vorbildkanal beschreibt den Vorbildkanal.
  Sie wird erst durch seine Zustimmung eine Regel für ihn.**
  → betrifft: alle

- **Sein Serienformat-Fund ist erledigt.** *„ich plane jetzt nicht, eine Serie
  fortzusetzen mit Applications."* Der Grund dahinter, und er ordnet die
  Prioritäten: *„idealerweise will ich meinen Podcast so schnell, so groß
  aufziehen, dass ich für niemanden anderen mehr arbeiten muss."*
  **Keine vierte `This Is My Application` titeln.**
  → betrifft: head-of-content

### Nachtrag 21.10., 10:30 — Jack Neel nachgemessen, und ein erfundenes Zitat in meinem eigenen Titel

- **Jack Neel ist verifiziert**, selbst gemessen statt übernommen: `@jackneel`,
  `UCFRCiFkWWJN2rO6dsKU9-1A`, **3.520.000 Abos**, 100 Titel. **58 mit Zitat, 50
  davon als Ruf mit Ausrufezeichen im Zitat.** Länge Median 86, 7 bei genau 100.
  Du 19 %, Ich/Wir 25 %. Die Zahlen des Head of Content halten; Abweichungen nur
  im Rundungsbereich (er: 18/27, Median 85,5).
  **Das ist der Name, der im Auftrag als „kein Kanal dieses Namens verifiziert"
  stand.** Jetzt ist er es.
  → betrifft: head-of-content, thumbnails, content-*

- **Neels zweiter Slot trägt 21× die eigene Marke und 27× einen anderen Namen —
  und diese Namen sind Alex Hormozi, Rhonda Patrick, Robert Pape.** Also global
  bekannte. **Yannicks Namensregel wird von Neels Daten gestützt, nicht
  widerlegt.** Und der Slot hat eine zweite Verwendung, die bei Yannick frei ist:
  die eigene Marke (`│ Man's Search for Meaning`).
  → betrifft: head-of-content, thumbnails

- **Ich hatte ein erfundenes Zitat in meinem empfohlenen Titel.**
  `"The Trouble With AI Is That It Does Work"` — Aaronson sagt *„The trouble with
  AI right now is **not** that it doesn't work. It's that it does work."* Meine
  Fassung verschmolz zwei Sätze zu einem. Ebenso `"We Are The Orangutans Now"`
  aus einer früheren Fassung: er sagt *„it will be to us, as we are to
  orangutans"*.
  **Regel: ein Zitat in Anführungszeichen wird vor dem Ablegen mit einer
  Zeichenkettensuche gegen das Transkript geprüft, nie aus dem Gedächtnis. Eine
  Behauptung ohne Anführungszeichen darf verkürzen; eine mit nicht.** Das gilt
  für Titel, Thumbnail-Copy, Beschreibungen und Kapitelzeilen gleichermaßen —
  überall, wo wir ihm Worte in den Mund legen, die er veröffentlichen soll.
  → betrifft: alle

- **Die Ruf-Form passt nicht zu jedem Gast, und das Ausrufezeichen ist keine
  Messung.** Es steht nicht im Ton; es ist eine Behauptung über den Vortrag.
  Aaronson sagt seine härtesten Sätze leise und mit Einschränkungen davor. Bei
  Neel trägt die Form nachweislich (50 von 100) — **ob sie bei einem leisen Gast
  trägt, steht in keiner Zahl.** Als Einschätzung gekennzeichnet, nicht als Regel.
  → betrifft: head-of-content, thumbnails

### Nachtrag 21.10., 10:45 — drei Korrekturen von ihm an meiner Titelarbeit

- **Paraphrasieren in Anführungszeichen ist erlaubt. Seine Entscheidung,
  wörtlich:** *„wir können gerne paraphrasieren, wenn es zu Zitaten kommt."*
  **Damit ist die Regel aus `video/titel-regeln.md` („ein Zitat, das in der
  Aufnahme nicht vorkommt, ist eine Erfindung") für seinen Kanal aufgehoben.**
  Was bleibt: **jede Paraphrase muss auf einer belegten Stelle stehen**, und die
  Stelle gehört neben den Entwurf. Erfunden ist nicht paraphrasiert.
  **Die Regel dahinter, die mich das gekostet hat:** eine Messung an fremden
  Kanälen wird erst durch seine Zustimmung eine Regel für ihn — ich hatte das
  selbst notiert und dann doch eine fremde Regel über seinen Entwurf gestellt.
  → betrifft: head-of-content, thumbnails, content-*

- **„Wörtlich" ist kein Qualitätskriterium für einen Titel.** Ich habe
  `"I'm still thinking about that"` und `"It's that it does work"` empfohlen,
  weil sie die Zitatprüfung bestanden. Seine Antwort: *„Die sind richtig schwach,
  richtig schwach."* **Er hat recht** — aus dem Zusammenhang gerissen sagen beide
  nichts. **Die Prüfung schließt Titel aus, sie wählt keine aus.** Erst
  auswählen, was zieht, dann prüfen, worauf es steht.
  → betrifft: alle

- **„Deutlich provokativer schreiben."** Stehender Auftrag für Titel,
  Thumbnail-Copy und Clip-Texte. Für mich heißt das konkret: der Titel verspricht
  die härteste Aussage, die in der Folge wirklich vorkommt — nicht die
  korrekteste. Die Einordnung („er relativiert das danach") gehört in die
  Beschreibung und in mein Begleitblatt, **nicht in den Titel.**
  → betrifft: head-of-content, thumbnails, content-*

- **Fachbegriffe erklären, bevor ich sie benutze.** Ich habe „Du-Ansprache"
  dreimal in Berichten verwendet; seine Rückmeldung: *„ich weiß nicht ganz genau,
  was du die ganze Zeit mit der Du-Ansprache meinst."* Es heißt nur: steht
  `you`/`your` im Titel. **Er hat uns nicht onboardet — unsere Messgrößen sind
  ihm nicht bekannt, nur weil sie unter uns eingeführt sind.** Einmal in einer
  Zeile erklären, mit einem Beispiel aus seinem eigenen Material.
  → betrifft: alle

### Nachtrag 21.10., 11:00 — der Suchausschnitt ist nicht das Dokument

- **Ich habe seine Prep-Dokumente nicht gelesen, sondern einen Suchausschnitt.**
  Auf seine Frage, ob ich seine Podcast-Dokumente durchgegangen bin, war die
  Antwort nein: ich hatte **ein** Dokument gesehen (Aaronson) und davon nur das
  `contentSnippet` aus der Drive-Suche, das nach rund 2.000 Zeichen abbricht.
  **Die Hälfte seiner Titelliste stand nicht darin.**
  **Regel: `contentSnippet` ist ein Abschnitt, kein Dokument.** Wer darauf
  aufbaut, muss es sagen — oder das Dokument lesen.
  → betrifft: alle

- **Ich habe ihm seine eigene Zeile als meine vorgelegt.**
  `We're Building God & Nobody Is Ready` steht wörtlich in seinem Scott-Dokument,
  zweimal (unter *Title* und unter *Thumbnail*). Ich habe sie als meinen
  Titelvorschlag präsentiert. Ebenso `The End of Humanity`, das er heute als
  Thumbnail „bestellt" hat — **es stand schon in seiner Datei.**
  **Regel: wenn eine Zeile aus seinem Material kommt, steht das dabei.** Ein
  Vorschlag, der ihm seine eigene Idee zurückgibt, kostet ihn eine Runde und
  verschleiert, was wirklich von uns ist.
  → betrifft: head-of-content, thumbnails, content-*

- **Sein Titelbau ist zweispaltig, und die Dokumente zeigen es.** Spalte A ist
  die Rolle mit Doppelpunkt (`The #1 Quantum Expert:`, `OpenAI Insider:`,
  `Hollywood Star turned Men's Therapist:`, `The $100M IronMan Founder:`).
  Spalte B ist entweder ein **Themen-Dreier mit `&`** (`Andrew Tate, Manosphere &
  God` · `Segregation, Whiteness & Male Violence` · `ChatGPT/Judaism, God & The
  End of Humanity`) oder eine **Versalien-Behauptung** (`NOBODY Knows If AI Is
  Actually Safe!` · `Everything You've Heard About Quantum Computers Is WRONG`).
  **Der Dreier steht in drei von vier Dokumenten mit B-Spalte — er ist seine
  Signatur**, und ihn nach dem Vorbild von Diary of a CEO zu streichen war
  falsch. Sein Widerspruch von heute hat jetzt seinen Beleg.
  → betrifft: head-of-content, thumbnails, content-*

- **Seine Thumbnail-Braindumps sind deutlich härter als seine Titel — das ist
  die Antwort auf „provokativer schreiben", und sie ist von ihm.**
  `Feminists are just ugly` · `Patriarchy is GREAT!` · `Women Are Just HOT` ·
  `Racism Is Just DUMB` · `The Nazis Never Left` · `Nobody Talks About This` ·
  `We Need A Matriarchy` · `Human Extinction?!`
  Drei wiederkehrende Formen: **das „Nobody"-Motiv** (in vier von vier
  Dokumenten, seine häufigste einzelne Bewegung), **`X Is Just Y`** als
  Abwertung in drei Wörtern, und **der nackte Zustandssatz**
  (`Segregation Still Exists`).
  → betrifft: thumbnails, head-of-content, content-*

- **Das Fragezeichen im Thumbnail ist entschieden, von ihm selbst.**
  `Human Extinction?!` steht wörtlich in seinem Dokument. `video/thumbnails.md`
  sagt „kein Fragezeichen" — **das ist an sechs veröffentlichten gemessen und
  beschreibt, was durchgekommen ist, nicht was er will.** Ich hatte den
  Widerspruch als offene Frage an ihn zurückgegeben; die Antwort lag in seiner
  eigenen Datei.
  **Regel: bevor ich ihm eine Entscheidung zurückgebe, in seinem Material
  nachsehen, ob er sie längst getroffen hat.**
  → betrifft: alle
