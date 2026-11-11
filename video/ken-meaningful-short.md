# Ken Stern — „What makes life meaningful?" (11.11.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

| Datei | Länge | Ton |
|---|---|---|
| `YNB Podcast Ken Stern Meaningful (In This Shirt).mp4` | 58,5 s | Stimme + Bett bis 54,3 s |
| `YNB Podcast Ken Stern Meaningful.mp4` | 58,5 s | nur Stimme |

Plan: `video/plaene/ken-meaningful-plan.json`.

---

## Was drin ist

Rohzeit **1:42:29,19 – 1:43:31,60**, 62,4 s roh, bei Tempo **1,15** noch
54,27 s (1628 Bilder). **Eine Stelle am Stück, kein Innenschnitt, keine
Auslassung.**

> **Yannick:** „Since we're on the *Man's Search for Meaning* podcast — what
> makes life meaningful?"
> **Ken:** „So, not having to eat water buffalo for 10 days. … I've gotten so
> much mileage over the years from that story, I wouldn't have it any other
> way. … I think the hackneyed answer, which I'll give because it's kind of
> hackneyed: having a purpose, having a reason for getting up in the morning.
> But ultimately I think **we get meaning from others** — helping others,
> being with others, being surrounded by others. We all have our interior
> lives, but I think it's our exterior life that gives most of us purpose and
> meaning. I get meaning from being a father in relation to my son, a husband
> in relation to my wife, a friend to my friends, someone who brings service.
> That's what gives me meaning. **All of it is in relation to others.**"

### Die alte Fassung endete zu früh

`video/shorts/03-ken-meaningful.srt` (22.10., anderer Agent) endet auf
*„being surrounded by others"* — mitten im Gedanken. `video/meaningful-serie.md`
führt Kens Antwort deshalb als **32,7 s** und Master **6150,1–6189,3**.

**Tatsächlich geht sie 22 s weiter**, und dort steht der eigentliche Schluss:
*„All of it is in relation to others."* Dieses Short endet dort — und damit
auf demselben Gedanken wie das Ubuntu-Short (*„we are who we are through our
relationships"*). Die beiden lassen sich hintereinander stellen.

Danach läuft die Antwort noch 20 s weiter („part of my journey now…"), bis
zur nächsten Frage. Mit diesem Teil wären es 76 s; als Angebot in der Liste.

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `396:0:608:1080` | 0,0000–3,8333 | Yannick, Nah — seine Frage |
| 2 | `1312:0:608:1080` | 3,8333–8,6000 | Totale, Kasten auf Ken |
| 3 | `836:0:608:1080` | 8,6000–31,7333 | Ken, Nah |
| 4 | `1312:0:608:1080` | 31,7333–38,6000 | Totale, Kasten auf Ken |
| 5 | `836:0:608:1080` | 38,6000–54,2667 | Ken, Nah |

**Kens Nahaufnahme sitzt bei x 836, nicht bei 1312.** In der Totale steht er
rechts (x ≈ 1660), in seiner eigenen Kamera in der Mitte (x ≈ 1140). Der
erste Kasten zeigte deshalb nur seinen Hinterkopf.

## Der Fehler, der mich drei Durchläufe gekostet hat

**`-ss` taugt nicht, um ein einzelnes Bild zu prüfen.** Ich hatte die vier
Schnittkanten mit `ffmpeg -ss <zeit> -frames:v 1` kontrolliert und daraus
geschlossen, die Szenenerkennung liege je ein Bild daneben — also alle
Grenzen um ein Bild vorgezogen. **Beides war falsch:** die Erkennung am
Vorlagenband war exakt, und die `-ss`-Stichproben trafen nicht das Bild, das
ich angefordert hatte.

**Richtig ist, nach Bildnummer zu greifen:**

```
ffmpeg -i band.mov -vf "select='between(n,253,260)'" -vsync 0 bild%02d.png
```

So gezählt liegen die Kanten bei Bild **115 · 258 · 952 · 1158**
(= 3,8333 · 8,6000 · 31,7333 · 38,6000 s) — genau die Werte, die
`select='gt(scene,0.04)'` **ohne** `-ss` gemeldet hatte.

**Das Ubuntu-Short vom selben Tag nach derselben Methode nachgeprüft:**
Bilder 46–53 über die Naht, alle sauber, kein Fremdbild. Die dortige
Korrektur war also im Ergebnis richtig, auch wenn die Prüfmethode es nicht
war.

## Untertitel

74 Einblendungen. **Eine Korrektur:** `man search for meaning ->
Man's Search for Meaning` — das Genitiv-s verschleift sich, und es ist der
Name seines eigenen Podcasts. `large-v3` hört es bei 1,0 und 0,6 zweimal.

Nicht korrigiert: sein „Ken," vor „since we're on…" fällt in der Einblendung
weg; im Ton ist es da.

## Musik

„In This Shirt" ab **0:23,25** des Titels (die Regel vom 22.10.: den Einsatz
vorziehen). Bett 0,00–54,27 s, Einblende 0,2 s, Ausblende 4 s, Outro allein.
Durch Subtraktion geprüft, hörbar ab der ersten Sekunde, ab 54,3 s unter
−77 dB. Stimme −33,5 dB, Bett −31,8 dB.

**Dasselbe Bett liegt jetzt auch unter dem Ubuntu-Short**
(`YNB Podcast Ken Stern Ubuntu (In This Shirt).mp4`).

## Abnahme

1080×1920 · 48 kHz · 58,5 s · Outro da · 74 Untertitel · Ortscheck sauber.
„Kein Musikbett" schlägt bei der Musikfassung erwartungsgemäß fehl
(−46,8 dB); die Fassung ohne Musik besteht alle Prüfungen (−80,1 dB).


---

## Fassung 2 (11.11., nach seiner Rückmeldung)

*„Das Meaning Short ist absolut katastrophal geschnitten. Du lässt diese
Buffalo-Szene drin, die überhaupt gar keine Substanz hat."* Fünf Ansagen,
alle umgesetzt.

**57,3 s** (53,1 + Outro), **Tempo 1,1**. Zwei Stücke:
Rohzeit 1:42:29,18–1:42:33,10 (seine Frage) und 1:42:58,15–1:43:52,60.

**Raus ist ein Stück von 25,1 s:** der Wasserbüffel-Witz, die
Mileage-Bemerkung und der Anlauf („I think sort of the hackneyed answer,
which I'll give because it's kind of hackneyed…"). Das Short setzt direkt
auf *„having a purpose, having a reason for getting up in the morning"* an.

**Der Schluss ist 21 s länger als in Fassung 1** und reicht jetzt bis
*„…and encourage other people to do, and inspire others to do the same."*
Das ist alles bis zu seiner nächsten Frage; weiter geht die Antwort nicht.

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `396:0:608:1080` | 0,0000–3,5667 | Yannick, Nah — seine Frage |
| 2 | `700:0:608:1080` | 3,5667–10,4333 | Ken, Nah |
| 3 | `1312:0:608:1080` | 10,4333–17,6000 | Totale, Kasten auf Ken |
| 4 | `700:0:608:1080` | 17,6000–53,0667 | Ken, Nah |

### Der Kasten auf Ken — er hatte recht, und die Zahl erklärt es

*„Sein Kopf ist viel zu weit links. Der ist gar nicht voll drin im Bild."*

Gemessen an 13 Bildern über die ganze Strecke: Kens Kopf reicht von
**x 853 bis 1267**. Der Kasten stand bei **x 836**, also **17 Pixel Luft
links** — und er schaut nach links. Technisch war nichts angeschnitten;
der Eindruck „nicht voll drin" kommt von diesen 17 Pixeln.

Jetzt **x 700**: 153 px links, 41 px rechts, Gesicht bei 0,56 der
Kastenbreite. **Lehre: bei einem Gesicht im Profil zählt nicht, ob der Kopf
hineinpasst, sondern auf welcher Seite die Luft liegt.** Blickrichtung
bekommt den Platz, der Hinterkopf darf eng sitzen.

### Drei Korrekturen am Ton

`having reason -> having a reason` · `interior lies -> interior lives` ·
`do inspire -> do and inspire` (er stolpert: „encourage other people to do,
and inspire others…"). Alle drei mit `large-v3` bei 1,0 und 0,6 am
ungedehnten Ton geprüft.

**Nicht geändert:** er sagt „having a purpose, having a **reason** for
getting up in the morning", nicht „having a meaning". So steht es im Bild.

### Schnittkanten

Am Vorlagenband gemessen (ohne `-ss`) und **jede Kante an den Bildnummern
nachgezählt**: Bild 107 · 313 · 528. Die drei Übergänge im fertigen Short
einzeln geprüft, keine Fremdbilder.

Dabei noch eine Lehre über mich selbst: ich hatte die Kante bei Bild 313
zuerst auf 314 gelesen, weil ich den Kontaktabzug mit 150-px-Feldern
angesehen hatte. **Bei 150 px ist ein Kamerawechsel nicht sicher zu
erkennen — solche Prüfungen gehören auf mindestens 240 px.**

### Musik und Abnahme

„In This Shirt" ab 0:23,25, Bett 0,00–53,07 s, Ausblende 4 s, Outro allein.
Stimme −37,0 dB, Bett −35,3 dB. 1080×1920 · 48 kHz · 57,3 s · Outro da ·
71 Untertitel · Ortscheck sauber.

---

## Nachtrag 11.11.: das Bett läuft jetzt über das Outro

*„bei beiden soll die Musik länger laufen und dann mit dem Outro ausfaden."*

In beiden Ken-Shorts läuft „In This Shirt" jetzt **bis zum letzten Bild**
und blendet über dem Outro aus — Ausblende **4,208 s**, also genau die
Länge des Outros, beginnend am Ende des Hauptteils.

| | Bett | Ausblende ab | Ende |
|---|---|---|---|
| Ubuntu | 0,00–57,575 s | 53,367 s | 57,575 s |
| Meaningful | 0,00–57,275 s | 53,067 s | 57,275 s |

Durch Subtraktion geprüft (Ubuntu): −45 dB bei 53 s · −48 bei 54 ·
−56 bei 56 · −65 bei 57. Sauber bis auf null.

**Der Gesamtpegel des Outro-Abschnitts ändert sich dadurch nicht:**
−26,1 dB mit Bett wie ohne. Der eigene Ton des Outros bestimmt den Pegel,
das Bett liegt darunter.

**Das ist seine dritte Ansage zum Bettende, und wieder eine andere:**
AI 2027 „nicht vorm Ende aufhören" · Safety „vor dem Outro aufhören" ·
Ken „mit dem Outro ausfaden". Bestätigt die Regel: pro Stück fragen.
