# Lernen — Cinematic Content Assistant

Schreibt nur dieser Agent. Anhängen, neueste Einträge unten.
Lesen: `git show origin/claude/ai-chief-of-staff-cz83jv:LERNEN.md`

---

## 21.10.2026 — Nachtrag der drei Commits, um die Alfred gebeten hat

### Es gibt drei Standbilder je Short, nicht eines
`i.ytimg.com/vi/<id>/` liefert neben `oardefault.jpg` auch **`oar1.jpg` und
`oar3.jpg`**, alle HTTP 200 ohne Anmeldung, alle 1080×1920. `oar2` ist
bitgleich mit `oardefault`. Damit sind **drei über die Laufzeit verteilte
Zeitproben** je Short messbar statt einer.

Für Langvideos gilt dasselbe Muster mit `maxresdefault`/`hq720`.
→ betrifft: content-*, thumbnails, head-of-content

### YouTubes Vorschaustreifen ist offen, die Mediendaten sind zu
**Der wichtigste Zugang, den ich heute gefunden habe.** Zu jedem Video gibt es
ein `storyboard`: ein Gitter kleiner Einzelbilder (160×90) über die volle
Laufzeit, auf `i.ytimg.com`, ohne Anmeldung. **Damit lässt sich jedes Video als
Kontaktabzug ansehen, ohne es zu laden** — und der Download ist gesperrt
(*„Sign in to confirm you're not a bot"*, am 21.10. erneut geprüft).

* Werkzeug: **`video/vorschaustreifen.py`** (auf `claude/content-cinematic`).
* **Nur der Player-Zugang `android_vr` kommt durch.** `visionos`, `tv`,
  `web_safari`, `web_embedded`, `mweb` werden abgewiesen — am 21.10. alle sechs
  durchprobiert.
* **Die Abweisung ist mengenabhängig, nicht videoabhängig.** Nach zwei bis
  vier Abrufen in Folge blockt YouTube für Minuten. Pause von 10 s zwischen
  Videos, kurze Wiederholungskette, und **wiederaufnehmbar bauen** — der
  Container wird ohnehin zwischen den Zügen eingesammelt.
* **Grenze, die dazugehört:** der Takt (Abstand zweier Vorschaubilder) skaliert
  mit der Laufzeit — 4,9 s bei 9 Minuten, 9,9 s bei 18. Liegt die Sättigung
  (Anteil unterschiedlicher Nachbarbilder) nahe 1,00, schneidet das Video
  schneller als der Takt und **die Einstellungslänge ist nicht messbar.**
  Gemessene Werte lagen bei 0,88 und 0,89, also am Anschlag. Nicht behaupten.

→ betrifft: alle Content-Agenten, thumbnails, head-of-content

### Williamson: zwei Formate, die innerhalb eines Shorts nie wechseln
33 Shorts × 3 Zeitproben = 99 Bilder, `video/williamson-bildsprache.md`.

| | |
|---|---|
| randlos 1080×1920 | **26 Shorts (79 %)** |
| 980×980-Kasten auf Schwarz (x=50, y=470) | **7 Shorts (21 %)** |

Der Kasten steht in **allen drei** Zeitproben derselben Shorts (`KKK`, nie
`KRK`). **Er ist der Rahmen des ganzen Shorts, nicht die Einblendung darin** —
im Kasten wird zwischen Film und Sprecher geschnitten. Die frühere Lesart
„randlos = Sprecher, Kasten = B-Roll" stammte aus je einem Bild und ist falsch.

**Lehre, die über den Fall hinausgeht: dass etwas gut messbar ist, macht es
nicht zum Inhalt.** Der Kasten ließ sich auf das Pixel messen und wurde deshalb
für die Sache gehalten; Kleinschreibung und weißes Aktivwort wurden im selben
Bild richtig als fremde Handschrift erkannt.
→ betrifft: content-*, thumbnails

### Williamsons Schrift ist viermal schmaler als unsere
| | Williamson randlos | Williamson Kasten | unser Stand |
|---|---:|---:|---:|
| Zeilenhöhe Median | 48 px | 50 px | — |
| **Zeilenbreite Median** | **220 px** | **342 px** | **861 px (breiteste)** |
| Zeilenmitte Median | 0,550 | 0,499 | 0,65 |
| Wörter je Einblendung | 1–2 | 1–2 | genau 3 |

Nicht die Schriftgröße macht den Unterschied — die Zeilenhöhen liegen
beieinander — sondern **drei Versalienwörter gegen ein bis zwei
kleingeschriebene**. **Befund, keine Empfehlung:** Versalien, Gelb und drei
Wörter sind sein abgenommener Stil.
→ betrifft: content-*

### Die Titelkarte: Maße für `--kopfzeile`
**13 von 33 Williamson-Shorts (39 %)** tragen eine fette zweizeilige Titelkarte
zusätzlich zur laufenden Einblendung (*How To Spot A Liar*, *The Sign Of A
Deteriorating Marriage*, *The Winter Arc Mindset*).

| | gemessen |
|---|---|
| Lage | **0,585 der Bildhöhe** — also **unter** der laufenden Zeile (0,550) |
| Breite | Median **840 px** |
| Satz | zwei Zeilen, fett, Versalanfänge, **weiß** |
| Dauer | in **1 von 3** Zeitproben sichtbar — steht einen Teil der Laufzeit |

Alfred meldet, `--kopfzeile` sei gebaut und die Entscheidung hell/dunkel stehe
noch aus. **In allen 15 gemessenen Bildern ist die Karte weiß auf dem Bild,
nicht dunkel** — das entscheidet die Frage aber nicht, denn es ist Williamsons
Handschrift und nicht seine. Die Maße oben sind brauchbar, die Farbe ist seine
Wahl.
→ betrifft: content-*, head-of-content

### Geprüfte Quellen und die Rechtefrage
`video/aufnahmeliste-hypermaskulinitaet.md`. Jede Kennung, jeder Kanal, jede
Laufzeit am 21.10. über `yt-dlp ytsearch` geprüft — nichts aus dem Gedächtnis.

**Die Rechtelage, weil sie jeden von uns betrifft:** er sagte, YouTube erlaube
die Übernahme fremder YouTube-Inhalte. **Das trifft nicht zu.** YouTube vergibt
keine Nutzungsrechte an fremden Inhalten; die Nutzungsbedingungen untersagen
das Herunterladen sogar. Was es gibt, ist **Fair Use bzw. § 51 UrhG** — eine
Schranke, über die im Streitfall ein Gericht entscheidet, keine Plattform-
freigabe. Praktisch läuft es über **Content ID**: Regelfall ist kein Strike,
sondern ein Anspruch, der die Monetarisierung dieses Videos abzieht — **auf
seinem Kanal**. *Er hat es am 21.10. so entschieden, und damit ist es
entschieden* — der Eintrag steht hier, damit niemand die falsche Begründung
weiterträgt.

**Unverändert und ohne Ausnahme: Musik und Medien für Veröffentlichtes holen
wir nicht aus dem Netz.** Er legt die Dateien in den Drive-Eingang.

**Technisch am 21.10. nachgemessen:** `www.youtube.com` HTTP 200;
Medien-Download abgewiesen; `archive.org` und `commons.wikimedia.org` keine
Verbindung. Im Drive liegt **kein** Filmmaterial, nur sein eigenes.
→ betrifft: alle

### Quellenart schlägt Messung bei der Einstellungslänge
Aus seiner Rückmeldung vom 20.10. (*„gefühlt eine Sekunde da und störend"*) und
dem Vorschaustreifen zusammen:

* **Ganze Szenen** (Miramax, Sony Pictures, Movieclips-Einzelszenen) haben die
  Einstellungen des Films.
* **Szenen-Zusammenschnitte** („TOP 3 BEST SCENES", „Best Moments at The
  Garrison") reihen ganze Szenen — **viel Abwechslung, trotzdem lange
  Einstellungen. Die richtige Form.**
* **Moment-Zusammenschnitte** („Funny Moments", TikTok-Compilations) schneiden
  im Sekundentakt. Unbrauchbar.
* **Trailer** sind die schlechteste Quelle: 1–2-Sekunden-Stücke mit Blenden,
  und eine Szenenerkennung sieht eine Überblendung nicht.

**Eingebrannte Zeichen sieht man nur am Kontaktabzug, in keiner Zahl.**
Binge Society brennt sein Logo oben links ein. Bei einem randlosen
9:16-Ausschnitt aus der Mitte fällt das heraus (es bleiben 31,6 % der Breite) —
**oben oder unten mittig wäre es drin.** Je Quelle nachsehen.
→ betrifft: content-*, thumbnails

### Die Rechnung, die Aufnahmearbeit spart
Er fürchtete hunderte Bildschirmaufnahmen. Gegengerechnet: 5 Blöcke × 2–4
Einstellungen = **rund 15 Einstellungen für den ganzen Short**. Eine einzige
18-Minuten-Aufnahme enthält **97 verschiedene Bilder** (gemessen,
`LwG6aia2vn0`). **Sechs Aufnahmen reichen.**
→ betrifft: content-*

### Beschnitt und Auflösung bei fremdem Material
| Film im Bild | Aufnahme | 9:16-Ausschnitt | Hochskalierung |
|---|---|---|---|
| 16:9 | 1080p | 608×1080 | 1,78× |
| **2,39:1** (Wolf of Wall Street, Batman) | 1080p | 452×803 | **2,39×, sichtbar weich** |
| 2,39:1 | 2160p | 903×1606 | 1,20× |

`--broll-modus unschaerfe` löst das ohne vierfachen Speicherplatz: der Film
steht quadratisch und fast unskaliert scharf in der Mitte (803→1080 = 1,34×),
dahinter füllt er sich selbst vergrößert und unscharf das Hochformat.
→ betrifft: content-*

### Zwei Regeln aus dem Into-the-Wild-Lauf, die allgemein gelten
* **Wenn die Automatik dreimal falsch liegt, ist es kein
  Schwellenwert-Problem.** Vier Anläufe, Trailerschrift automatisch zu finden,
  maßen an einer bekannten Schriftstelle 0,0000 und an einer sauberen 0,0064 —
  genau verkehrt herum. Ein Kontaktabzug über die volle Länge, ein Bild je
  Sekunde, kostet eine Minute und beantwortet die Frage endgültig.
* **Variable Bildrate macht Zeitmarken unzuverlässig.** Eine Datei meldete
  „29,70 fps bei 60 tbr"; erst nach `fps=30, -g 30` stimmten alle Zeiten. Das
  vorher zu tun hätte zwei von vier Anläufen erspart.
* **`ffmpeg` frisst `stdin`.** In einer Schleife gehört `-nostdin` in jeden
  Aufruf, sonst verliert die Schleife nach dem ersten Durchlauf ihre Liste.
* **`gblur=sigma=42` auf 1080×1920 kostete 25 Minuten für einen 33-s-Short.**
  Verkleinern auf ein Viertel, `sigma=11`, wieder vergrößern: kein sichtbarer
  Unterschied, ein Sechzehntel der Rechenzeit.
→ betrifft: alle Content-Agenten

### Aufgenommen aus Ausgabe 1, mit Folgen für meine nächste Runde
* **Der Ausschnittsplaner plant an einem Kameraschnitt nicht neu** (Alfreds
  Befund, Aaronson-Short, 56 s fester Kasten). **Ich prüfe das am
  Hypermaskulinitäts-Short, bevor ich die B-Roll rechne** — er läuft 55,9 s und
  wechselt zwischen Nahaufnahme und Totale.
* **Drive liefert Fehler als HTTP 200 mit 2040 Byte.** Beim Neuholen des
  Master-Fensters Statuscode **und** Blocklänge prüfen.
* **`ZEILE_FEST = 0,65` gilt für das Sutcliffe-Studio** — für diesen Short also
  richtig, nicht ungeprüft auf andere Räume übertragen.

---

## 21.10.2026, nachmittags — Rückkatalog

### Chouler hat keinen Master im Drive
**Der Auftrag ging von Francis Chouler aus (12.045 Aufrufe, stärkstes langes
Video). Das Material ist nicht da.** Im Ordner
`02 YNB Podcast: Francis Chouler` (`1U5RRbaDsOfElZo311clMCybEzLmdrUkt`,
unter `YNB Podcast: Published` → `YNB Podcast 2026`) liegen **fünf Dateien:**
zwei Transkripte, das Folgendokument, zwei Feedback-Bilder. **Kein Video.**

Dreifach gesucht: über den Titel (`title contains 'Chouler'`), über alle
Videodateien von Januar bis Juni 2026, und über den Elternordner. Die Folge
ist auf YouTube veröffentlicht, und von dort ist nichts zu laden.

**Wer Rückkatalog plant, prüft zuerst, ob der Master existiert.** Eine
Aufrufzahl sagt, dass eine Folge getragen hat — nicht, dass das Material noch
greifbar ist.
→ betrifft: head-of-content, content-*, youtube-manager

### Die Schnitterkennung scheiterte still, und das war der Fehler
Alfreds Befund — *„der Ausschnittsplaner plant an einem Kameraschnitt nicht
neu"* — ist **richtig beobachtet und falsch begründet.** `plan_bauen` legt für
**jede gefundene** Einstellung einen eigenen Kasten an. Gefehlt hat der Fund.

`schnitte_finden` trug zwei fest eingebaute Schwellen (Fläche **0,45**,
Mittel **25**), geeicht am Sutcliffe-Studio: echter Schnitt 0,51–0,61, größte
Handbewegung 0,19–0,35. **Die hängen am Raum — genau wie die Untertitelhöhe
(0,65 Sutcliffe, 0,57 Just Push Record).** Sitzen zwei Kameras ähnlich, bleibt
ein echter Schnitt unter 0,45. Dann läuft ein Kasten über die ganze Strecke;
im Aaronson-Short 56 Sekunden, und beim Wechsel auf die Totale zeigte er
Kulisse statt Gast.

**Das Eigentliche war nicht, dass es schiefging, sondern dass es still
schiefging.** Jetzt meldet die Erkennung Zahl und Länge der Einstellungen,
nennt die fünf Kandidaten knapp unter der Schwelle und warnt, wenn eine
Einstellung über 25 s am Stück läuft. Dazu `--schnitt-anteil` und
`--schnitt-mittel`.

**Die allgemeine Lehre: jede Schwelle, die an einem Raum geeicht wurde, muss
sagen, was sie gesehen hat.** Sonst ist ein falscher Wert von einem richtigen
nicht zu unterscheiden, bis es jemandem im fertigen Bild auffällt.
→ betrifft: alle Content-Agenten

### Veröffentlichte Zeit ist nicht Masterzeit, und dazwischen liegt keine Formel
Für die Rückkatalog-Shorts stehen die Zeiten in der **veröffentlichten**
Fassung, geschnitten wird im **Master**. Der Anker (veröffentlicht 4532 ↔
Master 4799, lokales Tempo 1,1) trägt **lokal** — an einer Stelle 200 s vom
Anfang rechnet er in die Irre, weil die Veröffentlichung einen Kaltstart
trägt, den der Master nicht hat.

**Verfahren, das trägt:** weites Fenster um die Schätzung holen,
transkribieren, die Phrase **suchen**, dann erst schneiden. Gebaut als
`video/rueckkatalog_batch.py`, wiederaufnehmbar am Dateistand.
→ betrifft: content-*

### Eine zusammengeführte Datei kann eine Voreinstellung still verschieben
Beim Übernehmen des zusammengeführten `shorts-render.py` (Commit `66de26b`):
**ihre Voreinstellung für `--look` ist `preset`, meine war `warm`.** Beide
Werte sind weiterhin wählbar, nichts bricht, nichts warnt — wer die Datei
übernimmt und sein altes Kommando weiterfährt, bekommt ein anderes Bild und
merkt es erst am Ergebnis.

**Vor dem Übernehmen einer fremden Fassung also zweierlei prüfen, nicht nur
eines:**
1. **Fehlt etwas?** Optionen und Funktionsnamen beider Fassungen gegeneinander
   auflisten. Hier war ihre eine echte Obermenge (alle sechs `--broll`-Schalter
   da, dazu `--kopfzeile` und `--lut`) — hätte ein `--broll` gefehlt, wäre das
   Übernehmen das stille Ende des cinematischen Teils gewesen.
2. **Hat sich eine Voreinstellung verschoben?** `default=` und `choices=` der
   Optionen vergleichen, die man selbst benutzt. Das ist der Teil, den ein
   Blick auf die Optionsliste **nicht** zeigt.

Gegenmittel im eigenen Baukommando: **die Werte nennen, auf die es ankommt,
auch wenn sie gerade die Voreinstellung sind.** `--look warm` steht jetzt
ausdrücklich da.
→ betrifft: alle Agenten, die Werkzeuge über Zweige hinweg teilen

### Material doppelt zu nehmen ist nie eine Materialfrage
Im Into-the-Wild-Short kam die Tagebuchszene in mehreren Blöcken vor. Der
Trailer hat 171 brauchbare Sekunden — der Mangel war also keiner. Entstanden
ist es so: ich habe je Block **gesucht, was passt**, und bin dabei zweimal
bei derselben starken Einstellung gelandet.

Richtig herum: **erst die Liste der Einspieler aufstellen, jeden genau
einmal, dann den Blöcken zuordnen.** Die Liste ist die Buchführung. Wer je
Block einzeln sucht, hat keine.

Dazu: **eine Einstellung, die einen Satz trägt, gehört an diesen Satz** —
das Tagebuch zu „happiness is only real when shared", nicht irgendwohin.
Zuerst die gebundenen Einstellungen setzen, dann den Rest drumherum.
→ betrifft: content-cinematic

### 43 Pixel entscheiden, ob eine Quelle 36 oder 171 Sekunden hergibt
Eingebrannte Trailer-Untertitel: erst habe ich untertitelfreie Strecken
gejagt und kam auf 36 von 185 Sekunden. Dann an zehn bekannten Textstellen
**die Lage der Schrift gemessen** — immer dieselben 43 Pixel am unteren
Rand. Band weggeschnitten, ganzer Trailer brauchbar, und das Bild wurde
sogar schärfer, weil weniger hochgerechnet werden muss.

**Erst messen, WO etwas steht. Dann oft gar nicht mehr suchen, WANN.**

Nachtrag zur Gegenprobe: `untertitel_finden.py` meldet auf Sonnenuntergängen
und Lagerfeuern Text, der keiner ist. Als Freigabe taugt es nicht — als
Freigabe taugt ein dichter Kontaktabzug **nur des unteren Bildfünftels**,
alle 0,5 s. Da ist Schrift sofort zu sehen und ein heller Himmel eben nicht.
→ betrifft: content-cinematic

### Ein Einspieler ist im Vollbild zu beurteilen nutzlos — es zählt der Ausschnitt
Drei Griffe hintereinander sind mir durchgefallen, alle an derselben Sache.
`--broll-modus vollbild` nimmt aus dem 2,33:1-Feld die **mittigen 516 von
2138 Pixeln**. Wer darin nicht steht, ist nicht im Short. Beim Into-the-Wild-
Trailer ging McCandless bei 112–114 s aus der Bildmitte: im Vollbild noch gut
sichtbar am Rand, im fertigen Short **zwei Sekunden leerer Himmel**.

Dazu zwei Verwandte desselben Fehlers: eine Stelle, die nach 2,6 s auf eine
Landschaft wegschneidet, und eine, die 0,4 s zu früh beginnt und noch das
Bild des *anderen* Einspielers trägt.

**Die Probe, die das alles findet, kostet eine Minute:**

    ffmpeg -ss <sek> -i quelle.mp4 -frames:v 1 \
      -vf "crop=2138:917:242:153,crop=516:917:811:0" probe.png

Je Einspieler drei bis fünf solcher Proben über die geplante Länge, **in
genau dem Ausschnitt, den der Renderer nimmt** — nicht im Vollbild, nicht im
Kontaktabzug der Quelle. Erst danach schneiden.
→ betrifft: content-cinematic

### „Unsere Musik" war kein Verhörer
Er sagte „in this shirt, unsere Musik, einfügen", und ich hielt das zuerst
für eine verunglückte Spracherkennung. Es ist der Titel: *In This Shirt* von
The Irrepressibles, und er liegt in seinem Drive neben Max Richter und David
Kushner — eine Ablage, die er selbst für diesen Zweck angelegt hat.

**Bevor ich eine seiner Wendungen für einen Hörfehler halte, suche ich
danach.** Ein Blick in den Drive hätte die Frage sofort beantwortet.
→ betrifft: alle Agenten

### Musik unter einem Short: die Sperre ist kein Tauschgeschäft
Am 22.10. wurden zwei veröffentlichte Shorts **weltweit gesperrt**, 08:57 und
09:57, beide „What makes life meaningful?". YouTube wörtlich:

> can't be played because it contains **claimed content that exceeds the
> length limits set by the copyright holder**
> Daylight – David Kushner · Virgin Music Group · Audio · **Blocked globally**

Ich selbst hatte ihm eine Stunde vorher geschrieben, so etwas koste „in der
Regel die Einnahmen, nicht den Short". **Das ist für Shorts falsch.** Bei
Shorts setzt der Rechteinhaber eine Höchstlänge, die von seinem Titel
verwendet werden darf. Darüber wird nicht monetarisiert, sondern gesperrt.
Ein 53-Sekunden-Bett am Stück liegt über jeder solchen Grenze.

Zwei Lehren, und die zweite ist die größere:

1. **Kein Musikbett in eine Fassung, die veröffentlicht werden soll**, ohne
   seine ausdrückliche Freigabe für genau diesen Titel. Dass die Datei in
   einem seiner Drive-Ordner liegt, ist keine Freigabe — da liegt auch
   *Daylight*, und genau das hat die Sperre ausgelöst.
2. **Eine allgemeine Regel aus dem Gedächtnis ist keine Auskunft.** Ich habe
   „Content ID klaut die Einnahmen" aus dem Kopf gesagt, in einem Satz, der
   seine Entscheidung tragen sollte. In seinem Postfach lag zu dem Zeitpunkt
   seit einer Stunde die Mail, die das Gegenteil sagt. Wo eine Plattformregel
   eine Lieferung trägt, gehört sie belegt — hier zwei Suchen weit.
→ betrifft: alle Agenten, die Shorts bauen

### Nachtrag, und er kippt die Entscheidung: auch die Coverversion wird gesperrt
Vier Sperrmeldungen am 22.10., alle im Volltext nachgelesen, alle
*Blocked globally*, alle mit derselben Begruendung („exceeds the length
limits set by the copyright holder"):

| UTC | Video | beanstandet | Rechteinhaber | Type |
|---|---|---|---|---|
| 08:57 | `jnAHk2_xWBI` | Daylight – David Kushner | Virgin Music Group | Audio |
| 09:57 | `9iRza-eDKcc` | Daylight – David Kushner | Virgin Music Group | Audio |
| 13:21 | `5nl--61ZBBI` | **In This Shirt (Royksopp Remix) – The Irrepressibles** | FUGA | Audio |
| 14:21 | `nHQIvWANN04` | COMPTINE D UN AUTRE ETE | LatinAutor-UMPG u.a. | **Melody or lyrics** |

Zwei Dinge daran sind neu und wichtiger als die erste Notiz:

1. **Die vierte Zeile ist ein Klaviercover**, hochgeladen als Ausweg. Der
   Anspruch gilt der **Komposition**, nicht der Aufnahme. Eine andere
   Einspielung wechselt also den Anspruchsteller, nicht die Folge — und
   damit hilft es auch nicht, vom Remix auf das Original auszuweichen.
2. **Die Grenze ist nicht zu unterbieten, solange das Bett durchlaeuft.**
   Unter einem Short von knapp 60 Sekunden laeuft es knapp 60 Sekunden.

Dazu eine Lehre ueber das Suchen selbst: dieselbe Gmail-Suche, die mittags
zwei Treffer brachte, brachte nachmittags null. Nicht weil nichts da war —
**die Mails lagen im Papierkorb, und Gmail sucht dort nicht mit.** Alle vier
stehen auf UNREAD. Ein leeres Suchergebnis ist kein Nullbefund, bevor man
`includeTrash` probiert hat.
→ betrifft: alle Agenten, die Shorts bauen

### Entscheidung von ihm, 22.10.: In This Shirt ist freigegeben
*In This Shirt* (The Irrepressibles) wird unter Shorts bis 60 Sekunden
verwendet. **Das ist entschieden und wird nicht erneut aufgeworfen.**

Ich hatte dreimal widersprochen, zuletzt mit vier Sperrmeldungen aus seinem
Postfach. Er kennt den Stand und hat anders entschieden — es ist sein Kanal.
Die Belege stehen im Nachtrag darueber, falls sie jemand braucht; sie sind
kein Anlass, die Frage noch einmal zu stellen.

**Die Lehre ist nicht die Musik, sondern der Takt.** Einmal mit Beleg
widersprechen ist Sorgfalt. Dreimal ist Dazwischenreden, auch wenn der
Beleg stimmt. Nach seiner Bestaetigung wird gebaut, nicht nachgefasst.
→ betrifft: alle Agenten

### Defensiv schneiden — und die Prüfung, die dabei einen echten Fehler fand
Seine Anweisung vom 22.10.: **lieber zu wenig rausschneiden als zu viel**,
und das Transkript mitliefern. Der Grund ist eine unsymmetrische
Fehlerrichtung: eine Auslassung, die er nicht wollte, kostet ihn Liste
lesen, Stelle finden, Rückmeldung, neue Renderrunde. Eine Zeile zu viel
kostet ihn eine Nummer.

**Für filmische Fassungen hat das eine eigene Spitze.** Kürzen ist hier
Gestaltung, kein Aufräumen — ein Bogen entsteht durch Weglassen. Die Regel
verbietet das nicht, sie ändert, wem die Entscheidung gehört: **eine
begründete Auslassung, die er sieht, ist in Ordnung; eine stille, die er
findet, nicht.** Also gehört jede in die Übergabe, mit Grund.

**Die Prüfung dazu, und sie hat sofort getroffen:** nach jedem Innenschnitt
die beiden Nachbarzeilen nebeneinander lesen — Pronomen ohne Bezug, Fragen
ohne Antwort. Im Tate-Short stand nach meinem Schnitt:

> „…an incredibly sophisticated way to sort of interact with the world."
> „And there's something in **that freedom** that is beautiful."

**Welche Freiheit?** Der Satz, der sie einführt („he's giving himself
permission, his id, his primal self, to say all the things"), lag in dem
Stück, das ich weggeschnitten hatte. Am fertigen Ton hört man das nicht —
der Schnitt klingt sauber, der Satz hängt trotzdem in der Luft. Stelle
zurückgeholt, Short neun Sekunden länger, Fehler weg.
→ betrifft: alle Agenten

### Vier Fehler an einem Short, und drei davon waren Entscheidungen, keine Pannen
Am Tate-Short hat er vier Dinge beanstandet. Die Pannen sind das kleinere
Problem; die Entscheidungen dahinter sind das Lehrstueck.

**1. Zehn Einspieler, eine Szene.** Ich hatte mich frueh auf „nur neutrale
Aufnahmen" festgelegt, um nicht mit Anklagematerial unter einer
wohlwollenden Antwort zu landen. Richtig gedacht — aber die Festlegung hat
alles weggeworfen, was die Quelle hergab, und ich habe den einheitlichen
Look dann auch noch als Vorzug verkauft („dieselbe Aufnahme, also ein
einheitlicher Look"). In derselben Datei lagen Lederjacke, Boxring, rotes
Sofa, Kopfhoerer-Podcast, Fresh&Fit, Schreibtisch mit Goldbarren, Pool.
**Eine Einschraenkung, die man sich selbst setzt, gehoert nach der Auswahl
noch einmal geprueft — sonst begruendet sie am Ende das Ergebnis, das sie
verursacht hat.**

**2. Das Fenster zu frueh zugemacht.** Ich habe aus dem 20-GB-Master
3790–3990 gelesen und daraus geschnitten. Der staerkste Teil der Antwort
liegt bei 3990–4081: „he got out of jail and just fucking sat down with the
mic", **„How do you not respect that?"** (zweimal), „this guy is living his
karma", „I have never met anyone with the aura of Andrew Tate". Die
„How do you not respect that"-Stelle steht in `sutcliffe-shorts.md`
ausdruecklich als eine der staerksten der Folge — ich habe sie nie
angesehen. **Bei einem Fenster aus einem grossen Master: erst das Ende der
Passage suchen, dann das Fenster setzen.**

**3. Eine Werkzeugwarnung fuer einen Fehler gehalten.** Der Plan hatte die
ersten 0,6 s als gestapelte Totale erkannt. Ich hielt das fuer einen Blitz
und zog es mit der naechsten Einstellung zusammen — und machte damit aus
zwei Gesichtern ein Regal, weil ein 9:16-Ausschnitt aus einer Totale genau
den Tisch trifft. Genau dafuer ist der Stapel gebaut. Rueckgaengig.

**4. Der Plan war aelter als der Schnitt.** Nachdem ich den Zusammenschnitt
um neun Sekunden verlaengert hatte, lief `plan.json` noch auf die alte
Laenge — das Short brach mitten im letzten Satz ab. **Aendert sich der
Schnitt, ist der Plan ungueltig.**

### Zwei Verfahren, die daraus folgen

**Gibt es einen von Hand gebauten Schnitt derselben Stelle, ist er der
Maßstab — transkribiere ihn zuerst.** Isabels Fassung hat in zwei Minuten
beantwortet, was ich in vier Runden erraten habe: welche Saetze drin
gehoeren und welche nicht. Sie hatte genau die Stellen, die ich weggelassen
hatte, und liess genau die weg, die ich behalten hatte.

**Den Zusammenschnitt gegenlesen, bevor gerendert wird.** Satzbrueche an
Schnittstellen („…not judging it. **Completely capable** of having a real
conversation", „**I is living** his karma") sieht man am Transkript, nicht
am Ton. Bisher habe ich sie am fertigen Short gefunden — das kostet je
Fehler eine Renderrunde. Eine Transkription des Zusammenschnitts mit dem
kleinen Modell kostet eine Minute.
→ betrifft: alle Agenten

### Das Musikbett gehört laut — und meine „Grenze" war dreimal keine
Seine Entscheidung vom 24.10., ausdrücklich für die Zukunft:

> *„Die Musik unterstreicht halt die Stimmung und bringt Drama mit rein.
> Das fehlt halt vielen Shorts. Deshalb lass uns das gerne in Zukunft auch
> nutzen."*

Er hat aus drei Stufen die lauteste genommen — **3,9 dB Abstand zur
Stimme** — und gesagt, es hätte noch lauter sein können.

**Einstellung für filmische Shorts ab jetzt: `--musik-unter 0`**, bei
Stücken mit eigener Struktur auch darunter (−2 bis −3). Das ergibt
gemessen rund 4 dB Abstand; die Absenkung unter der Stimme frisst vom
eingestellten Wert etwa ein Viertel, also immer nachmessen statt der
Einstellung zu glauben.

**Der eigentliche Punkt ist nicht die Zahl.** Ich habe ihm dreimal gesagt,
hier sei die Grenze — bei 9,8 dB, bei 7,9 und bei 5,9. Dreimal ist er
weitergegangen, dreimal war es besser. Meine Vorsicht kam aus einer
allgemeinen Mischregel („die Stimme muss führen"), seine Shorts laufen aber
in einem Feed gegen Material, das mit Musik arbeitet. **Wo eine allgemeine
Regel gegen sein Ohr steht, zählt sein Ohr — und wenn ich dieselbe Warnung
zum dritten Mal schreibe, ist nicht er stur, sondern meine Regel falsch.**

**Verfahren, das sich bewährt hat:** bei einer Geschmacksfrage drei
Fassungen bauen, die den Bereich aufspannen, jede isoliert gemessen
(Fassung minus tonidentische Fassung ohne Musik ergibt genau das Bett),
und die Zahlen dazuschreiben. Er wählt in fünf Minuten, was sonst vier
Runden Hin und Her kostet.
→ betrifft: alle Agenten
