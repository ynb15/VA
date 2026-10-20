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

**Offen, seine Entscheidung:** zwischen Sekunde 43,6 und 51,7 schneidet der
Studioschnitt auf die Totale — mitten im stärksten Teil der Notiz („But armor
is not strength"). Ich stapele sie derzeit. Alternative: in diesen acht
Sekunden auf ihm bleiben und die Totale auf ihn beschneiden.

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
