# Scott Aaronson — „What do you believe in?" (26.10.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

Auf seine Ansage: *„zum Ende hin frage ich ihn ja auch sehr viel über seine
Religion, über Judentum und alles. Das würde ich gerne auch noch als Short
nehmen."*

| Datei | Länge | Ton |
|---|---|---|
| `YNB Podcast Scott Aaronson Belief.mp4` | 59,2 s | Stimme + „In This Shirt" bis 55,0 s |
| `YNB Podcast Scott Aaronson Belief (ohne Musik).mp4` | 59,2 s | nur Stimme |

Dazu je `.srt` und `-liste.txt`. Plan: `video/plaene/aaronson-belief-plan.json`.

---

## Was drin ist

Rohzeit **1:11:38–1:14:14**. Seine Frage „What do you believe in?", dann
Aaronsons Antwort: jüdische Familie · mit zwölf, über Asimov, Sagan und
Dawkins: *„this is really all a bunch of Iron Age myths, isn't it?"* ·
militanter Atheist · und die Kehrtwende *„a more relaxed attitude — this is
just part of my history, my culture."*

**Eine Auslassung**, bei 00:43.7 im fertigen Short: Rohzeit 1:12:27–1:14:02,
1:35 Minuten — der Teil, in dem die Wissenschaft Gott in eine immer engere
Ecke drängt, und die Hillel-Geschichte. Wörtlich in der `-liste.txt`.
Grund ist allein die Länge; inhaltlich schließt *„and so I sort of evolved"*
direkt an *„militant atheist"* an.

Die **Hillel-Geschichte** (1:13:06–1:14:02, ~56 s) trägt für sich ein
eigenes Short. In der Liste steht sie als Vorschlag, dazu sechs weitere
Stellen des Blocks bis 1:19:43. Ab 1:19:44 geht es um Oktober 7 und Gaza —
daran baue ich nichts ohne ausdrückliche Ansage.

---

## Aufbau

Vorlage aus zwei Stücken des Masters, Tempo 1,12, mit dem concat-**Filter**
zusammengesetzt (v 54,967 s / 1649 Bilder, a 54,979 s).

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `41:0:608:1080` | 0,000–1,161 | Totale, Kasten auf Yannick — seine Frage |
| 2 | `686:0:608:1080` | 1,161–35,654 | Aaronson, Nah |
| 3 | `1166:0:608:1080` | 35,654–40,893 | Totale, Kasten auf Aaronson |
| 4 | `686:0:608:1080` | 40,893–43,733 | Aaronson, Nah — „militant atheist" |
| 5 | `596:0:608:1080` | 43,733–54,967 | Aaronson, Nah — zweites Stück |

Die ersten vier Wechsel sind **die Kameraschnitte des Studios**, am
Vorlagenband nachgemessen (1,167 · 35,667 · 40,900 bei Score ≈ 0,53).
Der einzige eigene Schnitt ist der bei 43,733 — und er liegt zwischen zwei
sehr ähnlichen Nahaufnahmen (Score 0,064), sein Kopf springt dort ein Stück.
Als Gegenmittel liegt ein engerer Kasten für Stück 2 bereit, dann liest es
sich als gewollter Schnitt; nicht gebaut, weil er es nicht angesagt hat.

Kästen an **15 Einzelbildern** über alle fünf Einstellungen gemessen: sein
Gesicht wandert in den Nahaufnahmen zwischen x 850 und 1120, in Stück 2
zwischen 770 und 1050 — daher die zwei verschiedenen Kästen (686 und 596).
Die beiden Totale-Kästen sind dieselben wie im Safety-Short.

## Untertitel

67 Einblendungen, wörtlich inklusive aller „you know". **Eine Korrektur:**
bei 0:20.8 hört `medium` am gedehnten Ton *„well"*; am ungedehnten Ton
sagt `large-v3` *„so, I said, wow, this is really all a bunch of Iron Age
myths, isn't it?"* — also **wow**. In `korrekturen-religion.txt` als
`said well like -> said wow like` festgehalten.

Namen kamen ohne Zutun richtig: Isaac Asimov, Carl Sagan, Richard Dawkins,
Iron Age, Hebrew day school.

**Nicht mit `large-v3` durchtranskribiert**, obwohl es das bessere Modell
ist: es glättet seine Stotterer (aus *„like this is, this is really all"*
wird *„this is really all"*). Für eingebrannte Untertitel, die zu den Lippen
passen müssen, ist das ein Nachteil, kein Vorteil.

## Musik

Nicht angesagt, deshalb als Annahme gebaut und in der Liste benannt:
„In This Shirt", Bett 0,00–54,97 s, Ausblende 53,5–55,0, Outro allein.
Durch Subtraktion geprüft: **−40 bis −50 dB durchgehend, ab 55,0 s unter
−72 dB**. Stimme −34,4 dB, Bett −43,9 dB.

## Abnahme

1080×1920 · 48 kHz · 59,2 s · Outro da · 67 Untertitel · Ortscheck sauber.
„Kein Musikbett" schlägt bei der Musikfassung fehl — gewollt. Die Fassung
ohne Musik besteht alle Prüfungen (leisestes Prozent −85,3 dB).

## Material

Der Master liegt als Sparse-Datei mit Byte-Fenster (`drive_fenster.py`),
Fenster Masterzeit 4217–4458 s, 1142 MB von 16,1 GB.
**Zeitrechnung: Rohzeit = Masterzeit + 12,6 s**, geprüft an „What do you
believe in?" (Master 4285,96 → roh 1:11:38,6, Transkript 1:11:38).
