
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
