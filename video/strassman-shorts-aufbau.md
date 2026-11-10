# Rick Strassman — zehn Shorts, gebaut T−3 (10.11.2026)

Quelle: die **Rohsitzung** `1Hwt3_c_Ifhd7onXyC8nrHIdtjwJjxdjH`, 15,50 GB,
7251,77 s. Drive-Ordner am 10.11. um 05:00 selbst geprüft: vier Dateien,
dieselben IDs wie am 02.11., **weiterhin keine Schnittfassung**.

**Bildrate vor dem ersten Schnitt gemessen:** `average_rate`, `base_rate`
und `guessed_rate` sind alle **30/1**, `time_base` 1/30000. Kein
24000/1001-Fall. Jedes Bildstück ist über die **Länge** auf eine ganze Zahl
Frames gerechnet, plus ein Frame gegen den bekannten Versatz nach unten:
`L = (round((bis−von)·30) + 1) / 30`.

## Was gebaut ist

| Datei | Länge | Rohzeit | Musik |
|---|---|---|---|
| Shoulders | 32,5 s | 12:48–13:26 | In This Shirt ab 0:10 |
| Grays | 77,3 s | 25:52–27:20 | Mom's Got Work ab 0:20 |
| Dying | 37,3 s | 35:48–36:28 | In This Shirt ab 0:10 |
| Banal | 38,6 s | 50:36–51:17 | In This Shirt ab 0:10 |
| Answer | 36,7 s | 55:37–56:16 | In This Shirt ab 0:10 |
| Death | 49,8 s | 58:43–59:38 | In This Shirt ab 0:10 |
| Bowing | 38,1 s | 81:47–82:28 | In This Shirt ab 0:10 |
| Envy | 29,7 s | 89:44–90:15 | In This Shirt ab 0:10 |
| Meme | 38,7 s | 99:45–100:26 | In This Shirt ab 0:10 |
| Pride | 37,4 s | 117:39–118:19 | In This Shirt ab 0:10 |

Alle zehn: Tempo 1,2 · `--look warm` · Logo 700 px auf 0,877 ·
`--musik-unter 0` · Outro 9:16 · `--laut aus`, `--dehnung atempo` (Vorgabe).

**Das Bett beginnt nie bei Songsekunde 0.** In This Shirt läuft die ersten
zehn Sekunden bei −18 dB und ist ab 0:10 auf Pegel (Median −12,3 dB) — darum
`--musik-ab 10`. Mom's Got Work hat bei 0:10 einen Einbruch auf −22 dB und
liegt ab 0:20 wieder auf seinem Median — darum `--musik-ab 20`; von dort
bleiben 97 s bis zum Songende, das Bett muss also nicht umlaufen.

**He's Alive liegt nicht im Container.** Nach der Regel wäre es für Grays
(77 s) der richtige Titel. Ich habe Mom's Got Work genommen, weil es da ist
und seine Festlegung vom 05.11. trägt. Sobald die Datei da ist, ist Grays
der eine Short, der neu gerechnet werden muss.

## Was NICHT gebaut ist, und warum

**„Die Zahl 49" (1:03:48–1:05:23).** Die Passage endet **59 Sekunden vor**
der Pause bei 01:06:22 — vollständig außerhalb, aber in ihrer Nähe. Die
Grenze aus T−8 gilt damit weiter: wenn die Schnittfassung die Pause anders
behandelt als erwartet, liegt dieser Kandidat als einziger nah genug, dass
die Verortung über den Wortlaut Arbeit macht statt keine. Er wird gebaut,
sobald die Fassung feststeht.

**Die beiden Langstücke** (Samstag 3–10 Min, Sonntag 10–20 Min) bleiben
ungebaut. Das Sonntagsstück (01:19:40–01:35:10) liegt vollständig hinter der
Pause, das Samstagsstück davor — beide sind lang genug, dass ein Versatz an
der Pause sie an unterschiedlichen Stellen trifft. Dafür braucht es die
Fassung.

## Drei Dinge, die beim Bauen aufgefallen sind

**Der Ton ist 12 dB leiser als bei Craig.** Mittelwert −28,5 bis −30,6 dB,
Spitze −7,0 dB — die Craig-Shorts liegen bei −17 bis −18 dB Mittel und
−0,0 bis −0,5 dB Spitze. Grund: die Rohsitzung ist ungemastert (−31 LUFS),
und `--laut aus` ist seit dem 20.10. Vorgabe, weil die Lautheitsangleichung
den Rauschboden um 18 dB hebt. YouTube normalisiert nur nach unten; diese
zehn bleiben also leise. **Die Frage dazu steht im Lernkanal.**

**Eine Schleife, die ihre eigene Eingabe auffrisst.** Der erste Bauversuch
lief über `while read … done <<'EOF'`, und die Werkzeuge im Schleifenrumpf
haben die restlichen Zeilen von stdin gelesen: von zehn Shorts wurden zwei
gebaut, dazwischen stand ein Lauf namens `rt.mp3`. `ffmpeg -nostdin` hilft
nur ffmpeg. Behoben über eine Array-Schleife und `< /dev/null` an jedem
Aufruf.

**Fünf von zehn brauchten einen zweiten Lauf**, vier davon nur wegen des
Endes: der Schnitt lag ein bis zwei Sekunden vor dem Satzende, und die
Einblendung brach mitten im Satz ab („…WHERE THE RUBBER MEETS",
„…INTERPRETED AS"). Der fünfte war ein verhörtes Wort („SOME PIGS" statt
„SOME PICKS"). **Das Satzende gehört vor dem ersten Rendern gemessen, nicht
nach dem ersten Ansehen.**
