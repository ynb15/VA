# Craig / Into the Wild — Aufbau der Vollbild-Fassung

Stand 22.10. Die Fassung, die aus Variante A hervorgeht, nachdem vier Dinge
beanstandet waren: Rand an den Einspielern, zu später Einstieg, doppelt
benutztes Material, Tagebuch nicht beim Zitat.

## Quelle

Bildschirmaufnahme des Trailers, 2622x1206, 185 s.
Das Filmbild darin: **2138x917 bei x=242, y=153.**

Die 917 statt 961 sind Absicht: in den unteren 43 Pixeln des Filmfeldes
stehen die eingebrannten Trailer-Untertitel — jedes Mal an derselben Stelle.
Weggeschnitten ist der **ganze** Trailer brauchbar statt 36 von 185 Sekunden.
Kosten: 4,5 Prozent der Bildhöhe. Siehe `untertitel_finden.py`.

Gegengeprüft am fertigen Short: 105 Proben im Abstand 0,5 s über das untere
Fünftel — kein einziger eingebrannter Untertitel mehr im Bild.

## Die zwoelf Einspieler (Fassung D)

Bedingung dieser Runde: **die Kamera muss auf McCandless sein.** Nicht
Landschaft, nicht nur Haende. Dazu Craig im Bild beim ersten Satz, beim
letzten Satz und einmal in der Mitte.

| Nr | Trailer ab | Dauer | Bild                                   | im Short     |
|----|-----------:|------:|----------------------------------------|--------------|
| –  |          – |     – | **Craig** - erster Satz                | 0,00–2,28    |
| m1 |      100,0 |  7,2s | Lauf frei, dann Rucksack und Hut       | 2,28–9,00    |
| m2 |      144,0 |  6,6s | **TAGEBUCH** - HAPPINESS-Seite         | 9,00–15,18   |
| m3 |      168,6 |  3,6s | Gesicht ganz nah                       | 15,18–18,37  |
| m4 |       36,3 |  3,2s | Silhouette am Abendmeer                | 18,37–21,08  |
| m5 |       44,0 |  3,4s | laeuft mit den Pferden                 | 21,08–24,02  |
| –  |          – |     – | **Craig**                              | 24,02–25,98  |
| m6 | 118,8+129,3|  4,8s | blickt ueber die Berge, dann Gesicht   | 25,98–30,70  |
| m7 |      131,0 |  4,8s | Anzug, die Familie                     | 30,70–35,00  |
| m8 |       27,0 |  3,3s | geht auf die Kamera zu, am Wasser      | 35,00–37,82  |
| m9 |       74,0 |  3,5s | Lauf durch den Wald                    | 37,82–40,83  |
| m10|      115,2 |  3,3s | Arme ausgebreitet am Schneehang        | 40,83–43,65  |
| m11|       84,0 |  3,6s | Kajak im Wildwasser                    | 43,65–46,75  |
| m12|      155,0 |  3,8s | **TAGEBUCH** - REAL WHEN SHARED        | 46,75–50,07  |
| –  |          – |     – | **Craig** - der Ubuntu-Satz, ohne Bild | 50,07–Ende   |

**Das Tagebuch laeuft an beiden Stellen durch, ohne ein Bild zu wiederholen.**
Moeglich ist das, weil bei 144–167 s 24 Sekunden Tagebuch am Stueck liegen:
m2 nimmt das Schreiben der HAPPINESS-Seite, m12 die Worte REAL WHEN SHARED
unter dem Stift. Zwei Stellen derselben Szene, kein gemeinsames Bild.

Craig ist 6,75 von 52,58 Sekunden zu sehen: **87 Prozent B-Roll.**

m3 sitzt auf „that made his death worth it", m7 auf „this giant parental
system", m9 auf „going into the wilderness". Einstellungen, die einen Satz
tragen, gehoeren an diesen Satz.

## Musik

`--musik` mit „In This Shirt" (The Irrepressibles), `--musik-unter 14`.
Gemessen: Stimme −17,3 dB, Bett −11,6 dB, abgesenkt auf −19,7 dB. Der
Spitzenpegel des Shorts bleibt bei −0,5 dB und damit genau da, wo er ohne
Musik schon lag (−0,4 dB) — das Bett hebt den Mittelwert um 0,3 dB, mehr
nicht.

Der Titel ist durchgehend dicht (−12 dB RMS ab Sekunde 2), es gibt kein
leises Intro, auf das man sich legen koennte. Darum die 14 dB statt der
voreingestellten 8.

**Es ist eine Handelsaufnahme.** Content ID wird sie finden; das kostet in
der Regel die Einnahmen des Shorts, nicht den Short. Seine Entscheidung,
ausdruecklich und namentlich getroffen.

## Was dabei nicht zu haben ist

`--broll-modus vollbild` schneidet aus dem 2,33:1-Feld ein echtes 9:16
heraus: von 2138 Pixeln Breite bleiben 516. Hochgerechnet auf 1080x1920 ist
das **Faktor 2,09** — die Einspieler sind weicher als das Interviewbild.

Daran ist mit dieser Quelle nichts zu ändern; mehr Pixel hat die Aufnahme
nicht. Wer es schärfer will, nimmt den Film im Vollbild eines größeren
Monitors auf, nicht im Browserfenster.

Die Alternative `--broll-modus unschaerfe` bleibt randlos **ohne** zu
beschneiden (scharfe Mitte, unscharf vergrößerte Kopie dahinter) und
rechnet nur 1,18-fach hoch. Sie kostet dafür das echte Vollbild.

## Zweiter Punkt am Rande

In der gestapelten Zwei-Personen-Einstellung (z. B. 37,5 s) steht das
YNB-Zeichen zweimal im Bild: einmal eingebrannt in der Aufnahme unten links,
einmal vom Renderer mittig. Das ist nicht neu und nicht von dieser Fassung
gemacht — es steckt im Master. Wegzubekommen wäre es nur, indem der
Stapel-Ausschnitt die untere linke Ecke meidet.
