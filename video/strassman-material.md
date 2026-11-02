# Rick Strassman — das Material

Stand 02.11.2026. Aufnahme **18.09.2026**, The Podcast Studio NM, Albuquerque.
Veroeffentlichung **Fr 13.11.** — einer seiner fuenf eigenen Termine.

Drive-Ordner `1OKUFDBDyeEqV7iwypV5Q-vyQi7WL9b_C`.

## Was im Ordner liegt

| Datei | Groesse | Was es ist |
|---|---|---|
| `00 YNB Podcast: Rick Strassman` (Doc) | 8 KB | Vorbereitung: Titelideen, Fragen, Zitate, Launch-Liste |
| `00 YNB Podcast: Rick Strassman` (mp4) | **15,50 GB** | die Aufnahme, 1920×1080, 30 fps, **7251,77 s = 2:00:51** |
| `IMG_3451.MOV` | 58,7 MB | iPhone-16-Pro-Aufnahme, 3840×2160 |
| `YNB & Rick Strassman` (jpeg) | 2,4 MB | Foto |

Eine einzige Fassung der Aufnahme, also keine Wahl zwischen gross und klein.
Der Ton darin: 48 kHz, 317 kbit/s AAC — die Signatur der **Mischung**, nicht
die der Kameradatei (die laeuft auf 44,1 kHz und deutlich niedrigerer Rate).

## Die Laenge gegen eine zweite Quelle

Aus der Lehre von Shorts I: ein Transkript aus einer Rohdatei ist nicht die
Folge. Dort waren 77:12 transkribiert und die Schnittfassung lief 129:50.

Die zweite Quelle ist hier **`IMG_3451.MOV`**. Ihre QuickTime-Metadaten:

```
com.apple.quicktime.creationdate  2026-09-18T12:42:29-06:00
com.apple.quicktime.model         iPhone 16 Pro
ISO6709                           +35.0787-106.5863   (Albuquerque)
```

Gebucht war **10:30–12:30 Ortszeit**. Das Telefonvideo entsteht um **12:42**,
also kurz nach dem Ende. Eine Aufnahme von 2:00:51, die auf dieses Ende
zulaeuft, beginnt gegen **10:41** — der Termin hat elf Minuten spaeter
angefangen als gebucht und den ganzen Block gefuellt. Laenge und Zeitpunkt
passen zusammen.

## Es ist die ganze Sitzung, nicht die geschnittene Folge

Die ersten Sekunden:

> „Yeah, I actually brought you a little gift, Rick, some drugs." — „Oh,
> really?" — „Yeah, some drugs. Some cacao."

Das ist Vorgespraech, kein Folgenanfang. Die Datei traegt die **ganze
Sitzung**: Begruessung, Gespraech, und vermutlich auch das Nachher. Fuer ein
Transkript ist das die richtige Quelle — es fehlt nichts. Wo das Gespraech
selbst einsetzt, steht im Transkript, sobald es durch ist.

## Keine Sprecherzuordnung moeglich

Der Ton ist zweikanalig, aber beide Kanaele tragen dasselbe Signal.
Gemessen an einer Minute aus der Mitte (Rohzeit 3600–3660):

| Mass | Wert |
|---|---|
| Pegel L / R | −31,4 dB / −31,4 dB |
| Korrelation L/R | **1,0000** |
| Differenzsignal L−R | −78,7 dB (das ist AAC-Rauschen, kein Inhalt) |
| Pegelverhaeltnis je Sekunde | Median 0,00 dB, Quartilsabstand **0,00 dB** |

Doppelmono. Die Kanaele tragen keine Information darueber, wer spricht —
eine Zuordnung daraus waere erfunden. Das Transkript bleibt deshalb ohne
Sprechernamen, wie schon bei Aaronson.

## Weg

1. Ton holen: `video/ton_holen.py`, 16 kHz Mono FLAC aus der 15,5-GB-Datei
   ueber Bereichsanfragen (rund 2,4-fache Echtzeit).
2. Transkript: `video/transkript_stueckweise.py --model medium`, in Fenstern
   von zehn Minuten, Stand nach jedem Fenster auf die Platte. Gemessen laeuft
   `medium` hier mit **1,17-facher Echtzeit** — fuer 2:00:51 also rund
   **2,4 Stunden**. Das ueberlebt kein Lauf am Stueck; darum stueckweise.
3. `large-v3` nur als Schiedsrichter fuer ein strittiges Wort, am
   ungedehnten Ton.

**Ende offen, seine Entscheidung.** Im Plan steht das ausdruecklich — es
kommt also kein Vorschlag zum Schluss, bevor er danach gefragt hat.
