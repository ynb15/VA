# Pegelangleichung Strassman + Ken, 12.11.

## Vorlage

Zuletzt abgenommenes Short, **YNB Podcast Craig Makhosi Ubuntu**, Hauptteil ohne Outro
(0 bis 84,115 s von 88,323 s), gemessen mit `loudnorm=print_format=json`:

| | integriert | wahre Spitze |
|---|---|---|
| Craig Makhosi Ubuntu (Hauptteil) | **-14,23 LUFS** | **-0,12 dBTP** |
| Craig Makhosi School (Hauptteil) | -14,86 LUFS | +0,05 dBTP |

Die Aufgabenstellung nannte -29,7 LUFS für dasselbe Short. Das ist nicht meine Datei:
meine abgenommene Fassung misst -14,23. Ich habe gegen die gemessene Datei
angeglichen und nicht gegen die Zahl aus der Aufgabe, weil die Vorlage die Datei ist.
Mit -29,7 als Ziel wären alle Faktoren negativ geworden, also leiser statt lauter.

## Verfahren

Reine Festverstärkung auf den Hauptteil, Schnitt bei Dauer minus 4,208 s
(Outro-Länge), danach wieder angesetzt. Der Ton wird einmal in zwei Teile geteilt,
nur der vordere verstärkt, beide wieder aneinandergesetzt. Keine
Loudness-Normalisierung, keine Kompression, kein Limiter. `--laut aus` bleibt.
Bild unverändert durchkopiert (`-c:v copy`), Bildzahl in jeder Datei identisch.

Decke: -0,5 dBTP. Der Faktor ist das Kleinere von „Vorlage erreicht" und
„Spitze bleibt unter der Decke".

## Ergebnis: Vorlage wird in keiner einzigen Datei erreicht

**Alle 21 Fassungen sind von der Spitze gekappt.** Die Vorlage ist 14 bis 19 dB
lauter und liegt selbst schon an der Decke (-0,12 dBTP, School sogar +0,05).
Soviel Verstärkung lässt die Spitze nicht zu. Was ohne Clipping geht, sind
+6,9 bis +14,1 dB; danach fehlen noch 0,6 bis 8,2 dB.

Lauter geht nur mit einem zweiten Eingriff am Ton (Kompression oder Limiter), und
das ist nach Deiner Regel nicht dieselbe Runde. Entscheidung liegt bei Dir.

### Strassman (10 Shorts)

| Datei | LUFS vorher | Festverstärkung | LUFS nachher | Spitze vorher | Spitze nachher | fehlt zur Vorlage |
|---|---|---|---|---|---|---|
| YNB Podcast Strassman Answer | -27.6 | +8.77 (2.74×) | -18.9 | -9.3 | -0.5 | +4.7 |
| YNB Podcast Strassman Banal | -29.1 | +9.96 (3.15×) | -19.1 | -10.5 | -0.9 | +4.9 |
| YNB Podcast Strassman Bowing | -28.1 | +12.03 (3.99×) | -16.1 | -12.5 | -0.5 | +1.9 |
| YNB Podcast Strassman Death | -28.8 | +11.22 (3.64×) | -17.6 | -11.7 | -0.4 | +3.4 |
| YNB Podcast Strassman Dying | -28.9 | +12.36 (4.15×) | -16.6 | -12.9 | -0.5 | +2.4 |
| YNB Podcast Strassman Envy | -28.9 | +14.06 (5.05×) | -14.9 | -14.6 | -0.6 | +0.7 |
| YNB Podcast Strassman Grays | -29.5 | +11.23 (3.64×) | -18.3 | -11.7 | -0.4 | +4.1 |
| YNB Podcast Strassman Meme | -28.7 | +14.00 (5.01×) | -14.8 | -14.5 | -0.6 | +0.6 |
| YNB Podcast Strassman Pride | -28.7 | +11.63 (3.82×) | -17.1 | -12.1 | -0.5 | +2.9 |
| YNB Podcast Strassman Shoulders | -29.3 | +10.79 (3.46×) | -18.6 | -11.3 | -0.6 | +4.4 |

### Ken Stern (11 Shorts)

| Datei | LUFS vorher | Festverstärkung | LUFS nachher | Spitze vorher | Spitze nachher | fehlt zur Vorlage |
|---|---|---|---|---|---|---|
| YNB Podcast Ken Stern Aging | -30.2 | +9.94 (3.14×) | -20.3 | -10.4 | -0.6 | +6.1 |
| YNB Podcast Ken Stern Alone | -33.1 | +10.76 (3.45×) | -22.4 | -11.3 | -0.6 | +8.2 |
| YNB Podcast Ken Stern Bismarck | -32.2 | +13.65 (4.81×) | -18.6 | -14.2 | -0.6 | +4.4 |
| YNB Podcast Ken Stern Cigarettes | -33.0 | +11.96 (3.96×) | -21.1 | -12.5 | -0.5 | +6.9 |
| YNB Podcast Ken Stern Compliments | -27.9 | +6.93 (2.22×) | -21.0 | -7.4 | -0.5 | +6.8 |
| YNB Podcast Ken Stern Decent | -30.4 | +8.69 (2.72×) | -21.8 | -9.2 | -0.9 | +7.6 |
| YNB Podcast Ken Stern Fit | -27.4 | +7.90 (2.48×) | -19.6 | -8.4 | -0.6 | +5.4 |
| YNB Podcast Ken Stern Hunting | -29.2 | +9.09 (2.85×) | -20.2 | -9.6 | -0.5 | +6.0 |
| YNB Podcast Ken Stern Phones | -31.8 | +12.66 (4.30×) | -19.1 | -13.2 | -0.5 | +4.9 |
| YNB Podcast Ken Stern Pledge | -29.2 | +8.91 (2.79×) | -20.3 | -9.4 | -0.4 | +6.1 |
| YNB Podcast Ken Stern Scientology | -28.0 | +6.93 (2.22×) | -21.1 | -7.4 | -0.6 | +6.9 |

Letzte Spalte: dB, die nach der Verstärkung noch zur Vorlage fehlen.

## Nachweis, dass das Outro seinen Pegel behält

Letzte 4,208 s gemessen, original gegen angeglichen:

| Datei | original | angeglichen |
|---|---|---|
| Strassman Envy | -26,31 LUFS / -7,05 dBTP | -26,31 / -7,05 |
| Strassman Answer | -26,34 / -7,05 | -26,35 / -7,05 |
| Ken Bismarck | -26,34 / -7,05 | -26,36 / -6,94 |
| Craig Ubuntu (Vorlage) | -26,32 / -7,04 | — |

Das Outro liegt in allen Dateien bei -26,3 LUFS, auch in der Vorlage, und bleibt
nach der Verstärkung dort. Die Tonspur wird dabei 9 bis 16 ms länger (AAC-Rahmen
an der Nahtstelle), die Bildspur nicht; die Bildzahl ist vorher und nachher gleich.

## Dateien

Originale bleiben unverändert liegen. Die angeglichenen Fassungen stehen daneben
und heissen `YNB Podcast <Gast> <Stichwort> (angeglichen).mp4`. Für die Lieferung
geht pro Short eine Datei raus, nicht zwei — welche von beiden, sagst Du.

Offen bleibt: Deine LUT, und He's Alive fehlt im Container (sechs Ken-Shorts
zwischen 60 und 90 s und Strassman Grays haben ersatzweise Mom's Got Work).
