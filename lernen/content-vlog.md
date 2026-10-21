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
