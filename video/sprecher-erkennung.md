# Sprecher im Transkript — warum es nicht geht, und wie es gehen wird

**Seine Frage vom 21.10.2026:** *„Es scheint mir noch nicht der Fall, dass du
bei den Transkripten wirklich unterscheiden kannst, ob ich rede oder ob mein
Gast redet. Wie können wir das optimieren?"*

**Er hat recht, und das ist Absicht.** `video/transkript_lokal.py` **verweigert**
Sprechernamen, wenn es sie nicht belegen kann — nicht aus Bequemlichkeit,
sondern weil die erste Fassung am 20.10. welche erfunden hatte. Die Regel bleibt:
*lieber kein Sprechername als ein erfundener.*

## Was gemessen ist

Die drei Aaronson-mp3s **trennen die Sprecher nicht**:
* paarweise Pegelverhältnisse je Segment, **IQR 2,3–2,4 dB**, unimodal
* feste Versätze von ≈ −17 und −7 dB zwischen den Spuren
* alle drei **dual-mono** (linker Kanal == rechter Kanal)

Ein echtes Ansteckmikrofon pro Person ergäbe eine zweigipflige Verteilung mit
10–20 dB Abstand. Diese Spuren sind drei Abgriffe desselben Raums bei
unterschiedlicher Verstärkung.

## Der Befund von heute, der das erklären könnte

Die Dateien im Rohordner heißen:

```
2026-08-21 13-15-35 1.mp3      82,9 MB
2026-08-21 13-15-35 2.mp3      81,1 MB
2026-08-21 13-15-35 4.mp3      84,4 MB
```

**Eins, zwei, vier. Die Drei fehlt.** Das ist die Nummerierung eines
Mehrspurrekorders, und eine Spur ist nicht in seiner Kopie. Ob sie beim
Original liegt, **ist ungeprüft** — der Raw-Ordner von
`team@justpushrecord.com` lässt sich nicht auflisten, fremder Besitzer.

**Das ist ein Verdacht, keine Tatsache.** Möglich ist auch, dass nie eine Spur 3
existierte. Beides klärt eine Frage an das Studio, nicht eine weitere Messung.

## Drei Wege, in der Reihenfolge ihres Werts

### 1 · Die isolierten Spuren anfragen — einmal fragen, dauerhaft gelöst
Wenn Just Push Record pro Mikrofon aufzeichnet, ist die Sprecherzuordnung
**exakt statt geschätzt**, für jede dort aufgenommene Folge, rückwirkend und
künftig. Entwurf liegt in `drafts/justpushrecord/spuren-anfrage.md`.
**Er schickt, nicht wir.**

### 2 · Ein Stimmabdruck von ihm — der Weg, der unabhängig funktioniert
**Er ist in jeder Folge.** Also braucht es keine blinde Sprechertrennung,
sondern **einen Anker**: ein Stimmprofil von ihm, einmal gebaut, danach je
Segment ein Ähnlichkeitsvergleich. Alles, was nicht er ist, ist der Gast.

Das ist deutlich robuster als übliche Diarisierung, weil nur **eine** Klasse
gelernt werden muss und sie mit jeder Folge besser belegt ist.

**Und die Trainingsdaten liegen schon da.** `video/meaningful-archiv.md` enthält
für sechs Folgen die Zeitmarken, an denen **er** fragt und der **Gast**
antwortet — beschriftetes Material für beide Klassen, ohne eine Minute
Handarbeit:

| Folge | Frage/Antwort im Master |
|---|---|
| Sutcliffe | 7222,0–7281,6 |
| Aaronson | 5894,3–5972,6 |
| Ken Stern | 6150,1–6189,3 |
| Logan Gonzalez | 4957,1–5009,4 |
| Matt Defina | 6474,7–6513,1 |
| Rick Strassman | ~7100–7160 (grob) |

Werkzeug: Sprecher-Einbettungen (ECAPA-TDNN über SpeechBrain, oder
Resemblyzer), je Whisper-Segment eine Einbettung, Kosinus-Abstand zum
Schwerpunkt seiner Stimme.

### 3 · Die Kameraführung — genau, aber nur wo Mehrspurmaterial liegt
Bei Aaronson kam die Zuordnung am Ende hierher: **Left Cam = Gast,
Right Cam = er, Middle = Totale.** Die Regie schneidet auf den, der spricht.
Das ist exakt — aber es setzt die drei Kameradateien voraus, und **Kingsbury
hat sie nicht** (eine 16,9-GB-MOV und ein BTS-Clip, sonst nichts). Taugt als
Prüfmaßstab, nicht als Verfahren.

## Wie bewiesen wird, dass es funktioniert

**Nicht mit „es läuft jetzt".** Gegen die sechs Folgen oben messen, bei denen
die Wahrheit bekannt ist, und **eine Zahl nennen**: wie viel Prozent der
Segmente richtig zugeordnet sind, bei wie vielen Segmenten. Dazu eine
Stichprobe von Hand.

**Und die Verweigerungsregel bleibt bestehen.** Unterschreitet ein Segment die
Sicherheitsschwelle, bekommt es **kein** Etikett — es bekommt `?`. Ein
Transkript, das bei 8 % schweigt und bei 92 % recht hat, ist brauchbar. Eins,
das überall etwas behauptet und bei 15 % irrt, ist es nicht.
