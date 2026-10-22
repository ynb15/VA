# Lernkanal — Vlog Content Assistant

Geschrieben auf `claude/content-vlog`, nur von mir. Neueste Einträge unten.
Jeder Eintrag mit Zahl oder wörtlichem Zitat. Fortschrittsmeldungen gehören
nicht hierher.

---

## 21.10.2026 — Wo die Frage „What makes life meaningful?" sitzt

**An acht Folgen gemessen, nicht geschätzt.** Masterzeit der Frage gegen
Gesamtlaufzeit; bei Francis Chouler veröffentlichte Zeit, weil es keinen Master
mehr gibt.

| Gast | Frage bei | Gesamt | vom Ende | Anteil |
|---|---:|---:|---:|---:|
| David Sutcliffe | 7222,0 | 7518,0 | 296,0 s | 96,1 % |
| Scott Aaronson | 5894,3 | 6138,0 | 243,7 s | 96,0 % |
| Ken Stern | 6150,1 | 6333,4 | 183,3 s | 97,1 % |
| Logan Gonzalez | 4957,1 | 5159,5 | 202,4 s | 96,1 % |
| Matt Defina | 6474,7 | 6572,3 | 97,6 s | 98,5 % |
| Rick Strassman | ~7100 | 7251,8 | ~151,8 s | 97,9 % |
| Kyle Kingsbury | 7485,8 | 7790,0 | 304,2 s | 96,1 % |
| Francis Chouler | 4112,0 | 4239,0 | 127,0 s | 97,0 % |

**Das Muster ist eng: 96,0–98,5 % der Folge, immer in den letzten fünf Minuten.**
Der Abstand vom Ende liegt zwischen **98 und 304 Sekunden**, Median 193.

**Die brauchbare Regel daraus:** rückwärts vom Ende in 210-Sekunden-Stücken
suchen — **ein Fenster fängt 5 von 8, zwei Fenster fangen 8 von 8.** Wer die
Frage sucht, braucht also im Regelfall 420 Sekunden vom Ende, nicht mehr. Das
sind rund 500 MB Abruf je Folge statt eines Blindflugs durch die ganze Datei.
→ betrifft: content-shorts, content-cinematic, alle, die eine feste Frage in
einer langen Folge suchen

**Die Antwort ist 38–78 Sekunden lang** (Masterzeit, sieben gemessene Stücke;
Median 59 s). Bei Tempo 1,2 werden daraus 32–65 Sekunden fertiges Stück. **Eine
feste Ziellänge ist deshalb falsch** — zweimal ist der automatische Schluss
genau daran ins Outro gelaufen („wo findet man dich", Instagram, Spotify).
Auf das letzte Satzende vor der nächsten Frage schneiden.
→ betrifft: alle Content-Agenten

## 21.10.2026 — YouTube-Transkripte: wortgenau, aber seit heute gesperrt

**Alfreds Frage, beantwortet.** Zwei Teile, und sie fallen unterschiedlich aus.

**Taugen sie? Ja, für das Finden — nein für das Schneiden.** Die automatischen
Untertitel sind **wortgenau**; die Zeitstempel stehen cue-weise alle 2–3
Sekunden. Für „wo in der Folge steht diese Stelle" reicht das vollkommen. Für
den Schnitt nicht: die Ein- und Ausstiege wären auf ±3 s genau, und ein Einstieg
drei Sekunden zu früh zeigt drei Sekunden Vorredner.
**Zum Vergleich: sein eigenes Vorbereitungsdokument lag bei Sutcliffe zwölf
Minuten daneben** (`1:40:00` notiert, tatsächlich 01:52:04). Das Transkript ist
also um Größenordnungen besser als die Kapitelliste — und trotzdem keine
Schnittvorlage.

**Seit dem 21.10. kommt man nicht mehr heran.** Am 19.10. holte
`video/yt-transkript.py` die Untertitel ohne Anmeldung. Heute antwortet YouTube
auf denselben Abruf mit **„Sign in to confirm you're not a bot"**. Vier
Abspielclients durchprobiert:

| Client | Ergebnis |
|---|---|
| Standard, `android_vr` | Botprüfung |
| `tv` | „The page needs to be reloaded." |
| `web_safari`, `mweb` | **Titel und Metadaten ja — Untertitelliste leer** |

Die Kanalliste über `--flat-playlist` geht weiter (Titel, Länge, Aufrufe,
IDs — damit ist `video/youtube-kanal.md` weiter herstellbar).
**Wer also noch ein Transkript im Repo liegen hat, soll es nicht wegwerfen.**
Zwei liegen dort: `swZGLesMb8Y` (Francis Chouler) und `frNOUgxE0IM` (Sutcliffe),
beide am 19./20.10. geholt. Francis' Archivzeile konnte nur deshalb ohne
Videodatei fertig werden.
→ betrifft: alle, die mit veröffentlichten Folgen arbeiten

## 21.10.2026 — Zum Ausschnittsplaner: die Meldung trifft, die Begründung nicht

**Gemeldet war:** der Planer plane an einem Kameraschnitt nicht neu, im
Aaronson-Short habe ein fester Kasten 56 Sekunden am Stück gelaufen.

**Am eigenen Stück nachgesehen, und so stimmt es nicht.** Kyle Kingsbury,
70 Sekunden, `bildausschnitt.py --zoom 1.15 --kein-stapel`: der Plan enthält
**sieben Einstellungen**, Grenzen bei 4,6 / 21,0 / 32,0 / 52,1 / 63,1 / 66,1 s.
Der Kasten springt von x=360 auf 1044 auf 1200 auf 1080 auf 1392. **Die
Schnitterkennung arbeitet.**

**Der Fehler liegt woanders, und er ist echt.** In der **Totale** setzt der
Planer den Kasten auf den Bewegungsgipfel, und der ist die gestikulierende Hand,
nicht das Gesicht. Nachgemessen mit eingezeichnetem Kasten auf ausgelesenen
Einzelbildern:

| Clipsekunde | Einstellung | Kasten | was im Fenster steht |
|---|---|---|---|
| 10 | Nahaufnahme | `1044:141` | Gesicht mittig, richtig |
| **26** | **Totale** | **`1200:141`** | **Kopf am rechten Rand abgeschnitten**, davor Bücherregal |
| 57 | Totale | `1392:141` | im Bild, aber außermittig |
| 68 | Nahaufnahme | `960:141` | Gesicht mittig, richtig |

Bei 26 und 57 Sekunden ist es **dieselbe Totale** — und die Kästen liegen
192 px auseinander. Das Maß `mitte` steht in beiden auf **0,07**, also weit
unter dem Bereich, der laut Messung eine Totale kennzeichnet (0,22–0,28). Der
Planer erkennt die Totale, aber das Maß trägt die Entscheidung nicht.

**Es ist dasselbe wie „Der Bewegungsgipfel ist nicht das Gesicht" aus Ausgabe 1,
nur in der Totale statt in der Nahaufnahme** — und dort ist es schlimmer, weil
der Kopf im Breitbild klein ist und schon 150 px Versatz ihn halbieren.

**Gegenmittel ohne eine Zeile neuen Code: `--kein-stapel` weglassen.** Dann
werden aus denselben Totalen zwei gestapelte Kästen à 850×756, einer je Person.
Für dieses Studio ist das auch inhaltlich richtig: die beiden sitzen weit
auseinander, eine Tür dazwischen, **ein 528-px-Fenster im 1920er Bild kann sie
gar nicht beide fassen.**
→ betrifft: content-shorts, content-cinematic, thumbnails

**Offen, und bewusst nicht gebaut:** im Stapel weiß das Werkzeug nicht, wer
gerade spricht. Das wäre der eigentliche Fortschritt, ist aber nicht bestellt.

## 21.10.2026 — Zwei Studiokameras steigen vor dem Ende aus

**Zweimal derselbe Fall, beide Male genau dort, wo die Abschlussfrage liegt.**

| Folge | Kameradatei | Länge der Datei | Länge des Gesprächs |
|---|---|---:|---:|
| Kyle Kingsbury | `1mQjt0g5GVptvEDVY8w3mVN2Qa8NFlTnp` (YNB), 4K | **77:12** | 129:50 |
| Marian Goodell | Kameraton bricht ab | **~60 min Ton** | ~120 min |

Bei Kyle fehlen **52 Minuten**, bei Marian die zweite Stunde Ton — er hat es am
21.10. selbst berichtet: *„die Kamera, die den Ton aufgenommen hat, die ist nach
einer Stunde irgendwie ausgegangen."*

**Regel daraus: vor dem Suchen die Laufzeit der Datei gegen die Laufzeit der
Folge prüfen.** Das kostet einen Abruf des Dateikopfes — **gemessen 8,0 MB bei
der 1,3-GB-Datei, 17,7 MB bei der 17-GB-Datei** — und erspart die Suche in einem
Material, das die gesuchte Stelle gar nicht enthält. Die Laufzeit steht im
Containerkopf (`av.open(...).duration`), nicht erst nach dem Laden.
→ betrifft: alle, die aus Studio-Mastern schneiden

## 21.10.2026 — Der Dateibeginn eines Fensters ist nicht der bestellte Start

`master_schnitt.py` setzt auf das **Schlüsselbild vor** dem bestellten Start.
Die Fensterdatei beginnt also früher, und Fensterzeit 0 liegt dort. Wer die
Masterzeitmarke als `bestellter Start + Fensterzeit` rechnet, liegt **bis zu
6 Sekunden daneben** — der Abruf begrenzt den Vorlauf auf `start - 6`.

Bei einer Antwort von 30 bis 60 Sekunden ist das der halbe Einstieg. Der Abruf
**meldet den tatsächlichen Beginn ohnehin** auf der Standardausgabe
(`Datei beginnt bei Master 7369.79s`); er wurde nur verworfen, weil der Aufruf
mit `capture_output=True` lief. Jetzt wird er ausgelesen und je Fenster in
`<k>_f<v>.beginn` abgelegt. Fehlt er, bleibt die Zeitmarke **leer** statt falsch.
→ betrifft: alle, die `master_schnitt.py` benutzen

## 21.10.2026 — Nachtrag, zwei Korrekturen an meinen eigenen Einträgen oben

**Erstens: `ton_holen.py` ist kein billiger Weg, eine Stelle zu suchen.** Ich
hatte es dafür erwogen, weil aus 16,1 GB rund 150 MB FLAC werden. **Die 150 MB
sind die Ausgabe, nicht der Abruf.** Das Werkzeug liest die Datei *ganz*
sequentiell durch — bei Rob Bennetts 34-GB-Master wären das 34 GB und damit
mehr als das Tageslimit, für eine Suche. Grund steht im Werkzeug selbst:
`demux(audio)` überspringt die Videopakete nicht, der mov-Demuxer liest sie
trotzdem. **Tonspur holen lohnt nur, wenn dieselbe Folge mehrfach durchsucht
wird** — einmal 34 GB gegen beliebig oft transkribieren. Für einen einzelnen
Treffer am Ende ist das Fenster über `master_schnitt.py` richtig.
→ betrifft: alle, die aus Drive-Mastern suchen

**Zweitens: mein „zwei Fenster fangen 8 von 8" gilt für acht Folgen, nicht für
neun.** Rob Bennett bricht es. In den letzten 420 Sekunden seiner Folge stehen
Reue, Rückblick und Verabschiedung — *„Thank you so much, Rob. Book him before
you die"* — und **keine Frage nach dem Sinn.** Er war der erste Gast überhaupt
(Januar 2026); möglich, dass das Ritual damals noch nicht bestand. Das ist meine
Vermutung, keine Messung.

**Die Kosten der Suche hängen an der Bitrate, nicht an der Dateigröße.** Gemessen
am 21.10.: ein 210-Sekunden-Fenster kostet bei Kyles 1,3-GB-Export **35 MB**, bei
Bennetts 34-GB-Master **580 MB**. Das ist Faktor 17 für dasselbe Zeitfenster.
**Wer blind rückwärts sucht, muss das vorher ausrechnen** — sieben Versuche à
580 MB sind 4 GB für eine Folge, bei einem Tageslimit von rund 28 GB pro
Eigentümer. Die Suche ist deshalb jetzt auf **vier Fenster (840 s)** gedeckelt;
das deckt das Dreifache des größten gemessenen Abstands. Wird nichts gefunden,
legt das Werkzeug einen Befund mit Grund ab, statt es bei jedem Lauf neu zu
versuchen.
→ betrifft: alle, die aus Drive-Mastern suchen

**Drittens, zur Wiederaufnahme:** das Werkzeug hatte am Vorhandensein der
*Fensterdatei* erkannt, was erledigt ist. Falsch — erledigt ist ein Fenster,
wenn sein *Transkript* vorliegt. Ich hatte zwei durchsuchte Fensterdateien
gelöscht, um Platte frei zu machen, und der nächste Lauf hätte sie für 1,1 GB
noch einmal geholt, obwohl die Transkripte danebenlagen. Jetzt entscheidet das
Transkript.
→ betrifft: alle, die wiederaufnehmbare Läufe bauen

## 21.10.2026 — Die feste Ziellänge war die Ursache, nicht die neue Frage

**Vierter Fall derselben Art, und erst der zeigt die Wurzel.** Bisher hieß die
Erklärung: der Schnitt läuft ins Outro, weil die Endpunktwahl eine feste
Ziellänge nimmt statt bis zur nächsten Frage zu schneiden. **Das war zu kurz
gedacht.** Bei Eben Britton stand 108 Sekunden lang *keine* neue Frage — also
entschied die Ziellänge von 72 Sekunden, und zwar mitten in einer ganz anderen
Antwort: dem Byron-Katie-Werkzeug *„is it true?"*. **25 Sekunden über das Ende
des Bogens hinaus.**

| Gast | Antwort endet | geschnitten wurde bis | daneben |
|---|---:|---:|---:|
| Kyle Kingsbury | 177,59 | 186,39 | **8,8 s** in die Community-Ankündigung |
| Eben Britton | ~97 | 123,70 | **25,4 s** in eine andere Antwort |

**Drei Dinge, die zusammen tragen:**

1. **Die Ziellänge entscheidet nichts mehr.** Sie ist nur noch Obergrenze für
   den Fall, dass kein Übergang gefunden wird — 100 s, weil die längste
   gemessene Antwort Aaronsons mit 78 s Masterzeit war. Geschnitten wird auf
   das **letzte** Satzende vor dem Übergang, nicht auf das nächstgelegene an
   einer Wunschlänge. Wie lang die Antwort ist, entscheidet der Gast.
2. **Der Übergang steht nicht immer am Anfang eines Abschnitts.** Bei Britton
   steckt *„and to close it off"* im selben Whisper-Abschnitt wie sein
   Schlusssatz: *„Buntu baby. That's it. That's it and to close it off."* Die
   Lage wird deshalb über den **Zeichenabstand** im Abschnitt geschätzt
   (Wortzeiten liefert Whisper hier nicht) — das ergibt 97,0 statt 94,5 und
   hält damit genau die Pointe im Stück.
3. **Der gemessene Übergangspunkt ist selbst ein gültiger Schnittpunkt**, und
   der bessere, wenn das letzte Satzende deutlich davor liegt. Liegt es dicht
   daran (Kyle: 0,25 s), bleibt es beim Satzende.

**Und ein Fallstrick, der mir dabei in die Falle gegangen ist:** die Kandidaten
liefen ab dem Abschnitt der Frage selbst. **Die Frage endet auf ein
Fragezeichen** und war damit das einzige „Satzende", weil Whisper bei Britton
*keinen einzigen* Antwortabschnitt interpunktiert hat. Der Schnitt wäre 6
Sekunden lang geworden. Kandidaten ab `idx + 1`.
→ betrifft: alle, die einen Bogen automatisch beenden

## 21.10.2026 — Dritte Kamera, die vor dem Ende aussteigt

Whitney Wheelocks Zweier-Kamera `(Whit & YNB)` läuft **61:53** bei einer Folge
von **104:07** — sie endet 42 Minuten vor dem Gespräch, die Abschlussfrage steht
dort gar nicht drin. Gesucht wurde trotzdem, 840 Sekunden weit, für nichts.
**Die beiden Einzelkameras laufen 114:00 und 113:56**, decken die Folge also.

Damit sind es **drei von drei geprüften Mehrkamera-Aufnahmen**, bei denen eine
Datei vorzeitig endet: Kyle (77:12 statt 129:50), Marian (Ton nach ~60 von
~120 min), Whitney (61:53 statt 104:07).

**Regel, jetzt belastbar: bei Mehrkamera-Material zuerst die Laufzeit *jeder*
Datei gegen die Laufzeit der Folge halten, dann die längste nehmen.** Kostet
8–23 MB je Datei und erspart eine Suche im falschen Material. Und: **die
Zweier-Kamera ist nicht automatisch die beste Quelle**, auch wenn sie
inhaltlich die schönste wäre.
→ betrifft: content-shorts, content-cinematic, alle mit Studio-Material

## 21.10.2026 — Welche Master abrufbar sind, vorher abfragen

`get_file_permissions` beantwortet in einem Aufruf, was der Bereichsabruf sonst
erst nach dem Fehlschlag zeigt. **Ohne `{"role":"reader","type":"anyone"}` ist
eine Datei über `drive_fernzugriff.py` nicht erreichbar** — der Abruf bekommt
dann rund **921 KB HTML statt 8 MB Nutzdaten** (Curtis 920.758 Bytes, Makhosi
921.335 Bytes). Das ist ein anderer Fehler als das Tageslimit, das als
**2040-Byte-Seite mit HTTP 200** kommt. Beide fängt der Längenprüfer ab.

**Nützlich wurde es sofort:** Curtis Cranes eigener 2,0-GB-Export ist *nicht*
freigegeben, der 33,2-GB-Rohschnitt im Drive des Cutters aber schon. Statt
„blockiert" war es ein Quellenwechsel.
→ betrifft: alle, die aus Drive-Mastern lesen

## 21.10.2026 — Der Zwischenspeicher hing an der Folge, nicht an der Quelldatei

**Beinahe-Fehler, in der eigenen Änderung von heute, und er hätte wie ein
Treffer ausgesehen.** Die Suchfenster hießen `<folge>_f<n>.mp4/.json`. Als
Whitney Wheelocks Quelle von der Zweier-Kamera auf die Gastkamera umgestellt
wurde, lagen die Transkripte der **alten** Kamera noch unter genau diesen Namen
— und da die Wiederaufnahme am Transkript entscheidet (richtig, siehe oben),
hätte der nächste Lauf sie stillschweigend weiterbenutzt. Gesucht worden wäre
also in einem Material, das 42 Minuten vor dem Gespräch endet, **mit dem
Ergebnis eines Fehlschlags, der nach einem Befund aussieht.**

**Die Quelle gehört in den Namen:** `<folge>_<id8>_f<n>`. Dann sind Dateien
einer anderen Quelle schlicht nie ein Treffer. Die 19 vorhandenen Fenster
wurden umbenannt statt neu geholt — das hätte sonst mehrere Gigabyte gekostet.
→ betrifft: alle, die wiederaufnehmbare Läufe mit Zwischenspeicher bauen

**Und der zweite Teil desselben Fehlers:** ich habe die Dateien umbenannt,
während der alte Lauf noch lief. Der suchte weiter unter den alten Namen und
hätte Brittons 911-MB-Fenster neu geholt. Rechtzeitig gestoppt, aber
**Dateinamen ändern, während ein Lauf sie benutzt, ist dasselbe wie den Boden
unter ihm wegziehen.** Erst anhalten, dann umbenennen, dann starten.
→ betrifft: alle

## 21.10.2026 — Whisper lässt den letzten Abschnitt fallen, wenn der Ton dort endet

Kyles Stück endet auf *„I got nothing else to add to that."* — **im Ton, nicht
im Untertitel.** Gemessen: der Rohschnitt läuft 61,6 s, die Untertitel enden bei
51,1 s von 51,3 s Hauptteil; der Satz liegt bei Clipsekunde 60,0–61,6 und steht
in **keiner** Einblendung.

**Er ist da, und das ist gemessen, nicht vermutet:** Pegel in diesem Fenster
**−27,1 dB** gegen −24,3 dB in „that's really it" und −15,2 dB im lauten Teil.
Also leise Sprache, keine Stille. Die Suche hatte den Satz auch sauber erkannt
(Abschnitt 175,99–177,59 im Fenstertranskript) — **dort lief das Material
danach weiter.** Beim Untertiteln endet die Datei direkt hinter dem Satz, und
Whisper gibt den angebrochenen letzten Abschnitt nicht mehr aus.

**Was das praktisch heißt:** bei einem Stück, dessen Pointe die letzten ein bis
zwei Sekunden sind, fehlt genau dort die Zeile. Die sechs Stücke vom 20.10.
haben dasselbe in klein — ihre Untertitel enden 0,2–0,5 s vor dem Stück, weil
dort kein eigener Satz mehr steht. **Nicht ungefragt umgebaut**: der saubere Weg
wäre, dem Renderer das Suchtranskript mitzugeben statt neu zu transkribieren.
→ betrifft: alle, die mit --auto-captions arbeiten

## 21.10.2026 — Die Antwort läuft über die Fenstergrenze

**Whitney Wheelocks Stück endete mitten im Satz** — *„…the word for fear and
ignorance is that by"*. Der Befund sagte, warum: Schnitt bei **211,29 s** bei
einer **Fensterlänge von 211,13 s**. Der Schnitt stand auf der Fensterkante,
nicht am Ende des Bogens.

**Das ist ein eigener Fehler, kein Sonderfall.** Wer rückwärts in Stücken sucht,
findet die Frage irgendwo im Fenster — und eine Antwort von 68 Sekunden, die
55 Sekunden vor der Fensterkante beginnt, läuft zwangsläufig hinaus. **Der
Zuschnitt endet dann stumm an der Kante und sieht aus wie ein Ergebnis.**

**Das Gute: das Anschlussfenster liegt schon da.** Gesucht wird rückwärts, das
Fenster `v-1` ist also näher am Folgenende und bereits geholt. Transkripte
aneinanderhängen (versetzt um die gemessene Fensterlänge), und wenn der Schluss
hinter der Kante liegt, die beiden MP4s über den `concat`-Demuxer zusammensetzen
und daraus schneiden. **Kostet keinen einzigen zusätzlichen Abruf.** Die
Masterzeit hinter der Kante zählt dann vom Beginn des Anschlussfensters.

**Prüfung, ob so etwas vorliegt, in einer Zeile:** `fenster_bis` gegen die
Fensterlänge halten. Liegt es dichter als ein, zwei Sekunden an der Kante,
ist der Schnitt mit großer Wahrscheinlichkeit abgeschnitten und kein Ende.
→ betrifft: alle, die in Fenstern aus einem langen Master suchen

## 21.10.2026 — Eine Frage fängt nicht mit einem Fragewort an

Nachdem die Fenstergrenze überbrückt war, lief Whitneys Stück **zu weit**: bis
in seine Nachfrage *„So you don't agree that a cute little poodle called Mauro
doesn't make life a little bit more meaningful?"*. Zwei Gründe auf einmal —
sie beginnt mit *„So"* (kein Fragewort), und **das Fragezeichen steht zwei
Whisper-Abschnitte später**.

**Also wird ab einem Abschnitt der ganze Satz zusammengesetzt** (bis zum
nächsten Satzzeichen, höchstens 12 Sekunden) und dieser geprüft, nicht der
einzelne Abschnitt.

**Und sofort der Gegenfehler, am selben Material gemessen:** mit *„so"* in der
Öffnerliste brach Kyle Kingsburys Stück bei **31 statt 61 Sekunden** ab — sein
eigener Satz *„So when you speak about the infallible nature of God … it's
beyond language, right?"* beginnt mit „so" und endet acht Sekunden später auf
ein Fragezeichen. **Ein rhetorisches „right?" am Satzende ist in diesen
Antworten der Normalfall, nicht die Ausnahme.**

**Die Eingrenzung, die beides löst:** *„so"* zählt nur, wenn direkt ein Frage-
oder Anredewort folgt (`so you`, `so do`, `so is`, …). *„So when"* fällt damit
heraus, *„So you don't agree"* nicht. **An allen drei Stücken gegengeprüft:**
Wheelock 224,41 · Kyle 177,59 · Britton 97,25 — alle drei auf dem richtigen
Satzende.
→ betrifft: alle, die einen Bogen automatisch beenden

## 21.10.2026 — Zwei von elf Folgen haben die Frage nicht

| Folge | durchsucht | Ergebnis |
|---|---|---|
| Rob Bennett | 840 s, 1,74 GB | Reue, Rückblick, Verabschiedung — keine Sinnfrage |
| Curtis Crane | 840 s, ~2,5 GB | Schlussbotschaft an die Trans-Bewegung, dann Abmoderation |

**Beide Male sind die Fenster lückenlos und vollständig** — bei Curtis
nachgemessen: 5751,3 → 6593,0, vier Fenster à 210–212 s, keine Lücke, und das
letzte endet auf *„Ladies and gentlemen, this was Dr. Curtis Crane."* Es fehlt
also nicht Material, sondern die Frage.

**Eine Chronologie-Erklärung trägt nicht.** Rob Bennett war Folge 01 (Januar),
Curtis Crane Folge 07 (August) — aber Francis Chouler als Folge 02 (März) hat
die Frage, belegt über sein Transkript. **Er stellt sie also nicht jedes Mal.**
Das ist die sparsamste Erklärung, und sie ist zu bestätigen, nicht zu glauben.

**Praktisch heißt das: ein ergebnisloser Lauf ist ein Ergebnis.** Deshalb legt
das Werkzeug auch dann einen Befund mit Grund und durchsuchtem Bereich ab —
sonst sucht jeder spätere Lauf dieselben 2,5 GB noch einmal.
→ betrifft: alle, die eine feste Frage über viele Folgen suchen

## 21.10.2026 — Zwei eigene Fehler derselben Familie: nebeneinander laufen lassen

**Erstens, schon einmal passiert und trotzdem wiederholt:** ich habe einen neuen
Lauf gestartet, ohne den alten zu stoppen. Beide schrieben dieselben Dateien.
Der alte trug noch die vorige Fassung des Codes im Speicher und hat den Befund
mit der **falschen Zeitmarke überschrieben** — 224,41 statt 223,28. Gemerkt habe
ich es nur, weil ich die Zahl gegen meine eigene Nachrechnung gehalten habe.
**Ein Hintergrundlauf ist erst beendet, wenn `ps` ihn nicht mehr zeigt**, nicht
wenn der nächste gestartet ist.

**Zweitens, beim Reparieren genau dieses Fehlers:** beim zeilenweisen Ersetzen
blieb die **alte** Zuweisung `versatz = dauer(fenster)` eine Zeile unter der
neuen stehen und hat sie überschrieben. Syntaktisch einwandfrei, Prüfung grün,
Ergebnis falsch. **Eine Prüfung auf Syntax ist keine Prüfung auf Wirkung.**
Was gegriffen hätte: `grep -n versatz` nach dem Patch — zwei Zuweisungen
derselben Größe in zwei aufeinanderfolgenden Zeilen sind sofort sichtbar.

**Die Zahl, die es aufgedeckt hat, war die, die nicht passte.** Ich hatte vorher
von Hand 223,28 ausgerechnet; der Befund sagte 224,41. Hätte ich nur geschaut,
ob das Stück „jetzt länger ist", wäre es durchgegangen.
→ betrifft: alle

## 21.10.2026 — Ein Verhörer korrigiert sich nicht von selbst, aber large-v3 hört besser

**In Whitney Wheelocks Antwort standen drei Verhörer**, und der Weg zu ihnen ist
übertragbar.

| im Untertitel | tatsächlich | womit belegt |
|---|---|---|
| UP BY SAME SORRY I'VE BEEN HERE | **avidya** | dieselbe Stelle noch einmal transkribiert — `medium` schreibt dort von selbst „sorry, avidya" |
| THE TIME CHURCH WOULD SAY | **the Tantrics would say** | `large-v3`, bestätigt von einem zweiten `medium`-Lauf mit anderem Ausschnitt |
| SO I'D LIKE THE IGNORANCE | **so Advaita, ignorance** | `large-v3` |

**Mein erster Vorschlag für „the time church" war „the Tao Te Ching".** Klingt
plausibel, passt zum Thema — und ist falsch. Aufgefallen ist es nur, weil ich
ihn nachgeprüft habe, statt ihn einzutragen. **Eine Korrektur, die man sich
zusammenreimt, ist genauso ein erfundener Name wie ein erfundener Sprecher.**

**Der übertragbare Teil:** `large-v3` löst auf, woran `medium` scheitert —
Fachbegriffe und Namen, also genau das, was in der Korrekturliste landet.
Der Renderer arbeitet mit `medium`, und das soll so bleiben (schnell, und es ist
der abgenommene Stand). **Aber für die Prüfung eines verdächtigen Wortes ist
`large-v3` auf zwanzig Sekunden Ton die billigste Zweitmeinung, die es gibt** —
kein Download aus dem Netz nötig, das Modell lädt beim ersten Aufruf.

**Faustregel:** klingt eine Stelle im Untertitel nach Unsinn, ist sie Unsinn.
Zwanzig Sekunden mit `large-v3` nachhören, dann in `video/korrekturen.txt`.
→ betrifft: alle Content-Agenten

## 21.10.2026 — `--kopfzeile-hoehe` ist die Mitte, und die Vorgabe kollidiert

**Wer `--kopfzeile` mit lippenfolgenden Untertiteln benutzt, verdeckt sie.**
Am gerenderten Bild gemessen, Sutcliffe-Short, 1080×1920:

| | Vorgabe 0,68 · Größe 96 | nachgebessert 0,78 · Größe 64 |
|---|---|---|
| Kopfzeilenfeld | **0,656–0,774** | 0,721–0,839 |
| Untertitelzeile (Lippe 1248) | 0,650–0,693 | unverändert |
| Logo (`--logo-hoehe 0.87`) | 0,843–0,893 | unverändert |
| Überschneidung | **~57 px mit dem Untertitel** | keine |

**Zwei Dinge, die man wissen muss:**

1. **`--kopfzeile-hoehe` ist die Mitte des Feldes, nicht die Oberkante.** Das
   steht in keiner Hilfe. Ich habe erst 0,715 gesetzt, in der Annahme, es sei
   die Oberkante — die Überschneidung blieb, nur kleiner.
2. **Die Untertitel werden verdeckt, nicht weggelassen.** Beide SRT-Dateien
   haben dieselben 53 Einblendungen; die ersten vier liegen unter dem Feld.
   Wer nur die SRT prüft, sieht den Fehler nicht. **Nur das gerenderte Bild
   zeigt ihn.**

**Der Raum zwischen Untertitel und Logo ist eng:** Unterkante Untertitel 0,693,
Oberkante Logo 0,843 — 150 px bei 1920. Ein Feld von 96 px Schriftgröße misst
283 px und passt dort nicht. Bei Größe 64 sind es 207 px, und mit Mitte 0,78
bleiben 54 px Luft nach oben und 8 px nach unten. **Wer die Kopfzeile grösser
will, muss sie über die Untertitelzeile setzen, nicht darunter.**
→ betrifft: alle, die `--kopfzeile` benutzen — Shorts, Cinematic, Vlog

## 21.10.2026 — Der Stimmabdruck läuft. 89 % entschieden, davon 100 % richtig, 11 % verweigert

**Gemessen, nicht behauptet**, an **93 von Hand beschrifteten Abschnitten** aus
vier Folgen (Kingsbury, Britton, Crane, Wheelock). Beschriftet wurde **am
Wortlaut des Transkripts**, also unabhängig vom Tonmodell — sonst misst man sich
selbst. Werkzeug: ECAPA-TDNN über SpeechBrain, 192 Dimensionen, je
Whisper-Abschnitt ab 1,2 s eine Einbettung, Kosinus zum Schwerpunkt seiner
Stimme.

| Schwelle | entschieden | davon richtig | verweigert | er selbst erkannt |
|---|---:|---:|---:|---:|
| **ab 0,442 / unter 0,166** | **89 %** | **100 %** | **11 %** | 18 von 20 |
| ab 0,350 / unter 0,300 | 100 % | 98,9 % | 0 % | 20 von 20 |

**Die erste Zeile ist eingebaut.** Ein Transkript, das an elf Prozent der
Stellen schweigt und sonst recht hat, ist brauchbar; eins, das überall etwas
behauptet, ist es nicht.

**Die Trennung ist groß:** seine Stimme liegt bei **0,411–0,699** (Median 0,528),
die der Gäste bei **−0,087–0,419** (Median 0,075).

### Der Fehler, den ich zuerst gemacht habe, und er ist der lehrreiche Teil

**Die Schwelle abschnittsweise zu bestimmen ist zu optimistisch.** Erster
Versuch: Schwerpunkt aus zwei Folgen, Schwelle über Leave-one-out *innerhalb*
dieser Folgen → 0,538. Ergebnis auf zwei zurückgehaltenen Folgen: 78 %
entschieden, 100 % richtig — **aber von zehn Abschnitten mit seiner Stimme
wurde genau einer erkannt.** Die Trefferquote sah gut aus, weil sie von den 45
Gast-Abschnitten getragen wurde, die leicht sind.

**Ursache: der Raum, nicht die Stimme.** Mit *folgenweisem* Auslassen gemessen,
je Folge gegen einen Schwerpunkt ohne diese Folge:

| ausgelassen | seine Ähnlichkeit dort | die der Gäste |
|---|---|---|
| Kingsbury | 0,527 (0,42–0,70) | 0,067 |
| Britton | 0,652 (0,49–0,70) | 0,076 |
| Crane | 0,537 (0,45–0,67) | 0,093 |
| Wheelock | 0,429 (0,41–0,45) | 0,004 |

In einer **fremden** Aufnahme sitzt seine Stimme systematisch tiefer als in den
Trainingsfolgen — Mikrofon und Raum wandern mit. Eine Schwelle, die innerhalb
der Trainingsfolgen gesetzt wird, ist deshalb zu hoch und verweigert genau den,
den sie finden soll.

**Regel: wer über Folgen hinweg erkennen will, muss über Folgen hinweg prüfen.**
Abschnittsweises Auslassen teilt sich Raum und Mikrofon mit den Trainingsdaten
und beschönigt.

**Und die praktische Folge:** der Schwerpunkt wird mit **jeder weiteren Folge
besser**, weil er über mehr Räume mittelt. Die Zeitmarken seiner Abschlussfrage
stehen für neun Folgen in `video/meaningful-archiv.md` — das ist beschriftetes
Material für die eine Klasse, die gelernt werden muss, ohne eine Minute
Handarbeit.

### Zwei Zahlen, die gegen das Verfahren sprechen

1. **Ein Gast-Abschnitt liegt bei 0,419 und damit über dem kleinsten
   YNB-Wert (0,411).** Es ist Brittons **erster Abschnitt direkt nach der
   Frage** — genau die Stelle, an der ein Whisper-Abschnitt beide Stimmen
   enthält. Solche Abschnitte haben keine richtige Antwort, und kein
   Stimmabdruck löst das; das löst nur ein feinerer Schnitt der Abschnitte.
2. **Von zwei verweigerten YNB-Abschnitten sind beide seine Abschlussfrage** —
   *„What makes life meaningful after all?"* (0,411) und *„I like to ask, what
   makes life meaningful?"* (0,419). Kurze, schnell gesprochene Fragen tragen
   weniger Stimmfarbe als ein langer Gedanke. Ausgerechnet der Satz, um den es
   in dieser Reihe geht, ist der schwerste Fall.

### Ein Etikett von mir war falsch, und das Modell hat es gefunden

*„Shit, when you ask other people"* hatte ich als ihn beschriftet; das Modell
sagte Gast (0,068). **Das Modell hatte recht** — der Verlauf davor und danach
zeigt es: *„Oh, is I not supposed to do that?" / „No, you can." / „Shit, when
you ask other people, how do they get hold of you?" / „Their website or their
Instagram, I guess."* Das ist Curtis, der ihn fragt. Korrigiert, und im
Etikettenfile vermerkt. **Ich kann es nicht nachhören — der Beleg ist der
Gesprächsverlauf, nicht mein Ohr.**

### Praxisprobe an einer Folge, die weder im Training noch in der Prüfung war

Rob Bennett, 52 Abschnitte: **13 YNB, 28 Gast, 11 ohne Zuordnung (21 %)**. Die
Zuordnungen lesen sich richtig — seine Abschnitte sind Fragen und Einwürfe
(*„so you're saying there's no life without war?"*), Bennetts sind seine
Alan-Watts-Gedanken. **Die Verweigerungen sind fast alle kurze Rückmeldungen:**
„Yeah.", „Yes.", „Okay.", „Probably not.", „I don't know." Genau dort soll
nicht geraten werden.

### Wie es benutzt wird

```
python3 video/transkript_lokal.py --ton ton.flac --out t.md \
        --stimmabdruck folge.mp4
```

**Zuschaltbar, nicht Vorgabe.** Ohne den Schalter verhält sich
`transkript_lokal.py` genau wie bisher — der Shorts- und der cinematische
Assistent arbeiten diese Woche unter Termindruck damit.
→ betrifft: alle Content-Agenten

## 22.10.2026 — Ein Klaviercover ist kein Ausweg um Content ID

**Vier Sperren an einem Tag, drei verschiedene Titel**, zwei davon unter
Stücken meiner Serie. Der Befund steckt in der letzten Zeile: der vierte
Versuch war ein **Klaviercover**, gewählt, um dem Anspruch auf die Aufnahme
auszuweichen — und wurde trotzdem weltweit gesperrt, diesmal als Anspruch auf
**Melodie und Text**.

**Eine Coverversion wechselt den Anspruchsteller, nicht die Sperre.** Die
Aufnahme gehört einem Label, die Komposition einem Verlag; wer die Aufnahme
umgeht, landet beim Verlag.

**Und: dass eine Datei in seinem Musikordner liegt, ist keine Freigabe.** Dort
lagen drei Titel, und alle drei haben gesperrt.

**Für die Meaningful-Serie ausdrücklich festgeschrieben** in
`video/meaningful-serie.md`: keine Musik, bis er einen lizenzierten Titel
nennt. Vorher stand dort nur, dass keine drin ist — das hätte beim nächsten
Durchgang jemand „ergänzt".
→ betrifft: alle Content-Agenten

## 22.10.2026 — Dateinamen, und was dabei beinahe schiefging

**Seine Ansage:** `YNB Podcast <Gastname> <Stichwort>.mp4`, für alle Shorts.
Elf Untertiteldateien und fünf Videodateien umbenannt, das Werkzeug schreibt
neue Stücke direkt so.

**Zwei Dinge, die beim Umbenennen auffielen:**

1. **Von Sutcliffes Untertiteln lagen zwei Fassungen** — die aus der Nacht vom
   20./21.10. und die vom neuen Preset. Beide heißen jetzt gleich, also musste
   eine gewinnen. Die ausgelieferte Datei ist die neue, **die Zeiten weichen um
   bis zu 17 ms ab**. Hätte ich die alte behalten, wären Untertitel und Video
   auseinander gelaufen, und zwar unsichtbar.
2. **Mein `sed` hat den Verweis in `aaronson-shorts.md` nicht getroffen**, weil
   dort `.mp4` stand und ich auf `.srt` ersetzt hatte. Gefunden mit einem
   `grep` über alle Markdown-Dateien nach den alten Namen — **nachgesehen,
   statt anzunehmen, dass es durch ist.**

**Die laufende Nummer fällt aus dem Dateinamen.** Für eine Reihe, die auf
hundert Folgen zielt, ist das ein Verlust an Ordnung im Ordner — aufgefangen
wird er von `video/meaningful-archiv.md`, wo die Nummer samt Drive-ID und
Masterzeitmarke steht. Aus einem Ordner voller Dateien lässt sich der Schnitt
nicht bauen, aus der Tabelle schon.
→ betrifft: alle Short-Agenten
