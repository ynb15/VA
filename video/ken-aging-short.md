# Ken Stern — Frankl-Zitat und sein Essay über das Altern (12.11.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

| Datei | Länge |
|---|---|
| `YNB Podcast Ken Stern Aging (In This Shirt).mp4` | 75,4 s |
| `YNB Podcast Ken Stern Aging.mp4` | 75,4 s, ohne Musik |

Plan: `video/plaene/ken-aging-plan.json`.

---

## Die Stelle gefunden — und wie ich sie fast nicht gefunden hätte

Sie steht in seinem eigenen Vorbereitungsdokument:
**`1:17:55 edit & Short: Aging`**.

**Ich hatte sie übersehen, weil ich dem Suchausschnitt getraut habe statt
dem Dokument.** Die Drive-Volltextsuche liefert einen Ausschnitt **vom
Anfang** der Datei, nicht um den Treffer herum — und er brach genau eine
Zeile vor dieser ab, nach `1:05:00 Short: Ubuntu`. Daraus hatte ich
geschlossen, das Dokument enthalte keine Marke dafür, und ihn gefragt.
Seine Antwort war eindeutig und berechtigt.

**Regel: ein Suchausschnitt ist ein Fund, kein Inhaltsverzeichnis.** Wenn
eine Datei die Antwort haben könnte, wird sie gelesen (`read_file_content`),
nicht nach dem Ausschnitt beurteilt. Das ganze Dokument sind 7 kB Text —
der Ausschnitt hatte 90 % davon gezeigt und genau die eine fehlende Zeile
verschluckt.

## Was drin ist

Zwei Stücke, Tempo **1,1**:
Rohzeit **1:17:22,41–1:17:58,01** und **1:18:09,94–1:18:52,69**
(971 + 1166 = 2137 Bilder = 71,233 s).

> **Frankl said:** „What you have experienced, no power on earth can take
> from you. Not only our experiences, but all we have done, whatever great
> thoughts we may have had and all we have suffered — all this is not lost,
> though it is past. We have brought into being; having been is a kind of
> being, and perhaps the surest kind."
>
> „And it made me write a little mini essay about the art of aging.
> **Aging is not a slow surrender to time, but a powerful journey into the
> fullest expression of who we are meant to become.** It is not the dimming
> of the light, but the deepening of its glow. With each passing year we
> gain layers of insight, empathy and resilience. The rush of youth gives
> way to the richness of perspective. The urgency of ambition softens into
> the quiet confidence of knowing what truly matters. To grow older is not
> to fade — it is to become more rooted, more radiant, more whole. It is a
> privilege, a transformation and a quiet triumph that many are not
> granted. And for that, **it should be honoured, not feared.**"

**Zwei Auslassungen:**

1. **Sein Fehlstart beim Vorlesen, 11,0 s** — genau das „edit" aus seinem
   Dokument: er liest den ersten Satz, sagt „Sorry, I'll read that again"
   und liest neu. Der Short nimmt den zweiten Durchlauf.
2. **Die Anmoderation davor, 12,6 s** („It reminds me of one of my favorite
   quotes from Viktor Frankl, which really was — which really made me
   reflect on my ideas of aging"). Draußen, weil er das Short als „wo ich
   das Zitat lese" beschrieben hat und „Frankl said" den Namen ohnehin
   nennt. Mit ihr wären es 88 s.

## Es passt nicht unter 60 Sekunden

Der Essay allein ist **42,7 s** roh, das Zitat **25,3 s**. Mit Überleitung
und Outro sind das 75,4 s — bei Tempo 1,1 und ohne ein einziges Füllwort.
**Das ist kein Schnittfehler, sondern die Länge des Materials.**

In der Liste stehen drei Wege mit Zahlen; mein Rat ist der erste: den
Mittelsatz des Zitats heraus (9,8 s) → 65,6 s. Zur Einordnung: YouTube
lässt Shorts seit Oktober 2024 bis drei Minuten zu.

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `396:0:608:1080` | 0,0000–7,7000 | Yannick, Nah |
| 2 | `0:0:608:1080` | 7,7000–13,8000 | Totale, Kasten auf Yannick |
| 3 | `396:0:608:1080` | 13,8000–32,3666 | Yannick, Nah |
| 4 | `0:0:608:1080` | 32,3666–36,1333 | Totale, Kasten auf Yannick |
| 5 | `396:0:608:1080` | 36,1333–71,2334 | Yannick, Nah |

Alle vier Wechsel sind Kameraschnitte der Aufnahme (Bilder 231 · 414 · 971 ·
1084, am Vorlagenband gemessen und einzeln nachgezählt). Der eigene
Tonschnitt liegt bei Bild 971 und fällt mit einem Kameraschnitt zusammen.

## Eine Grenze um 0,4 Millisekunden zu hoch — und ein Bild war falsch

Ich hatte die Grenze als **32,3667** geschrieben; Bild 971 liegt bei
**32,366667**. Die Prüfung des Renderers ist `t < ende`, und
32,366666 < 32,3667 ist **wahr** — Bild 971 bekam deshalb noch den Kasten
der vorigen Einstellung. In der Totale zeigt dieser Kasten den **leeren
Tisch mit Laptop und Dosen**, einen Frame lang, mitten im Short.

**Regel: eine Einstellungsgrenze wird auf die Bildzeit ABGERUNDET, nie
aufgerundet.** 32,3666 statt 32,3667. Dieselbe Klasse Fehler wie am 11.11.,
nur diesmal nicht in der Messung, sondern im Aufschreiben.

## Untertitel

87 Einblendungen. **Eine Korrektur:** `frenkel/frankle/frankel -> Frankl` —
das Modell schreibt den Namen je nach Lauf anders. Es ist der Name, nach dem
sein Podcast heißt. Die Essay-Passage kam wortgleich durch, „honoured"
eingeschlossen.

## Musik

Nicht angesagt; als Annahme gebaut und in der Liste benannt — wie bei den
anderen beiden Ken-Shorts: „In This Shirt" ab 0:23,25, Bett bis zum letzten
Bild, Ausblende 4,208 s über dem Outro. Stimme −30,9 dB, Bett −29,4 dB.

## Abnahme

1080×1920 · 48 kHz · 75,4 s · Outro da · 87 Untertitel · Ortscheck sauber.
Die musikfreie Fassung besteht alle Prüfungen (−76,1 dB).
