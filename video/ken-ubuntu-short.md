# Ken Stern — „There's no I in Ubuntu" (11.11.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

Auf seine Ansage: *„kannst du aus dem Podcast mit Ken Stern genau auch diese
Stelle rausschneiden, bitte liefer mir das Skript mit, weil da muss auf jeden
Fall was geschnitten werden."*

| Datei | Länge |
|---|---|
| `YNB Podcast Ken Stern Ubuntu.mp4` | 42,2 s (38,0 + 4,2 Outro) |

Dazu `.srt`, `-liste.txt` und **das Skript**:
`video/transkripte/ken-stern-ubuntu-block.txt`.
Plan: `video/plaene/ken-ubuntu-plan.json`.

---

## Die Stelle gefunden, ohne 16,8 GB zu laden

Die Folge ist **unveröffentlicht**, es gibt also kein YouTube-Transkript, und
der Master ist **16,8 GB** (`1RGq-Mw0QEm5jE2WMthKPkP5OHrXvmotF`, 1:45:33).

**Sein eigenes Vorbereitungsdokument hat die Zeit geliefert.** Im Drive-Ordner
der Folge liegt das Doc `00 YNB Podcast: Ken Stern`, und darin unter
*Timestamps* steht wörtlich **„1:05:00 Short: Ubuntu"**. Gefunden mit einer
Drive-Suche `fullText contains 'Ubuntu' and parentId = ...` — der
Suchausschnitt gab das ganze Kapitel zurück, ohne das 823-KB-Dokument zu
öffnen.

**Das ist der billigste Weg, den es in dieser Reihe bisher gab:** eine
Drive-Suche statt eines Blindflugs durch die Datei. Von dort ein Byte-Fenster
4217–4458 s… genauer: **3840–4080 s, 1141 MB von 16,8 GB** mit
`drive_fenster.py`.

## Was drin ist

Rohzeit **1:05:21,00 – 1:06:03,60**, 42,6 s roh, bei Tempo 1,12 noch
**38,03 s** (1141 Bilder). **Eine Stelle am Stück, kein Innenschnitt, keine
Auslassung.**

> **Yannick:** „And we talked about that on your show briefly, if you
> remember, I threw in the African proverb Ubuntu."
> **Ken:** „Yes." — **Yannick:** „Remember the definition?" —
> **Ken:** „I don't remember this, but I remember liking when you said it."
> **Yannick:** „Yeah, and I find it beautiful. So most people misinterpret
> it, most Westerners misinterpret it as *I am because we are*. But in fact,
> there's no I in Ubuntu, technically. It actually means *a person is a person
> through other people*. Or as I like to translate it: **we are who we are
> through our relationships.**"

Derselbe Bogen wie im Craig-Short — nur erklärt hier **er** es und Ken hört
zu. Das Ende liegt auf demselben Satz, wie bestellt.

| # | Kasten | von–bis | wer |
|---|---|---|---|
| 1 | `396:0:608:1080` | 0,000–6,786 | Yannick, Nah |
| 2 | `1312:0:608:1080` | 6,786–11,446 | Totale, Kasten auf Ken |
| 3 | `0:0:608:1080` | 11,446–13,330 | Totale, Kasten auf Yannick |
| 4 | `396:0:608:1080` | 13,330–38,033 | Yannick, Nah |

Die drei Wechsel sind die **Kameraschnitte der Aufnahme** (3928,60 · 3935,93,
Szenenwerte 0,48). Der mittlere Wechsel ist meiner: innerhalb der Totale
springt der Kasten bei 11,446 s von Ken auf Yannick, weil dort der Sprecher
wechselt. **Beide Teilstücke sind 4,7 s und 1,9 s lang**, also über der
Halbsekundengrenze vom 26.10.

In der Totale sitzen die beiden **1400 px auseinander** in einem 1920er Bild —
ein 9:16-Kasten kann sie unmöglich beide fassen, deshalb folgt der Kasten dem
Sprecher statt einen von beiden wegzulassen.

## Zwei Stellen am Ton nachgeprüft

**„misinterpret it", nicht „misinterpreted".** Bei normalem Tempo hören
`medium` **und** `large-v3` „misinterpreted"; auf **0,7-** und **0,55-facher**
Geschwindigkeit hört `large-v3` zweimal eindeutig „misinterpret it" — und nur
das ergibt den Satz. Als Korrektur festgehalten (kommt zweimal vor).
**Dieselbe Methode wie bei den isiXhosa-Wörtern am 05.11., und sie hat sich
zum zweiten Mal bewährt.**

**Kens Antwort** heißt „I don't remember **this**, but I remember liking when
you said it" — nicht „…the definition… liking **it**…". Vier Durchläufe
stimmen überein; nur mein erster, `medium` über das ganze 280-s-Fenster, wich
ab. **Ein langes Fenster transkribiert eine kurze, leise Stelle schlechter als
ein Ausschnitt von sechs Sekunden.**

## Das Skript

Er hatte es ausdrücklich bestellt, weil „auf jeden Fall was geschnitten werden
muss". `ken-stern-ubuntu-block.txt` enthält deshalb den **ganzen Block
1:04:38–1:07:00**, 45 Zeilen mit Rohzeit und Wortzahl, markiert was im Short
steht — plus drei benannte Streichvorschläge und zwei Blöcke zum Dazunehmen:

- **Streichen:** „and we talked about that on your show briefly" (3,2 s —
  „your show" ist Kens eigener Podcast, für den Zuschauer orphan) · der
  Wortwechsel mit Ken (4,9 s) · „yeah, and I find it beautiful" (2,4 s).
  Alle drei raus ergäbe **31,8 s**, Beginn direkt auf „So most people
  misinterpret it".
- **Dazunehmen:** Südafrika und die Ältesten der Zulu, Khoi und San (32 s) ·
  Kens selbstironische Antwort (18 s).

**Platz ist da:** unter 60 s passen rund 136 Wörter, der Short hat 92.

**Ortsprüfung:** der Short selbst nennt keinen Ort. Der Block zum Dazunehmen
enthält „living in South Africa" — nach seiner Regel vom 21.10. erlaubt
(Land ja, genauer nein). Steht so in der Liste.

## Abnahme

1080×1920 · 48 kHz · 42,2 s · Outro da · 43 Untertitel · Ortscheck sauber ·
kein Musikbett (−80,2 dB). **Alle Prüfungen bestanden.**

## Musik

Keine. Nicht angesagt. Falls gewünscht, mit vorgezogenem Einsatz:
*In This Shirt* ab 0:23,25, *On The Nature Of Daylight* ab 0:24,50.
