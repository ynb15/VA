# Scott Aaronson — „How safe is AI?" (Fassung 2, 26.10.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

Dateien in `video/shorts/` (MP4s sind gitignored, liegen im Container):

| Datei | Länge | Ton |
|---|---|---|
| `YNB Podcast Scott Aaronson Safety.mp4` | 55,8 s | Stimme + „In This Shirt" bis 51,6 s |
| `YNB Podcast Scott Aaronson Safety (ohne Musik).mp4` | 55,8 s | nur Stimme |

Dazu je `.srt` und `-liste.txt` (nummerierte Streichliste plus die
Auslassungen). Plan: `video/plaene/aaronson-safety2-plan.json`.

---

## Was Fassung 2 von Fassung 1 unterscheidet

Drei Punkte von ihm, alle drei umgesetzt.

### 1 · Schluss auf „the burden is on them"

Fassung 1 lief 2,1 s weiter bis „to explain where this wall is". Teil 2 ist
jetzt aus der Quelle neu geschnitten: **40,30 → 77,90 s** (37,60 s roh, bei
Tempo 1,12 noch **33,633 s**), letztes Wort „them" bei **51,44 s**.

Derselbe Fall wie in der dritten Runde am 20.10.: ein Nachsatz, der den
Satz erklärt, statt ihn stehen zu lassen.

### 2 · Die drei Bilder Totale sind raus

Bei 17,967–18,067 s standen drei Bilder Studio-Totale, die ich am Morgen
des 26.10. als „kurzer Weitblick" **absichtlich** drin gelassen und in
`lernen/content-shorts-2.md` sogar als Regel notiert hatte. Er liest sie als
Glitch. **Seine Lesart sticht meine Begründung** — das ist derselbe Fehler
wie bei `--look aus` am 22.10.

Beim Entfernen ein Werkzeugfund: ein Schnitt mit `-c:v copy` ließ **zwei
Bilder zu viel** stehen (v = 18,033 gegen a = 17,967), weil er bis zum
nächsten Keyframe geht. Neu codiert statt kopiert:

```
ffmpeg -i s1-g.mov -t 17.966667 -r 30 -c:v libx264 -crf 15 ...
```

Ergebnis exakt **539 Bilder = 17,9667 s**. Sieben Bilder über die Naht
einzeln angesehen: Profil, Profil, Profil → Frontale. Kein Rest.

### 3 · Musik, die vor dem Outro aufhört

Er wollte „In This Shirt" darunter, **aber vor dem Outro enden** — das
Gegenteil der AI-2027-Ansage vom 22.10. („dass er es nicht vorm Ende
aufhört"). Beides geht nicht mit `--musik`, dessen Ausblende fest 2 s vor
dem Hauptteil-Ende sitzt. Also wieder ohne `--musik` gerendert und das Bett
danach daruntergemischt:

```
[0:a]asplit=2[st1][st2];
[1:a]aloop=loop=-1:size=2000000000,volume=-30.5dB,
     afade=t=in:st=0:d=0.4,atrim=0:51.6,asetpts=N/SR/TB,
     afade=t=out:st=50.1:d=1.5[bett];
[bett][st2]sidechaincompress=threshold=0.04:ratio=8:attack=15:release=350[duck];
[st1][duck]amix=inputs=2:normalize=0:dropout_transition=0:duration=longest[a]
```

`atrim` auf 51,6 s setzt das harte Ende, die Ausblende liegt davor
(50,1–51,6). Das Outro ab 51,6 s läuft mit seinem eigenen Ton allein.

**Belegt durch Subtraktion**, nicht nach Gehör — musikfreie Fassung
phaseninvertiert auf die Musikfassung, übrig bleibt genau das Bett:

| Zeitraum | Pegel der Differenz |
|---|---|
| 0,0–50,5 s | −40 bis −48 dB, durchgehend |
| 50,5–51,0 s | −55 dB (Ausblende) |
| ab 51,5 s | −80 dB und tiefer = Stille |

Pegel: **Stimme −32,9 dB, Bett −44,3 dB** → 11,4 dB darunter, dazu
`sidechaincompress`. Lautheit der Musikfassung **−29,4 LUFS**.

---

## Abnahme

```
Format 1080x1920 · Tonquelle 48000 Hz · Laufzeit 55.8s
Dateiname ok · Outro da (Abstand 0.2) · 62 Untertitel · Ortscheck sauber
Kein Musikbett: FEHLT — leisestes Prozent bei -44.8 dB
```

Die eine fehlgeschlagene Prüfung ist **gewollt**: das Bett liegt auf seine
Ansage hin darunter. Die Fassung ohne Musik besteht alle Prüfungen
(leisestes Prozent −91,8 dB).

Nebenbei bestätigt: `abnahme.py` lässt die letzten 4,5 s (das Outro) bei der
Musikprüfung außen vor. Mein Befund vom 22.10., das Outro mache die Prüfung
blind, ist im Werkzeug bereits behoben — **die Musikfassung wird auch dann
erkannt, wenn das Bett vor dem Outro endet.**

---

## Aufbau

Drei Einstellungen, 1920×1080-Vorlage → 1080×1920:

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `41:0:608:1080` | 0,000–1,900 | Totale, Kasten auf Yannick — seine Frage |
| 2 | `626:0:608:1080` | 1,900–17,967 | Aaronson, Nah |
| 3 | `606:0:608:1080` | 17,967–51,600 | Aaronson, Nah — Schluss auf „the burden is on them" |

Untertitelhöhen 1100 (Einstellung 1) und 1280 (2 und 3). Hauptteil 51,600 s
+ Outro 4,208 s = **55,808 s**.

Zwei Auslassungen, beide in der `-liste.txt` wörtlich aufgeführt: die
Apokalyptiker-Anekdote (14 s) und der Nachsatz am Schluss (2,1 s).
Ohne die Anekdote wäre das Stück 71 s lang.
