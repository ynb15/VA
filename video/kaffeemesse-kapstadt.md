# Kaffeemesse Kapstadt, 21.11. — Short

**Geliefert:** `YNB Kapstadt Kaffeemesse.mp4` · 57,77 s · 1080×1920 · 30 fps.

**Stand 22.11., zweite Fassung:** Logo-Outro raus, `IMG_4179.MOV` komplett
als Schlusseinstellung. Das Wasserzeichen bleibt — seine Ansage galt dem
Outro-Abspann.

**Stand 24.11., sechste Fassung — auf seine vier Ansagen:**

**Wasserzeichen raus** („das Logo kann raus, in diesem Fall").

**Der Balken war zu starr und nahm zu viel Bild.** Jetzt durchscheinend
(Alpha 0x78 statt massiv schwarz), Eckenradius 70, Grad 124 → **84**, Feld
782×661 → **634×489 px**: von **24,9 % auf 15,0 % der Bildfläche**.

**Schrift viel weicher.** Inter Display **Light** statt SemiBold, dazu
**Sperrung 14** und Zeilenabstand 1,30 — die Zeilen stehen luftig statt
gedrängt. Blenden 420/520 ms statt 260/340, also ein weicheres Kommen und
Gehen. Lesbarkeit kostete das: in der ersten Fassung lag das Feld bei
Alpha 0x96 und die dünne Schrift verschwand im hellen Hintergrund —
nachgezogen auf 0x78 mit kräftigerem Schatten (0x30 statt 0x78, Weite 4).

**Die Eröffnung läuft länger und langsamer, dann zieht es an.** 6,40 s roh
auf **Tempo 1,25** → 5,17 s; alle 31 Messe-Einstellungen bleiben auf 1,65.
Das ist der Tempowechsel, den er wollte: der Anfang atmet, danach nimmt es
Fahrt auf.

**Stand 24.11., fünfte Fassung — auf seine fünf Ansagen:**
**Tempo 1,65 statt 1,5** („alles ein bisschen schneller … unter 60 Sekunden
auf jeden Fall") → **54,00 s**. **Eröffnung auf 2,20 s roh gekürzt**
(„es reicht, wenn ich das Glas ansetze") — das Glas erreicht bei **1,8–2,0 s**
die Lippen, Schnitt bei 2,20 s, auf Tempo also 1,33 s. **Kopfzeile größer**:
Schrift 96 → **124**, Polster 44/28 → **58/38**, Eckenradius 26 → **44**,
Feld 705×396 → **782×661 px**. **Vierte Zeile „2026"** dazu. **Weichere
Schrift**: Inter Display SemiBold statt Inter Black, und die 112-%-Dehnung
raus — die war nur dafür da, den Ersatz für Eveleth breitzuziehen. Feld
steht jetzt bei 55 % der Höhe (726–1386 px), damit es dem Wasserzeichen
nicht in die Quere kommt.

**Stand 24.11., vierte Fassung:** Eröffnung vorangestellt und Einblendung.
`1h2H7sbofWgCPUy9eGk2UiTHmhq5EoFT6` (8,01 s, Kaffeetisch im Freien vor dem
Berg) läuft komplett als erste Einstellung, auf Tempo 1,5 also **5,37 s**.
Darüber die Kopfzeile **„CAPE TOWN | COFFEE | CONVENTION"**, drei Zeilen,
4,5 s mit Ein- und Ausblendung — schwarzes Feld mit runden Ecken, weiße
Schrift, also die Form, die er am 21.10. bestellt hat. Erzeugt mit
`kopfzeile_ass()` aus `video/shorts-render.py`, Feld 705×396 px, Mitte bei
68 % der Höhe. Schrift ist **Inter Black**; Eveleth liegt nicht im Container
und hat, anders als die Outros, keine Drive-Kennung in `.gitignore`.

Dateiname ist geraten — das Schema `YNB Podcast <Gast> <Stichwort>` passt hier
nicht, weil es keine Folge ist.

## Material

32 Clips aus `1cN6GLocnvDC166PrWcCUen60sZpP0EQN`, 12:12–12:18 UTC hochgeladen,
zusammen **143,7 s**. `IMG_4179.MOV` kam um 12:18:52 dazu, also nach meiner
ersten Abfrage um 12:16 — beim Nachsehen am 22.11. habe ich dann auf „neuer
als 13:00" gefiltert und ihn wieder verfehlt. **Nach dem Hochladen fragt man
gegen den Zeitpunkt der letzten Abfrage, nicht gegen eine runde Uhrzeit.** Hochformat ab Werk: 3840×2160 mit
Drehmarke −90, also 2160×3840 im Bild — für 1080×1920 ein glatter Halbschnitt,
kein Ausschnitt nötig. Vier Clips (4144, 4145, 4146, 4160) liegen in
abweichenden Größen (Stabilisierung), die werden formatfüllend skaliert und
mittig beschnitten. 4166 liegt zweimal im Ordner, einmal als `.MOV` und einmal
als `.mov`, mit unterschiedlicher Länge — **dieselbe Einstellung**, deshalb nur
einmal verwendet.

## Schnitt

**32 Einstellungen, Tempo 1,65.** Aus 88,6 s Rohmaterial werden 53,7 s. Jede Einstellung ist über die Länge auf ganze Frames gerechnet, das
Fenster liegt mittig im Clip, damit der Ruck beim Start und beim Stopp der
Aufnahme draußen bleibt. Kürzeste Einstellung 1,1 s, längste 2,3 s — über der
Halbsekunden-Grenze.

Reihenfolge als Bogen: Eingangsschild → Lieferwagen → draußen → Halle →
Roasters Village → Handwerk (Siebträger, Barista, Ausguss) → Maschinen bis zur
vergoldeten Victoria Arduino → Produktwände → Marken (Truth, Origin, Mother
City) → Wein mit Bohnen → Du mit dem Becher → Auto → die Tasse „COFFEE IS MY
SECOND FAVOURITE C WORD" → **Schluss: die Tüten kommen zu Hause auf den
Tisch, letzte Einstellung ist Deine Reaktion.** Der Schlussclip läuft wie
alles andere auf 1,5 — bei 2,17 s bleibt für die Reaktion knapp eine halbe
Sekunde.

Zwei Eingriffe gegen Wiederholung: die zweite Fassung des Tischs „WE'RE FULL OF
BEANS" ist raus, und die beiden Einstellungen, in denen Du trinkst, stehen
nicht mehr nebeneinander.

**Ortsregel eingehalten:** sichtbar sind „CAPE TOWN COFFEE SHOW" und „MOTHER
CITY EDITION" — Stadt, sonst nichts. Kein Straßenname, keine Hausnummer, keine
Adresse im Bild.

## Ton — der gemeldete Mangel war mein Fehler

In der ersten Fassung liefen sechs Einstellungen stumm, zusammen **10,8 s von
55,5 s**, und ich habe das als Eigenschaft des Materials gemeldet. Das war
falsch.

**Diese Clips tragen zwei Tonspuren.** Die erste ist ein Vierkanalformat, das
hier nicht dekodiert wird (`codec_name=none`) — daneben liegt eine ganz
normale AAC-Stereospur. Mein Bauskript hatte `-map 0:a:0` und damit immer die
erste genommen. Jetzt sucht es die AAC-Spur:

```
ffprobe -select_streams a -show_entries stream=index,codec_name
4144: 1,unknown,4   2,aac,2
```

Gemessen am fertigen Stück: **0,0 s digitale Stille**, Umgebungston im Median
−19,9 dBFS, gesamt −18,3 LUFS, Spitze −1,1 dBFS. Die Spitze lag vorher bei
+0,5 dBFS, also über der Decke; **ein flaches −1,0 dB auf die Summe**, sonst
nichts — keine Kompression, kein Limiter.

## Musik, dritte Fassung (23.11.)

**Frank Sinatra — „The Coffee Song"** (Ring-A-Ding-Ding!, 1961), von ihm
geschickt. MP3 320 kbit/s, 171,15 s, −14,3 LUFS, Spitze +0,8 dBFS.

**Bett ab Songsekunde 12,67**, nicht bei 0 — seine stehende Regel, und seine
eigenen Werte liegen im selben Bereich (In This Shirt ab 0:10, Mom's Got Work
ab 0:20). Der Versatz ist nicht beliebig gewählt: der Song hat bei **66,25 s**
seinen lautesten Abschnitt (−12,5 bis −14,6 dBFS im Viertelsekundenraster,
sonst −18 bis −24). Bei diesem Versatz fällt genau dieser Abschnitt auf die
Schlusseinstellung. **Gemessen: die letzten 2,2 s liegen bei −9,2 LUFS gegen
−16,0 LUFS im Mittel** — die Tüten knallen auf den lautesten Takt.

Der Versatz wird bei jeder Fassung neu gesetzt, damit das Ende immer auf
derselben Songstelle liegt (70,4 s): 12,75 s bei 57,7 s Länge, 7,37 s bei
63,1 s, 16,43 s bei 54,0 s, jetzt **12,67 s bei 57,8 s**. Gemessen: letzte
2 s bei **−9,2 LUFS** gegen **−15,8 LUFS** im Mittel, Spitze −1,1 dBFS.

| | |
|---|---|
| Musik | +1,0 dB, Einblendung 1,0 s |
| Ausblendung | 0,25 s, damit die Pointe nicht weggezogen wird |
| Messe-Atmo | **13 dB unter der Musik** — Maschinen und Stimmen bleiben hörbar, drängen sich aber nicht vor |
| Summe | **−15,8 LUFS**, Spitze **−1,1 dBFS** |

**Die abgenommenen Shorts liegen bei −14,2 LUFS.** Die fehlenden 1,8 dB gehen
mit einer flachen Verstärkung nicht mehr: die Spitze steht schon bei −0,7. Dafür
bräuchte es einen Limiter, und das ist der Eingriff, den er am 20.10. abgelehnt
hat. Liegt bei ihm.

**Nichts geht raus.**
