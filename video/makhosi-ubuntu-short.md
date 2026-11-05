# Craig Makhosi — „There is no I in Ubuntu" (05.11.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

Auf seine Ansage: *„fangen da gerne an mit meiner Fehldefinition, wo ich
sage, Ubuntu, I am because we are, und dann erklärt Craig, warum das falsch
ist. und es sollte enden bei: we are through our relations. Stell bitte
sicher, dass du die richtige Worte findest für die Xkhosa Worte die Craig
nutzt."*

| Datei | Länge |
|---|---|
| `YNB Podcast Craig Makhosi Ubuntu.mp4` | 54,2 s (50,0 + 4,2 Outro) |

Dazu `.srt` und `-liste.txt`. Plan: `video/plaene/makhosi-ubuntu-plan.json`.

---

## Quelle

Nicht die Folge — die liegt nicht vor —, sondern sein eigener Ausschnitt
**„YNB Podcast - Craig Makhosi - Ubuntu(1).mp4"**
(`1KqnuMz1X3SZ7g5vd5487x-5eOM_Dk7u4`, 1,04 GB, **3:58,65**, 3840×2160 HEVC,
30 fps, Ton 44,1 kHz). In 1,3 Minuten mit `drive_holen.py` geladen.

**Das ist das erste 4K-Material in dieser Reihe, und es ändert die
Rechnung.** Bei 1920×1080-Quellen kostet der 9:16-Ausschnitt eine
Hochskalierung von 1,78×. Hier ist der volle Höhenausschnitt **1215×2160**
und wird auf 1080×1920 **herunter**gerechnet (0,89×); die Totale ist mit
**1080×1920 exakt 1:1** geschnitten, ohne jede Skalierung.

**Tempo unverändert (1,0):** der Ausschnitt ist bereits ein Export seines
fertigen Schnitts, läuft also schon auf Endgeschwindigkeit. Eine weitere
Dehnung wäre doppelt.

## Was drin ist

Ausschnittzeit **1:56,40 – 2:46,37**, **50,0 s in einem Zug — keine
Auslassung, kein Innenschnitt.** Alle vier Einstellungswechsel sind die der
Folge, am Material gemessen (Szenenwerte 0,38–0,45):

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `1409:0:1215:2160` | 0,000–2,200 | Yannick — „Ubuntu, I am because we are" |
| 2 | `1352:0:1215:2160` | 2,200–20,233 | Craig, Nah |
| 3 | `2404:200:1080:1920` | 20,233–31,967 | Totale, Kasten auf Craig — die isiXhosa-Wörter |
| 4 | `1352:0:1215:2160` | 31,967–49,967 | Craig, Nah — bis „through our relations" |

**Yannick bleibt bei seinem eigenen Satz im Bild.** Die Folge schneidet an
genau dieser Stelle selbst auf ihn (116,40 → 118,60 der Quelle), und das
habe ich übernommen. Seine Rückmeldung dazu, noch während ich schnitt:
*„nein ich kann da drin bleiben weil ich das doch da sage."*

Untertitelhöhen 1100 (er) · 1080 (Craig nah) · 1020 (Totale) — höher als in
den Aaronson-Shorts (1280), weil die Gesichter in diesem Studio höher im
Bild stehen.

---

## Die isiXhosa-Wörter

Craig nennt das Sprichwort zweimal:

> **Umntu ngumntu ngabanye abantu** — *oder* — **Umntu ngumntu ngabantu**
> „a person is a person through or by means of people"

**Schreibweise isiXhosa, nicht isiZulu.** Zulu: *umuntu ngumuntu ngabantu*;
Xhosa lässt das u fallen: *umntu*. Craig sagt selbst „defined in **Xhosa**".

**Vier Durchläufe, weil einer nicht reicht:**

| Lauf | Ergebnis |
|---|---|
| `medium`, normal | „umtu ngumtu ngabania ubuntu ah ngabania abantu" — **und die kurze Form gar nicht** |
| `large-v3`, normal | „umtu ngumtu ngabanya abantu / otherwise umtu ngumtu ngabantu" |
| `large-v3`, 0,7× | wortgleich |
| `large-v3`, 0,6× | wortgleich |

`medium` verdoppelt also „ngabanye" und **überhört die kurze Form
vollständig** — zwischen „otherwise" und „which" klafft eine Lücke von
2,2 s, in der die Wörter gesprochen werden. Beides wäre eingebrannt
gewesen.

Schreibweise zusätzlich gegen Quellen geprüft (BU African Studies, SA
Ubuntu Foundation, Wikipedia „Ubuntu philosophy"): beide Formen belegt, die
kurze ist die bekanntere. `iafrika.org` und `en.wikipedia.org` sind aus
dieser Sitzung nicht erreichbar — die Prüfung stützt sich auf die
Suchergebnisse, nicht auf die Seiten selbst.

### Die Korrekturen

```
in cross as                                      -> in Xhosa as
umtu ngumtu ngabania ubuntu ah ngabania abantu   -> Umntu ngumntu ngabanye abantu
otherwise which                                  -> otherwise Umntu ngumntu ngabantu which
like the day car                                 -> like Descartes
i and ubuntu                                     -> I in Ubuntu
```

Die dritte **fügt ein**, wo das Modell nichts geschrieben hat:
`korrekturen_anwenden` verteilt die Ersetzung gleichmäßig über die Zeit der
ersetzten Gruppe, und die Lücke ist genau die Sprechzeit. Nachgemessen
liegen die eingefügten Wörter auf 0,05 s genau auf dem gesprochenen Wort.
**Das ist die erste Korrektur in dieser Reihe, die etwas hinzufügt statt
etwas zu ersetzen** — der Mechanismus kann es, weil er n→m-Abbildungen
zulässt.

## Abnahme

1080×1920 · 48 kHz · 54,2 s · Outro da · 66 Untertitel · Ortscheck sauber.

**„Kein Musikbett" schlägt fehl — und das ist ein Fehlalarm.** Gemessen
−62,4 dB im leisesten Prozent, Schwelle ist −65 dB. Es liegt keine Musik
darunter; der **Rohausschnitt misst an derselben Stelle −62,5 dB**, am
Anfang des Ausschnitts −61,7 dB. Das ist der Raumton dieses Studios.
Zum Vergleich: das Aaronson-Studio liegt bei −85,3 dB.

**Die Schwelle ist an einem einzigen Studio kalibriert.** Beschrieben, nicht
geändert — `abnahme.py` gehört Shorts I.

## Musik

Keine. Nicht angesagt, und nach der Regel vom 26.10. („bei Musik gilt immer
die Ansage zu diesem Stück") wird hier nicht geraten. Die Kette aus dem
Safety-Short liegt bereit, falls er sie will.

---

## Nachtrag 05.11.: zwei Musikfassungen

Auf seine Ansage: je eine Fassung mit *In This Shirt* und mit *On The Nature
Of Daylight*, Letztere **nicht am Songanfang** — *„denk dran, dass On The
Nature Of Daylight vorgespielt werden muss."*

Die Regel dahinter stand beim Gastauftritte-Agenten
(`lernen/content-gastauftritte.md`, 22.10.): die `ab_sekunde` gehört auf den
Sprung in den Höhen, nicht auf die erste Sekunde mit vollem Pegel.

| Titel | ab | erste 2 s gegen Schnitt | Pegel des Betts |
|---|---|---|---|
| In This Shirt | **0:23,25** | −0,2 dB (bei 0:00: −4,1 dB) | −14,4 dB |
| On The Nature Of Daylight | **0:24,50** | −2,8 dB (bei 0:00: −12,8 dB) | −3,6 dB |

Bei *In This Shirt* ist der Einsatz ein Sprung (19 dB über 2 kHz in einer
Zehntelsekunde), bei Richter eine **Steigerung über 1,2 s** (23,3 → 24,5) —
deshalb liegt der Start an ihrem Ende. Maßstab ist dabei nicht die absolute
Abweichung, sondern die **Streuung des Stücks selbst**: sie beträgt hier
2,3 dB, die Startabweichung 2,8 dB.

Beide Betten: Einblende 0,2 s · 0,00–49,97 s · Ausblende 4 s (46,0–50,0) ·
Outro allein. `sidechaincompress` ratio 4, release 250 (seine Ansage vom
21.10., sanfter wegdrücken). Durch Subtraktion geprüft: hörbar ab der
ersten Sekunde, ab 50,0 s unter −75 dB.

**Nebenbefund, der die Schwellenfrage von oben entscheidet:** dasselbe Short
misst ohne Musik −62,4 dB, mit In This Shirt −35,0 dB, mit Richter
−38,1 dB. Ein Bett hebt den Boden um **24 bis 27 dB** — die Prüfung gegen
den Boden der Quelle trennt beide Fälle sauber, eine feste Schwelle nicht.

**Rechte:** *On The Nature Of Daylight* ist der einzige nie getestete Titel
im Ordner und zugleich der heikelste (Handelsaufnahme, „Arrival",
„Shutter Island"). Aus demselben Ordner hat *Daylight* am 22.10. zwei
veröffentlichte Shorts weltweit gesperrt. Geliefert mit dem Hinweis, ihn
vorher an einem ungelisteten Testupload zu prüfen.

**Offen aus diesem Lauf:** AI 2027, Safety und Belief tragen *In This Shirt*
noch **ab 0:00**, also gegen diese Regel. Je eine Minute Arbeit, wenn er sie
neu gemischt haben will.
