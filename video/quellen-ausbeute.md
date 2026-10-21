# Ausbeute statt Einzelszenen — wie Quellen ausgewählt werden

**Sein Einwand vom 21.10.:** *„Ich möchte nicht einfach nur eine Szene screen
recorden, sondern ich will ja so viele verschiedene Szenen wie möglich aus
einem Film haben. Sonst muss ich ja hunderte von Screen-Recordings machen, die
dann auch Speicherplatz in Drive aufnehmen. … Aber gleichzeitig sollten die
schon lang genug sein, nicht immer nur eine Sekunde."*

Richtig, und beide Hälften ziehen gegeneinander: viel Abwechslung kommt aus
Zusammenschnitten, lange Einstellungen kommen aus ganzen Szenen.

---

## Die wichtigste Zahl zuerst: er braucht keine hundert Aufnahmen

| | |
|---|---|
| Blöcke im Short | **5** |
| Einstellungen je Block (4–6 s bei 1,5–2 s je Einstellung) | **2–4** |
| **gebrauchte Einstellungen insgesamt** | **rund 15** |
| verschiedene Bilder in **einer** 18-Minuten-Aufnahme (gemessen, `LwG6aia2vn0`) | **97** |

**Eine einzige Aufnahme enthält sechsmal so viel, wie der ganze Short
braucht.** Sechs Aufnahmen decken die fünf Blöcke mit großem Abstand ab. Die
Sorge vor hunderten Aufnahmen ist unbegründet — die Frage ist nur, *welche*
sechs.

---

## Wie ich Quellen prüfe, ohne sie zu laden

**YouTube liefert zu jedem Video einen Vorschaustreifen** (`storyboard`): ein
Gitter kleiner Einzelbilder über die volle Laufzeit, auf `i.ytimg.com`,
ohne Anmeldung. **Die Mediendaten sind zu, der Vorschaustreifen nicht.**

`video/vorschaustreifen.py` holt ihn, zerlegt ihn und legt zwei Dinge vor:

1. **Ein Kontaktabzug des ganzen Videos.** Dasselbe Verfahren, das am 20.10.
   die Trailer-Frage gelöst hat, als vier Anläufe mit Automatik danebenlagen.
2. **Eine Messung der Abwechslung.**

### Was die Messung kann und was nicht

| | |
|---|---|
| **Takt** | Abstand zweier Vorschaubilder. YouTube wählt ihn nach Laufzeit: 4,9 s bei einem 9-Minuten-Video, 9,9 s bei 18 Minuten. |
| **Ausbeute** | verschiedene Bilder je Minute. **Das ist seine Frage.** |
| **Sättigung** | Anteil benachbarter Vorschaubilder, die sich unterscheiden. |

**Die Grenze gehört dazu, und sie ist hart:** der Takt ist die Auflösung. Bei
Sättigung nahe 1,00 schneidet das Video schneller als der Takt — **wie viel
schneller, ist nicht zu sehen.** Beide bisher gemessenen Wolf-of-Wall-Street-
Quellen liegen bei 0,88 und 0,89, also am Anschlag. **Die Einstellungslänge
ist aus dem Vorschaustreifen für Videos über ein paar Minuten nicht messbar,
und ich behaupte sie deshalb nicht.**

Was stattdessen trägt, ist die Herkunft:

* **Ganze Szenen** (Miramax, Sony Pictures, Movieclips-Einzelszenen) haben die
  Einstellungen des Films — lange Einstellungen, weil der Film so geschnitten
  ist.
* **Szenen-Zusammenschnitte** („TOP 3 BEST SCENES", „Best Moments") reihen
  ganze Szenen aneinander. **Abwechslung hoch, Einstellungen trotzdem lang.**
  Das ist die richtige Form.
* **Moment-Zusammenschnitte** („Funny Moments", TikTok-Zusammenschnitte,
  „Best of") schneiden im Sekundentakt. **Das ist genau das, was er am 20.10.
  abgelehnt hat.** Erkennbar am Titel und am Kontaktabzug.
* **Trailer** sind die schlechteste Quelle überhaupt — 1–2-Sekunden-Stücke mit
  Blenden.

## Was nur der Kontaktabzug zeigt: eingebrannte Zeichen

Am Blatt zu `LwG6aia2vn0` sofort zu sehen und in keiner Zahl enthalten:
**Binge Society brennt sein Logo oben links in jedes Bild.**

Bei einem randlosen 9:16-Ausschnitt aus der Bildmitte fällt ein Zeichen am
linken Rand heraus — es bleiben ja nur 31,6 % der Breite übrig. **Oben oder
unten mittig wäre es dagegen drin.** Also: je Quelle am Blatt nachsehen, wo
das Zeichen sitzt, bevor aufgenommen wird. Offizielle Kanäle (Miramax, Sony
Pictures, Official Rocky Balboa) brennen in der Regel keines ein.

---

## Aufnehmen: 1080p oder 4K — die Rechnung

Das entscheidet über Speicherplatz **und** Schärfe, und hängt am
Seitenverhältnis des Films.

| Film im Bild | Aufnahme | 9:16-Ausschnitt | Hochskalierung auf 1080×1920 |
|---|---|---|---|
| 16:9 (Peaky Blinders, viele Clips) | 1080p | 608×1080 | **1,78×** |
| 2,39:1 (Wolf of Wall Street, Batman) | 1080p | 452×803 | **2,39× — sichtbar weich** |
| 2,39:1 | 2160p | 903×1606 | **1,20×** |

**Drei Wege, und alle drei sind vertretbar:**

1. **4K aufnehmen**, wo YouTube es anbietet. Schärfster Weg, vierfacher
   Speicherplatz.
2. **1080p aufnehmen und `--broll-modus unschaerfe` nehmen.** Der Film steht
   quadratisch und fast unskaliert scharf in der Mitte (803→1080, also 1,34×),
   dahinter füllt er sich selbst vergrößert und unscharf das Hochformat.
   Randlos, ohne den Beschnitt zu bezahlen — **gebaut genau für diesen Fall.**
3. **1080p randlos**, und die Weichheit in Kauf nehmen. Bei 1,5-Sekunden-
   Einstellungen fällt sie weniger auf als auf dem Standbild.

**Mein Vorschlag:** 1080p aufnehmen, Weg 2. Das hält den Drive klein und sieht
besser aus als Weg 3. Wenn er den Unterschied sehen will, rechne ich dieselbe
Stelle in beiden Fassungen — das ist eine Viertelstunde.

**Speicherplatz überschlagen:** 1080p-Bildschirmaufnahme liegt grob bei
2–3 MB/s. Sechs Aufnahmen von zusammen 90 Minuten sind **rund 12–16 GB**.
In 4K das Vierfache.

---

## Ein Nebeneffekt, der Arbeit spart

Der Vorschaustreifen gibt mir den Kontaktabzug **vor** der Aufnahme. Ich kann
ihm also sagen, **welche Minuten** einer 25-Minuten-Quelle er überhaupt
aufnehmen muss — statt die ganze Datei. Bei `UYlp0pkNjT0` (Rocky, 24:42) wären
das vielleicht acht Minuten statt fünfundzwanzig.

**Das kehrt die Reihenfolge um:** erst messe ich die Quellen, dann bekommt er
eine Liste mit Zeitangaben, dann nimmt er auf. Weniger Aufnahme, weniger
Speicher, weniger Suchen hinterher.
