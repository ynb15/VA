# Ken Stern — Die Kunst des Alterns, Kino-Fassung 2 (17.11.)

**Nicht veröffentlicht.** Liegt zur Abnahme.

| Datei | Länge |
|---|---|
| `YNB Podcast Ken Stern Aging (Kino).mp4` | 63,2 s (59,4 + Outro 3,8) |

## Fassung 2 — fünf Beanstandungen

### 1. Die Schrift stand ausgemessen im Repo

`video/broll-referenz.md`, Abschnitt „Die Schrift", seit 20.10. — an
denselben drei Williamson-Shorts gemessen, aus denen ich die B-Roll-
Geometrie übernommen hatte. Sechs Punkte, alle falsch gebaut:

| | Williamson | Fassung 1 | Fassung 2 |
|---|---|---|---|
| Schreibweise | Kleinschreibung | VERSALIEN | Kleinschreibung |
| Kontur | keine | 8 px schwarz | keine |
| Farbe | weiß | weiß + Gelb | weiß |
| Aktivwort | heller **und fetter** | gelb | heller + `\bord2` in Textfarbe |
| Wörter | zwei | drei | zwei |
| Schrift | aufrecht | aufrecht | **kursiv, auf seine Ansage** |

**Die Messung widerspricht seiner Beschreibung.** Er sagt „geschwungen,
kursiv"; die Vorschaubilder seiner eigenen drei Referenzen zeigen
„comes from" aufrecht. Beides liegt bei:
`video/williamson-schrift-original.png` (vergrößerte Originalzeile) und
`video/schriftwahl-williamson.png` (fünf Varianten an seinem Text).

### 2.–4. Aufbau, Dichte, Tempo

| | Fassung 1 | Fassung 2 |
|---|---|---|
| Einspieler | 6 | **16** |
| B-Roll-Anteil | 47 % | **73 %** |
| Tempo beim Rendern | 1,0 | **1,2** |
| Länge | 75,4 s | **63,2 s** |

Aufbau nach seiner Ansage: „Frankl said" auf ihm · Film durchgehend über
das Zitat · er bei der Überleitung · Film durchgehend über das Essay · er
für die letzten beiden Sätze.

Beim Tempo war der Befund unangenehm: Fassung 1 lief auf **1,0**, während
alle anderen Ken-Shorts auf 1,1 bis 1,15 laufen. Die Vorlage war zwar schon
mit 1,1 geschnitten, im Ergebnis war es trotzdem das langsamste der Reihe.

### 5. Neun Blitze statt siebzehn

Bei 16 Einspielern ist ein Blitz je Schnitt ein Stroboskop. Jetzt auf
Blockwechsel und starke Beats, etwa alle sechs Sekunden. Gemessen:
Helligkeit 76 → 254 → 92 in 0,3 s.

### Zwei Einspieler nach der Sichtprüfung getauscht

Mandela 1:28 trägt „TREASON TRIAL" als Schrift im Archivbild, Mandela 8:00
zeigte eine Hand am Fenster statt eines Gesichts. Beide im Kasten geprüft,
bevor gerendert wurde.

---

# Fassung 1 (16.11.) — der erste Bau

**Nicht veröffentlicht.** Liegt zur Abnahme.

Seine Ansage: *„ich möchte das Ganze nochmal richtig cinematisch aufbereiten
… ich möchte, dass sich die Schrift verändert, dass da Fotoblitze mit drin
sind. Das soll eines der besten Shorts auf YouTube sein. Und wenn du diese
Skills noch nicht hast, dann möchte ich, dass du dir diese Skills anlegst."*

| Datei | Länge |
|---|---|
| `YNB Podcast Ken Stern Aging (Kino).mp4` | 75,0 s (71,2 + Outro 3,8) |

## Was neu gebaut werden musste — und was schon da war

**Schon da, nicht neu gebaut:** B-Roll kann `shorts-render.py` längst —
`--broll` mit `--broll-modus karte`, 980×980 auf Schwarz, Ecken 40, exakt
die am 20.10. an den drei Williamson-Shorts gemessene Referenz. Und in
`video/broll-referenz.md` auf `claude/content-assistant` steht ein ganzer
dokumentierter Lauf mit dem Into-the-Wild-Trailer, **mitsamt der Liste aller
neun Schrifttafeln darin** und der Regel, die ich übernommen habe:

> „Richtig ist, durchgehende Strecken zu nehmen, mitsamt den Schnitten des
> Trailers. Die Schnitte sind dann kein Mangel, sondern das, was es nach
> Film aussehen lässt. Nicht ‚eine Einstellung', sondern ein Block."

**Neu: `video/kino-shorts2.py`.** Zwei Dinge, die der Renderer nicht kann:
bewegte Schrift und Fotoblitze.

`shorts-render.py` gehört Shorts I und ist **nicht angefasst**. Die
Kino-Schicht **importiert** ihn als Bibliothek (`whisper_cues`,
`korrekturen_lesen`, `cues_an_lippen`, `cues_als_srt`, `plan_graph`, die
Stilkonstanten) und schreibt nur die ASS selbst. Ändert Shorts I den Stil,
ändert er sich hier mit. Der Ablauf hat zwei Stufen:

1. `shorts-render.py` baut das Bild **ohne Untertitel** — Plan, B-Roll,
   Look, Logo, Outro, Tempo.
2. `kino-shorts2.py` rechnet die Einblendungen auf der Vorlage, schreibt sie
   als bewegte ASS und brennt sie mit den Blitzen darauf.

## Die sechs Einspieler

| im Short | Dauer | Clip | ab | worauf |
|---|---|---|---|---|
| 6,40–13,10 | 6,7 s | Batman (Funeral) | 1:05,0 | „all we have **suffered**" |
| 16,60–22,60 | 6,0 s | Mandela | 2:08,0 | „having been is a kind of being" |
| 32,30–38,90 | 6,6 s | Alan Watts | 1:10,0 | „aging is not a slow surrender to time" |
| 42,70–47,60 | 4,9 s | Good Will Hunting | 1:28,0 | „layers of insight, empathy" |
| 47,60–51,10 | 3,5 s | Into The Wild | 1:38,8 | „the **rush of youth**" |
| 57,10–63,20 | 6,1 s | Mandela | 8:10,0 | „more rooted, more radiant, more **whole**" |

33,8 s von 71,2 s = **47 %**. Der dokumentierte Into-the-Wild-Lauf lag bei
44 % — dieselbe Größenordnung.

**Die Clips sind 1206×2622 mit Drehmatrix, zeigen also 2622×1206 quer** —
echte Breitwand (2,17:1, Batman 2,6:1). Randlos ins Hochformat blieben
31 % der Breite. Darum die Karte.

Gesichtet per Kontaktabzug, ein Bild je 2–8 s, nach der Regel aus dem
Into-the-Wild-Lauf. Herausgehalten: Alan Watts hat 0:42–0:53 eine
eingebrannte Werbeeinblendung, Mandela 3:16–3:52 die Rivonia-Rede als
Schrift, Into The Wild neun Trailertafeln (Liste lag schon im Repo).

Batman und Into The Wild haben im Quadrat zunächst schwarze Balken gezeigt,
weil ihr Bild breiter als 2,17:1 ist — beide vor dem Schnitt auf ihre
Bildfläche beschnitten (2622×1004 bzw. 2622×974).

## Die Schrift

Jede Einblendung setzt auf **116 %** ein und fällt in 90 ms auf ihre Größe.
Auf neun Schlagwörtern **130 %** über 140 ms. Am fertigen Bild nachgemessen:
„SUFFERED" steht beim Einsetzen **509 px** breit, 140 ms später **391 px**.

**Die Animation sitzt nur auf dem Einsatz der Einblendung.** Der Renderer
gibt je Wort eine eigene Dialogzeile aus, damit das gesprochene Wort gelb
wird; bekäme jede davon die Animation, zuckte die Zeile bei jedem
Wortwechsel. Beide Ebenen (Kontur und Gewichts-Nachzug) bekommen denselben
Animationskopf, sonst franst die Schrift.

## Die Blitze — und der Fehler, der mich einen Durchlauf gekostet hat

Sieben Blitze: die sechs Schnitte in die B-Roll plus 70,38 auf „NOT FEARED".
Ein Bild fast weiß, danach exponentieller Abfall über 0,2 s.

**Der erste Durchlauf war schwarzrot.** Der Ausdruck lautete
`0.95*exp(-(t-T)/0.055)*between(t,T,T+0.2)`. Für Zeiten weit **vor** einem
Blitz wird `-(t-T)/0.055` groß positiv — bei einem Blitz 64 s später ist das
`exp(1164)`, also `inf`, und `inf*0` ist **NaN**. Ein einziger Blitz am Ende
färbt damit alles davor ein.

Behoben mit `exp(-max(0,t-T)/0.055)`. Sichtbar wurde es nur, weil ich
Einzelbilder aus drei verschiedenen Stellen geprüft habe — an der Stelle bei
47,6 s war der letzte Blitz nah genug, dass der Exponent noch endlich blieb,
und dort sah alles richtig aus.

## Zeilenhöhe auf 1000 vereinheitlicht

Der Aging-Plan hatte 1000 (nah) und 1020 (Totale). Zwei Einblendungen laufen
über einen Einstellungswechsel und sprangen dort um 20 px mitten im Wort —
dieselbe Ursache wie beim Meaningful-Short am 11.11., nur kleiner. Jetzt
1000 für alle fünf Einstellungen.

Nebenbefund: `cues_an_lippen` teilt so eine Einblendung in zwei Teile mit
demselben Text. Im Bild richtig, in der Strichliste stand der Text zweimal
(„EXPERIENCES BUT EXPERIENCES BUT"). Die SRT wird jetzt **vor** dem
Lippen-Teiler geschrieben.

## Ton

„In This Shirt" ab 0:23,25. Bett nach Bändern, gegen die abgenommene Fassung:

| | <300 Hz | 300 Hz–2 kHz | 2–8 kHz |
|---|---|---|---|
| bisher | 24,6 | 21,6 | 7,2 |
| **Kino** | **31,2** | **28,1** | **12,6** |

Rund 6 dB lauter, nach seiner Ansage zur Musik. Hauptteil −27,2 LUFS,
Spitze −9,2 dB.

## Offen

- **Die fünf Links enthalten keinen Steve-Jobs-Clip**, sondern Good Will
  Hunting und Into The Wild. Mit dem gearbeitet, was da ist.
- `luts/ynb_look.png` fehlt weiter.
- Eveleth als `.otf` in `video/fonts/`.
