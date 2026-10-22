# Aaronson — Übergabe an YNB Shorts II

**Stand 22.10.2026.** Yannick hat entschieden, dass **alle** Aaronson-Shorts
bei *YNB Shorts II (Scott Aaronson)* liegen, Branch `claude/content-shorts-2`.
Alles, was hier zu Aaronson entstanden ist, steht unten. Shorts I fasst
Aaronson ab sofort nicht mehr an.

## Quellen, mit IDs und Maßen

| | |
|---|---|
| **Geschnittene Folge** (Ton und Bild hier hernehmen) | `1C7CUI-B6_fBcdttR_zKIJBYraBMTtUvh` · 16.141.727.375 Byte · ~101 min |
| Left Camera (Rohaufzeichnung Scott) | `1JlDV8oP6y_icD07Y7XCFOuRMasgVI-LO` · 4.192.619.671 Byte |
| Right Cam (Yannick) | `1f-d9PensTxNlBMU7vynkQh5iAioF53lX` · 4.130.194.317 Byte |
| Middle Camera (Totale) | `1w5WPVVr2sECszL7MgwL_SCx09zPCFT9v` · 11.094.309.092 Byte |
| Ordner der Folge | `1Z5ioNa6P2Rn_TjHZOBHjUKQaxYyokb_L` |
| Outro 9:16 | `1kLsW8GjTWR-X4_02r7yqWuRUtCa6h5aX` — liegt als `video/marke/ynb-outro-9-16.mp4` im Repo |

**Zeitbasen:** die Kandidatenliste auf dem EA-Branch
(`video/aaronson-shorts.md`) führt **Rohzeiten** (Kamera-Zeitbasis). Die
geschnittene Folge läuft **12,2 s früher**: Schnittzeit = Rohzeit − 12,2 s.
An elf Stellen geprüft.

## Die Warnung, die hier drei Renderings gekostet hat

**Niemals den Ton aus den `Source Record`-Kameradateien nehmen.** Darauf
liegt das kamerainterne Mikrofon: **44,1 kHz, 128 kbit/s** gegen **48 kHz,
317 kbit/s** in der geschnittenen Folge. Yannick hat es im ersten Moment
gehört: *„der Ton ist absolut katastrophal."*

Der Grund, aus dem hier auf die Kameradatei ausgewichen wurde — der
Umschnitt auf die Totale — trägt an dieser Stelle nicht: im Fenster
Master 5760–5870 ist **kein einziger Kameraschnitt** (`select='gt(scene,0.25)'`
findet null). Die Regie bleibt 110 s auf derselben Einstellung.

## Short 1 „Is AI safe?" — fertig, Zeiten in Masterzeit der Folge

- **Einstieg 5776,50** (ein Sekundenbruchteil vor „**The** trouble with AI…";
  „The" beginnt bei 5776,56, „trouble" bei 5776,80)
- **Raus: 5810,20–5824,35** — der Eltern-Teil, auf seinen Wunsch
  („I mean, it's not even a safe thing for those of us who are parents…
  and the biological intelligences that we're creating")
- **Ausstieg 5831,00** — nach „…in the history of the world" (das Wort
  „world" beginnt bei 5830,64, „And so" bei 5831,12)
- Quelle damit 40,42 s, fertig **39,0 s** inklusive 3,8 s Outro

**Renderparameter, die er abgenommen hat:**

```
--tempo 1.15 --focus 0.53 --lippe 1360
--logo marke/ynb-logo-weiss.png
--outro marke/ynb-outro-9-16.mp4
--kopfzeile "Is AI safe?" --kopfzeile-hoehe 0.18 --kopfzeile-hell
--kopfzeile-groesse 170
--auto-captions --model medium --lang en
```

- **Kopfzeile auf 0,18 statt 0,68:** Scotts Kinn liegt bei 0,67, die
  Untertitelzeile muss darunter. Auf 0,68 stünde das Feld auf der Zeile;
  der Renderer warnt von selbst, wenn sich die Bänder überschneiden.
- **Größe 170:** Feld 899 px = 83 % der Bildbreite. Bei 96 waren es 50 %,
  das war ihm zu klein.
- Untertitel und Liste: `shorts/aaronson-01-is-ai-safe.srt` und
  `shorts/aaronson-01-is-ai-safe-liste.txt`.

## Zweiter Short mit demselben Namen — die Überschneidung

Auf `claude/content-cinematic` liegt `video/shorts/aaronson-01-how-safe-is-ai.srt`,
64 Einblendungen, drei Runden (`3bde9dc`, `5c7be04`, `a4db680`). Das ist ein
**anderes** Stück: dort stellt Yannick die Frage und Scott antwortet.
Cinema ist gebeten, seine Schnittzeiten in Quellzeiten zu übergeben — die
gehen jetzt an Shorts II, nicht hierher.

## Was offen ist

- **Die LUT fehlt.** Isabelles `ynb-shorts-preset.zip` (Slack, 21.10., 4 MB)
  enthält `luts/ynb_look.png`; bei den Agenten angekommen sind nur fünf
  Dateien ohne die LUT. Solange sie fehlt, schreibt der Renderer
  `Look: Annaeherung (LUT fehlt)` — das ist **nicht** sein CapCut-Filter.
- **Sieben weitere Kandidaten** stehen in `video/aaronson-shorts.md` auf dem
  EA-Branch, mit Rohzeiten und Begründung.

## Werkzeuge, alle auf `claude/content-assistant`

`shorts-render.py` (Preset, Kopfzeile, Outro, Logo-Zuschnitt) ·
`abnahme.py` (Prüfung vor der Übergabe) · `kurzliste.py` (Liste zum
Durchstreichen, seit heute Pflicht bei jedem Short) · `ortscheck.py` ·
`master_schnitt.py` (Fenster aus dem Drive-Master, Zeitstempel ab null) ·
`schnittliste.py` · `fuellwoerter.py`
