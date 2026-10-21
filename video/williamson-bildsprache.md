# Williamson, filmischer Aufbau — 33 Shorts, 99 Standbilder

**Gemessen 21.10.2026.** Grundlage: `@ChrisWillx/shorts`, die letzten 30 Shorts
über `yt-dlp --flat-playlist` (mit Aufrufzahlen, ohne Dauer), dazu die drei
Referenzen, die er am 20.10. geschickt hat.

## Der Zugang, der die Messung überhaupt erst trägt

Die B-Roll-Referenz vom 20.10. musste mit **einem** Bild je Short auskommen und
hat ihre Grenze sauber benannt: *„wie oft und wie lange B-Roll läuft, ist daraus
nicht abzulesen."*

**Es gibt drei Bilder je Short, nicht eins.** Neben `oardefault.jpg` liefert
`i.ytimg.com/vi/<id>/` auch `oar1.jpg` und `oar3.jpg`, beide HTTP 200 ohne
Anmeldung, beide 1080×1920. `oar2` ist bitgleich mit `oardefault`.
Also **drei über die Laufzeit verteilte Zeitproben** statt einer — und damit ist
genau die Frage beantwortbar, die vorher offenbleiben musste.

```
for v in oar1 oardefault oar3; do curl -s -O "https://i.ytimg.com/vi/<id>/$v.jpg"; done
```

**Die Grenze bleibt:** drei Proben sagen, *wie viel* Film läuft, nicht *wie lang
der einzelne Block* ist. Für die Blocklänge gibt es keine Messung von außen.

---

## 1. Es gibt zwei Formate, und sie wechseln innerhalb eines Shorts nie

| Format | Shorts | Anteil |
|---|---:|---:|
| **randlos 1080×1920** | 26 | **79 %** |
| **980×980-Kasten auf Schwarz** | 7 | **21 %** |

Der Kasten steht in **allen drei** Zeitproben derselben Shorts — `KKK`, nie
`KRK`. Umgekehrt genauso: 26 Shorts sind `RRR`.

**Das korrigiert die Lesart vom 20.10.** Dort hieß es, randlos sei der
*Sprecher* und der Kasten die *B-Roll*; das stand so da, weil aus drei
Einzelbildern genau diese Zuordnung fiel. Mit 99 Bildern ist sie falsch:
**der Kasten ist der Rahmen des ganzen Shorts**, nicht die Einblendung darin.
Im Kasten wird zwischen Film und Sprecher geschnitten — beide sitzen in
denselben 980×980 auf x=50, y=470.

Die Geometrie selbst hält: **19 Kastenbilder, alle auf das Pixel 980×980 bei
50/470**, Außenraum maximale Helligkeit 0. Das ist eine Vorlage, kein Schnitt
nach Gefühl.

## 2. Wie viel Film läuft — die Zahl, die vorher fehlte

Film gegen Studio ausgezählt, **durch Hinsehen** auf Kontaktabzügen, nicht
gerechnet:

| | Bilder | davon Film | Anteil |
|---|---:|---:|---:|
| Kasten-Shorts | 21 | ~11 | **≈ 50 %** |
| randlose Shorts | 78 | 2 | **≈ 3 %** |
| **alle** | 99 | ~13 | **13 %** |

Also: **drei von vier Williamson-Shorts tragen überhaupt keinen Film.** Wo Film
läuft, läuft er zur Hälfte der Zeit.

**Sein eigener Short liegt bei 44 % — das ist für einen filmgeführten Short
richtig gegriffen**, nicht zu viel. Die Korrektur vom 20.10. („gefühlt eine
Sekunde da und störend") hat ihn auf einen Wert gebracht, der neben Williamsons
filmgeführten Shorts steht. Was die Messung dazusagt: dieser Typ ist bei
Williamson die Minderheit.

## 3. `VWGWkfmJCq8` — randlos und trotzdem Film

Eine der drei Referenzen, die er selbst ausgesucht hat. In der Fassung vom
20.10. steht sie als „Sprecherbild, randlos" — weil das eine verfügbare Bild
den Sprecher zeigte. **Ihre drei Bilder sind: Film · Sprecher · Film, alle
randlos 1080×1920, schwarze Ränder null.**

Das ist der Beleg, der dem randlosen Weg gefehlt hat. Seine Entscheidung vom
20.10. abends — *„ich will's Vollbild lassen, das Einzige, was ich von Chris
Williamson kopieren möchte, sind die filmischen B-Rolls"* — ist **keine
Abweichung von der Referenz, sondern eine ihrer beiden Bauarten.** Sie ist bei
Williamson selten (1 von 26 randlosen Shorts), aber sie steht ausgerechnet in
dem Short, den er als Ideal geschickt hat.

## 4. Die Schrift ist deutlich kleiner als seine

Über alle Schriftbänder gemessen (neutralweiß, Minimalkanal > 200,
Kanalspreizung < 22), Breiten auf 1080 normiert:

| | Williamson randlos | Williamson Kasten | **sein Stand (8. Runde)** |
|---|---:|---:|---:|
| Zeilenhöhe, Median | 48 px | 50 px | — |
| **Zeilenbreite, Median** | **220 px** | **342 px** | — |
| breiteste laufende Zeile | 868 px¹ | 637 px | **861 px** |
| Zeilenmitte, Median | 0,550 | 0,499 | **0,65** |
| Wörter je Einblendung | 1–2 | 1–2 | **genau 3** |

¹ dieser Maximalwert ist eine Titelkarte, keine laufende Einblendung.

**Seine Zeile ist im Median rund viermal so breit.** Nicht wegen der
Schriftgröße — die Zeilenhöhen liegen beieinander — sondern weil **drei Wörter
in Versalien** gegen **ein bis zwei in Kleinschreibung** stehen. Das ist genau
der Platz, um den es in der achten Runde ging („YouTube schneidet da was ab").
**Das ist ein Befund, keine Empfehlung:** Versalien, Gelb und drei Wörter sind
seine abgenommene Handschrift.

Beim Kasten liegt die Zeile auf **0,499** — exakt auf der Mitte des Kastens,
nicht auf einer Bildhöhe. Die Zeile gehört zum Kasten, nicht zum Hochformat.

## 5. Die Titelkarte — 13 von 33 Shorts, im Werkzeug nicht vorhanden

**39 % der Shorts tragen eine fette, zweizeilige Titelkarte** zusätzlich zur
laufenden Einblendung: *How To Spot A Liar* · *The Sign Of A Deteriorating
Marriage* · *The Winter Arc Mindset* · *Don't Quit Before Your Breakthrough* ·
*How Do Lawyers Feel In The Courtroom?*

| | |
|---|---|
| Lage | **0,585 der Bildhöhe** (Hauptgruppe), also direkt **unter** der laufenden Zeile bei 0,550 |
| Breite | Median **840 px** |
| Satz | zwei Zeilen, fett, Versalanfänge, weiß |
| Dauer | in **1 von 3** Zeitproben sichtbar — steht also einen Teil der Laufzeit, nicht durchgehend |

Es ist der Titel des Shorts, ins Bild gesetzt. `shorts-render.py` kann das
nicht: `--zeile` setzt eine feste Zeile, aber nicht zwei fette Zeilen auf
eigener Höhe mit eigenem Zeitfenster.

## 6. Was das Format an Aufrufen bringt: nichts Messbares

| | n | Median | Mittel |
|---|---:|---:|---:|
| Kasten | 5 | 62.000 | 146.000 |
| randlos | 25 | 74.000 | 149.520 |

**Bei fünf gegen fünfundzwanzig ist das kein Beleg für irgendetwas** — es ist
nur der Beleg dafür, dass der Kasten *nicht* offensichtlich besser läuft. Wer
ihn wählt, wählt ihn aus Geschmack.

---

## Was die Werkzeuge heute schon können

* **randlos mit Film** — `--broll ... --broll-modus vollbild` ist die Vorgabe,
  am Ergebnis nachgemessen (x 0–1079, y 0–1919, schwarze Ränder null).
  Das ist die Bauart von `VWGWkfmJCq8`.
* **der Kasten** — `--broll-modus karte`, auf das Pixel 980×980 bei 50/470.
* **der dritte Weg für schwaches Quellmaterial** — `--broll-modus unschaerfe`,
  gebaut für den *Into the Wild*-Trailer, wo ein 9:16-Ausschnitt 76 % der
  Bildbreite verworfen hätte.
* **der Beschnitt steuerbar** — `--broll-fokus 0..1`.

## Was fehlt

1. **Die Titelkarte.** Zwei fette Zeilen auf 0,585 mit eigenem Zeitfenster.
   Kein neues Verfahren, nur ein Overlay — aber heute nicht da.
2. **Die Blocklänge von außen.** Drei Zeitproben sagen *wie viel*, nicht *wie
   lang je Block*. Seine 3,6–8,2 s stammen aus seiner eigenen Korrektur und
   sind damit besser belegt als alles, was von außen messbar wäre.

## Was von ihm kommen muss

* **Welcher der beiden Bauarten.** Randlos mit Film ist entschieden und durch
  `VWGWkfmJCq8` gedeckt. Der Kasten steht gebaut daneben.
* **Woher das Filmmaterial.** Alle sieben Kasten-Shorts unterlegen
  Spielfilmmaterial — *Good Will Hunting*, *The Imitation Game* und anderes.
  Unverändert gilt: ein Content-ID-Anspruch träfe seinen Kanal. Material und
  Entscheidung kommen von ihm.
* **Ob die Titelkarte gebaut wird.**
