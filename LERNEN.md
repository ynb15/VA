# LERNEN — das gemeinsame Gedächtnis des Teams

Wie der Kanal funktioniert: `lernen/KANAL.md`. Kurzform: Du schreibst nach
`lernen/<dein-schlüssel>.md` auf Deinem Branch, Du liest **diese** Datei am
Anfang jedes Arbeitsblocks:

```
git fetch origin claude/ai-chief-of-staff-cz83jv
git show origin/claude/ai-chief-of-staff-cz83jv:LERNEN.md
```

Alfred sammelt zweimal täglich (06:40 und 15:54 Kapstadt) und schreibt hier
zusammen. Neueste Ausgabe oben.

---

## STEHT ÜBER ALLEM — gilt für jeden Agenten, jeden Tag

Diese vier sind keine Befunde, sondern Bedingungen. Sie stehen hier, damit kein
Agent sie je nur aus zweiter Hand kennt.

1. **Nichts geht raus.** Keine Mail, kein Slack, keine Nachricht, kein Upload,
   kein Kommentar — weder selbst noch in seinem Namen. Er hat das am 26.08.
   gesagt und am **21.10. wörtlich bestätigt: „Regel bleibt, Agenten
   entwerfen."** Entwerfen, übergeben, er schickt.
2. **Er hat uns nicht onboardet.** Ihm nicht erklären, was seine Prioritäten
   sind. Weniger Karten, weniger Alarme, kein Drängen. Und kennzeichnen, welcher
   Teil einer Aussage Schlussfolgerung ist und welcher Messung.
3. **Deutsch rein, deutsch raus.** Er wechselt mitten im Thread. Entwürfe in der
   Sprache des Entwurfs, nicht in der Sprache des Werkzeugs.
4. **Nur auf den eigenen Branch schreiben.** Fremde Branches liest man, man
   schreibt sie nicht. Kein PR ohne ausdrückliche Bitte. Kein Modellname in
   irgendetwas Gepushtem.

5. **„Weicht ab", nie „wirkt besser."** Ein Formvergleich ist keine
   Wirkungsmessung. Bei 38 eigenen Videos, 8 davon ohne öffentliche Aufrufzahl,
   und ohne Klickrate und Impressionen ist jede Korrelation Form↔Reichweite
   Zufall. Wer eine gemessene Abweichung als Verbesserung weitergibt, verkauft
   ihm eine Behauptung als Befund. Gilt für Titel, Thumbnails, Schnitt, Ton.
6. **Eine Aussage über ihn braucht mehr als eine Plattform als Grundlage.** Der
   Head of Content schrieb am 21.10., ihm fehle ein Serienformat — er hat eins
   („This Is My Application", dreimal, zwei Plattformen), es kommt auf YouTube
   nur einmal vor. **Der Fehler war methodisch, nicht inhaltlich:** eine
   Plattform gemessen, über die Person geschlossen.

---

## Ausgabe 6 — 21.10.2026, 14:30 Kapstadt · ein totes Werkzeug und ein geteilter Renderer

- **`video/yt-transkript.py` holt keine Videos mehr — YouTube sperrt diesen
  Container aus.** Gemessen vom Gastauftritte-Agenten an `q3_kLgYIXGQ`:
  `yt-dlp` meldet über **sechs** Player-Clients *„Sign in to confirm you're not
  a bot"*, die Videoseite liefert `playabilityStatus: LOGIN_REQUIRED`, und ein
  echter Chromium landet auf `google.com/sorry/index`, also auf einem CAPTCHA.
  **Das ist eine IP-Sperre, keine Freigabefrage** — `youtube.com` ist im Proxy
  erlaubt (HTTP 200), und `google.com` freizuschalten hilft nicht, weil
  dahinter das CAPTCHA steht. **Die Dokumentation vom 19.10. („geht ohne
  Schlüssel") gilt nicht mehr.**
  **Wichtig für die Einordnung:** Metadaten gehen weiter. Der Head of Content
  hat am 21.10. mit `yt-dlp --flat-playlist -J` Titel, IDs und Abozahlen
  geholt — **das ist etwas anderes als eine Videodatei.** Und der Rückfallweg
  über `ytInitialData` liefert weiterhin Kapitel und Beschreibung.
  **Wer ein fremdes Video braucht, braucht es von ihm**, nicht aus dem Netz.
  → betrifft: alle
- **`shorts-render.py` ist wieder auseinandergelaufen, und zwar in beide
  Richtungen.** Heute gezählt: `claude/content-assistant` hat das Preset
  (Inter Black, `#F9F13A`) und **kein** `--kopfzeile`;
  `claude/ai-chief-of-staff-cz83jv` hat `--kopfzeile` (6 Fundstellen) und
  **kein** Preset; `claude/content-cinematic` hat **keines von beidem**.
  **Keine Fassung ist die vollständige.** Das ist dasselbe Muster wie am
  20.10., als der Content-Assistant-Zweig zusammengeführt werden musste.
  **Gemeinsames Werkzeug gehört einem Branch** — hier dem Shorts-Assistenten.
  Wer eine Erweiterung baut, bringt sie dorthin zurück, bevor er weiterarbeitet.
  → betrifft: content-*
- **Playwright/Chromium laufen in diesen Containern nur mit absolutem
  ESM-Importpfad und ausdrücklichem `proxy:`-Argument.**
  → betrifft: alle

---

## Ausgabe 5 — 21.10.2026, 14:05 Kapstadt · ein Auftrag, der nicht von ihm kam

**Mein Fehler, und er gehört in den Kanal, weil er jedem von uns passieren
kann.** Ich habe dem Thumbnail-Assistenten einen Auftrag geschickt, überschrieben
mit **„AUFTRAG VON YANNICK, gerade eben"** — ein Thumbnail für das
Sutcliffe-Stück *„What makes life meaningful?"*. Er hat drei Fassungen gebaut.

**Yannick hatte kein Thumbnail bestellt, sondern ein Short.** Seine Worte, über
den Thumbnail-Assistenten zurückgemeldet: *„Ich habe nie gesagt, dass ich ein
Thumbnail von David Sutcliffe will, sondern ein Short. Was zur Hölle? Das gehört
hier überhaupt nicht hin. Ein Riesenfehler."*

- **In einem Auftrag stehen seine Worte wörtlich und in Anführungszeichen.
  Alles andere wird als das gekennzeichnet, was es ist** — „Vorschlag von mir",
  „abgeleitet aus dem Kalender", „meine Schlussfolgerung". **Ein Agent kann das
  nicht nachprüfen:** steht „Auftrag von Yannick" darüber, glaubt er es, und
  das zu Recht. Jetzt Regel 8 in `plan/ABLAUF.md`.
  → betrifft: alle
- **Wer ein Wort als unzuverlässig erkannt hat, darf es im selben Absatz nicht
  als Beleg nehmen.** In derselben Nachricht hatte er ein fertiges **Video**
  „ein fertiges Thumbnail" genannt. **Ich habe das bemerkt und
  richtiggestellt** — und zwei Sätze später dasselbe Wort wieder wörtlich
  genommen. Der Gegenbeleg lag vor mir, ich habe ihn nicht auf den zweiten Satz
  angewendet. Dieselbe Form wie der Lautheitsfehler vom 20.10.
  → betrifft: alle
- **Ist seine Formulierung mehrdeutig, wird gefragt, nicht ausgelegt.** Eine
  Rückfrage kostet eine Minute; ein falsch verstandener Auftrag kostet einen
  Arbeitstag und das Vertrauen des Agenten in jeden weiteren Auftrag.
  → betrifft: alle
- **Die Gegenregel des Thumbnail-Assistenten ist richtig und gilt für jeden:**
  ein Auftrag, der im eigenen Gespräch mit ihm nicht vorkommt, wird bei ihm
  rückgefragt, bevor gebaut wird — **auch wenn die geplante Aufgabe ihn als
  seinen ausweist.**
  → betrifft: alle
- **Das Kingsbury-Thumbnail entfällt.** Seine Anweisung vom 21.10.: *„das Kyle
  Kingsbury Thumbnail, das lasse ich jetzt von ChatGPT machen."* Stichtag T−5
  am 26.10. ist gestrichen, `bin/plan-pruefen.py` kennt die Ausnahme. **Nicht
  daran bauen, und am 26.10. nicht darauf warten.**
  → betrifft: thumbnails, youtube-manager

---

## Ausgabe 4 — 21.10.2026, 13:25 Kapstadt · sein Preset schlägt unsere Messung

Der Shorts-Assistent hat Isabelles Preset eingebaut (`video/preset-ynb.md` auf
`claude/content-assistant`, Commit `1e155d4`). Nachgeprüft, es stimmt.

- **Sechs Stilwerte, von uns an seinen veröffentlichten Shorts abgelesen, waren
  falsch.** Schrift **Inter Black** (nicht DejaVu Sans Bold) · Größe **82**
  (nicht 78) · Gelb **`#F9F13A`** (nicht `#FFD530`) · Zeilenbreite **72 % der
  Bildbreite** (nicht 1000 px fest) · Logo **28 % breit** auf Höhe **0,87**
  (nicht 520 px / 0,845) · Gradation **entsättigt-kühl** (nicht warm).
  **Die Regel daraus, und sie gilt für jedes Fach:** an Ausgabebildern
  abgelesene Stilwerte sind ein **Notbehelf, bis die Quelldatei da ist**.
  **Erst nach der Vorlage fragen, dann messen** — nicht umgekehrt. Eine
  Messung am Ergebnis trifft das Ergebnis, nicht die Absicht.
  → betrifft: alle
- **Das trifft den Thumbnail-Bauplan mit derselben Wucht.** `video/thumbnails.md`
  ist vollständig an sechs veröffentlichten Thumbnails abgelesen — gleiche
  Methode, gleiches Risiko. **Und dieselbe Person baut sie**: Isabelle Semler
  macht Shorts *und* Thumbnails. Bevor dort weiter gemessen wird, muss nach der
  Vorlage gefragt werden.
  → betrifft: thumbnails, head-of-content
- **Wer libass benutzt, darf die Zeilenbreite nicht roh mit PIL messen.**
  libass legt die Schriftgröße auf Ober- plus Unterlänge (Inter Black:
  1,21 Geviert), Faktor `groesse / sum(font.getmetrics()) = 0,82`. Gemessen am
  gerenderten Bild: `WHAT MAKES LIFE` ist bei 82 px **643 px** breit, PIL sagt
  **776**. Ohne die Korrektur misst der Umbruch **21 % zu breit** und trennt
  Zeilen, die längst passen.
  → betrifft: content-*, thumbnails
- **Die Untertitelhöhe hängt am Raum, jetzt mit drei Messpunkten:** **50 %** bei
  Rick Strassman (Webcam) · **57 %** im Just-Push-Record-Studio · **70 %** als
  Vorgabe, wenn keine Lippe gemessen ist. Und: **die gemessene Lippe schlägt
  die Vorgabe** — seine Ansage vom 21.10., *„dass der Text nicht direkt unter
  seiner Lippe ist"*.
  → betrifft: alle Content-Agenten
- **Offen und nur von ihm zu lösen: `luts/ynb_look.png` fehlt.** In der
  Übergabe lagen nur `make_lut.py` und die Anleitung. Solange die Datei fehlt,
  läuft eine **Annäherung statt seines Filters**, und der Renderer schreibt das
  ehrlich in die Ausgabe (`Look: Annaeherung (LUT ... fehlt)`).
  → betrifft: content-*

---

## Ausgabe 3 — 21.10.2026, 13:10 Kapstadt · Slack, erster Durchgang

Sein Arbeits-Slack ist **`team-ynb.slack.com`** und war nie gelesen — auf seine
eigene Regel vom 02.10. Er hat sie heute aufgehoben. Voller Befund:
`video/slack-befunde.md`. Was davon jeden betrifft:

- **KEIN SHORT DARF VERRATEN, WO ER WOHNT.** Am 02.09. zu seiner Cutterin:
  *„Vielleicht doch den Scarborough-Teil rausnehmen in diesem Short? Gewisse
  Menschen müssen nicht so easy wissen wo wir wohnen."* **Das gilt für Bild,
  Ton und Untertitel** — Straßennamen, Viertel, erkennbare Fassaden, Aussicht,
  Schilder. Es stand bisher in keinem Werkzeug und in keiner Prüfliste.
  **Ab sofort Teil jeder Short- und Clip-Abnahme.** Im Zweifel rausschneiden
  und ihm sagen, dass und warum.
  → betrifft: alle
- **Es gibt ein geschriebenes Short-Regelwerk, das wir nie gelesen haben.**
  Am 05.09. schickte er seiner Cutterin ein *„Short-Form Cheat Sheet"* und das
  Notion-Dokument *„Short-form editing guide for friends of Dan and Matt"*.
  **Vermutlich die wichtigste einzelne Quelle in diesem Slack** — und in keinem
  unserer Werkzeuge berücksichtigt. Wer daran arbeitet, bevor ich es gelesen
  habe, baut womöglich gegen eine Regel, die er längst gesetzt hat.
  → betrifft: content-*, thumbnails
- **Tempo 1,1 ist seine Anweisung, keine Eigenart der Dateien.** 14.09.:
  *„Kannst du das letzte und alle kommenden Shorts für ihn nicht up-pacen —
  oder zumindest auf 1,1?"* Deckt sich mit dem gemessenen Export-Faktor.
  → betrifft: alle Content-Agenten
- **Er schreibt Short-Stellen im Format Zeitmarke + Stichwort heraus.**
  *„16:00 Movie · 40:40 Joe Hudson · 41:00 Integration · 44:00 Workaholism ·
  1:00:23 Hormozi · 1:06:00 Confidence · 1:21:00 My Why."*
  **Unsere Kandidatenlisten sollten genauso aussehen** — das ist das Format,
  in dem er denkt.
  **Zu welchem Video die Liste gehört, ist offen.** Gemessen: die Liste steht
  in der DM an Isabelle am **15.09. um 17:01**; der Link zum
  Garden-Gastauftritt (`q3_kLgYIXGQ`) steht am **14.09. um 22:20** — und die
  beiden liegen in **verschiedenen Threads** derselben DM. Der
  Gastauftritte-Agent hält die Liste für die Auswahl zu genau diesem Video und
  stützt das auf die Kapitel (`1:21:00 My Why` ↔ `1:19:07 His why…`); **seine
  Datierung („14.09. 22:20, direkt nach dem Link") stimmt nicht.** Die
  Kapitelprobe kann trotzdem richtig sein. **Wer die Liste benutzt, prüft sie
  erst gegen die Kapitel des Videos** — und behauptet die Zuordnung nicht,
  bevor das steht.
  → betrifft: content-*, head-of-content
- **Modern Wisdom ist seit mindestens 12.10. sein erklärtes Vorbild**, mit drei
  verlinkten Shorts an seinen Editor. Die Kopfzeile von heute liegt also auf
  einer Linie, die er selbst gezogen hat — nicht auf einer, die wir geraten
  haben.
  → betrifft: content-*, thumbnails
- **Ein Widerspruch, den nur er auflösen kann: kommerzielle Musik.** Im
  Preset-Ordner seiner Cutterin liegt *David Kushner – Daylight*, und er bittet
  um mehr. **Gemessen** ist die Datei; **geschlossen** (nicht gemessen) ist,
  dass sein Short-Ablauf kommerzielle Musik nutzt. Das widerspricht der Regel
  in meinem Handbuch („keine Musik aus dem Netz für etwas, das er
  veröffentlicht"). Die Regel galt für **uns** — damit wir nicht eigenmächtig
  Musik beschaffen —, und sie bleibt für uns bestehen. **Seine eigene Praxis
  ist seine Entscheidung.** Nicht eigenmächtig Musik unter ein Stück legen, und
  ihn nicht dafür belehren.
  → betrifft: alle

---

## Ausgabe 2 — 21.10.2026, 12:05 Kapstadt

Erste eingesammelte Ausgabe. Quelle: `lernen/head-of-content.md` auf
`claude/head-of-content` — dort stehen alle Belege und Zahlen im Volltext, hier
nur, was über das Fach hinausgeht. Der Head of Content hat `thumbnails` und
`youtube-manager` bereits selbst angeschrieben; nicht doppelt verteilen.

### Titel und Copy — die anwendbare Fassung ist `video/titel-regeln.md`
- **Die Vorbildkanäle sprechen den Zuschauer an, seine Titel sprechen von ihm.**
  Du-Ansprache in den letzten 100 Titeln: Shetty 55 %, Manson 49 %, DOAC 41 %,
  Williamson 14 % — **seine eigenen 38 langen Videos 13 %**. Ich/Wir dagegen
  **bei ihm 36 %**, mehr als jeder Vorbildkanal. Williamson kommt mit 14 % aus,
  weil in **52 %** seiner Titel ein Name steht, der allein zieht — wer solche
  Namen nicht hat, hat die Position nicht. **Das ist eine Abweichung, keine
  Empfehlung** (siehe Regel 5 oben), und ein Teil davon ist seine Entscheidung:
  in seinen eigenen Entwürfen trennt er die Register pro Plattform schriftlich
  und hat eine Titelfassung eigenhändig `(YT only)` markiert.
  → betrifft: youtube-manager, thumbnails, content-*
- **Der zweite Titel-Slot kostet nichts und er benutzt ihn nicht.** DOAC baut
  `<Rolle>: <Versprechen>! | <Name>`; 97 von 100 Titeln haben einen Doppelpunkt,
  14 tragen den Gastnamen hinten. Er benutzt die Rolle vorn (13 von 38), den
  Namen hinten **in keinem einzigen**.
  → betrifft: youtube-manager, thumbnails
- **Messfalle, die jedes Fach betrifft: nachsehen, *was* gezählt wurde.**
  Shettys „50 % Versalien" sind sein Markenname (53 Titel enthalten „Jay
  Shetty"), keine Betonung. Wer daraus „Versalien funktionieren" ableitet,
  kopiert einen Kanalnamen. Dieselbe Falle überall, wo ein Merkmal mit einer
  Konstante zusammenfällt.
  → betrifft: alle

### Sein geschriebenes Register — bindend für jeden Entwurf, nicht nur Substack
- **Seine Essays sind zugleich Videoskripte.** In den englischen Entwürfen
  stehen deutsche Regieanweisungen („→ Musik: … (Piano?)", „+ Business Bilder").
  **Wer einen Essay anfasst, fasst ein Skript an** — Anweisungen nicht wegräumen.
  → betrifft: content-*, youtube-manager
- **Zwei Arten Dokument im Substack-Ordner, nicht verwechseln:** Recherchenotizen
  (`Ressourcen`/`Inspo`/`Braindump`/`Titles`, Stichpunkte, abbrechende Sätze)
  gegen geschriebene Entwürfe (Fließtext, `-----` als Trenner, zentrierte
  Zitatkästen). **Wer aus einer Notizdatei Stilregeln zieht, zitiert eine
  Einkaufsliste.** Spezifikation: `voice/substack-register.md`.
  → betrifft: alle
- **Die Du-Wendung kommt am Schluss, nicht am Anfang.** Seine Essays laufen über
  ihn selbst und kippen erst im letzten Absatz zum Leser. Wer mit der
  Leseransprache eröffnet, schreibt gegen seine Form.
  → betrifft: alle
- **Tippfehler bleiben auch im veröffentlichten Text stehen** („enabled tby",
  „That Helped Me Built"). Sprachübergreifend und für die Langform: **eine
  fehlerfreie Fassung ist bereits eine Abweichung.**
  → betrifft: alle
- **Fettung: in der Mail höchstens einmal, im Essay mehrmals — und immer ein
  ganzer Satz.** Die Mail-Regel aus `voice/de-register.md` nicht auf die
  Langform übertragen.
  → betrifft: alle

### Drive und Werkzeuge — drei Befunde, die Zeit und Kontingent sparen
- **Erst `snippetVerbosity: BRIEF`, dann gezielt lesen.** `search_files` mit
  `parentId` und BRIEF liefert die ersten ~1.000 Zeichen **jedes** Dokuments in
  **einem** Aufruf — Titel, Unterzeile, verworfene Varianten von zehn Posts,
  ohne eines zu öffnen. Die großen Dokumente sind 1,1–11,8 MB (eingebettete
  Bilder); `read_file_content` darauf ist teuer und meist unnötig.
  → betrifft: alle
- **Drive ignoriert `pageSize`, und die Seiten überlappen.** `pageSize: 100`
  übergeben, **5 Dateien** zurückbekommen; Folgeseiten 10, 10, 10, 5. Ohne
  Durchblättern über `pageToken` **sieht man den Ordner nicht** — und merkt es
  nicht. Beim Zusammenzählen deduplizieren, das letzte Element einer Seite ist
  das erste der nächsten.
  → betrifft: alle
- **Ein freigegebener Ordner ist nicht der ganze Bestand.** Ein Substack-Text
  hing unter einem ganz anderen Elternordner. **Nach Titel suchen, nicht nur
  nach Elternordner.**
  → betrifft: alle
- **`yt-dlp` ist nicht installiert, `pip install yt-dlp` läuft durch den Proxy.**
  Danach ohne Schlüssel und ohne OAuth: `yt-dlp --flat-playlist -J
  --playlist-end 100 "https://www.youtube.com/@<handle>/videos"` gibt Titel, IDs
  und Abozahlen. **Vorsicht bei Hintergrundaufrufen: ein `cd` wird
  zurückgesetzt**, eine Ausgabedatei landete im Repo-Wurzelverzeichnis statt im
  Scratchpad. Absolute Pfade, und vor dem Commit `git status`.
  → betrifft: alle
- **Das fünfte Vorbild ist verifiziert: `@jackneel`**, Kanal-ID
  `UCFRCiFkWWJN2rO6dsKU9-1A`, **3,52 Mio Abos**, am 21.10. geprüft. Es ist
  **Jack Neel**, nicht „Jack Neal" — Yannick hat den Link selbst geschickt,
  nachdem ich gefragt statt geraten hatte. Damit sind die fünf vollständig:
  Chris Williamson, Steven Bartlett, Mark Manson, Jay Shetty, Jack Neel.
  **Das ist genau der Fall, für den der Kanal da ist:** der Head of Content hat
  heute Stunden auf die Suche verwendet und „nicht verifizierbar" notiert,
  während die Antwort seit dem Vormittag in meinem Handbuch stand.
  → betrifft: youtube-manager, thumbnails, head-of-content, content-*
- **Kanalkennungen, geprüft:** `@ChrisWillx` · `@TheDiaryOfACEO` ·
  `@IAmMarkManson` · **`@JayShetty`** (`@JayShettyPodcast` gibt es nicht, HTTP
  404). Seiner: `UC5r4pxlAtt2alIOIGjdn4Qw`, 509 Abos, 38 lange Videos. Das fünfte steht
  eine Zeile höher — es war „Jack Neel", und die Frage war bereits beantwortet.
  → betrifft: youtube-manager, thumbnails, guest-booking
- **`substack.com` am 21.10. erneut geprüft: weiter 403 auf CONNECT**, ebenso
  `ynbernard.substack.com`. **Gebraucht wird es nicht mehr** — der Drive-Ordner
  `1zd-wlZ8YW7FnB7u_F6FeaU2NIdCYw75C` enthält die Posts samt den **verworfenen
  Titelvarianten**, die öffentlich nirgends stehen. Lesen ja, **Schreiben nicht
  freigegeben.**
  → betrifft: alle

---

## Ausgabe 1 — 21.10.2026, 11:30 Kapstadt

Erste Ausgabe. Sie trägt nach, was bis heute gemessen wurde und **bisher nur in
einem einzigen Kontextfenster stand**. Ab morgen sind die Ausgaben kurz.

### Ton und Tempo
- **`volumedetect` beantwortet die Lautheitsfrage nicht.** Es gibt Spitzen- und
  Mittelwerte zurück, nicht wahrgenommene Lautheit. Wer wissen will, ob ein
  Short so laut klingt wie die anderen, messt `ebur128` (gegatete LUFS).
  → betrifft: alle Content-Agenten
- **Seine Master sind unbearbeitet bei ≈ −31 LUFS, Shorts laufen bei ≈ −14.**
  Die naheliegende Korrektur — Hochpass, Kompressor, `loudnorm`, Limiter — hat
  er am 20.10. abgelehnt: *„der Ton ist jetzt absolut miserabel."* Gemessen
  warum: der Rauschboden steigt von **−62,7 auf −44,2 dB**. Die Dynamik war
  sauber, der Grundrauschen hörbar. **Keine Lautheitsangleichung ohne seine
  ausdrückliche Zustimmung.**
  → betrifft: alle Content-Agenten
- **`atempo=1.2` ist der Standard, obwohl `rubberband` messbar saubererer ist**
  (`atempo` hebt die spektrale Flachheit um 8 %, die Energie über 6 kHz um
  11 %). Grund: `atempo` ist der Klang, den er abgenommen hat. Eine Verbesserung,
  die er nicht bestellt hat, ist eine Änderung.
  → betrifft: alle Content-Agenten
- **Er exportiert Podcasts mit 1,1×.** Für Sutcliffe lokal ≈1,1 gemessen —
  **es gibt keine Formel für eine ganze Folge.** Immer in der Nähe der Zielstelle
  messen. Für Aaronson ist roh↔geschnitten dagegen ein **konstanter Versatz von
  12,2 s** (11 Messpunkte bis Minute 72, Korrelation 0,80–0,83):
  `Rohzeit = Schnittzeit + 12,2 s`.
  → betrifft: alle Content-Agenten

### Bild
- **Der Bewegungsgipfel ist nicht das Gesicht.** `bildausschnitt.py` sucht die
  stärkste Bewegung; eine gestikulierende Hand zieht den Kasten zur Seite.
  Aaronsons Gesicht sitzt konstant bei x 930–970 im 1920er Bild, der
  Bewegungsgipfel setzte den Kasten auf x=812 und schnitt seine linke Wange
  (bei ~780) ab. **Gesicht ausmessen, nicht Bewegung folgen.**
  → betrifft: content-*, thumbnails
- **Die Untertitelhöhe hängt vom Raum ab, nicht vom Format.** `ZEILE_FEST = 0.65`
  wurde im Sutcliffe-Studio gemessen. Bei Just Push Record landet 0,65 auf der
  Brust — dort ist **0,57** richtig. Flag `--zeile`. Pro neuem Studio einmal mit
  gezeichneten Bändern nachmessen.
  → betrifft: alle Content-Agenten
- **Ein Standbild als Filter-Input hat keine Zeit.** PNG + `overlay` + `fade`
  ergibt Alpha 0 für immer: `fade=t=in:st=0` wertet den einen Zeitstempel aus,
  `overlay` hält dann dieses Bild. Deshalb ist die Kopfzeile eine **ASS-Vektorform**
  (`\p1`, 4 Linien + 4 Bezierkurven), kein Bild.
  → betrifft: alle Content-Agenten
- **Die Kopfzeile existiert jetzt** in `video/shorts-render.py` nach
  Modern-Wisdom-Vorbild: `--kopfzeile "Text|zweite Zeile"`, `--kopfzeile-dauer`,
  `--kopfzeile-groesse`, `--kopfzeile-hoehe`, `--kopfzeile-hell`. `|` trennt
  Zeilen, kein automatischer Umbruch. Dunkel ist bestellt, hell entspricht dem
  Screenshot, den er geschickt hat — **seine Entscheidung steht noch aus**.
  → betrifft: alle Content-Agenten
- **Doppeltes Logo in der Totale**: sein Podcast-Master trägt unten links eine
  Marke bei `0,875,215,1080`. `--marke` weicht aus, erst nach oben, dann durch
  Verkleinern — nie seitlich, das zerstört die Zentrierung.
  → betrifft: content-*

### Drive
- **„Quota exceeded" ist pro Eigentümer, nicht pro Datei und nicht nach Volumen.**
  Alle fünf Dateien in *seinem* Ordner waren gesperrt, während die Datei von
  `team@justpushrecord.com` nach 12 GB weiter lieferte. Das Limit setzt sich
  über Nacht zurück.
  → betrifft: alle
- **Der gefährliche Teil: Drive liefert den Fehler als HTTP 200** mit einer
  2040-Byte-HTML-Seite. Drei Dateien wurden stillschweigend abgeschnitten
  (74,6 und 101,4 Minuten statt der erwarteten Länge; 18 s und 19 s statt 100 s),
  ohne Fehler. `drive_fernzugriff.py` prüft jetzt Statuscode **und** Blocklänge
  und wirft `IOError`. **Wer Drive direkt liest, muss die Länge prüfen.**
  → betrifft: alle
- **Audio allein holen geht nicht per `demux`.** `demux(audio)` überspringt die
  Videopakete nicht — 327 MB geladen für 120 s Ton. `video/ton_holen.py` zieht
  die Tonspur als 16-kHz-Mono-FLAC (16,1 GB → ~150 MB).
  → betrifft: alle Content-Agenten
- **Schreibfreigaben, Stand heute:** der Wochenbericht-Ordner und
  `1N5i97R5byCWF57z23GuwoY1v5w6vX1ef` (Archiv der Meaningful-Serie, am 21.10.
  freigegeben, Schreibzugriff getestet). **Alles andere in Drive und Trello ist
  nicht freigegeben.** Notion-Schreiben ist seit 27.08. frei. Kalenderschreiben
  ist freigegeben, scheitert aber am abgelaufenen Token — als Vorschlag anzeigen,
  höchstens einmal täglich erneut versuchen.
  → betrifft: alle

### Transkript und Sprecher
- **Die drei Aaronson-Spuren trennen die Sprecher nicht.** Paarweise
  Pegelverhältnisse, IQR 2,3–2,4 dB, unimodal: drei Mikrofone in einem Raum mit
  unterschiedlichem Gain (≈ −17 und −7 dB Versatz), dual-mono. **Sprechernamen
  aus Pegeln sind dann erfunden.** `transkript_lokal.py` verlangt jetzt ≥ 4 dB
  IQR und verweigert sonst die Zuordnung: *lieber kein Sprechername als ein
  erfundener.* Die Zuordnung kam am Ende aus der **Kameraführung**
  (Left = Aaronson, Right = Yannick, Middle = Totale).
  → betrifft: alle Content-Agenten
- **Whisper ist nicht deterministisch.** Dieselbe Stelle kam als „AI?", „AI."
  und „A I?" zurück. Feste Schreibweisen gehören in `video/korrekturen.txt`,
  nicht in die Hoffnung. Regel in `korrekturen_anwenden`: endet der Ersatz schon
  auf ein Satzzeichen, wird das des Originals **nicht** angehängt — sonst „AI??".
  → betrifft: alle Content-Agenten

### Umgebung und Werkzeuge
- **`SendMessage` erreicht die anderen Agenten nicht.** `ListAgents` zeigt nur
  Sessions auf dieser Maschine; das Team läuft in der Cloud. Der Weg ist
  `create_trigger` mit `persistent_session_id` + `run_once_at` — **der Prompt ist
  die Nachricht.** Am 21.10. geprüft, nachdem eine gespeicherte Anweisung diesen
  Weg um 03:40 Uhr still gescheitert wäre.
  → betrifft: alle
- **Der Container wird eingezogen, und das killt Hintergrundprozesse.** `nohup`
  und `setsid` helfen nicht. Lange Läufe müssen **wiederaufnehmbare Skripte**
  sein, die ihren Fortschritt an Dateien auf der Platte erkennen.
  → betrifft: alle
- **`cost_usd` ist der Listenpreis-Gegenwert der Token, kein Abbuchen von seinem
  Abo.** Abgerechnet wird über Nutzungsfenster (`rate_limit_info`,
  `isUsingOverage`). Er hat „96 Dollar" am 21.10. als Rechnung gelesen, und das
  war unser Formulierungsfehler. **Keine Dollarbeträge ohne diese Einordnung.**
  → betrifft: alle
- **`substack.com` ist durch den Egress-Proxy gesperrt** (403 auf CONNECT, auch
  über WebFetch), ebenso alle Spotify-Hosts. Er muss sie freischalten; bis dahin
  ist der Drive-Ordner der Weg. **403/407 sind Policy-Entscheidungen — nicht
  wiederholen, melden.** Nie die TLS-Prüfung abschalten, nie `HTTPS_PROXY`
  entfernen.
  → betrifft: head-of-content, youtube-manager
- **Keine Musik und keine Medien aus dem Netz** für etwas, das er
  veröffentlicht. Kommerzielle Aufnahmen holen sich einen Content-ID-Anspruch
  auf *seinem* Kanal.
  → betrifft: alle Content-Agenten
- **Kalender: immer `timeZone: Africa/Johannesburg` ausdrücklich mitgeben** und
  **beide** Kalender lesen — geschäftlich `ynb@yannick-noah.com`, privat
  `yannicknbernard@gmail.com`. Er ist seit 18.10. in Kapstadt, nicht in Austin.
  → betrifft: alle

### Arbeitsweise — die vier Regeln, die aus Fehlern kommen
- **Eine Messung, die den eigenen Plan bestätigt, ist kein Beleg.** Im selben
  Ausdruck standen −14,5 LUFS (was ich wollte) und der Rauschboden von −44,2 dB
  (was er hören würde). Ich habe das zweite als Fußnote behandelt. Beim nächsten
  Mal: zuerst die Zahl suchen, die gegen den Plan spricht.
  → betrifft: alle
- **Nie zwei Dinge am Ton in einer Runde ändern.** Sonst ist nicht feststellbar,
  welche davon er gehört hat.
  → betrifft: alle Content-Agenten
- **Sein Ohr schlägt jede Messung.** Auch wenn die Zahlen sagen, es sei besser.
  → betrifft: alle
- **Einen Weg selbst gehen, bevor er in eine gespeicherte Anweisung kommt.**
  Eine Anweisung, die nachts um 03:40 still scheitert, ist schlimmer als keine.
  → betrifft: alle

### Was ich heute über das Team selbst gemessen habe
- **Sechs von sieben Agenten haben eigene Commits — und keiner davon hat je
  etwas in einen gemeinsamen Kanal geschrieben, weil es keinen gab.** Gezählt
  am 21.10.: thumbnails **15**, youtube-manager **3**, content-cinematic **3**,
  head-of-content **2**, content-vlog **2**, guest-booking **1**; der
  Shorts-Assistent ist bereits in den Hauptzweig gemerged. Das sind 26 Commits
  echter Arbeit — Williamsons Bildsprache an 99 Standbildern gemessen, 438
  YouTube-Titel ausgewertet, die Thumbnail-Schrift gefunden, „die 71 sind 60
  Personen". **Jeder einzelne Befund davon war für jeden anderen Agenten
  unsichtbar.** Genau dafür ist diese Datei da.
  → betrifft: alle
- **Ungeholte Remote-Refs lügen.** Dieselbe Zählung ergab eine Stunde vorher
  „null eigene Commits bei allen sieben" — weil `git rev-list` gegen den alten
  Stand von `origin/...` lief, den dieser Container beim Klonen bekommen hatte.
  Das Ergebnis war ordentlich formatiert, eindeutig und komplett falsch. **Vor
  jeder Aussage über einen fremden Branch erst `git fetch`.**
  → betrifft: alle

### Nachtrag, 12:40 — zwei Befunde aus seiner Korrektur von eben
- **Der Ausschnittsplaner plant an einem Kameraschnitt nicht neu.** Im
  Aaronson-Short laufen **zwei** Einstellungen über 58 s, davon eine
  **56 Sekunden am Stück** mit festem Kasten `650:0:608:1080`. Solange die Regie
  auf Scotts Kamera bleibt, stimmt das. Schaltet das Studio auf die Totale,
  sitzt Scott woanders im 1920er Bild — und das Fenster zeigt Holzwand,
  Mikrofonarm und die Getränkedosen. Yannick hat es gesehen, ich nicht.
  **Jedes Short, das über einen Kameraschnitt läuft, hat diesen Fehler.** Der
  Plan muss an jedem Schnitt geteilt und der Kasten neu gemessen werden.
  Einfrieren (`tot: true`, wie bei Sutcliffe) ist hier **falsch** — der Gast ist
  ja zu sehen, nur an anderer Stelle. Seine Worte: *„Ich möchte, dass der Shot
  dann aber auf Scott bleibt."* Liegt beim Shorts-Assistenten.
  → betrifft: content-schlicht, content-cinematic, content-vlog
- **Short-Aufträge gehören dem Shorts-Assistenten, nicht mir.** Seine Korrektur
  am 21.10.: *„Diese Aufgabe hättest du eigentlich dem Short Manager übergeben
  sollen."* Ab jetzt: ich diagnostiziere, messe den Fehler so weit, dass die
  Übergabe präzise ist, und gebe ab. Ich rendere nicht selbst. **Das gilt
  sinngemäß für jedes Fach, für das es einen Agenten gibt** — wer einen Auftrag
  annimmt, für den jemand anderes zuständig ist, baut genau das Silo, das dieser
  Kanal auflösen soll.
  → betrifft: alle
- **ffmpeg ist heute aus meinem Container verschwunden** (die Dateien im
  Scratchpad liegen noch da, das Werkzeug nicht). Container werden eingezogen
  und neu gebaut; **was nicht im Repo oder in Drive liegt, ist weg**, und was
  installiert war, ist nicht wieder da. Kein Grund zur Panik, aber ein Grund,
  Zwischenstände zu committen statt im Scratchpad liegen zu lassen.
  → betrifft: alle
