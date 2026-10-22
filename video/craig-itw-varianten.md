# Into the Wild / Craig — zwei Varianten mit 83 % Einspielern

**Sein Auftrag vom 22.10.:** *„Ich möchte viel mehr B-Rolls … diese
cinematischen Shorts sollten 80 bis 90 % B-Rolls haben."* Dazu zwei Bauarten:
Vollbild und alles im Kasten.

---

## Der Befund, der beides erst möglich gemacht hat

Der Trailer trägt eingebrannte Untertitel. Zuerst habe ich **untertitelfreie
Strecken gesucht** und kam auf **36 brauchbare Sekunden von 185** — für 83 %
bräuchte es 44.

Dann habe ich die Frage gedreht: nicht *wann* steht Text, sondern **wo**. An
zehn bekannten Textstellen die Lage der Schriftzeilen ausgemessen:

| Sekunde | Schriftzeilen im Filmfeld |
|---|---|
| 14, 34, 56, 99, 137, 166 | y **918–960** |
| 144 | y 929–960 |

**Immer dieselben 43 Pixel am unteren Rand.** Filmfeld von 961 auf **917**
Pixel Höhe geschnitten, und alle zehn Stellen sind sauber — an gerenderten
Bildern nachgeprüft, nicht angenommen.

| | vorher | jetzt |
|---|---|---|
| brauchbares Material | 36 s von 185 | **~171 s von 185** |
| Quadrat für den Unschärfe-Modus | 961×961, **1,12×** hoch | 917×917, **1,18×** hoch |
| Kosten | — | 4,5 % der Bildhöhe |

**Die Lehre: erst messen, wo etwas steht — dann muss man oft nicht suchen,
wann.** Steht in `video/untertitel_finden.py` ganz oben.

---

## Beide Varianten, gleicher Aufbau

Grundlage ist sein Schnitt (13–31 raus, Ende nach *„the essence of Ubuntu,
essentially"*), 52,5 s Sprache plus 4,2 s Outro.

| | im Short | Dauer | Trailer | worüber |
|---|---|---|---|---|
| **Einspieler 1** | 4,0–17,0 | **13,0 s** | 145,0–160,6 | das Notizbuch, die Zeile wird geschrieben — darunter *„I read that book … happiness is only real when shared"* |
| **Einspieler 2** | 18,0–31,0 | **13,0 s** | 24,0–39,6 | Wald, Rucksack, Meer, Sonnenuntergang — *„he went and lived what we were fantasizing about"* und die Naht |
| **Einspieler 3** | 32,0–49,5 | **17,5 s** | 106,0–127,0 | Wildnis, Bus im Schnee, Lagerfeuer — *„cutting ties … not meant to be alone"* |

**43,5 s von 52,5 s = 83 %.** Craig ist nur am Anfang (4 s), zweimal für eine
Sekunde dazwischen und am Ende für die Ubuntu-Pointe (3 s) im Bild.

**Einspieler 2 liegt über der Naht** bei 25,6 s, wo sein Schnitt die beiden
Teile zusammensetzt — der Sprung ist damit unsichtbar.

---

## A · Vollbild

Randloses 9:16, `--broll-modus unschaerfe`: der Film steht quadratisch und
fast unskaliert scharf in der Mitte, dahinter füllt er sich selbst vergrößert
und unscharf das Hochformat. **Nichts wird beschnitten** — randlos aus einem
2,33:1-Bild würden sonst 75 % der Breite wegfallen.

## B · Alles im Kasten

Interview **und** Einspieler als 16:9-Kasten auf Schwarz, 1080 breit:
Interview 1080×608, Einspieler 1080×463, beide mittig.

**Der Renderer kennt für das Hauptbild keinen Rahmen.** Er ist deshalb vorher
gesetzt, und der Plan reicht das fertig gerahmte Bild nur durch; für die
Einspieler ist `--broll-modus vollbild` bei einer 1080×1920-Quelle die
Identität. Die Einblendungen sitzen auf **1180 px**, im unteren Drittel des
Kastens.

Das ist nicht Williamsons Quadrat — er rahmt **980×980**. Hier ist es 16:9,
weil er das so wollte.

---

## Was offen bleibt

* **Der Filter ist weiterhin die Annäherung.** Seine LUT fehlt; mit dem
  CapCut-Export ist das Umrechnen Minuten.
* **Bei 83 % hört man Craig mehr, als man ihn sieht.** Das ist die
  filmgeführte Bauart und lebt davon, dass der Ton trägt. Die Zahl ist in
  einer Minute geändert.
