# Kingsbury-Folge: was das Material wirklich hergibt

Gemessen am 21.10.2026. **Die Annahme „die Auflösung ist nicht so optimal"
stimmt nicht — und das eigentliche Problem ist ein anderes.**

## Die Kameras

| Datei | Auflösung | Länge | Besitzer |
|---|---|---|---|
| `YNB Podcast: Kyle Kingsbury (YNB)` | **3840×2160** | 77 min | Yannick |
| `C0105.MP4` | 1920×1080, sehr hohe Bitrate (53,6 GB) | 133 min | Kyle |
| `DJI_…_0080_D.MP4` | **3840×2160 @ 60 fps** | 8,4 min | Kyle |
| `DJI_…_0077`, `0079`, `0075` | **3840×2160 @ 60 fps** | je ~8 min | Kyle |
| `2026_09_…_v1_LOW_RES.mp4` | Proxy vom Cutter | — | Christoph |

**Es ist in 4K gedreht.** Das „LOW_RES" im Namen gehört zur Schnittdatei des
Cutters, nicht zum Material.

## Das wirkliche Problem: alle Kameras stehen zu weit weg

Für ein Thumbnail braucht ein Gesicht rund **145 px Pupillenabstand**. Was
die Aufnahmen hergeben:

| Quelle | Pupillenabstand | nötige Hochrechnung |
|---|---:|---:|
| Yannicks 4K-Kamera | 71 px | **2,05×** |
| Kyles C0105 (1080p) | 21–31 px | 5–7× — unbrauchbar |
| DJI 0080 (4K) | 70 px | **2,07×** |
| DJI 0077 / 0079 | 67 / 73 px | ~2× |

Kein einziger Winkel ist eine Nahaufnahme. **Nicht die Auflösung ist zu
klein, sondern die Einstellungsgröße zu weit.** Bei 4K und einer Totalen
bleibt vom Gesicht trotzdem nur ein Bruchteil übrig.

Eine Falle dabei: der Gesichtsdetektor meldete in der DJI-Datei einmal
109 px — das war **Kyles Hand**, nicht sein Gesicht. Jeden Messwert, auf dem
eine Entscheidung steht, am Bild nachsehen.

## Was es sonst gibt, und es ist besser

**Im selben Drive-Ordner liegt ein Foto von beiden vom Drehtag:**
`YNB & Kyle Kingsbury`, HEIF, **2316×2264**.

| Quelle | Pupillenabstand | Faktor |
|---|---:|---:|
| **Selfie, Kyle** | **289 px** | **0,50×** — herunterrechnen |
| **Selfie, Yannick** | **267 px** | **0,54×** — herunterrechnen |
| Yannicks eigenes Thumbnail `frNOUgxE0IM` | 167 px | 0,87× |
| fremdes Thumbnail (Vorlage 6), Kyle | 153 px | 0,95× |

Das Selfie hat **doppelt so viel Auflösung wie gebraucht.** Sein Problem ist
nicht die Schärfe, sondern dass beide breit lachen und es Außenlicht ist —
also genau das Register, das er nicht will.

Der Vergleich liegt als Bild bei: `kingsbury-material-vergleich.jpg`, alle
sechs Quellen auf dieselbe Thumbnail-Größe gebracht.

## Was ich nicht mache

**Kein Rekonstruieren seines Gesichts.** Er hatte vorgeschlagen, Kingsburys
Gesicht aus den drei fremden Thumbnails „zu rekonstruieren". Das hiesse, ein
Modell malt das Gesicht einer wirklichen Person neu — genau die Regel, die am
20.10. festgeschrieben wurde: erzeugt werden darf die Bildmitte, **nie ein
Gesicht.**

**Fremde Thumbnails als Quelle sind heikel.** Die drei Vorlagen sind die
Titelbilder anderer Kanäle; das Foto darin gehört deren Produktion. Für den
eigenen Kanal daraus ein Gesicht auszuschneiden ist etwas anderes, als ein
Pressefoto zu benutzen.

## Empfehlung

1. **Kyle um ein Foto bitten.** Eine Nachricht, und das Problem ist weg — er
   ist selbst Podcaster und hat Pressebilder. Das ist der kürzeste Weg zu
   einem scharfen Gesicht im richtigen Ausdruck.
2. **Yannick aus seinen eigenen Thumbnails** nehmen (0,87×, scharf, eigenes
   Material, und der Ausdruck stimmt dort schon).
3. **Kyle notfalls aus dem Dreh** mit 2× Hochrechnung. Sein Gesicht verträgt
   das besser als Yannicks — mehr Textur, härteres Licht. Weich wird es
   trotzdem.
4. **Fürs nächste Mal:** eine Kamera näher ans Gesicht. Bei den
   Aaronson-Aufnahmen lag der Pupillenabstand bei 150–190 px, da gab es nie
   ein Problem.
