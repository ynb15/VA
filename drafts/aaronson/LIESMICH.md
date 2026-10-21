# Aaronson — Beschreibung, Entwurf 2 (21.10.2026)

Zwei Dateien, beide **nur die Beschreibung**, nichts drumherum — zum Markieren
und Einsetzen in einem Zug:

| Datei | gilt, wenn die Folge läuft |
|---|---|
| `beschreibung-A-master-1.0.txt` | **101:24** (der Studio-Master, unbeschleunigt) |
| `beschreibung-B-export-1.1.txt` | **92:11** (derselbe Master auf 1,1 exportiert) |

**Die Laufzeit entscheidet, nicht ich.** Schau in YouTube Studio nach der
Laufzeit des Uploads und nimm die Datei, die dazu passt. Steht dort etwas
Drittes, sag mir die Zahl — dann rechne ich neu.

---

## Zum Tempo — Du hast recht, und es ist genau die Stelle, an der es bricht

**Die Formel ist:** `veröffentlicht = (Rohzeit − 12,2 s) ÷ Tempo`

Bei 1,1 verschiebt sich das Ende um **über neun Minuten**. Beispiel, dasselbe
Kapitel:

| | Master 1,0 | Export 1,1 |
|---|---|---|
| „The trouble with AI…" | `96:16` | `87:31` |
| „What makes life meaningful" | `98:22` | `89:25` |
| **Laufzeit** | **101:24** | **92:11** |

**Was für diese Folge gemessen ist:** der Versatz Roh ↔ Master ist an elf
Stellen zwischen Minute 1 und 50 konstant **12,2 s** (Korrelation 0,80–0,83).
Ein Tempofaktor von 1,1 würde den Versatz über die Länge **wachsen** lassen —
bei Minute 50 wäre er fünf Minuten, nicht 12 Sekunden. **Im Master von diesem
Studio ist also nicht beschleunigt.** Dazu passt die Laufzeit: 101:24 gegen
102:14 Rohton.

**Was ich daraus nicht schließen kann:** ob Du *danach* auf 1,1 exportierst.
Bei Sutcliffe ist im Handbuch ein Tempofaktor vermerkt, bei Aaronson nicht —
das ist mein Grund für die zwei Dateien statt einer Annahme.

**Und die Lehre für alle künftigen Folgen, damit das nicht jedes Mal
hochkommt:** Sag mir die Laufzeit des fertigen Uploads, einmal pro Folge, und
ich rechne die Timestamps darauf. Eine Zahl, und die Frage ist weg. Ohne sie
rate ich, und bei 1,1 liegt das letzte Kapitel neun Minuten falsch.

## Woher ich das mit dem Foto wusste — aus dem Rohton

Aus `video/transkripte/aaronson-roh.transkript.json`, Rohzeit 101:47:

> *„Can we take a quick picture?" — „Absolutely, absolutely." — „With you
> sitting in your chair, that'd be great."*

**Das steht nur im Rohton, nicht in Deiner Datei** — und Deine Bemerkung, dass
die Studiodatei zum richtigen Zeitpunkt endet, hat meine offene Frage von vorhin
beantwortet. Die Rechnung schließt jetzt auf die Sekunde:

- Rohton endet 102:14, Master 101:24 → 50 s Differenz
- davon 12,2 s vorne abgeschnitten → bleiben 37,8 s
- der Schnittpunkt liegt damit bei Rohzeit **101:36**
- und dort, zwischen *„Of course. Great."* (101:35) und *„To you."* (101:37),
  **hört das Gespräch auf und das Geplauder über Link und Foto fängt an**

Kein Schnitt in der Mitte. **Damit gelten die Timestamps auch hinter Minute 72**
— die Prüfung, um die ich Dich vorhin gebeten habe, ist erledigt. Nur die
Tempo-Frage bleibt.

## Was ich geändert habe

| Du sagtest | geändert |
|---|---|
| Absatz 3 und 4 gehören nicht rein | **beide raus.** Jetzt: Frage → Gast → Inhalt |
| maximal 5 Bullet Points | **5 statt 10** |
| Bullets sind zu lang | **einzeilig**, 10–16 Wörter statt 20–25 |
| zu lang insgesamt | **von ~390 auf ~250 Wörter** Eigentext |

Rausgefallen ist mit Absatz 4 auch Deine Nerven-Passage („today I'm the idiot in
the room"). **Verloren ist sie nicht** — sie steht als erstes Kapitel auf
`0:00`, und `video/aaronson-shorts.md` empfiehlt sie als ersten Short. Dort
wirkt sie stärker als in einem vierten Absatz, den keiner liest.

Die Bullets habe ich auf die KI-Achse gelegt. Quantencomputer, das Jüdische und
die Politik tragen jetzt der dritte Absatz und die Timestamps — **das ist meine
Entscheidung**, weil fünf Bullets über drei Gebiete von jedem Gebiet nur eine
Andeutung liefern. Wenn Du die Politik in den Bullets willst, tausche den
Erdős-Punkt gegen:

> `• Being Jewish after October 7th, the Book of Job, and why might does not make right`

## Die Timestamps bleiben 37

Du hast dazu nichts gesagt, also habe ich nicht gekürzt. Deine Folgen haben
rund 20 — diese hat drei Gebiete statt einem. **Wenn Du auf ~30 willst:**
`29:08`, `34:18`, `48:12`, `61:44`, `78:06`, `91:52` raus (Variante A) bzw.
`26:29`, `31:11`, `43:49`, `56:07`, `71:00`, `83:31` (Variante B). Dann verliert
kein Gebiet seinen Einstieg.

## In YouTube als Draft ablegen — nein, und das ist nicht umgehbar

**Ich kann es nicht.** In dieser Umgebung gibt es keinen YouTube-Zugang; ich habe
die Werkzeugliste eben danach durchsucht, es ist keiner da. Beschreibung,
Titel oder Tags in YouTube Studio schreiben geht nur über die YouTube Data API
mit OAuth — genau das Google-Cloud-Projekt, bei dem Du am 19./20.10. an den
API-Schlüsseln hängengeblieben bist.

**Lesen geht ohne Anmeldung, schreiben nicht.** Das ist die ganze Grenze.

Und selbst mit OAuth bliebe Deine eigene Regel vom 21.10.: *Agenten entwerfen.*
Dann würde ich den Draft anlegen und Du drückst auf Veröffentlichen — der
Unterschied wäre, dass Du nicht mehr kopieren musst.

**Was es billiger macht, solange das so ist:** die beiden `.txt` enthalten
**nichts außer der Beschreibung** — kein Markdown, keine Überschrift, keine
Kommentare. Einmal alles markieren, einmal einsetzen. Das ist der kürzeste Weg,
den ich Dir ohne API bauen kann.

Wenn Du das Google-Cloud-Projekt zu Ende bringen willst, sag Bescheid — dann
schreibe ich Dir auf, welche drei Dinge genau fehlen (Projekt, aktivierte
YouTube Data API v3, OAuth-Client mit `youtube.force-ssl`), statt dass Du das
nochmal selbst zusammensuchst.
