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
