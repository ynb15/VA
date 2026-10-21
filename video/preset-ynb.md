# Sein Shorts-Preset, eingebaut — Stand 21.10.2026

Am 21.10. hat er den Ordner übergeben, mit dem seine Shorts bisher gebaut
wurden: *„ist jetzt der Filter und die Schrift, die wir bisher für meine
Shorts verwendet haben, kannst du das jetzt ab sofort bitte auch
einbauen"*. Das hier ist der Abgleich — **seine Werte gelten, meine
Messungen weichen.**

## Was sich in `shorts-render.py` geändert hat

| | bisher hier | jetzt (sein Preset) |
|---|---|---|
| Schrift | DejaVu Sans Bold | **Inter Black** aus `fonts/` (Ersatz für Eveleth) |
| Schriftgröße | 78 | **82** |
| Gelb | `#FFD530` | **`#F9F13A`** |
| Zeilenbreite | 1000 px (Rand 40) | **777 px = 72 % der Breite** |
| Höhe ohne Lippe | 320 px über dem Rand | **Zeilenmitte auf 70 % der Höhe** |
| Logobreite | 520 px | **302 px = 28 % der Breite** |
| Logohöhe | 0,845 | **0,87** |
| Gradation | mein warmer Look | **sein CapCut-Filter als LUT** (`--look preset`) |

Kontur bleibt 8 px, höchstens 3 Wörter je Einblendung, Versalien — darin
waren beide Fassungen schon gleich.

## Zwei Stellen, an denen ich nicht wörtlich übernommen habe

**1. Die Lippe schlägt die 70 %.** Sein Preset setzt die Zeile fest auf
70 % der Höhe. Hier folgt sie der Lippe des Sprechers, weil er genau das
am 21.10. am Rick-Short verlangt hat (*„dass der Text nicht direkt unter
seiner Lippe ist"*). Die 70 % sind jetzt der Wert für den Fall, dass keine
Lippe gemessen ist. Beides gleichzeitig geht nicht; die jüngere Ansage
gewinnt.

**2. Die Breitenmessung ist korrigiert.** Sein `render_short.py` misst die
Zeilenbreite mit PIL und vergleicht sie mit 72 % des Bildes. libass legt
die Schriftgröße aber nicht aufs Geviert, sondern auf Ober- plus
Unterlänge — bei Inter Black 1,21 Geviert. Gemessen am gerenderten Bild:
`WHAT MAKES LIFE` ist bei 82 px **643 px** breit, PIL sagt 776. Ohne die
Korrektur misst der Umbruch 21 % zu breit und teilt Dreier, die längst
passen. Sichtbare Folge: `WHAT MAKES LIFE` bleibt hier **auf einer Zeile**,
sein Preset hätte es getrennt.

## Probe

`schriftprobe-preset.png` — Inter Black 82, Gelb `#F9F13A` auf dem
gesprochenen Wort, Kontur 8 px, Zeile auf 70 % der Höhe, Logo 28 % breit
auf 0,87. Die Zeile misst 725 px, die Schranke liegt bei 777.

## Was fehlt

- **`luts/ynb_look.png` — der Filter selbst.** In der Übergabe lagen nur
  `make_lut.py` und die Anleitung, nicht die LUT und nicht der
  CapCut-Export. Ohne sie läuft die Annäherung aus seinem Preset
  (entsättigt, kühl), und der Renderer schreibt das in die Ausgabe:
  `Look: Annaeherung (LUT ... fehlt)`. **Das ist nicht sein Filter.**
- **Eveleth** (die CapCut-Schrift). Liegt die `.otf`/`.ttf` in `fonts/`,
  nimmt der Renderer sie von selbst und lässt das Nachziehen weg, mit dem
  Inter Black auf Eveleth-Gewicht gebracht wird.
- **Chrom-Logo und Outro** aus seinem `assets/`-Ordner. Hier liegt
  `marke/ynb-logo-weiss.png`; `--outro` gibt es schon.

## So kommt die LUT zustande (5 Minuten, in CapCut)

`luts/hald_identity_1080.png` liegt bereit — hier erzeugt und geprüft:
durch `make_lut.py` zurückgerechnet kommt die Identität **pixelgenau**
wieder heraus.

1. Neues CapCut-Projekt, Format **1:1**.
2. `luts/hald_identity_1080.png` auf die Timeline, ~3 s, auf **Vollbild**
   skalieren — Bild füllt das Quadrat randlos, kein Zuschnitt.
3. Den Oppenheimer-Filter in seiner Stärke darauf. Keine Vignette, kein
   Korn, sonst nichts.
4. Als Video exportieren (1080p) und: `python3 make_lut.py export.mp4`
5. Danach rendert `--look preset` mit seinem Filter statt mit der
   Annäherung; in der Ausgabe steht dann `Look: LUT ...`.

Die Vignette kommt im Renderer dahinter (`vignette=PI/6`), wie in seinem
Preset — deshalb darf sie nicht in den Export.
