# Craig Makhosi — das dritte Stück

Gebaut 05.11.2026 für Fr 06.11., nach Ubuntu (30.10.) und Into the Wild /
Fassung E (02.11.).

**Geliefert wird „The Biggest Scandal School System" (unten).** Zuerst
gebaut war „What makes life meaningful?" — das ist verworfen: *„Bruh. Ich
sehe gerade 'what makes life meaningful' haben wir schon für Craig."* Die
Recherche dazu steht hier trotzdem, weil der Weg in den Master und die
beiden Planeingriffe für jedes weitere Stück aus dieser Folge gelten.

---

## Verworfen: „What makes life meaningful?"

## Warum nicht aus der kleinen Fassung

`YNB Podcast - Craig Makhosi - Ubuntu.mp4` (1,03 GB, 238,65 s) ist
**aufgebraucht**: Into the Wild nahm 22,80–118,54, Ubuntu 116,70–238,65.
Frei blieben 0–22,8 — die Vorrede, zu wenig für ein Stück.

Die Datei `YNB Podcast: Into The Wild` (274 MB) im selben Ordner ist **kein
Podcastmaterial**: 1206×2622, 29,70 fps, `ReplayKitRecording`, 144,84 s —
eine Bildschirmaufnahme des Kinotrailers, also B-Roll.

Bleibt der Master `YNB Podcast - Craig Makhosi.mp4`, 27,41 GB, **8710,67 s =
2:25:11**, 2560×1440, 30 fps, 44,1 kHz.

## Sein Vorbereitungsdokument trägt zwei verschiedene Zeitleisten

Im Dokument `06 YNB Podcast: Craig Makhosi` stehen **beide**:

* eine **Kapitelliste** („31:37 Into The Wild & Self-Initiation", „33:44
  Ubuntu", „1:40:33 How Apartheid started") — Zeiten der **fertigen Folge**,
  sie reicht bis 2:37:16;
* ein **volles Transkript** mit Zeitmarken, das bei 2:24:55 endet und mit
  „Amen." schließt — Zeiten des **Masters**.

Gegengeprüft am Wortlaut: „Seen the movie Into the Wild?" steht im
Transkript bei **28:49**, in der Kapitelliste bei **31:37**; „Ubuntu I am
because we are" bei **30:11** gegen **33:44**. Der Versatz wächst von 2:48
auf 3:33 — er ist also nicht konstant und nicht ausrechenbar. **Das
Transkript im Dokument ist der Schlüssel zum Master**, die Kapitelliste
der zur Folge.

## Die Stelle

Mastertranskript **2:21:25–2:23:31**: die Schlussfrage des Formats, „What
makes life meaningful?", und Craigs Antwort. Sie greift beide vorherigen
Shorts auf — *„it speaks to Ubuntu and it speaks to old Alexander
Supertramp"* — und endet auf *„but it's a school, bro."*

Geholt als Fenster **Master 8480–8640** (`master_schnitt.py`, 515,6 MB über
65 Bereichsanfragen). Fensterzeit 0 = Master 8479,14.

Zwei Teile, Schnittpunkte an gemessenen Sprechpausen:

| | Fensterzeit | Master | Länge | Pegel am Schnitt |
|---|---|---|---|---|
| A | 18,85–89,95 | 8498,0–8569,1 | 71,10 s | −52 dB / −60 dB |
| B | 104,95–146,20 | 8584,1–8625,3 | 41,25 s | −59 dB / −63 dB |

**Herausgeschnitten: 89,95–104,95.** Dort liegt ein Zwischenruf („Fuck
happiness"), danach eine Kreuzung aus Ja/Nein-Lauten beider Stimmen. Der
erste Durchlauf hatte ihn drin und schrieb **FUCK HAPPINESS** in Versalien
ins Bild — mitten in eine Passage über Dankbarkeit. Zwischen 95,8 und 97,5
gibt es keine Stille, der Schnitt musste deshalb davor liegen; bei 89,90 bis
90,00 steht eine echte Lücke bei −57 dB.

B beginnt mit „Yeah, but it is friendship as well, definitely." — vorher
nachgehört, damit der Einstieg ein ganzer Satz ist und kein Satzrest.

## Zwei Eingriffe in den Einstellungsplan

**Glitch-Regel.** `bildausschnitt.py` fand neun Einstellungen, darunter eine
von **1,5 s**, die den Ausschnitt um 192 px verschiebt und gleich
zurückspringt. Genau das hat er am 22.10. beanstandet („zwischen 0:16 und
0:18 ist wieder ein minimaler glitch"). Sie ist in die folgende
aufgegangen; kürzeste Einstellung jetzt **3,9 s**.

**Das eingebrannte Logo.** Auch dieser Master trägt das YNB-Zeichen unten
links im Bild. Der gestapelte obere Kasten bei Clipzeit 86,7 begann bei
y=432 und hätte es mit eingefangen; er beginnt jetzt bei y=100. Dasselbe
Problem wie beim Ubuntu-Short, diesmal vor dem ersten Rendern gefunden.

## Einstellungen

`--plan` · `--tempo 1.45` · `--look warm` · Logo 700 px auf 0,877 ·
`--musik momsgotwork.mp3 --musik-unter 0` · Outro 9:16 ·
`--laut aus`, `--dehnung atempo` (Vorgabe).

Ergebnis **81,7 s**, 1080×1920, Spitze −0,5 dB, Mittel −18,3 dB.

Aus 1440 Bildhöhe bleiben im 9:16-Fenster **810 px Breite**; auf 1080
gerechnet ist das eine Hochrechnung um 1,33. Sichtbar ist das bei einer
Sprechaufnahme nicht, aber es ist der Grund, warum diese Folge weniger
Reserve hat als die Ubuntu-Datei (dort 1215 px).

## Untertitel

Zwei Stellen aus dem Lauf mit `small` ersetzt, der Rest steht wie gehört:

| | `small` schrieb | hier steht |
|---|---|---|
| 00:07 | „ASK ROB THAT QUESTION THESE RELATIONSHIPS" | „… QUESTION IT'S RELATIONSHIPS" |
| 00:49 | „YEAH BROTHER IT IS FRIENDSHIP" | „YEAH BUT IT IS FRIENDSHIP" |

Beide am Ton nachgehört (`medium` auf dem Fenster).

---

## Geliefert: „The Biggest Scandal School System"

Aus seiner eigenen Kapitelliste, Abschnitt **„Short"**: *„39:55 The Biggest
Scandal School System"* — von ihm als Short markiert und noch nicht gebaut.

**Stelle:** Master **2156,6–2272,7** (116,13 s), Fenster 2130–2275 geholt
(467,6 MB über 59 Bereichsanfragen). Schnittpunkte an gemessenen Pausen:
Anfang 26,95 s im Fenster (−48 dB), Ende 143,08 s (−53 dB).

**Aufbau:** seine Frage als Haken — *„Should I tell you a crazy fact about
the school system in Germany?"* — dann die Regel (Lehramtsanwärter dürfen
nicht in Therapie, weil das psychische Krankheit unterstellt), dann sein
Schluss *„no wonder we create fucking bullies"*, und zuletzt Craigs
südafrikanische Gegenseite bis *„there's not enough adults around. Like in
a village situation, there's more adults than kids."*

**Dieselben zwei Eingriffe im Plan** wie oben: eine Einstellung von 1,3 s
ist in die folgende aufgegangen (kürzeste jetzt 7,0 s), und **alle drei**
gestapelten oberen Kästen begannen bei y=432 und hätten das eingebrannte
Logo mitgenommen — jetzt y=100.

**Untertitel:** eine Stelle ersetzt, `small` schrieb bei 00:00 „A CREATIVE
FACT" statt „A CRAZY FACT".

**Ergebnis** 84,3 s, 1080×1920, Mittel −17,4 dB, Spitze −0,0 dB. Die Spitze
liegt höher als bei Ubuntu (−0,5 dB), weil die Stimme hier 1,2 dB lauter
ist; 632 von 8,1 Millionen Abtastwerten berühren die Vollaussteuerung, also
0,008 Prozent. Kein hörbares Clipping, aber keine Reserve mehr — sollte der
nächste Master noch lauter sein, muss das Bett einen Schritt runter.

**Zwei Flüche stehen in Versalien im Bild** („SO MANY FUCK UPS", „NO WONDER
WE CREATE FUCKING BULLIES"). Beide sind seine eigenen, im eigenen Register,
und tragen die Pointe — anders als das „FUCK HAPPINESS", das oben
herausgeschnitten wurde.
