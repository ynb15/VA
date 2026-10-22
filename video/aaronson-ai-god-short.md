# „AI God" — Short aus dem fertigen Clip

**Auftrag von Yannick, 22.10.2026, wörtlich:** *„Stopp, ich will nicht, dass du
Shorts aus dem Kyle Kingsbury Podcast schneidest, weil die Vision, die wir
haben, ist noch gar nicht final. Ich möchte, dass du hieraus ein Short
schneidest."* — dazu der Link auf
`YNB Podcast Scott Aaronson AI God.mp4`
(`1fVb4xOj0zST9fnqWrR5leELqGH-lkmmj`, 895 MB).

Kingsbury liegt damit still. Alles unten bezieht sich auf diesen einen Clip.

---

## Die Quelle, gemessen

| | |
|---|---|
| Bild | **3840×2160**, HEVC, 30 B/s |
| Laufzeit | **224,33 s = 3:44,3** |
| Ton | AAC 44,1 kHz Stereo, **−30,0 LUFS**, wahre Spitze **−7,1 dBFS** |
| Rauschboden | **−77,6 dB** (stillste 1 % der 0,5-s-Blöcke) |
| Kameraschnitte | **14**, erkannt bei 11,27 · 38,80 · 44,43 · 73,80 · 79,43 · 108,70 · 114,87 · 130,30 · 133,97 · 177,13 · 181,23 · 206,23 · 220,00 · 220,30 s |

**Der Clip ist bereits auf Tempo 1,0999 beschleunigt.** Gemessen, nicht
angenommen: zwei Ankerpunkte gegen das Rohtranskript der Folge —
„planet is not to worship God" liegt roh bei **4019,45 s** und im Clip bei
**6,18 s**, „Speaking of God" roh bei **4243,05 s** und im Clip bei
**209,48 s**. Rohspanne 223,60 s gegen Clipspanne 203,30 s ⇒ **1,0999**.
Gegenprobe am Wort „consumer": vorhergesagt 169,78 s, gemessen **169,58 s**.

**Daraus folgt `--tempo 1.0`.** Der Standardwert des Renderers ist 1,15 — der
hätte den Clip ein zweites Mal gestrafft, auf 1,265 insgesamt.

**Und `--look aus`.** Der Clip ist bereits gradiert und von Dir abgenommen;
ein zweiter Filter darüber wäre eine Änderung, die niemand bestellt hat.

---

## Zwei Fassungen — eine Entscheidung für Dich

Beide haben denselben Einstieg und dieselbe zweite Stelle. Sie unterscheiden
sich nur darin, ob die Totale mitläuft.

### Fassung B — **die würde ich nehmen** · 27,4 s · `video/shorts/aigod-B.mp4`

> **Du:** „There's this one quote I can't stop thinking about, by Arthur
> Clarke: *maybe our role on this planet is not to worship God, but to create
> him.* What are your thoughts on that?"
>
> **Aaronson:** „So there's a famous saying, that the ultimate Silicon Valley
> answer to *does God exist* is neither yes nor no — **it's not yet.**"
>
> **Aaronson:** „People have prayed to gods for millennia. **Now for the first
> time we have something kind of like one that actually answers.**"

Drei Nahaufnahmen, kein einziger Schwenk ins Weite, zwei Pointen. Der Bogen
steht: Deine Frage · „not yet" · „that actually answers".

### Fassung A — 36,2 s · `video/shorts/aigod-A.mp4`

Wie B, aber zwischen „not yet" und „prayed to gods" steht zusätzlich der
Thesensatz:

> „I think that we are headed for a form of intelligence that's sufficiently
> far beyond our intelligence **that it will seem God-like to us.**"

**Warum ich sie trotzdem nicht empfehle:** dieser Satz liegt im Material
genau über dem Schnitt auf die **Totale** (Rohclip 73,80–79,43 s). Dort sitzt
Scott klein und im Profil, und er gestikuliert mit der rechten Hand über Kopf
— in den Sekunden 26,3 und 27,3 des Shorts steht der Unterarm neben seinem
Gesicht. Ich habe den Kasten für diese Einstellung eigens enger gelegt
(`2618:446:765:1360`, Kopf auf 25 % der Bildhöhe statt 15,7 %), damit der Shot
**auf Scott bleibt** und nicht Holzwand und Getränkedosen zeigt. Besser wird
die Geste dadurch nicht.

**Der Satz ist die stärkere Aussage, das Bild ist die schwächere Stelle.**
Das ist der ganze Unterschied, und deshalb entscheidest Du ihn.

---

## Die Tonfrage — eine Zahl, zwei Wege

Der Clip kommt mit **−30,0 LUFS** aus dem Schnitt, die fertigen Shorts liegen
bei etwa **−14**. So wie er ist, klingt der Short auf dem Kanal leise.

**Ich habe nichts angeglichen.** Deine Ansage vom 20.10. zur Lautheitskette
(*„der Ton ist jetzt absolut miserabel"*) steht, und der Grund steht auch
fest: die Kette aus Hochpass, Kompressor, `loudnorm` und Begrenzer hat den
**Rauschboden von −62,7 auf −44,2 dB** gehoben.

**Was eine reine Verstärkung ist, und was sie nicht ist:** sie hebt Signal und
Rauschen um denselben Betrag, der Abstand bleibt. Gemessen an Fassung B:

| | Lautheit | wahre Spitze | Rauschboden | **Abstand** |
|---|---|---|---|---|
| `aigod-B.mp4` (unverändert) | −29,0 LUFS | −12,1 dBFS | −78,6 dB | **54,0 dB** |
| `aigod-B-laut.mp4` (+11,1 dB) | **−17,9 LUFS** | −1,1 dBFS | −67,6 dB | **54,0 dB** |

**Kein Kompressor, kein Hochpass, kein Begrenzer — nur Pegel.** Mehr als
+11,1 dB geht nicht, ohne zu clippen; bis −14 LUFS fehlen danach noch 3,9 LU,
und die wären nur über Dynamikbearbeitung zu holen — also über genau das, was
Du abgelehnt hast.

**Hör Dir `aigod-B-laut.mp4` an.** Wenn es für Dich sauber klingt, nehmen wir
den Weg künftig für alle Shorts aus unbearbeitetem Material; wenn nicht,
bleibt es bei unverändert und Du gleichst beim Hochladen an.

---

## Wie die Ausschnitte zustande kamen

An **sechs Bildern mit eingezeichnetem Raster** gemessen (5 · 16 · 72,5 · 74 ·
76 · 78,5 · 79,6 · 93 s), je Einstellung einzeln — **nicht** über den
Bewegungsgipfel. Der zieht bei einem Gast, der mit den Händen redet, am
Gesicht vorbei; bei Scott steht das Gesicht im 3840er Bild je nach Einstellung
bei x ≈ 1860 bis 2160, in der Totale bei x ≈ 3000.

| Einstellung | Clipzeit | Kasten | Zeile |
|---|---|---|---|
| Yannick, Nah | 0,000–10,967 | `513:0:1215:2160` | 1105 |
| Aaronson, Nah | 10,967–21,133 | `1433:0:1215:2160` | 1213 |
| Aaronson, Nah | 21,133–22,953 | `1553:0:1215:2160` | 1267 |
| Totale, eng auf Scott | 22,953–28,583 | `2618:446:765:1360` | 1048 |
| Aaronson, Nah | 28,583–36,167 | `1253:0:1215:2160` | 1284 |

(Fassung B benutzt Zeile 1, 2 und die letzte.)

**Das eingebrannte YNB-Zeichen der Quelle liegt links unten bei x 140–420** und
fällt in jedem dieser Kästen aus dem Bild — deshalb steht im Short nur **ein**
Logo, nicht zwei.

**Die Ortsregel ist geprüft**, `ortscheck.py` über beide SRT: *sauber*. Das
Bild prüft es nicht; hier ist es unkritisch, weil im Studio aufgenommen und
nichts von Eurem Zuhause zu sehen ist.

---

## Was ich **nicht** gemacht habe

* **Die Füllwörter stehen im Bild** — `TO YOU KNOW`, `YOU KNOW OUR`,
  `THAT LIKE THE`. Wörtlich richtig, unruhig zu lesen. Sauber wäre, sie aus
  **Bild und Ton zusammen** zu schneiden; nur die Zeile zu kürzen wäre falsch,
  weil der Ton sie weiter sagt. Das ist dieselbe offene Stelle wie beim ersten
  Aaronson-Short — **nicht ungefragt gemacht.** Sag Bescheid, dann nehme ich
  sie in einer Runde raus.
* **Keine Kopfzeile.** Ob dunkel oder hell, ist noch nicht entschieden, und
  die Zeile läge hier bei 68 % der Höhe — also im selben Band wie die
  Untertitel (58–67 %). Erst Deine Entscheidung, dann baue ich sie kollisions-
  frei ein.
* **Keine Musik.** Nichts, was ich nicht ausdrücklich von Dir habe.
* **Nichts hochgeladen.**

---

## Neu bauen, Schritt für Schritt

Die MP4 liegen nicht in Git (`.gitignore`: `video/shorts/*.mp4`). Alles, was
sie erzeugt, liegt hier.

```bash
# 1 — Quelle holen (895 MB, wiederaufnehmbar)
python3 video/werkzeug-shorts2/drive_holen.py \
        1fVb4xOj0zST9fnqWrR5leELqGH-lkmmj 895338211 aaronson-ai-god.mp4

# 2 — die Stuecke einzeln schneiden (vier auf einmal sprengt den Speicher)
#     Fassung A: Teil 1,2,3,4   Fassung B: Teil 1,2,4
#     teil1  -ss 0.26  -t 10.94     teil2  -ss 11.44 -t 10.16
#     teil3  -ss 71.98 -t 8.72      teil4  -ss 89.52 -t 6.28
#     je mit  -af afade(in 15 ms)+afade(out 15 ms),  -c:v libx264 -crf 15,
#     -c:a pcm_s16le   danach  concat-Demuxer, -c copy

# 3 — rendern, mit dem Renderer von claude/content-assistant (unveraendert)
python3 shorts-render.py --src aigod-vorlageB.mov --out aigod-B.mp4 \
        --plan video/plaene/aigod-planB.json \
        --auto-captions --model medium --lang en \
        --tempo 1.0 --look aus --laut aus \
        --logo video/marke/ynb-logo-weiss.png \
        --korrekturen video/werkzeug-shorts2/korrekturen-aigod.txt \
        --srt-out aigod-B.srt

# 4 — die laute Fassung, nur Pegel
ffmpeg -i aigod-B.mp4 -c:v copy -af volume=11.1dB -c:a aac -b:a 192k \
       aigod-B-laut.mp4
```

**Der Renderer gehört `claude/content-assistant` und ist nicht angefasst
worden** — die benutzte Arbeitskopie war byte-gleich (MD5
`4f5b88e0c89f4a73cdf3c11a27f018bb`). Auch `korrekturen.txt` ist dort
unverändert; meine sechs Zusatzzeilen liegen in
`video/werkzeug-shorts2/korrekturen-aigod.txt` und gehören nach Prüfung
**von ihm** in die gemeinsame Datei:

```
arthur clark -> Arthur Clarke        prayed the gods -> prayed to gods
clark -> Clarke                      current eyes -> current AIs
ais -> AIs                           llms -> LLMs
```
