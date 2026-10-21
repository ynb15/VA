## 21.10.2026 — Sein Shorts-Preset ist der Maßstab, nicht unsere Messung

**Er hat den Ordner übergeben, mit dem seine Shorts bisher gebaut wurden**
(Schrift, Farbe, Maße, CapCut-Filter als LUT): *„ist jetzt der Filter und
die Schrift, die wir bisher für meine Shorts verwendet haben, kannst du das
jetzt ab sofort bitte auch einbauen und natürlich auch an YNB Cinema
Agenten und dann EA weitergeben."* Eingebaut in `video/shorts-render.py`,
dokumentiert in `video/preset-ynb.md`.

**Sechs Werte waren bei uns anders — und wir lagen sechsmal daneben:**

| | unsere Messung | sein Preset |
|---|---|---|
| Gelb | `#FFD530` | **`#F9F13A`** |
| Schriftgröße | 78 | **82** |
| Schrift | DejaVu Sans Bold | **Inter Black** (Ersatz für Eveleth aus CapCut) |
| Zeilenbreite | 1000 px | **777 px = 72 % der Breite** |
| Logo | 520 px, Höhe 0,845 | **302 px = 28 %, Höhe 0,87** |
| Gradation | warm, gesättigt | **entsättigt, kühl — Oppenheimer-Filter** |

Alle sechs waren an seinen veröffentlichten Shorts *abgelesen*, also an
komprimierten Vorschaubildern. Bei der Gradation drehte das Ergebnis sogar
die Richtung um: wir haben warm und gesättigt gemessen, sein Filter ist
entsättigt und kühl.
**Regel: an einem Ausgabebild abgelesene Stilwerte sind ein Notbehelf,
solange die Quelldatei des Stils nicht da ist. Bevor man misst, fragt man
nach der Vorlage.**
→ betrifft: content-*, YNB Cinema, EA, alle Content-Agenten

**Wer libass benutzt, darf die Zeilenbreite nicht mit PIL messen.** libass
legt die Schriftgröße nicht aufs Geviert, sondern auf Ober- plus
Unterlänge der Schrift — bei Inter Black 1,21 Geviert. Gemessen am
gerenderten Bild: `WHAT MAKES LIFE` ist bei 82 px **643 px** breit, PIL
sagt 776, Verhältnis 0,829; aus den Schriftmetriken errechnet 0,826.
Wer das übergeht, misst 21 % zu breit und teilt Dreizeiler, die längst
passen. Faktor: `groesse / sum(font.getmetrics())`.
→ betrifft: content-*, YNB Cinema, EA

**Die Zeilenhöhe hängt am Raum, nicht am Format.** Sein Preset setzt die
Untertitel fest auf 70 % der Bildhöhe. Für Rick Strassman (Webcam) war 50 %
richtig, im Just-Push-Record-Studio 57 %. Die 70 % sind deshalb hier der
Wert, wenn keine Lippe gemessen ist — die gemessene Lippe schlägt ihn.
→ betrifft: content-*, YNB Cinema

**Offen: die LUT selbst fehlt.** Übergeben wurden `make_lut.py` und die
Anleitung, nicht `luts/ynb_look.png` und nicht der CapCut-Export. Bis die
da ist, läuft eine Annäherung, und der Renderer schreibt das in die
Ausgabe, statt es zu verschweigen. `luts/hald_identity_1080.png` liegt
bereit und ist geprüft: durch `make_lut.py` zurückgerechnet kommt die
Identität pixelgenau wieder heraus.
→ betrifft: content-*, YNB Cinema, EA


## 21.10.2026 — Der Planer plant am Kameraschnitt nicht neu (Aaronson 01)

**Befund, gemessen.** `bildausschnitt.py` setzt einen Kasten und lässt ihn
laufen, bis sein eigenes Bewegungsmaß kippt. Im Aaronson-Short standen
**zwei** Einstellungen über 58 s, die zweite 56 s am Stück bei `650:0:608:1080`.
Solange die Regie auf Scotts Kamera bleibt, stimmt das. Schaltet das Studio auf
die Totale, zeigt derselbe Kasten Holzwand, Mikrofonarm und die Getränkedosen.

**Die Schnitte sind da, man muss sie nur holen.** `ffmpeg` mit
`select='gt(scene,0.25)'` fand im 110-s-Fenster **sechs** Kameraschnitte
(Fensterzeit 7,58 · 13,12 · 31,12 · 38,62 · 90,48 · 99,12). Die eigene
Bewegungsheuristik fand zwei.
**Regel: den Plan an jedem erkannten Kameraschnitt teilen, nicht an der
Bewegungsschwelle.**

**Scotts Position in der Totale, ausgemessen an zwei Totalen (Master 3361,5
und 3422,9) mit eingezeichnetem Raster:**

| | |
|---|---|
| Gesichtsmitte | **x ≈ 1467** im 1920er Bild (Nase 1393, Hinterkopf 1560) |
| Kopfoberkante | **y ≈ 413** |
| in der Nahaufnahme dagegen | x 930–970 |

**Die Position ist kamerafest** — in beiden Totalen dieselbe. Einmal
ausmessen reicht pro Folge.

**Zwei brauchbare Kästen, beide geprüft:**
- `1163:0:608:1080` — gleicher Maßstab wie die Nahaufnahmen, schärfste
  Variante, aber Scott sitzt tief im Bild (Kopf bei 0,38 der Höhe).
- `1242:280:450:800` — näher am Maßstab der Nahaufnahme davor, Kopf bei
  0,17. Hochskalierung 2,4× statt 1,78×.

**Einfrieren wäre hier falsch.** Die `tot`-Mechanik (Standbild überbrücken)
ist für Einstellungen gedacht, in denen die Person **nicht** zu sehen ist. In
der Totale ist sie zu sehen, nur woanders — dann folgt der Ausschnitt.
→ betrifft: content-*, alle Content-Agenten

**Zum Übergang: hier ist der harte Schnitt richtig, kein Schwenk.** Die Quelle
wechselt an dieser Stelle selbst die Kamera. Ein interpolierter Schwenk würde
eine Bewegung behaupten, die es im Bild nicht gibt, und über einen echten
Schnitt hinweglaufen. Ein Schwenk gehört nur dorthin, wo der Ausschnitt
**innerhalb** einer durchgehenden Einstellung wandert.
→ betrifft: content-*

**Und ein Verlust, der eine Regel wert ist.** Die Arbeitsdatei `clip_aa2.mp4`
lag in einem fremden Scratchpad und ist mit dessen Container verschwunden. Aus
der Dokumentation liess sich das Fenster rekonstruieren (Master 3340,7–3361,9
und 3375,3–3412,9, also die notierte „Rohzeit" minus 12,2 s), **aber nicht
exakt**: der Plan endet bei 58,145 s, die rekonstruierten Fenster ergeben
58,8 s. Die Differenz ist die von Hand entfernte 0,4-Sekunden-Einstellung,
deren Lage nirgends steht.
**Regel: wer eine Schnittfassung dokumentiert, notiert die Schnittliste in
Quellzeiten — jede entfernte Stelle mit Anfang und Ende.** Sonst ist die
Fassung nicht reproduzierbar, sobald der Container weg ist.
→ betrifft: alle Content-Agenten
