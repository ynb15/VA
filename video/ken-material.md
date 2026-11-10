# Ken Stern — das Material

Stand 10.11.2026. Aufnahme **14.09.2026**. Gast: Ken Stern, ehemaliger
Wahlkampfanwalt von Bill Clinton und neun Jahre Chef von NPR, Autor von
*Republican Like Me*.

## Der Ordner, über zwei Wege geprüft

Ordner `18nUfXLmrKTPBfgwh90MATPKjgmNsjTJQ`, zusätzlich die Datei-ID selbst
abgefragt — beide Wege nennen dieselbe Datei im selben Ordner. Vier Einträge,
eine zweite Seite der Suche ist leer:

| Datei | Größe | Was es ist |
|---|---|---|
| `00 YNB Podcast: Ken Stern` (Doc) | 823 KB | Vorbereitung |
| `00 YNB Podcast: Ken Stern` (mp4) | **16,82 GB** | die Aufnahme |
| `YNB & Ken Stern Ice Bath` (jpeg) | 2,5 MB | Foto |
| `YNB & Ken Stern` (jpeg) | 2,4 MB | Foto |

**Keine Schnittfassung.** Und: das Vorbereitungsdoku trägt **kein
Transkript und keine Kapitelliste** — nur 3351 Zeichen Text (Titelideen,
Themen, Zahlen zum Medienvertrauen, Fragen). Anders als bei Craig gibt es
hier also keine Abkürzung; das eigene Transkript ist das einzige.

## Die Aufnahme

| | |
|---|---|
| Dauer | **6333,43 s = 1:45:33** |
| Bild | 1920×1080, `r_frame_rate` **30/1**, `time_base` 1/30000 |
| Ton | 48 kHz, 317 kbit/s AAC — die Signatur der Mischung |

## Es ist die ganze Folge

Drei Belege, keine Rechnung:

1. **Der Anfang ist der Anfang.** Erstes Segment, 00:00:00: *„Ken Stern,
   what's the most American thing you've ever done?"* — genau die Frage, die
   im Vorbereitungsdoku unter „Intro" steht. Kein Vorgespräch davor.
2. **Das Ende ist das Ende.** 01:45:28: *„Thank you for having me on the
   show. It was a fun conversation. … Let's get a fist bump in. All right,
   there we go."*
3. **Der geeichte Anker trifft auf die Sekunde.** Das fertige Short
   `YNB Podcast Ken Stern Meaning` sitzt im Masterfenster 6150,1–6189,3 s.
   Im Transkript steht bei **01:42:30** — also 6150 s — *„since we're on the
   Man's Search for Meaning podcast, what makes life meaningful?"* Die
   Zeitleiste des Transkripts und die des Masters sind damit dieselbe.

Bei Kingsbury deckte ein Transkript nur 61 % der Folge ab, weil die Rohdatei
nicht die Folge war. Hier ist sie es.

## Der Tonabzug, über die Laufzeit geprüft

`ffprobe` auf das Ergebnis meldet **6333,433313 s** gegen 6333,43 s im
Container — kein Fehlbetrag. Geprüft wurde die **Laufzeit**, nicht die
Dateigröße und nicht der Rückgabewert: genau an dieser Folge wurden schon
einmal 600 s bestellt, 192 s geliefert und ein sauberer Abschluss gemeldet.
Der Abzug lief 55 Minuten und holte die vollen 16,82 GB.

## Keine Sprecherzuordnung

Gemessen an einer Minute aus der Mitte (Rohzeit 3000–3060): Pegel L und R
beide −35,6 dB, **Korrelation 1,0000**, Differenzsignal −93,7 dB,
Quartilsabstand des Pegelverhältnisses **0,00 dB**. Doppelmono. Wer spricht,
steht im Transkript deshalb nicht.

## Transkript

`video/transkripte/ken-roh.transkript.md` · **1760 Segmente** · 105,6 min ·
`medium` · in elf Stücken gerechnet, Grenzen auf Sprechpausen, Stand nach
jedem Stück im Repo.

**Ein Hinweis für spätere Shorts:** bei **00:58:18** steht *„Deaths from
suicide and drug overdose"*. Seine Ansage, „suicidal" im Text zu zensieren,
trifft dieses Wort nicht wörtlich — wer die Stelle verwendet, wendet die
Regel sinngemäß an.

Noch offen: Clip- und Short-Auswahl, Paket. Dieser Auftrag war nur das
Transkript.
