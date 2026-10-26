## 23.10.2026 — Der Rückkatalog über die Master kostet das Doppelte der Datei

**Gemessen, dann abgebrochen.** Drei Stücke des Eben-Britton-Masters (27,0 GB,
102 min) geholt, je 3 Minuten Ton:

| Stück | Ton bis | geholt | Laufzeit |
|---|---|---|---|
| 0 | 3,0 min | 1,09 GB | 2,6 min |
| 1 | 6,0 min | 1,98 GB | 5,2 min |
| 2 | 9,0 min | 1,97 GB | 5,3 min |

**Hochgerechnet auf 34 Stücke: 57 GB Transfer und 148 Minuten** — für eine
Datei von 27 GB. **Das Doppelte der Datei.** Der Grund ist der Zuschnitt
selbst: jedes Stück setzt auf dem Schlüsselbild **vor** seinem Anfang auf und
der Demuxer liest über sein Ende hinaus. Stück 0 brauchte ohne vorangehenden
Sprung nur 1,09 GB, die folgenden je rund 2.

**Damit ist der Weg zu.** Das Drive-Tageslimit gilt pro Eigentümer und war am
21.10. schon bei **31 GB** erschöpft. 57 GB für **eine** Folge verbrauchen die
Quote aller Agenten für einen Tag. Ich habe nach drei Stücken (≈5 GB)
abgebrochen, statt es zu Ende laufen zu lassen.

**Die Klemme, die das erklärt:** große Stücke sind sparsam, aber ein Zug über
mehr als ein paar Minuten stirbt am Containerwechsel. Kleine Stücke überleben,
kosten aber den doppelten Transfer. **Beides zugleich geht nicht.**

**Was billig bleibt und deshalb die Reihenfolge bestimmt:**
1. Folgen, deren Transkript schon vorliegt — kein Zug nötig.
2. Folgen mit einer **kleinen Exportfassung** neben dem Master: bei Aaronson
   liegen 895 MB neben 16 GB, das ist ein Sechzigstel. Bei Britton gibt es
   keine.
3. Erst danach der Master, und dann nur mit abgesprochener Quote.

**Die Bitte, die daraus folgt, geht an ihn, nicht an uns:** eine kleine
Exportfassung je Folge, die bearbeitet werden soll.
→ betrifft: content-*, YNB Cinema, Shorts II, EA, alle Content-Agenten

## 22.10.2026 — Defensiv schneiden, und die Naht nachlesen

**Seine neue Anweisung, für alle Short-Agenten:** *„dass du lieber zu
defensiv als zu offensiv schneidest, weil es mir das einfacher macht, dir
dann zu sagen, was noch raus soll."*

**Der Grund ist eine unsymmetrische Fehlerrichtung**, und das ist der Teil,
den man sich merkt: eine Auslassung, die er nicht wollte, kostet ihn Liste
lesen, Stelle finden, melden, neue Runde rendern. Eine Zeile zu viel im
Short kostet ihn: eine Nummer nennen. **Gleich großer Fehler, völlig
verschiedener Preis.** Also im Zweifel drinlassen.

**Und die Prüfung dazu, an zwei echten Fehlern belegt** (Shorts II, Short
„AI 2027", beide von ihm zurückgeholt): ein gestrichener Block nahm die
einzige Nennung von Eliezer Yudkowsky mit, danach stand im Short *„**he**
just regarded it as obvious"* ohne Bezug. Ein zweiter gestrichener Block
begann mit *„He would say, by default, this kills us"* — der **Antwort**
auf Yannicks eigene Frage, die dadurch unbeantwortet blieb.
**Nach jedem Innenschnitt die beiden Nachbarzeilen nebeneinander lesen:**
auf Pronomen ohne Bezug, und auf Fragen, deren Antwort im entfernten Block
lag. **Beides hört man dem Render nicht an, weil der Schnitt sauber
klingt.**
→ betrifft: content-*, YNB Cinema, Shorts II, EA, alle Short-Agenten

## 22.10.2026 — Ein langer Zug stirbt am Containerwechsel, nicht am Netz

**Der Tonzug über den 27-GB-Britton-Master starb nach fünf Minuten:**

    ProxyError: Unable to connect to proxy
    HTTPSConnection(host='127.0.0.1', port=40217): Connection refused

Nicht Drive hat abgelehnt, nicht das Tageslimit — **der Container wurde
eingezogen, der Proxy bekam einen neuen Port, und der laufende Prozess
hielt am alten fest.** Ein sequentieller Lauf über eine Stunde überlebt das
nie, egal wie geduldig er ist.

`ton_holen.py` nimmt jetzt `--von/--bis`, und `ton_stueckweise.py` holt die
Spur in Zehn-Minuten-Stücken: **je Stück ein eigener Prozess mit frischem
Proxy**, fertige Stücke bleiben liegen, unvollständige werden an ihrer
Laufzeit erkannt und neu geholt, am Ende wird zusammengefügt.
**Regel: was länger als ein Zug dauert, muss in Stücke, die kürzer sind als
ein Zug.**
→ betrifft: content-*, YNB Cinema, Shorts II, EA, alle Content-Agenten

## 22.10.2026 — Der billige Weg zum Rückkatalog ist zu

**Die Annahme, auf der der Rückkatalog-Plan steht, hält nicht mehr.** Es
hieß: *„Veröffentlichte Folgen haben ein wortgenaues YouTube-Transkript —
kein Drive-Download, kein Tageslimit, keine Versatzrechnung. Das ist der
Grund, warum der Rückkatalog billiger ist als eine neue Folge."*

**Aus diesem Container nicht mehr.** Drei Wege geprüft, alle drei zu:

| Weg | Ergebnis |
|---|---|
| `yt-transkript.py` (yt-dlp) | `Sign in to confirm you're not a bot` |
| `video.google.com/timedtext` direkt | **403**, der Proxy lässt den Host nicht durch |
| Watch-Seite nach `captionTracks` durchsuchen | kein Treffer, die Seite ist ebenfalls gesperrt |

**Was weiter geht:** oEmbed. Titel zu einer Video-ID bekommt man, die
Kanalseite liefert die IDs. **30 veröffentlichte Videos mit Titeln** stehen
damit fest — das reicht für die Auswahl, aber nicht für den Inhalt.

**Also kostet eine Rückkatalog-Folge genauso viel wie eine neue:** Master
aus Drive, Ton ziehen, selbst transkribieren. Beim Eben-Britton-Master sind
das **27,0 GB**. Das Tageslimit gilt pro Eigentümer und war heute schon
einmal erschöpft — wer parallel zieht, nimmt dem anderen die Quote weg.
**Vor jedem Zug absprechen, wer welche Folge zieht.**
→ betrifft: content-*, YNB Cinema, Shorts II, EA, alle Content-Agenten

**Und der Teil, der trotzdem billiger bleibt:** bei einer veröffentlichten
Folge ist die Veröffentlichung selbst die Quelle — es gibt keinen Versatz
zwischen Rohzeit und Schnittzeit zu messen, weil nur eine Fassung
existiert. Das war die halbe Ersparnis, und die bleibt.

## 22.10.2026 — Musikbett messbar gemacht, und eine Prüfung, die zuerst nichts taugte

**Vier Sperrmeldungen an einem Tag, drei Titel, auch ein Klaviercover** —
die Sperre hängt an der **Komposition**, nicht an der Aufnahme, und der
Grund steht in jeder Mail: *„exceeds the length limits set by the
copyright holder."* Ein durchlaufendes Bett unter einem 59-Sekunden-Short
hält diese Grenze nie ein. **Keine Musik, bis er einen lizenzierten Titel
nennt.**

**Damit es nicht wieder an einem Menschen hängt, prüft `abnahme.py` das
jetzt.** Und dabei der eigentliche Befund: **die erste Fassung der Prüfung
hat das Bett durchgelassen.** Sie maß den Anteil der 20-ms-Fenster unter
−55 dB:

| | leisestes Prozent | Anteil unter −55 dB |
|---|---|---|
| saubere Fassung | −83,6 dB | 13,6 % |
| dieselbe mit Testbett | −58,3 dB | **11,3 %** |

Der Anteil fiel nur von 13,6 auf 11,3 — kein Alarm. **Nicht der Anteil
leiser Fenster verrät das Bett, sondern wie tief es in den Sprechpausen
überhaupt wird.** Umgestellt auf das leiseste Prozent, Schwelle −65 dB:
die saubere Fassung besteht mit −83,6, die Testfassung fällt mit −58,3
durch. Und das war ein absichtlich **leises** Testbett; ein hörbares liegt
bei −30 bis −40.
**Regel: eine neue Prüfung wird an einem Fall getestet, von dem man weiß,
dass er durchfallen muss. Sonst prüft sie nichts und man glaubt, sie tue
es.**
→ betrifft: content-*, YNB Cinema, Shorts II, EA, alle Content-Agenten

**Dazu seine Ansage zu den Dateinamen**, ebenfalls als Prüfung eingebaut:
`YNB Podcast <Gastname> <Stichwort>.mp4`, das Stichwort **ein** Wort,
Nebenfassungen in Klammern dahinter.

**Und eine Meldung, die ich geprüft und verworfen habe:** es hieß, der
`xfade`-Fehler (Doppelbelichtung innerhalb einer Einstellung) betreffe
`shorts-render.py`. Hier kommt `xfade` in **keiner** Datei vor —
`schnittliste.py` und `fuellwoerter.py` schneiden hart und legen nur
30–40 ms Tonblenden an die Nahtstellen, also genau das, was empfohlen
wird. Der Fehler sitzt woanders. Nachgesehen statt übernommen.
→ betrifft: content-*

## 22.10.2026 — Musiksperre: meine Fassungen tragen keine Musik, gemessen

**Zwei veröffentlichte Shorts sind weltweit gesperrt** — „What makes life
meaningful?" mit Sutcliffe und mit Aaronson, beides Stücke, die hier
gebaut wurden. Grund laut YouTube: *Daylight — David Kushner · Virgin
Music Group · Impact: Blocked globally.*

**Nachgemessen, nicht beteuert.** Die Tonspuren der hier abgelieferten
Fassungen, in 20-ms-Fenstern:

| Datei | leisestes 1 % | Median | Anteil unter −55 dB |
|---|---|---|---|
| 01-sutcliffe-meaningful | **−78,1 dB** | −31,0 dB | 20,5 % |
| 02-aaronson-meaningful | **−87,2 dB** | −36,2 dB | 18,2 % |

**Ein Musikbett kann das nicht.** Läge Musik unter der Stimme, bliebe der
Boden in den Sprechpausen bei etwa −35 bis −45 dB, durchgehend. Hier
liegen rund ein Fünftel aller Fenster unter −55 dB und die leisesten bei
−78 und −87. Dazu: `--musik` wurde in keinem Lauf benutzt, die Spur kommt
unverändert aus dem Podcast-Master.
**Die Musik ist nach der Übergabe dazugekommen, nicht hier.** Das ist
keine Entlastung, sondern ein Hinweis, wo zu suchen ist — und es heißt,
dass sich die Stücke aus den vorhandenen Fassungen neu rendern lassen,
ohne etwas nachzubauen.

**Die Regel bleibt, wie sie war, und wird schärfer:** keine Musik aus
Handelsaufnahmen, und *„liegt in einem seiner Ordner" ist keine
Freigabe.* Freigabe heißt: er nennt den Titel.
→ betrifft: content-*, YNB Cinema, Shorts II, EA, alle Content-Agenten

**Und eine Lehre über Prüfwerkzeuge.** `abnahme.py` stürzte mit einem
IndexError ab, wenn `ortscheck.py` nicht danebenlag: der Aufruf lief ins
Leere, `stdout` blieb leer, `.splitlines()[-1]` griff auf eine leere
Liste. **Eine fehlende Prüfung darf die Abnahme nicht abstürzen lassen —
sie muss melden, dass sie fehlt.** Sonst ist das Werkzeug, das Fehler
verhindern soll, selbst eine Fehlerquelle.
→ betrifft: alle Content-Agenten

## 22.10.2026 — Eine Folge, ein Agent, der Reihe nach

**Seine Regel, 22.10.:** *„lass uns, um die Übersicht zu behalten, die
einfach alle Shorts zu Scott werden von ein und demselben Agenten
bearbeitet, nacheinander. Damit wir hier nicht durcheinander kommen, weil
wir haben hier jetzt eine Überschneidung."*

**Die Überschneidung, nachgesehen statt vermutet:** auf
`claude/content-cinematic` liegt `video/shorts/aaronson-01-how-safe-is-ai.srt`
— 64 Einblendungen, drei Runden (`3bde9dc`, `5c7be04`, `a4db680`). Hier
ist parallel ein anderes Stück derselben Folge entstanden („the trouble
with AI is not that it doesn't work", Kopfzeile „Is AI safe?").
**Zwei verschiedene Shorts unter demselben Namen, in zwei Containern, mit
zwei Zeitbasen.**

**Die Aufteilung, die das verhindern sollte, hat es verursacht.** EA hatte
verteilt: *„nimm die Kandidaten von hinten, er nimmt sie von vorn."* Beide
haben Kandidat 1 angefasst — er fängt von vorn an und ist der stärkste,
also greift jeder zuerst dorthin.
**Regel: eine Aufteilung innerhalb einer Folge ist keine Aufteilung,
solange die Kandidaten nicht nummeriert und namentlich vergeben sind. Also
die Folge verteilen, nicht die Kandidaten.**
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Und was eine Übergabe mitbringen muss, damit sie keine ist:** Schnittzeiten
**in Quellzeiten** (Anfang und Ende jeder behaltenen Strecke), Ausschnitt,
Lippenhöhe, und die getroffenen Entscheidungen im Klartext. Ohne das ist
die Vorarbeit im fremden Container verloren, sobald er eingezogen wird —
dieselbe Lehre wie bei `clip_aa2.mp4` am 21.10., nur eine Ebene höher.
→ betrifft: alle Content-Agenten

## 22.10.2026 — NEUE REGEL: jeder Short geht mit seinem Transkript raus

**Seine Ansage, und sie gilt für alle Short-Agenten:** *„dass die Shorts
mit dem Transkript geliefert werden müssen, damit ich einfacher Feedback
geben kann, beziehungsweise einfach dir sagen kann, was raus soll."*

**Ab sofort gehört zu jedem Short eine Liste zum Durchstreichen**, nicht
nur die Datei. `video/kurzliste.py` baut sie aus der `.srt`, die der
Renderer ohnehin über `--srt-out` schreibt: durchnummeriert, mit den
Zeiten **im fertigen Short** — er streicht eine Nummer, wir schneiden.

Die rohe `.srt` allein taugt dafür nicht: drei Wörter je Zeile, hundert
Einblendungen. Und Satzenden allein auch nicht, weil in eingebrannten
Untertiteln fast kein Satzzeichen steht (nur das Fragezeichen bleibt).
Die Liste bricht deshalb an Sprechpausen und spätestens nach vierzehn
Wörtern um.

    python3 video/shorts-render.py … --srt-out kurz.srt
    python3 video/kurzliste.py kurz.srt --titel "Aaronson 1" --out liste.txt

`video/abnahme.py` fragt die `.srt` bereits ab; ohne sie gibt es kein
„bestanden".
→ betrifft: content-*, YNB Cinema, EA, alle Short-Agenten

**Zweite Ansage derselben Runde:** die Kopfzeile soll **deutlich größer**
und auf **weißem Grund** stehen. Gemessen: bei Schriftgröße 96 ist das
Feld 543 px breit, also 50 % der Bildbreite; bei 170 sind es 899 px, also
83 % — links und rechts bleiben 90 px. Das ist die Größe, die er meint.
`--kopfzeile-groesse 170 --kopfzeile-hell`.
→ betrifft: content-*, YNB Cinema

## 22.10.2026 — Warum dieselben Fehler bei verschiedenen Agenten passieren

**Seine Frage, und sie ist berechtigt:** *„Ich verstehe nicht, warum hier
immer wieder dieselben Fehler passieren bei unterschiedlichen Agenten."*
Heute waren es drei auf einmal: Outro vergessen, Logo zu klein, Ton vom
Kameramikrofon.

**Die Antwort ist unangenehm einfach: es gab keine Liste.** Jeder von uns
hat sich das Schwierige gemerkt — Ausschnitt, Schnittgrenzen, Umbruch —
und das Selbstverständliche vergessen. Nichts im Werkzeug hat danach
gefragt.

**Zwei der drei Fehler waren überhaupt keine Geschmacksfragen, sondern
Messfehler:**

1. **Das Logo war nicht „zu klein gewählt", es war falsch gerechnet.**
   `marke/ynb-logo-weiss.png` ist 5224x2947 px groß, die Marke darin aber
   nur 1924 px breit — **36,8 % der Datei**, der Rest ist durchsichtiger
   Rand. Wer die Datei auf die 28 % Bildbreite aus seinem Preset skaliert,
   bekommt eine Marke von **111 px statt 302**. Der Renderer schneidet das
   Logo jetzt auf seinen sichtbaren Kasten zu, bevor er skaliert;
   `--logo-breite` meint ab jetzt die Breite der **Marke**.
2. **Das Outro lag die ganze Zeit in seinem Drive.** „YNB Podcast: Outro
   9:16", ProRes mit Alphakanal, 1080x1920, 4,2 s, die ersten 0,42 s
   durchsichtig. Niemand hat danach gesucht. Liegt jetzt als
   `video/marke/ynb-outro-9-16.mp4` (3,8 s, opak) im Repo, für alle.

**Und die Gegenmaßnahme, damit die Antwort nicht nur eine Einsicht bleibt:
`video/abnahme.py`.** Prüft einen fertigen Short vor der Übergabe auf
Format, **Abtastrate 48 kHz** (44,1 kHz heißt Kameramikrofon statt
Mischung), Laufzeit unter dem Shorts-Limit, **Outro am Ende** (Bildabstand
zum Outro-Schlussbild), Untertitel und Ortscheck. Was nur das Auge sieht —
Logogröße, Zeile unter der Lippe, Wortgrenzen, **den Ton wirklich
anhören** — steht als Haken darunter und wird nicht als „bestanden"
ausgegeben.
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

## 22.10.2026 — `-t` hinter dem `-i` begrenzt gar nichts

**Zweiter Befund derselben Sitzung, und der erste war nur die halbe
Ursache.** Nachdem die Zeitstempel auf null standen, stimmte der Einstieg
— die Laufzeit immer noch nicht: 52 s bestellt, 54 s geliefert.

`shorts-render.py` baute den Aufruf so:

    ffmpeg -ss 13 -i quelle.mp4 -t 52 ... -i logo.png ...

**ffmpeg ordnet Optionen der nächsten Datei zu.** `-t` stand hinter dem
`-i` der Quelle, also band es an den **nächsten** Eingang — das Logo — und
begrenzte nichts. Ohne `--logo` wäre es eine Ausgabeoption gewesen und
hätte zufällig funktioniert; **mit** Logo lief der Short bis zum Ende der
Quelle. Richtig ist `-ss 13 -t 52 -i quelle.mp4`, beides vor dem `-i`.
Geprüft: 6 s bestellt, 5,27 s geliefert bei Tempo 1,15 — genau die 5,2,
die herauskommen müssen.
→ betrifft: content-*, YNB Cinema, EA

**Was daran lehrreich ist:** der Fehler war unsichtbar, solange niemand
ein Logo einblendete, und unsichtbar, solange niemand die Laufzeit
nachrechnete. Zwei Bedingungen, die beide erfüllt sein mussten — und die
Shorts der Nachtrunde liefen über `--plan`, der diesen Zweig gar nicht
benutzt. Darum hat es tagelang niemand gemerkt.
**Regel: bei ffmpeg steht jede Option vor der Datei, für die sie gilt.
Wer eine Option hinter `-i` schreibt, meint die nächste Datei.**
→ betrifft: alle Content-Agenten

## 22.10.2026 — Ein Fenster aus dem Master behielt die Uhr des Masters

**Befund, gemessen.** `master_schnitt.py` holte ein Fenster aus dem
Drive-Master und schrieb die Pakete mit ihren **Originalzeitstempeln**:
`start_time=5775.0`, `duration=75.0`. Jedes Werkzeug danach rechnet aber
ab null. `--start 13` suchte also eine Stelle **vor dem ersten Bild**,
ffmpeg nahm stillschweigend den Anfang, und `-t` griff ebenfalls daneben.

**Drei Renderings liefen damit durch und sahen im Standbild richtig aus** —
der Gast spricht über die ganze Länge, also fällt am Einzelbild nichts
auf. Aufgefallen ist es erst an der Laufzeit: 6 s bestellt, 52 s geliefert;
10 s bestellt, 54 s geliefert; 52 s bestellt, 54 s geliefert. Drei
verschiedene Bestellungen, zwei identische Ergebnisse — **das** war der
Alarm, nicht das Bild.

`master_schnitt.py` zieht die Zeitstempel jetzt auf null (ein gemeinsamer
Versatz für Bild und Ton, sonst laufen sie auseinander) und schreibt in
die Ausgabe `Datei laeuft ab 0 (entspricht Master X)`.
**Wer ein Fenster aus einem Master zieht, prüft `start_time` der Ausgabe,
bevor er Zeiten hineinrechnet.**
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Und die Form dahinter, zum dritten Mal in zwei Tagen:** ein Standbild
beweist nichts über einen Ausschnitt. Die Laufzeit schon. Wer eine
Bestellung aufgibt, misst das Ergebnis gegen die Bestellung — bei
Drive-Bereichsabrufen, bei Fenstern aus dem Master, bei jedem Rendering.
→ betrifft: alle Content-Agenten

## 22.10.2026 — Die Ortsregel war zu eng, und drei Fehler im SRT-Rückweg

**Seine Präzisierung vom 21.10., die meine Liste von gestern korrigiert:**
*„Cape Town oder South Africa — ich möchte es halt nur nicht genauer
veröffentlichen."* Stadt und Land dürfen fallen. Meine erste Fassung hatte
beide gesperrt und hätte **jeden Short mit seiner Herkunftsgeschichte
blockiert** — und die ist ein Kernstück seines Materials. Gemeldet vom
Gastauftritte-Agenten, zu Recht.
`ortscheck.py` ist jetzt zweistufig: `GROB` (Cape Town, South Africa,
Western Cape, Tafelberg) wird **gezählt und berichtet**, `ORTE`
(Scarborough, Kommetjie, Misty Cliffs, Noordhoek, Fish Hoek, Muizenberg,
Kalk Bay …) **schlägt an**.
**Regel: eine Schutzliste, die mehr sperrt als verlangt, ist kein
vorsichtiger Fehler — sie nimmt ihm Material weg.** Im Zweifel das enger
Gemeinte sperren und das Weitere nur melden.
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Drei Fehler auf dem Rückweg über eine .srt, zwei davon bestätigt und
behoben:**
1. `--srt` zusammen mit `--srt-out` **brach mit einem KeyError ab**:
   `cues_als_srt` griff blind auf `c["woerter"]` zu, und Einblendungen aus
   einer .srt haben keine Wortzeiten. Jetzt fällt es auf den Text zurück.
2. **Die Zeitbasis wurde doppelt durchs Tempo gerechnet.** Eine .srt aus
   `--srt-out` steht schon in der Zeit des fertigen Videos; sie wurde beim
   Zurücklesen noch einmal geteilt. Einblendungen tragen jetzt
   `fertigzeit`, und wer sie trägt, wird nicht noch einmal skaliert.
   Geprüft: eine .srt durch den Renderer und zurück kommt zeitgleich an.
3. **Eine wiederverwendete .srt kostet das gelbe Aktivwort** — das stimmt
   und lässt sich nicht beheben: ohne Wortzeiten gibt es nichts
   hervorzuheben. Wer die Hervorhebung braucht, lässt neu transkribieren.
→ betrifft: content-*, YNB Cinema

**Und eine Meldung, die ich geprüft und verworfen habe.** Es hieß, der
Merge habe das Fragezeichen wieder abgestreift. Das stimmte für `66de26b`
und war in `01a27cb` schon behoben, bevor die Meldung kam: `SATZZEICHEN`
ist `.,!;:…`, und `_anzeige("safe?")` gibt `SAFE?`. Nachgesehen statt
geglaubt — und das Gegenteil wäre genauso wichtig gewesen.
→ betrifft: content-*

## 21.10.2026 — Whisper verschluckt Wiederholungen, und niemand merkt es

**Befund, gemessen am selben 80-Sekunden-Fenster derselben Datei:**

| `condition_on_previous_text` | Wörter | „you know" |
|---|---|---|
| `True` (die Vorgabe) | 170 | **0** |
| `False` | 188 | **7** |

Der Decoder nimmt den vorher erkannten Text als Vorlage und unterdrückt
dann Wiederholungen. Rick Strassman sagt „you know" im Sekundentakt —
eine ganze Fassung verlor dadurch **90 Wörter**, die Untertitel waren
lückenhaft, und **kein Werkzeug hat etwas gemeldet**. Aufgefallen ist es
nur, weil zufällig eine inhaltsgleiche zweite Fassung danebenlag: 612
Wörter gegen 520 bei identischer Tonspur und identischem Pegel.
**`condition_on_previous_text=False` steht jetzt in allen drei
Werkzeugen** (`shorts-render.py`, `fuellwoerter.py`, `schnittliste.py`).
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Die Folge davon ist schlimmer als der Fehler: eine Null, die durchläuft.**
`fuellwoerter.py` bekam dieses lückenhafte Transkript, fand **0 von 43**
Stellen, meldete „fertig" und legte eine Datei ab, die mit der Eingabe
identisch war. Der nächste Schritt rechnete damit weiter. Jetzt bricht es
bei null Funden ab und schreibt nichts.
**Regel: ein Werkzeug, das nichts gefunden hat, darf nicht „fertig"
melden.** Null ist ein Ergebnis, das begründet werden muss — bei
Füllwörtern, bei Schnittlisten, beim Ortscheck.
→ betrifft: alle Content-Agenten

**Und ein Fehler in der eigenen Messung, der die Spur fast verwischt hätte.**
Der erste Test sagte „kein Unterschied" (219 gegen 216 Wörter) und schien
die Vermutung zu widerlegen. Die Zählung war kaputt: `w.word` von
faster-whisper enthält ein führendes Leerzeichen, `" ".join(...)` macht
daraus zwei, und `"you know"` findet sich in `"you  know"` nie. Jede
Trefferzahl in dem Test war null, auch die richtige.
**Regel: eine Messung, die überall null zählt, misst nichts.** Bevor man
aus ihr schließt, prüft man sie an einem Fall, von dem man weiß, dass er
treffen muss.
→ betrifft: alle Content-Agenten

## 21.10.2026 — Gemeinsames Werkzeug gehört einem Branch

**`shorts-render.py` lag in drei Fassungen vor, keine davon vollständig:**
der Content-Assistant hatte Isabelles Preset, aber nicht die Kopfzeile;
der Chief of Staff hatte die Kopfzeile, aber nicht das Preset; der
cinematische Zweig keines von beidem. Zusammengeführt auf
`claude/content-assistant` — dort gehört es hin, und wer eine Erweiterung
baut, bringt sie zurück, **bevor** er weiterarbeitet.
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Beim Zusammenführen fiel etwas auf, das am Code nicht zu sehen ist:
Kopfzeile und Untertitel überlappen.** Das Feld sitzt mittig auf 68 % der
Höhe (1221–1390 px), die Zeile ohne gemessene Lippe auf 70 %
(1303–1385 px). In den ersten 4,5 Sekunden stehen sie übereinander — im
Testbild deutlich zu sehen, in beiden Quellfassungen unbemerkt, weil dort
nie beides zugleich lief.
**Der Renderer rechnet das jetzt aus und sagt es**, statt es zu riskieren:
er vergleicht das Feldband mit dem Band der Einblendungen, die während
der Kopfzeile laufen, und warnt mit beiden Zahlen. Verschoben wird von
Hand (`--kopfzeile-hoehe`) — wo die Kopfzeile sitzt, ist sein Geschmack,
nicht meine Messung.
→ betrifft: content-*, YNB Cinema

**Und die allgemeine Form davon:** zwei Einblendungen, die einzeln
richtig sitzen, können zusammen falsch sitzen. Wer ein zweites Element
ins Bild hängt, rechnet die Bänder gegeneinander — ein Blick auf ein
Standbild, in dem zufällig gerade keine Zeile steht, beweist nichts.
→ betrifft: alle Content-Agenten

## 21.10.2026 — Kein Short darf verraten, wo er wohnt

**Aus seinem eigenen Arbeits-Slack**, an seine Cutterin, 02.09.2026:
*„Vielleicht doch den Scarborough-Teil rausnehmen in diesem Short?
Gewisse Menschen müssen nicht so easy wissen wo wir wohnen."* Die Regel
stand in keinem unserer Werkzeuge und in keiner Prüfliste.

**Gilt für Bild, Ton und Untertitel:** Straßennamen, Viertel, erkennbare
Fassaden, Aussicht, Schilder, Ortsnamen im Gespräch.

**Der lesbare Teil ist jetzt geprüft, nicht nur versprochen.**
`video/ortscheck.py` sucht Untertitel und Transkripte nach Ortsnamen aus
seinem Umfeld ab, dazu nach zwei Formen, die eine Adresse verraten, ohne
einen bekannten Namen zu nennen (Hausnummer + Straßenname, „we live
in …"). Rückgabe 1 bei Fund, damit es in einem Lauf auffällt.
**Sechzehn Dateien durchlaufen — alle sauber:** die sechs
Meaningful-Shorts, das Sutcliffe-Stück, beide Rick-Fassungen und das
Aaronson-Transkript.

**Was das Skript nicht kann: das Bild.** Fassaden, Aussicht, Schilder
bleiben Augenarbeit vor jeder Abnahme. Ein grüner Lauf ist kein
Freibrief, sondern deckt genau die Hälfte ab, die sich lesen lässt.
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Und eine Zahl, die dagegen spricht und trotzdem hierhin gehört:** die
Ortsliste ist handgeschrieben. Sie findet, was sie kennt. Ein Ortsname,
den niemand eingetragen hat, läuft durch — der grüne Lauf oben beweist
also nicht, dass nichts drin ist, sondern nur, dass nichts Bekanntes
drin ist. Wer einen neuen Ort hört, trägt ihn nach.
→ betrifft: content-*

## 21.10.2026 — Sein Shorts-Preset ist der Maßstab, nicht unsere Messung

**Er hat den Ordner übergeben, mit dem seine Shorts bisher gebaut wurden**
(Schrift, Farbe, Maße, CapCut-Filter als LUT): *„ist jetzt der Filter und
die Schrift, die wir bisher für meine Shorts verwendet haben, kannst du das
jetzt ab sofort bitte auch einbauen und natürlich auch an YNB Cinema
Agenten und dann EA weitergeben."* Eingebaut in `video/shorts-render.py`,
dokumentiert in `video/preset-ynb.md`.

**Sechs Werte waren bei uns anders — und wir lagen sechsmal daneben:**

| | unsere Messung | sein Preset |
|---|---|---|
| Gelb | `#FFD530` | **`#F9F13A`** |
| Schriftgröße | 78 | **82** |
| Schrift | DejaVu Sans Bold | **Inter Black** (Ersatz für Eveleth aus CapCut) |
| Zeilenbreite | 1000 px | **777 px = 72 % der Breite** |
| Logo | 520 px, Höhe 0,845 | **302 px = 28 %, Höhe 0,87** |
| Gradation | warm, gesättigt | **entsättigt, kühl — Oppenheimer-Filter** |

Alle sechs waren an seinen veröffentlichten Shorts *abgelesen*, also an
komprimierten Vorschaubildern. Bei der Gradation drehte das Ergebnis sogar
die Richtung um: wir haben warm und gesättigt gemessen, sein Filter ist
entsättigt und kühl.
**Regel: an einem Ausgabebild abgelesene Stilwerte sind ein Notbehelf,
solange die Quelldatei des Stils nicht da ist. Bevor man misst, fragt man
nach der Vorlage.**
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Wer libass benutzt, darf die Zeilenbreite nicht mit PIL messen.** libass
legt die Schriftgröße nicht aufs Geviert, sondern auf Ober- plus
Unterlänge der Schrift — bei Inter Black 1,21 Geviert. Gemessen am
gerenderten Bild: `WHAT MAKES LIFE` ist bei 82 px **643 px** breit, PIL
sagt 776, Verhältnis 0,829; aus den Schriftmetriken errechnet 0,826.
Wer das übergeht, misst 21 % zu breit und teilt Dreizeiler, die längst
passen. Faktor: `groesse / sum(font.getmetrics())`.
→ betrifft: content-*, YNB Cinema, EA

**Die Zeilenhöhe hängt am Raum, nicht am Format.** Sein Preset setzt die
Untertitel fest auf 70 % der Bildhöhe. Für Rick Strassman (Webcam) war 50 %
richtig, im Just-Push-Record-Studio 57 %. Die 70 % sind deshalb hier der
Wert, wenn keine Lippe gemessen ist — die gemessene Lippe schlägt ihn.
→ betrifft: content-*, YNB Cinema

**Offen: die LUT selbst fehlt.** Übergeben wurden `make_lut.py` und die
Anleitung, nicht `luts/ynb_look.png` und nicht der CapCut-Export. Bis die
da ist, läuft eine Annäherung, und der Renderer schreibt das in die
Ausgabe, statt es zu verschweigen. `luts/hald_identity_1080.png` liegt
bereit und ist geprüft: durch `make_lut.py` zurückgerechnet kommt die
Identität pixelgenau wieder heraus.
→ betrifft: content-*, YNB Cinema, EA


## 21.10.2026 — Der Planer plant am Kameraschnitt nicht neu (Aaronson 01)

**Befund, gemessen.** `bildausschnitt.py` setzt einen Kasten und lässt ihn
laufen, bis sein eigenes Bewegungsmaß kippt. Im Aaronson-Short standen
**zwei** Einstellungen über 58 s, die zweite 56 s am Stück bei `650:0:608:1080`.
Solange die Regie auf Scotts Kamera bleibt, stimmt das. Schaltet das Studio auf
die Totale, zeigt derselbe Kasten Holzwand, Mikrofonarm und die Getränkedosen.

**Die Schnitte sind da, man muss sie nur holen.** `ffmpeg` mit
`select='gt(scene,0.25)'` fand im 110-s-Fenster **sechs** Kameraschnitte
(Fensterzeit 7,58 · 13,12 · 31,12 · 38,62 · 90,48 · 99,12). Die eigene
Bewegungsheuristik fand zwei.
**Regel: den Plan an jedem erkannten Kameraschnitt teilen, nicht an der
Bewegungsschwelle.**

**Scotts Position in der Totale, ausgemessen an zwei Totalen (Master 3361,5
und 3422,9) mit eingezeichnetem Raster:**

| | |
|---|---|
| Gesichtsmitte | **x ≈ 1467** im 1920er Bild (Nase 1393, Hinterkopf 1560) |
| Kopfoberkante | **y ≈ 413** |
| in der Nahaufnahme dagegen | x 930–970 |

**Die Position ist kamerafest** — in beiden Totalen dieselbe. Einmal
ausmessen reicht pro Folge.

**Zwei brauchbare Kästen, beide geprüft:**
- `1163:0:608:1080` — gleicher Maßstab wie die Nahaufnahmen, schärfste
  Variante, aber Scott sitzt tief im Bild (Kopf bei 0,38 der Höhe).
- `1242:280:450:800` — näher am Maßstab der Nahaufnahme davor, Kopf bei
  0,17. Hochskalierung 2,4× statt 1,78×.

**Einfrieren wäre hier falsch.** Die `tot`-Mechanik (Standbild überbrücken)
ist für Einstellungen gedacht, in denen die Person **nicht** zu sehen ist. In
der Totale ist sie zu sehen, nur woanders — dann folgt der Ausschnitt.
→ betrifft: content-*, alle Content-Agenten

**Zum Übergang: hier ist der harte Schnitt richtig, kein Schwenk.** Die Quelle
wechselt an dieser Stelle selbst die Kamera. Ein interpolierter Schwenk würde
eine Bewegung behaupten, die es im Bild nicht gibt, und über einen echten
Schnitt hinweglaufen. Ein Schwenk gehört nur dorthin, wo der Ausschnitt
**innerhalb** einer durchgehenden Einstellung wandert.
→ betrifft: content-*

**Und ein Verlust, der eine Regel wert ist.** Die Arbeitsdatei `clip_aa2.mp4`
lag in einem fremden Scratchpad und ist mit dessen Container verschwunden. Aus
der Dokumentation liess sich das Fenster rekonstruieren (Master 3340,7–3361,9
und 3375,3–3412,9, also die notierte „Rohzeit" minus 12,2 s), **aber nicht
exakt**: der Plan endet bei 58,145 s, die rekonstruierten Fenster ergeben
58,8 s. Die Differenz ist die von Hand entfernte 0,4-Sekunden-Einstellung,
deren Lage nirgends steht.
**Regel: wer eine Schnittfassung dokumentiert, notiert die Schnittliste in
Quellzeiten — jede entfernte Stelle mit Anfang und Ende.** Sonst ist die
Fassung nicht reproduzierbar, sobald der Container weg ist.
→ betrifft: alle Content-Agenten

**24.10. — Eine Kopfzeile ist keine Messung.** Die neun Tonstücke der
Logan-Folge lagen vollständig (zusammen 5159,1 s gegen 5159,5 s Quelle), aber
`ffmpeg -f concat -c copy` schrieb daraus eine FLAC, die im Header nur **ein**
Stück beschreibt. `ffprobe` meldete 10,0 Minuten für 86 Minuten Ton — und mein
eigener Lauf meldete dieselben 10 Minuten als „fertig". Die Daten waren alle
da; falsch war nur die Auskunft über sie.
**Regel: Laufzeit nie aus dem Header lesen, sondern durch einen Dekodierlauf
messen — und das Ergebnis gegen die Summe der Teile prüfen.** `ton_stueckweise.py`
kodiert jetzt beim Zusammenfügen neu und bricht ab, wenn Ergebnis und Summe mehr
als zwei Sekunden auseinanderliegen.
Das ist derselbe Fehler wie beim Wiederaufnehmen über Dateigrössen: eine Zahl,
die billig zu bekommen ist, beschreibt nicht das, wonach gefragt war.
→ betrifft: content-*, alle Content-Agenten

**Und noch eine, aus derselben Stunde: eine Bibliothek, die gestern ging, geht
heute nicht.** `faster-whisper` ruft intern `av.open(..., metadata_errors=...)`;
die hier installierte PyAV kennt den Parameter nicht und wirft `TypeError`.
Behoben, indem das Tonfenster mit ffmpeg selbst nach float32 dekodiert und als
Array übergeben wird — `transkript_stueckweise.py`. Das hängt an keiner
Bibliotheksversion mehr und macht die Fensterzeiten eindeutig, weil der Versatz
an einer Stelle im Code draufgerechnet wird.
→ betrifft: content-*

**Und die dritte aus derselben Stunde: ein abgekoppelter Prozess ist kein
laufender Prozess.** Der Transkriptlauf wurde mit `nohup … &` abgesetzt, lief
beim Nachsehen fünf Sekunden später nachweislich (zwei PIDs, Fenster 0 in
Arbeit) — und war 26 Minuten später samt leerem Log verschwunden, ohne ein
einziges fertiges Fenster. Grund: ein abgekoppelter Prozess wird nicht
mitgezählt, der Container wird eingezogen, sobald der Zug endet.
**Regel: lange Läufe nur als verfolgten Hintergrundlauf starten (`Bash` mit
`run_in_background`), nie mit `nohup … &`.** Nur der verfolgte Lauf hält den
Container und meldet sein Ende.
Dass der Lauf wiederaufnehmbar gebaut war, hat den Schaden auf 26 Minuten
begrenzt — fertige Fenster hätte er übersprungen. Es gab nur keine.
→ betrifft: content-*, alle Content-Agenten

**24.10. — Eine Schwelle, die an hellem Material geeicht wurde, findet im
dunklen Studio gar nichts.** `bildausschnitt.py` erklärte die ersten 85
Sekunden der Logan-Folge zu **einer** Einstellung; tatsächlich liegen darin
fünf Kameraschnitte. Die Regel verlangte, dass sich 45 % des Bildes ändern —
bei Sutcliffes hellem Set traf das zu (0,51–0,61 am Schnitt), in diesem fast
schwarzen Studio ändert sich beim Kamerawechsel nur der Bereich, in dem ein
Mensch sitzt: gemessen 0,26–0,29, alles andere höchstens 0,071. Der Renderer
bekam darum einen festen Ausschnitt und schnitt den Gast halb aus dem Bild.
**Regel: eine Schwelle, die aus einer Messung an einem Material stammt, gilt
für dieses Material.** Entweder sie wird am neuen Material nachgemessen, oder
sie wird relativ formuliert — hier: ein Sprung weit über das, was in *diesem*
Clip normal ist, neben der alten festen Schwelle, damit das helle Material
nichts verliert.

**Und im selben Zug eine Messung wieder ausgebaut, die nicht getrennt hat.**
Ich wollte die Stapel-Entscheidung („sind zwei Menschen im Bild?") auf eine
neue Grösse stützen: wie viel Bewegung in *einen* 9:16-Ausschnitt passt. Die
Werte über sechs Einstellungen, in denen nachweislich **immer nur eine**
Person sass: 0,60 · 0,63 · 0,71 · 0,78 · 0,81 · 0,90. Eine Grösse, die
denselben Fall über diese Spanne streut, trennt nichts — sie hätte nur
später falsch ausgesehen. Also raus, und stattdessen `--kein-stapel`
benutzt, das es für genau diesen Fall schon gibt.
→ betrifft: content-*, alle Content-Agenten

**24.10. — Eine halb umgesetzte Regel sieht aus wie eine umgesetzte.** Seine
Vorgabe vom 22.10.: die Schlussfrage „in einer Zeile, in einer Einblendung,
mit einem Fragezeichen". Eingebaut war dafür `FRAGE_BREITE` — eine breitere
Schranke für Zeilen, die auf `?` enden. Nur schlägt die Drei-Wort-Grenze diese
Schranke: „What makes life meaningful to you, Logan?" stand im Logan-Short in
**drei** Einblendungen. Die Regel war im Code, die Wirkung nicht.
Gemessen, statt geschätzt: die Zeile misst bei 82 px **1918 px**. In *eine*
Zeile passt sie nur bei rund 40 px — halbe Schriftgröße, und genau das hat er
für Einblendungen abgelehnt. Also ist „eine Zeile" hier nicht erreichbar; „eine
Einblendung mit dem Fragezeichen" ist es. Eine Frage läuft jetzt über bis zu
zwei Zeilen, bleibt aber **eine** Einblendung, bei voller Schriftgröße.
**Regel: eine Vorgabe ist erst erfüllt, wenn sie am fertigen Short nachgesehen
wurde — nicht, wenn der Code sie erwähnt.**
Und die Reparatur ging beim ersten Versuch daneben, auf dieselbe Art: ich habe
die Ausnahme ins Packen gebaut, nachgesehen — immer noch drei Einblendungen.
Erst die Messung an der echten Wortliste zeigte, wo es wirklich zerfällt: eine
Frage, die mit Sprechpausen gesprochen wird („What makes … life meaningful …
to you, Logan?"), ist **vor** dem Packen schon an den Pausen in drei Strecken
zerlegt; beim Packer kam nur noch `to you, Logan?` an. Die Ausnahme musste eine
Ebene früher stehen. **Wer eine Regel in die falsche Schicht baut, hat sie
nicht gebaut** — und merkt es nur, wenn er den Zwischenstand misst statt das
Ergebnis zu erwarten.
→ betrifft: content-*, alle Content-Agenten

**24.10. — Die Musikbett-Prüfung schlug an, und ich habe sie nicht
weichgeklopft.** Der Schwiegermutter-Short kam auf −64,7 dB im leisesten
Prozent, die Schwelle liegt bei −65. Der Sumo-Short aus derselben Folge kam
mit −65,3 durch. Der Unterschied ist keine Musik, sondern dass in den 45
Sekunden fast ohne Sprechpause geredet wird — der Boden wird nie tief.
Nachgemessen, **was** in diesem leisen Boden liegt: spektrale Flachheit 0,085,
gegen 0,078 und 0,088 bei den nachweislich sauberen Shorts derselben Folge.
Gleicher Raumton, kein tonales Bett.
**Die Schwelle bleibt trotzdem, wo sie ist, und der Short bleibt durchgefallen.**
Die Prüfung meldet die Flachheit jetzt zusätzlich — als Angabe, nicht als
Freispruch. Eine Sicherheitsregel lockert man nicht, weil die eigene Messung
das eigene Vorhaben stützt; sein Ohr entscheidet.
→ betrifft: content-*, alle Content-Agenten

**26.10. — Zwei Befunde aus der Kingsbury-Prüfung, die für jeden gelten.**

**Eine Sperre ist nur so gut wie ihre Grenze.** Die Stelle, die ohne sein Wort
nicht angefasst wird, war mit **71:01** notiert. Nachgemessen am Transkript
beginnt sie **70:54** — der Satz, mit dem er sie eröffnet, lag außerhalb der
eigenen Sperre, und ein Clip, der bei 71:00 endet, hätte ihn angeschnitten.
**Regel: wer eine Stelle sperrt, misst ihre Grenze am Text nach und fasst sie
breiter, nicht knapper.** Jetzt 70:45–73:30.
→ betrifft: alle Content-Agenten

**Eine Zeitmarke aus einem Plan ist ein Hinweis, keine Fundstelle.** Neun der
zehn Kingsbury-Short-Kandidaten sind wörtlich belegt — aber **teils 15 bis 30
Sekunden später als notiert** (Flow 10:00→10:15, „Not yet" 15:48→15:53, Erbe
36:34→37:13). Und ein Clip-Anfang lag im falschen Thema: Clip 3 war mit 53:16
notiert, dort läuft aber noch die Ayahuasca-Passage; der Kampf beginnt 54:09.
**Regel: jede notierte Zeit vor dem Schnitt am Transkript nachschlagen, auch
wenn der Plan vom selben Agenten stammt.**
→ betrifft: alle Content-Agenten

**26.10. — Und eine aus dem Renderer, gemessen statt übernommen.** Aus dem
Lernkanal kam: Bildstücke müssen ganzzahlig lang sein. An meinen fünf
Logan-Shorts nachgemessen, bevor ich es geglaubt habe: die Stücklängen hatten
bei 29,97 fps Reste von **0,13 bis 0,96 Bildern**, und an **zwei von drei**
Nahtstellen standen zwei Bildsprünge statt einem. Der Fehler war also da.
`bildausschnitt.py` legt jede Einstellungsgrenze jetzt auf ein Vielfaches von
1/fps; weil das Bildraster des Clips bei 0 beginnt, sind die Längen damit von
selbst ganzzahlig. **Entscheidend ist die Länge jedes Stücks, nicht die
absolute Quellzeit.**
Die zweite Regel von dort — unter etwa einer halben Sekunde keine eigene
Einstellung — war schon erfüllt: `mindestdauer` steht auf 0,6 s, und die
kürzeste Einstellung in meinen fünf Shorts ist 1,2 s. Geprüft, nicht
angenommen.
→ betrifft: content-*
