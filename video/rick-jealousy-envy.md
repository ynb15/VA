# Rick Strassman — Jealousy vs. Envy (28.11.)

**Noch nicht gebaut.** Der Schnitt steht, das Bild fehlt — Drive drosselt
heute jeden Abruf (siehe unten).

Seine Ansage: *„Bitte erstelle mir ein Short wo wir über Jealousy und Envy
und so diskutieren."*

## Die Stelle — von ihm selbst markiert

In seinem Vorbereitungsdokument (`13 YNB Podcast: Rick Strassman`) steht:

> **`1:30h Short: Jealousy vs. Envy`**

Das deckt sich auf die Sekunde mit dem Fund im Rohtranskript
(`strassman-roh.transkript.json`, Zweig `claude/content-cinematic`): der Kern
liegt bei **5392–5464 s Rohzeit**, also 1:29:52–1:31:04.

Der Anlass davor, falls er ihn will: Rick findet im Buchladen *The Kabbalah
of Envy* von Milton Bondar (1:27:12) — „if anybody is feeling envy and anger
and rage and jealousy, it's me."

## Der Schnitt — sechs Stücke, 66,5 s Rohzeit

Alle Grenzen liegen auf Segmentgrenzen des Transkripts, **bis auf den
Anfang von Stück 1** (siehe Vorbehalt).

| # | von | bis | Dauer | wer | Text |
|---|---|---|---|---|---|
| 1 | 5373,8 | 5383,85 | 10,1 s | **Du** | „…between jealousy and envy. I thought that they were of the same cloth. How do you differentiate them nowadays?" |
| 2 | 5392,37 | 5403,77 | 11,4 s | **Rick** | „Jealousy is you want something that somebody has. An envy is the wish to destroy that good thing that somebody has." |
| 3 | 5403,77 | 5414,29 | 10,5 s | **Rick** | „It's along the lines: if I can't have it, nobody will — as opposed to jealousy, which is I want that thing. And once you've got that thing, you're happy, or you're more or less happy." |
| 4 | 5426,12 | 5436,12 | 10,0 s | **Du** | „If I translate it into the German language, jealousy means kind of something like… **ambition addiction**" |
| 5 | 5436,88 | 5446,80 | 9,9 s | **Du** | „…which I would translate into some kind of drive — like if I'm jealous at you, it can give me the fuel to…" |
| 6 | 5449,12 | 5463,68 | 14,6 s | **beide** | „…pursue what you have achieved." — „Right. And envy, just as you said, is a much more destructive force. It's like a distillation of anger." |

**66,5 s Rohzeit → bei Tempo 1,2 sind das 55,4 s, plus Outro 3,8 s = 59,2 s.**
Unter der 60-Sekunden-Grenze, mit 0,8 s Luft.

### Was herausfällt und warum

| von–bis | | |
|---|---|---|
| 5361,05–5364,21 | „what is the difference between anger?" | Fehlstart, er korrigiert sich selbst |
| 5364,21–5373,8 | ~9,6 s | **Pause** im 12-Sekunden-Segment |
| 5384,81–5392,37 | „Well, you know, the distinction between, for example, jealousy, I'm an envy." | Versprecher |
| 5414,29–5417,84 | „And the rather focuses on." | unverständlich |
| 5417,84–5425,44 | „Like dichotomy is like if you can have it…" | Anlauf, er findet den Gedanken erst danach |
| ab 5463,68 | „um yeah yeah you know so that was…" | Ausklang |

### Der Dreh, der das Short trägt

Rick definiert sauber — **Eifersucht will haben, Neid will zerstören** —
und Du drehst es ins Deutsche: *Eifersucht* als „ambition addiction", also
Eifer plus Sucht, ein **Antrieb**. Das ist die Pointe und sie gehört ans
Ende, direkt vor Ricks „distillation of anger".

### Ein Vorbehalt

Der Anfang von Stück 1 (5373,8) ist **geschätzt**. Whisper gibt für
„I mean, between jealousy and envy" ein 12,1 s langes Segment aus
(5364,21–5376,33) — ein Satz von zwei Sekunden. Darin steckt eine lange
Pause, deren Lage ich nur am Ton bestimmen kann. **Wird vor dem Schnitt an
der Hüllkurve nachgemessen**, nicht aus dem Transkript übernommen.

## Warum es heute nicht gebaut werden konnte

Drive liefert „Quota exceeded" **als HTTP 200 mit 2040 Bytes HTML**, nicht
als Fehlercode. Gemessen:

| Stückgröße | bedient |
|---|---|
| 64 KB | 3/3 |
| 256 KB | 2/3 |
| 1 MB | 3/3 |
| 4 MB | 1/3 |
| 16 MB | **0/3** |

Daraufhin `drive_fenster.py` umgebaut: Stückgröße von 16 MB auf 1 MB, plus
acht Wiederholungen mit wachsender Wartezeit. Half zunächst — und kippte
dann auch bei 1 MB. **Der zweite Master (28,2 GB, vom 27.11.) wird ebenso
abgelehnt: 0 von 4.** Es ist also das kontoweite Tageslimit, nicht die
einzelne Datei. Google setzt es nach rund 24 Stunden zurück.

Weiteres Anklopfen macht es schlimmer, deshalb abgebrochen.

## Was zu klären ist

**Es gibt zwei Master.** Meine Zeiten stammen aus dem 15,5-GB-Master vom
29.09. (7252 s). Seit dem 27.11. liegt daneben `YNB Podcast Rick
Strassman(1).mp4` mit **28,2 GB**. Ist das derselbe Schnitt in höherer
Qualität, stimmen die Zeiten; ist es ein anderer Export, nicht. Das messe
ich am Anker nach, sobald ein Abruf wieder durchgeht.

## Was er sonst noch markiert hat

Aus demselben Dokument, für später:

* `31:31` Enlightenment Short
* `1:01:15` The Crazy Meaning Behind Number 49 (Exodus, Conception & Death)
* `1:20h–1:30h` Clip: Why I gave up Buddhism and returned to Judaism
* `1:41h` „what do you believe in?" → Short
