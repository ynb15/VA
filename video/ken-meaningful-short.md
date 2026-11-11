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
