# Craig Makhosi — die zweite Stelle: Ubuntu

Stand 27.10.2026. Gemessen, **nicht gebaut** — er hat noch nicht zugestimmt.

## Die Quelle ist ein Ausschnitt, keine Folge

`craig-roh.mp4` (Drive: `Craig Makhosi - Ubuntu.mp4`, 1,03 GB,
`11sXLR_Vizd5XXN2Ghn5nvxFek8xzn9bM`) ist **238,65 s lang**, also 3:58.
Die Groesse kommt von der Bitrate, nicht von der Laufzeit. Liegt lokal im
Container; herunterladen muss niemand etwas.

**Das Into-the-Wild-Short benutzte das Fenster 22,80–118,54 s.** Frei sind
damit 0–22,8 (Vorrede: Studium, Buddhismus, „Have you seen the movie Into
the Wild?") und **118,5–238,65**.

## Die freie Stelle traegt

Eine geschlossene Passage ueber Ubuntu, mit einer Struktur, die das erste
Short nicht hat — eine Korrektur mit Pointe:

| Rohzeit | Inhalt |
|---|---|
| 116,7–118,5 | „And Ubuntu, I am because we are." |
| **119,3–122,8** | **„So that's a common misunderstanding, in my judgment."** |
| 124–131 | „it's written a lot … the thing is there is no I in Ubuntu" |
| 138–148 | die Xhosa-Fassung, dann „a person is a person through other people" |
| 154–165 | seine eigene Uebersetzung: „we are who we are through our relations" |
| 169–208 | die Doerfer: kollektives Denken, Clanname statt Eigenname |
| 220–238,2 | **Schluss: die Dankbarkeitsuebung — „I'm so wealthy … it's just a waste"** |

Der Satz bei 119,3 hatte mein erstes Transkript verschluckt. Er ist der
Aufhaenger: erst der bekannte Satz, dann der Widerspruch.

**Das Ende ist wortgenau vollstaendig** — „waste" endet bei 238,2 s, die
Datei bei 238,65.

## Vorschlag

Rohfenster **116,7–238,65** (122,0 s), **ohne Innenschnitte** — defensiv
geschnitten. Bei Tempo 1,45 sind das **84,1 s Inhalt + 4,2 s Outro =
88,3 s**. Damit liegt es im Rahmen seiner bisherigen Shorts (58–90 s);
die 122 s sind Rohzeit, nicht Shortzeit.

## Drei offene Entscheidungen

1. **Ueberlappung:** die ersten 1,8 s („And Ubuntu, I am because we are")
   kommen im ersten Short schon vor. Als Haken richtig — ohne sie muesste
   das Stueck bei „So that's a common misunderstanding" einsteigen, und
   dann hat „that" keinen Bezug. **Seine Entscheidung.**
2. **Musikbett.** Am 24.10. hat er fuer das Tate-Short die lauteste von
   drei Fassungen genommen und gesagt, Musik solle kuenftig genutzt werden.
   Das steht gegen die aeltere Regel „kein Bett". Siehe
   `lernen/content-cinematic.md`.
3. **Xhosa:** Whisper schreibt die Stelle bei 138–148 als Kauderwelsch.
   Richtig ist **„Umntu ngumntu ngabantu"** — gehoert in
   `video/korrekturen.txt`, bevor gebaut wird.

---

## Gebaut am 29.10.2026

Rohfenster **116,70–238,65 s** aus `craig-roh.mp4`, wie vorgeschlagen, ohne
Innenschnitte. Schnittdatei 121,95 s, 3840×2160, 48 kHz.

### Die Mitte des Bildes ist an zwei Stellen leer

Der erste Griff waere ein fester 9:16-Ausschnitt aus der Mitte gewesen, wie
beim Into-the-Wild-Short. Im Probebild bei Sekunde 20 zeigt dieser
Ausschnitt **zwei Bierflaschen, einen Laptop und eine Hand** — kein Gesicht.
Die Aufnahme ist mehrkamerig geschnitten und wechselt zwischen Nahaufnahme
und Totale; in der Totale sitzen beide am Rand.

`bildausschnitt.py` findet sechs Einstellungen und legt die zwei Totalen als
Stapel an:

| Clipzeit | Form | Lippe |
|---|---|---|
| 0,0–2,0 | einzel 1456:0:1215:2160 | 1267 |
| 2,0–20,0 | einzel 1216:0:1215:2160 | 1229 |
| **20,0–31,7** | **stapel** 0:484 + 2126:316 | 672 |
| 31,7–51,5 | einzel 1168:0:1215:2160 | 1229 |
| **51,5–61,6** | **stapel** 0:508 + 2139:316 | 672 |
| 61,6–122,0 | einzel 1312:0:1215:2160 | 1250 |

Gerendert wird deshalb ueber `--plan`, nicht ueber einen festen Ausschnitt.
Die Untertitel folgen damit der Lippe, statt auf einer festen Hoehe zu
stehen — anders als beim Craig-Short mit B-Roll, wo es unter der B-Roll
keine Lippe gibt, der man folgen koennte.

### Einstellungen

`--tempo 1.45` · `--look warm` · Logo 700 px auf 0,877 ·
`--musik momsgotwork.mp3 --musik-unter 0` · Outro 9:16 ·
`--laut aus` und `--dehnung atempo` als Vorgabe, beides unveraendert.
**Keine Einspieler** — die Stelle handelt davon, dass niemand fuer sich
allein jemand ist; Bilder eines Mannes allein in der Wildnis sagten das
Gegenteil.

### Aufloesung: 1080×1920, und das ist nicht die halbe Aufloesung

Aus dem 3840×2160-Bild bleiben im 9:16-Fenster **1215 px Breite** (2160 ×
9/16). Bei 1080×1920 wird also von 1215 auf 1080 verkleinert — 89 % der
vorhandenen Schaerfe. Bei 2160×3840 wuerde dieselbe 1215-px-Spalte auf 2160
**hoch**gerechnet: vier Mal so viele Pixel, kein einziger davon neu.
Gemessen am Probelauf: 253 MB und elf Minuten Rechenzeit gegen 25 MB und
zwei. Die Behauptung, die bisherigen Craig-Shorts seien in halber
Aufloesung geliefert worden, war falsch — 1080 ist hier nahezu nativ.
`--hoch 3840` bleibt im Renderer, lohnt sich aber erst bei einer Quelle,
die hochkant gedreht ist oder aus der ein kleinerer Ausschnitt genommen wird.
