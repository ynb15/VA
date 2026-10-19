# David Sutcliffe — Shorts aus der veröffentlichten Folge

**Folge:** „The Hollywood Star Who Quit Everything To Heal Men: Feminism,
Manosphere & Andrew Tate (4K)" · `frNOUgxE0IM` · hochgeladen 30.09.2026 ·
**116:33** · **2.321 Aufrufe**, 10 Likes, 7 Kommentare (gemessen 19.10.2026).

**Master im Drive:** „YNB Podcast: David Sutcliffe"
`1oJjeQXjfIYtYph0gxfe8V1dhv17BBlPT` · **18,6 GB** · 1920×1080, 30 fps,
21 Mbit/s · **125:18**.

---

## Der Versatz zwischen Master und Veröffentlichung

**Die Zeitmarken passen nicht aufeinander** — das ist die erste Falle.
Der Master ist **8:45 länger**, und der Unterschied verteilt sich über die
ganze Folge, weil im Fluss gekürzt wurde. Zwei Messpunkte, je über eine
Tonprobe aus dem Master gegen das veröffentlichte Transkript:

| veröffentlicht | Master | Versatz |
|---|---|---|
| 08:52 | 10:00 | **+68 s** |
| 86:32 | 92:08 | **+336 s** |

Daraus: **Versatz ≈ 68 s + 0,0575 × (veröffentlichte Sekunde − 532)**.
Die Schätzung traf bei beiden geprüften Fenstern auf wenige Sekunden genau —
aber **immer nachmessen**, die Kürzungen sind klumpig, nicht gleichmäßig.

---

## Geschnitten und fertig

| # | Datei | Länge | Master | Inhalt |
|---|---|---|---|---|
| 1 | `shorts/sutcliffe-01-therapeut.mp4` | 35 s | 5527–5562 | „Your therapist better be in therapy" |
| 2 | `shorts/sutcliffe-02-drop-the-story.mp4` | 34 s | 1367–1401 | „Can you drop the story?" |
| 3 | `shorts/sutcliffe-03-love-me.mp4` | 58 s | 5143–5201 | „I just needed you to love me" |

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
idea any of that was inside me." Mit 58 s der längste — der Bogen braucht ihn.

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

# 2. Kamerawechsel und Kopfposition finden
python3 video/bildausschnitt.py clip.mp4 --json plan.json

# 3. Rendern, Untertitel aus dem Ton des Clips
python3 video/shorts-render.py --src clip.mp4 --plan plan.json \
        --auto-captions --model small --out short.mp4
```

**Der Trick bei Punkt 1:** die 18,6-GB-Datei wird nie geladen. Drive beantwortet
Bereichsanfragen, PyAV nimmt ein dateiähnliches Objekt — **gemessen 200–260 MB
pro Fenster** statt 18,6 GB, bei 12,8 MB/s.

**Der Grund für Punkt 2:** der Studioschnitt wechselt die Kamera mitten im
Short — im 34-Sekunden-Fenster von Short 2 dreimal. Ein fester 9:16-Ausschnitt
trifft dann die Zimmerpflanze statt den Sprecher. Die Erkennung arbeitet über
**Bewegung**, nicht über Hautfarbe: im warmen Studiolicht galten 26–48 % des
Bildes als Haut, Holzregal eingeschlossen.

**Was noch offen ist:** ob eine oder zwei Personen im Bild sind, erkennt das
Werkzeug nicht selbst. Bei einem Zweier-Shot schneidet es auf den, der sich
bewegt — brauchbar, aber eine gestapelte Fassung (beide übereinander) wäre
besser. Der Stapel-Modus ist gebaut (`--layout stapel`), nur die automatische
Entscheidung fehlt. Bis dahin trage ich sie von Hand in den Plan ein.
