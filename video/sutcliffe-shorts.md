# David Sutcliffe — Shorts aus der veröffentlichten Folge

**Folge:** „The Hollywood Star Who Quit Everything To Heal Men: Feminism,
Manosphere & Andrew Tate (4K)" · `frNOUgxE0IM` · hochgeladen 30.09.2026 ·
**116:33** · **2.321 Aufrufe**, 10 Likes, 7 Kommentare (gemessen 19.10.2026).

**Master im Drive:** „YNB Podcast: David Sutcliffe"
`1oJjeQXjfIYtYph0gxfe8V1dhv17BBlPT` · **18,6 GB** · 1920×1080, 30 fps,
21 Mbit/s · **125:18**.

---

## Das Tempo — Deine Erklärung war richtig, meine war falsch

Ich hatte geschrieben, der Master sei 8:45 länger und der Unterschied verteile
sich über die Folge, „weil im Fluss gekürzt wurde". **Das war die falsche
Erklärung.** Du beschleunigst den Podcast beim Export auf 1,1 — und genau das
misst man auch:

| gemessenes Fenster (veröffentlicht) | lokales Tempo | Streuung |
|---|---|---|
| 804–827 s (13:24) | **1,1055** | 0,91 s |
| 4.532–4.574 s (75:32) | **1,0949** | 0,75 s |

Verfahren: 60 s Ton aus dem Master holen, wortgenau transkribieren, die Wörter
gegen das veröffentlichte Transkript ausrichten und über die sicher gleichen
Wörter eine Gerade legen. 74–82 Wortpaare je Fenster, Streuung unter einer
Sekunde. **Lokal ist das Tempo 1,1, nicht 1,06.**

**Trotzdem bleibt Nachmessen Pflicht.** Über die ganze Folge gerechnet ergibt
sich nur 1,056 — und das geht mit 1,1 nur auf, wenn in der Veröffentlichung
Material steckt, das im Master nicht vorkommt. Rund drei Minuten. Der Anfang
der Folge ist so ein Fall: sie beginnt mit „There's no very little drama,
that's why the podcast between me and Tate was so good" — ein Kaltstart, der im
Gespräch viel später fällt. **Regel: Tempo 1,1 gilt lokal, der Versatz muss in
der Nähe der Stelle gemessen werden, die Du schneiden willst. Eine Formel über
die ganze Folge gibt es nicht.**

**Für die Shorts heißt das: `--tempo 1.1`.** Ein Schnitt aus dem Master läuft
sonst langsamer als alles andere auf Deinem Kanal — Ton über `atempo`, Bild
über `setpts`, die Untertitelzeiten werden mitgerechnet.

---

## Short 4 — „Vulnerability is not weakness" (dritte Fassung des Verfahrens)

**Gewünscht am 20.10.:** die Stelle über Hyper-Masculinity, in der er seine
Substack-Notiz über Vulnerability vorliest.

**Gefunden:** veröffentlicht **01:12:01–01:13:06**, im Master **4569–4640**
(Fenster 4550–4665 geholt, über den Ton nachgemessen, Anker bei
veröffentlicht 4532 ↔ Master 4799, lokales Tempo 1,1).

Der Bogen steht von selbst: er benennt, woran Hyper-Masculinity scheitert —
*„failing to become whole is in the tendency to completely suppress certain
traits or behaviors like vulnerability"* — sagt dann *„I put out a note
recently on Substack"* und liest sie ganz vor. Am Ende Sutcliffes drei Worte:
*„Yeah, that's true."* **71 Sekunden Master, mit Tempo 1,2 genau 59.**

**Fünf Änderungen aus seiner Rückmeldung vom 20.10.:**

| | |
|---|---|
| **zu kurz** | Dieser Short läuft **59 s** statt 31–53. Das Fenster endet an Sutcliffes Antwort, nicht an einer Satzgrenze. |
| **Tempo** | `--tempo 1.2` (seine Folgen laufen auf 1,1, die Shorts sollen schneller sein) |
| **drei Wörter** | `--worte 3`; eine Einblendung aus einem einzigen Wort wandert in die vorhergehende zurück |
| **Text unter die Lippe** | feste Zeilenhöhe bei **0,65 der Bildhöhe** — siehe unten, warum fest besser ist als gemessen |
| **sein Look** | Versalien, gelbes Aktivwort, dicke Kontur, engerer Ausschnitt, warme Gradation — abgelesen an seinen eigenen Shorts |

**Warum die Zeilenhöhe jetzt fest ist und nicht mehr gemessen wird:** der
Ausschnitt setzt die Kopfoberkante bauartbedingt auf 10 % der Kastenhöhe.
Damit liegt der Mund immer bei rund 0,56 und das Kinn bei 0,73 — die Lage ist
durch den Ausschnitt schon normiert. Die Messung schwankte zwischen 0,56 und
0,66 und landete im Versuch mal auf dem Mund, mal unter dem Kinn. **Eine feste
Zeile dazwischen ist genauer als die Schätzung.**

**Zweite Runde, 20.10. abends — seine Korrekturen:**

| | |
|---|---|
| **Punchline steht allein** | Sutcliffes *„Yeah, that's true"* ist raus. Der Short endet auf **„most men have neither."** — 55,9 s statt 59. |
| **zwei Verhörer** | *for short* war **fall short**, *endotades* war **Andrew Tates**. Beide in `video/korrekturen.txt`; die Liste kann jetzt auch Wortfolgen. |
| **Satzgrenzen** | Eine Einblendung läuft nie mehr über das Satzende. Entscheidend war nicht das Satzzeichen, sondern **Whispers eigene Abschnitte**: *„too afraid to touch."* und *„This is why…"* standen in getrennten Abschnitten und trotzdem in einer Zeile, weil der Punkt fehlte und die Pause zu kurz war. Jetzt trennt jeder Abschnittswechsel, jedes Satzzeichen und jede Pause über 0,45 s. |
| **Logo** | aus seinem Drive: *YNB Logo freigestellt weiß_neu.png*, 520 px breit, mittig auf 0,845 der Bildhöhe — wie auf seinen Shorts. |
| **Musik** | **Weg gebaut, Bett fehlt.** Siehe unten. |

**Zur Musik, offen:** die Kette steht — das Bett wird geloopt, ein- und
ausgeblendet und von der Stimme weggedrückt (`sidechaincompress`), und der
Pegel wird **gemessen** statt geraten: der erste Versuch mit festen −16 dB lag
14 dB unter der Stimme und war schlicht nicht zu hören (0,1 dB Unterschied
zwischen Mischung mit und ohne). Jetzt misst `--musik` beide Spuren und legt
das Bett `--musik-unter` dB unter die Stimme, voreingestellt 8.
**Was fehlt, ist der Track.** Ich habe keine Musikbibliothek und hole für etwas,
das veröffentlicht wird, nichts aus dem Netz. In seinem Drive liegt nur
*outro audio.mp3* (42 s, seine Podcast-Outro) — als episches Bett unter diesem
Text die falsche Farbe. **Eine Datei in den Drive-Eingang, und es ist eine
Minute Arbeit.**

**Vierte Runde, 20.10. — die Feinheiten, die er etablieren will:**

| | |
|---|---|
| **Outro** | hängt dran. `YNB_Podcast_Outro_9_16_NEU.mov`, 4,21 s, ProRes 4444, 1080×1920, 24 fps — wird auf 30 Bilder gebracht und bekommt **weder Look noch Logo noch Untertitel**. Gesamtlänge 59,4 s. |
| **Logo** | 700 px statt 1040, auf 0,877 der Bildhöhe. Luft über und unter der Zeile. |
| **Zeile bleibt auf einer Höhe** | auch beim Wechsel in die Totale. Konstant 0,65. Das Auge hat die Zeile immer am selben Fleck. |
| **keine Satzzeichen** | Punkt und Fragezeichen fallen im Bild weg. **Für die Trennung braucht das Werkzeug sie weiter**, deshalb fallen sie erst beim Schreiben der Zeile weg, nicht schon im Transkript. |
| **Sutcliffes Einwurf** | raus. Gemessen: er endet auf *„vulnerability"* bei 20,28 s, Sutcliffes *„Yeah. Right."* liegt bei **20,44–20,94**, sein nächster Satz beginnt bei 21,22. Geschnitten 20,32–21,12. Sein Reaktionsbild bleibt eine Sekunde stehen, nur stumm. |
| **genau drei Wörter** | Statt ein einzelnes Wort zum Nachbarn zu schieben (das machte vier), werden die Wörter einer durchgehenden Strecke **neu aufgeteilt**: vier werden 2+2, sieben werden 3+2+2. Über ein Satzende hinweg wird nichts umverteilt. |
| **eine Zeile je Einblendung** | Die Schriftgröße gilt **je Einblendung**: Grundgröße 78, und nur wo es nötig ist, wird verkleinert. `CALLED THE HYPERMASCULINITY` läuft so auf einer Zeile, ohne dass alle anderen kleiner werden. |

**Fünfte Runde, 20.10.:** Satzgrenzen aus dem Tonpegel statt aus Whispers
Zeitstempeln · eine Schriftgröße für alle, dafür werden zu breite
Einblendungen geteilt (`CALLED THE` + `HYPERMASCULINITY`) · Schriftbreiten
ausgemessen statt geschätzt · `~`-Muster in der Korrekturliste, weil Whisper
denselben Namen von Lauf zu Lauf anders buchstabiert (`endotades`,
`endotates`, `endate`) · Sutcliffes zweiter Einwurf bei 49,5 s stummgeschaltet
statt herausgeschnitten, damit das Bild ruhig bleibt.

**Zwei Fehler, die dabei auffielen:**

**`CALLED THE HYPER`** — die Korrektur `hyper masculinity → hypermasculinity`
griff nicht, weil Whisper den Bindestrich als eigene Vorsilbe liefert
(`hyper` + `-masculinity`) und mein Wortkern nur Satzzeichen abschnitt.
Jetzt fällt außen alles Nichtalphanumerische weg.

**`LIKE` stand allein im Bild** — eine Strecke aus einem einzigen Wort gibt
eine Einblendung aus einem einzigen Wort. Solche Strecken werden mit dem
Nachbarn zusammengelegt, **aber nur über eine Atempause hinweg**; über
Satzende und Abschnittswechsel weiterhin nicht.

---

## Geschnitten und fertig — zweite Fassung

| # | Datei | Länge | Master | Inhalt |
|---|---|---|---|---|
| 1 | `shorts/sutcliffe-01-therapeut.mp4` | 32 s | 5527–5562 | „Your therapist better be in therapy" |
| 2 | `shorts/sutcliffe-02-drop-the-story.mp4` | 31 s | 1367–1401 | „Can you drop the story?" |
| 3 | `shorts/sutcliffe-03-love-me.mp4` | 53 s | 5143–5201 | „I just needed you to love me" |

Alle drei sind am 19.10. neu gerechnet: **Tempo 1,1 · Untertitel an der Lippe ·
Totalen gestapelt statt auf den Tisch geschnitten.** Deshalb sind sie kürzer
als die erste Fassung (35/34/58 s) — das ist die Beschleunigung, nicht ein
anderer Schnitt.

**Warum diese drei:**

**1 — „Your therapist better be in therapy."** Deine Wut über die Regel, dass
Lehramtsanwärter nicht in Therapie dürfen, und seine Antwort in sechs Wörtern.
**Dein stärkster Short überhaupt ist „The Biggest Scandal in the German School
System" mit 2.700 Aufrufen** — das ist dasselbe Thema, mit einem
Hollywood-Therapeuten als Zeugen. Das ist meine Begründung, nicht Deine Vorgabe.

**2 — „Can you drop the story?"** Rob Paddocks eine Frage, auf Deine eigene
Geschichte angewandt. Du erzählst zehn Minuten, er fragt einmal. Funktioniert
als Short, weil die Frage offen stehen bleibt.

**3 — „I just needed you to love me."** Der emotionale Höhepunkt der ganzen
Folge: Sutcliffe, 35 Jahre alt, bricht in einem Workshop zusammen. „I had no
idea any of that was inside me." Mit 53 s der längste — der Bogen braucht ihn.

---

## Sieben weitere Stellen, die ich nicht geschnitten habe

Zeiten **veröffentlicht** (für den Master den Versatz oben draufrechnen):

| veröffentlicht | Inhalt | warum |
|---|---|---|
| 03:20–04:10 | Friends-Set: sie verdienten 750.000 $ pro Folge, er 3.000 | Zahlen als Haken, sofort verständlich |
| 06:20–07:00 | „I didn't like who I was becoming" — der Wendepunkt | der Ausstieg in einem Satz |
| 21:40–22:20 | „Maybe your fear is legitimate" | dreht den üblichen Therapiespruch um |
| 51:56–52:40 | „Where's the fucking father?" | härtester Satz der Folge |
| 63:00–63:40 | „HOW DO YOU NOT RESPECT THAT?" über Tate | lauteste Stelle, polarisiert |
| 94:00–95:20 | „He never saw me play. I played hard for him." | die Vaterwunde, mit Tränen |
| 115:40–116:10 | „Embrace the uncertainty" — sein Rat an Dich | als Abschluss-Short |

---

## Wie es technisch läuft

```
# 1. Fenster aus dem Master holen (lädt nur die gebrauchten Bytes)
python3 video/master_schnitt.py --id <drive-id> --start 1330 --ende 1425 \
        --groesse 19976733699 --out roh.mp4

# 2. Kamerawechsel, Lippenhöhe, Totalen und tote Stellen finden
python3 video/bildausschnitt.py roh.mp4 --json plan.json

# 3. Rendern — Untertitel aus dem Ton des Clips, Tempo wie im Export
python3 video/shorts-render.py --src roh.mp4 --plan plan.json \
        --tempo 1.1 --auto-captions --model small --out short.mp4
```

**Punkt 1:** die 18,6-GB-Datei wird nie geladen. Drive beantwortet
Bereichsanfragen, PyAV nimmt ein dateiähnliches Objekt — **gemessen 200–260 MB
pro Fenster** statt 18,6 GB, bei 12,8 MB/s.

**Punkt 2 — drei Dinge, die am 19.10. dazugekommen sind, alle aus Deiner
Rückmeldung:**

**Die Totale wird gestapelt, nicht beschnitten.** Das war Dein „da wird einfach
nur der Tisch gezeigt". Die Ursache war nicht eine leere Szene im Material,
sondern mein Ausschnitt: Ihr sitzt am Rand, der Tisch steht zwischen Euch, und
ein 9:16-Fenster (608 von 1920 Pixeln) trifft in der Totale genau die Mitte.
**In Short 1 waren das 6,9 Sekunden Tischplatte.** Erkannt wird die Totale jetzt
an der Bewegungsmasse in der Bildmitte: Totale 0,22–0,28, Nahaufnahme 0,55–0,73.
Dazwischen liegt Luft. Unter 0,45 werden zwei Ausschnitte gebaut, einer je
Person, übereinander.

**Die Untertitel sitzen an der Lippe.** Nicht gemessen als „bewegungsstärkste
Zeile im Gesicht" — das war der erste Versuch, und er landete verlässlich auf
Stirn und Brille, weil Augen und Brillenränder sich mehr bewegen als der Mund.
Auch die Hautfarbe taugte nicht: das Hautband lief ins graue T-Shirt und in die
Tischplatte und zog die Zeile auf die Brust. Was hält: die **Oberkante des
bewegten Bereichs ist der Kopf**, der Mund liegt 0,44 Bildhöhen darunter. An
vier Nahaufnahmen geprüft, Streuung der Kopfoberkante 0,156–0,189. Läuft eine
Einblendung über einen Kameraschnitt, wird sie geteilt und springt mit.

**Die Schnitterkennung zählt jetzt Fläche statt Helligkeit.** Vorher galt ein
Bild als neue Einstellung, wenn sich der Mittelwert stark änderte — und
Sutcliffe, der mit beiden Händen redet, erzeugte damit vier Schnitte, wo keiner
war. Entscheidend ist der **Anteil des Bildes**, der wechselt: echter
Kameraschnitt 0,51–0,61, größte Handbewegung 0,19–0,35.

**Tote Einstellungen** — wenn doch einmal eine Sekunde nur Kulisse im Bild
steht — werden mit dem letzten Bild davor überbrückt (`tpad=clone`), **der Ton
läuft unverändert weiter.** Den toten Abschnitt samt Ton herauszuschneiden habe
ich verworfen: das zerreißt den Satz, der darüberläuft. In Deinen drei Fenstern
kam der Fall nicht vor; die Mechanik steht für den Fall, dass er kommt.

**Was noch offen ist:** im Stapel weiß das Werkzeug nicht, wer gerade spricht —
die Zeile sitzt deshalb an einer festen Höhe unter dem oberen Kopf statt an
dessen Lippe. Dafür bräuchte es Lippenbewegung je Person; machbar, aber noch
nicht gebaut.

---

## Sechste Runde, 20.10. — „der Ton ist irgendwie anders"

**Ja, und zwar aus einem Grund, den ich fünf Runden lang übersehen habe: der
Master ist ungemastert.** Gemessen nach EBU R128 liegt er bei **−30,9 LUFS**,
Spitze −4,8 dBFS. Shorts laufen bei etwa **−14 LUFS**. Der fertige Short trug
diesen Pegel unverändert weiter — rund 17 LU leiser als alles andere auf dem
Kanal, und genau so klingt er: dünn und fern.

Dazu ein zweiter Sprung, den ich erst durch die Messung gesehen habe: das
Outro liegt bei **−24,9 LUFS**, also 6,5 LU über dem Hauptteil. Am Übergang
ging der Pegel hörbar hoch.

`--laut` (Vorgabe −14 LUFS) normalisiert jetzt **Hauptteil und Outro auf
dasselbe Ziel**, bevor sie aneinandergesetzt werden. Kette: Hochpass 80 Hz,
milder Kompressor (−26 dB, 3:1), `loudnorm`, Begrenzer auf −1 dBTP. Gemessen
am Ergebnis: Hauptteil −14,5 LUFS, Outro −14,4 LUFS, Spitze −1,4 dBFS. Die
Dynamik schrumpft dabei von 32,7 auf 30,4 dB — es pumpt also nicht. Der
Rauschboden steigt mit, von −62,7 auf −44,2 dB; bei Sprache auf −18 dB sind
das 26 dB Abstand, und entrauscht wird bewusst nicht: Artefakte auf einer
Stimme sind schlimmer als leises Raumrauschen.

**Zeitdehnung jetzt über `rubberband` statt `atempo`.** An derselben Passage
gemessen: `atempo=1.2` hebt die spektrale Flachheit um 8 % und die Energie
über 6 kHz um 11 % — das ist die Rauheit, die WSOLA beim stückweisen
Zusammensetzen erzeugt. `rubberband` bleibt in beiden Werten darunter.
Zeittreue geprüft: die stummen Fenster liegen im Ergebnis 0,03–0,04 s neben
dem Sollwert, also innerhalb eines Bildes.

### Der zweite Einwurf — und wie man ihn findet

Dein Hinweis war der richtige: **„du siehst es doch, wenn die Kamera auf ihn
wechselt."** Der Master schneidet bei Clipsekunde 19,28 auf David, und genau
davor liegt der Einwurf. Was ihn von Sprache trennt, ist nicht die Tonhöhe —
beide Stimmen liegen bei 100–140 Hz, und ein Vergleich der Spektren über
0,3 s trennt sie nicht (Ähnlichkeit zu David 0,72, zu Dir selbst 0,68–0,76,
also gar nichts). Was trennt, ist **Pegel plus Einbettung**: sein Mikrofon
steht heißer. Die Suche läuft jetzt über alle Läufe über −27 dB von 0,10 bis
0,90 s Dauer, die auf beiden Seiten innerhalb von 0,2 s unter −45 dB fallen.
Über den ganzen Clip trifft das zwölf Stellen; **zwei davon stechen heraus:**

| Clipzeit | Spitze | |
|---|---|---|
| 19,20–19,41 | **−15,6 dB** | David, Schnitt auf ihn bei 19,28 |
| 49,56–49,86 | **−19,7 dB** | David, in der Totale |

Die übrigen zehn liegen bei −23 bis −27 dB — das sind Deine eigenen Silben
nach einer Atempause. Beide Einwürfe sind jetzt stumm (gemessen −240 dB).
Dass „like" direkt davor liegt, ist kein Problem: das Wort endet bei 19,13,
danach fällt der Pegel auf −50 dB, und „vulnerability" setzt erst bei 19,65
wieder ein.

### Zwei Logos im Bild

In der Totale trug der fertige Short **Dein Logo doppelt**: einmal das, das
schon im Master eingebrannt ist (gemessen x 0–215, y 875–1080 im
1920×1080-Bild), und einmal unseres in der Mitte. In den Nahaufnahmen fällt
das eingebrannte aus dem 9:16-Fenster heraus, in der Totale nicht.
`bildausschnitt.py --marke 0,875,215,1080` schiebt den Ausschnitt jetzt
darüber — der Kasten der Totale wandert von `75:280` auf `75:75`, alle
anderen bleiben unverändert.

```
python3 video/bildausschnitt.py clip.mp4 --zoom 1.35 --kein-stapel \
        --marke 0,875,215,1080 --json plan.json

python3 video/shorts-render.py --src clip.mp4 --plan plan.json \
        --tempo 1.2 --dehnung rubberband --laut -14 \
        --auto-captions --lang en --model medium \
        --korrekturen video/korrekturen.txt \
        --stumm 19.15:19.56,49.50:49.99 \
        --logo marke/ynb-logo-weiss.png --logo-breite 700 --logo-hoehe 0.877 \
        --outro marke/outro_9_16.mov --out short.mp4
```

**Offen:** zwischen zwei Einblendungen bleibt das Bild kurz ohne Text — an der
längsten Stelle 1,5 s (Clipsekunde 6,18–7,66), weil dort wirklich eine Pause
ist. Die Zeile stehen zu lassen, bis die nächste kommt, wäre ein Einzeiler;
ich habe es nicht ungefragt geändert.
