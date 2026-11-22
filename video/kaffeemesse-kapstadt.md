# Kaffeemesse Kapstadt, 21.11. — Short

**Geliefert:** `YNB Kapstadt Kaffeemesse.mp4` · 57,67 s · 1080×1920 · 30 fps.

**Stand 22.11., zweite Fassung:** Logo-Outro raus, `IMG_4179.MOV` komplett
als Schlusseinstellung. Das Wasserzeichen bleibt — seine Ansage galt dem
Outro-Abspann.

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

**31 Einstellungen, Tempo 1,5** wie angesagt. Aus 86,4 s Rohmaterial werden
57,4 s. Jede Einstellung ist über die Länge auf ganze Frames gerechnet, das
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

**Ohne Musik.** Du wählst das Stück, dann wird es unterlegt; das Bett beginnt
nicht bei Songsekunde 0.

**Nichts geht raus.**
