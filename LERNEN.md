# LERNEN — das gemeinsame Gedächtnis des Teams

Wie der Kanal funktioniert: `lernen/KANAL.md`. Kurzform: Du schreibst nach
`lernen/<dein-schlüssel>.md` auf Deinem Branch, Du liest **diese** Datei am
Anfang jedes Arbeitsblocks:

```
git fetch origin claude/ai-chief-of-staff-cz83jv
git show origin/claude/ai-chief-of-staff-cz83jv:LERNEN.md
```

Alfred sammelt zweimal täglich (06:40 und 15:54 Kapstadt) und schreibt hier
zusammen. Neueste Ausgabe oben.

---

## STEHT ÜBER ALLEM — gilt für jeden Agenten, jeden Tag

Diese vier sind keine Befunde, sondern Bedingungen. Sie stehen hier, damit kein
Agent sie je nur aus zweiter Hand kennt.

1. **Nichts geht raus.** Keine Mail, kein Slack, keine Nachricht, kein Upload,
   kein Kommentar — weder selbst noch in seinem Namen. Er hat das am 26.08.
   gesagt und am **21.10. wörtlich bestätigt: „Regel bleibt, Agenten
   entwerfen."** Entwerfen, übergeben, er schickt.
2. **Er hat uns nicht onboardet.** Ihm nicht erklären, was seine Prioritäten
   sind. Weniger Karten, weniger Alarme, kein Drängen. Und kennzeichnen, welcher
   Teil einer Aussage Schlussfolgerung ist und welcher Messung.
3. **Deutsch rein, deutsch raus.** Er wechselt mitten im Thread. Entwürfe in der
   Sprache des Entwurfs, nicht in der Sprache des Werkzeugs.
4. **Nur auf den eigenen Branch schreiben.** Fremde Branches liest man, man
   schreibt sie nicht. Kein PR ohne ausdrückliche Bitte. Kein Modellname in
   irgendetwas Gepushtem.

---

## Ausgabe 1 — 21.10.2026, 11:30 Kapstadt

Erste Ausgabe. Sie trägt nach, was bis heute gemessen wurde und **bisher nur in
einem einzigen Kontextfenster stand**. Ab morgen sind die Ausgaben kurz.

### Ton und Tempo
- **`volumedetect` beantwortet die Lautheitsfrage nicht.** Es gibt Spitzen- und
  Mittelwerte zurück, nicht wahrgenommene Lautheit. Wer wissen will, ob ein
  Short so laut klingt wie die anderen, messt `ebur128` (gegatete LUFS).
  → betrifft: alle Content-Agenten
- **Seine Master sind unbearbeitet bei ≈ −31 LUFS, Shorts laufen bei ≈ −14.**
  Die naheliegende Korrektur — Hochpass, Kompressor, `loudnorm`, Limiter — hat
  er am 20.10. abgelehnt: *„der Ton ist jetzt absolut miserabel."* Gemessen
  warum: der Rauschboden steigt von **−62,7 auf −44,2 dB**. Die Dynamik war
  sauber, der Grundrauschen hörbar. **Keine Lautheitsangleichung ohne seine
  ausdrückliche Zustimmung.**
  → betrifft: alle Content-Agenten
- **`atempo=1.2` ist der Standard, obwohl `rubberband` messbar saubererer ist**
  (`atempo` hebt die spektrale Flachheit um 8 %, die Energie über 6 kHz um
  11 %). Grund: `atempo` ist der Klang, den er abgenommen hat. Eine Verbesserung,
  die er nicht bestellt hat, ist eine Änderung.
  → betrifft: alle Content-Agenten
- **Er exportiert Podcasts mit 1,1×.** Für Sutcliffe lokal ≈1,1 gemessen —
  **es gibt keine Formel für eine ganze Folge.** Immer in der Nähe der Zielstelle
  messen. Für Aaronson ist roh↔geschnitten dagegen ein **konstanter Versatz von
  12,2 s** (11 Messpunkte bis Minute 72, Korrelation 0,80–0,83):
  `Rohzeit = Schnittzeit + 12,2 s`.
  → betrifft: alle Content-Agenten

### Bild
- **Der Bewegungsgipfel ist nicht das Gesicht.** `bildausschnitt.py` sucht die
  stärkste Bewegung; eine gestikulierende Hand zieht den Kasten zur Seite.
  Aaronsons Gesicht sitzt konstant bei x 930–970 im 1920er Bild, der
  Bewegungsgipfel setzte den Kasten auf x=812 und schnitt seine linke Wange
  (bei ~780) ab. **Gesicht ausmessen, nicht Bewegung folgen.**
  → betrifft: content-*, thumbnails
- **Die Untertitelhöhe hängt vom Raum ab, nicht vom Format.** `ZEILE_FEST = 0.65`
  wurde im Sutcliffe-Studio gemessen. Bei Just Push Record landet 0,65 auf der
  Brust — dort ist **0,57** richtig. Flag `--zeile`. Pro neuem Studio einmal mit
  gezeichneten Bändern nachmessen.
  → betrifft: alle Content-Agenten
- **Ein Standbild als Filter-Input hat keine Zeit.** PNG + `overlay` + `fade`
  ergibt Alpha 0 für immer: `fade=t=in:st=0` wertet den einen Zeitstempel aus,
  `overlay` hält dann dieses Bild. Deshalb ist die Kopfzeile eine **ASS-Vektorform**
  (`\p1`, 4 Linien + 4 Bezierkurven), kein Bild.
  → betrifft: alle Content-Agenten
- **Die Kopfzeile existiert jetzt** in `video/shorts-render.py` nach
  Modern-Wisdom-Vorbild: `--kopfzeile "Text|zweite Zeile"`, `--kopfzeile-dauer`,
  `--kopfzeile-groesse`, `--kopfzeile-hoehe`, `--kopfzeile-hell`. `|` trennt
  Zeilen, kein automatischer Umbruch. Dunkel ist bestellt, hell entspricht dem
  Screenshot, den er geschickt hat — **seine Entscheidung steht noch aus**.
  → betrifft: alle Content-Agenten
- **Doppeltes Logo in der Totale**: sein Podcast-Master trägt unten links eine
  Marke bei `0,875,215,1080`. `--marke` weicht aus, erst nach oben, dann durch
  Verkleinern — nie seitlich, das zerstört die Zentrierung.
  → betrifft: content-*

### Drive
- **„Quota exceeded" ist pro Eigentümer, nicht pro Datei und nicht nach Volumen.**
  Alle fünf Dateien in *seinem* Ordner waren gesperrt, während die Datei von
  `team@justpushrecord.com` nach 12 GB weiter lieferte. Das Limit setzt sich
  über Nacht zurück.
  → betrifft: alle
- **Der gefährliche Teil: Drive liefert den Fehler als HTTP 200** mit einer
  2040-Byte-HTML-Seite. Drei Dateien wurden stillschweigend abgeschnitten
  (74,6 und 101,4 Minuten statt der erwarteten Länge; 18 s und 19 s statt 100 s),
  ohne Fehler. `drive_fernzugriff.py` prüft jetzt Statuscode **und** Blocklänge
  und wirft `IOError`. **Wer Drive direkt liest, muss die Länge prüfen.**
  → betrifft: alle
- **Audio allein holen geht nicht per `demux`.** `demux(audio)` überspringt die
  Videopakete nicht — 327 MB geladen für 120 s Ton. `video/ton_holen.py` zieht
  die Tonspur als 16-kHz-Mono-FLAC (16,1 GB → ~150 MB).
  → betrifft: alle Content-Agenten
- **Schreibfreigaben, Stand heute:** der Wochenbericht-Ordner und
  `1N5i97R5byCWF57z23GuwoY1v5w6vX1ef` (Archiv der Meaningful-Serie, am 21.10.
  freigegeben, Schreibzugriff getestet). **Alles andere in Drive und Trello ist
  nicht freigegeben.** Notion-Schreiben ist seit 27.08. frei. Kalenderschreiben
  ist freigegeben, scheitert aber am abgelaufenen Token — als Vorschlag anzeigen,
  höchstens einmal täglich erneut versuchen.
  → betrifft: alle

### Transkript und Sprecher
- **Die drei Aaronson-Spuren trennen die Sprecher nicht.** Paarweise
  Pegelverhältnisse, IQR 2,3–2,4 dB, unimodal: drei Mikrofone in einem Raum mit
  unterschiedlichem Gain (≈ −17 und −7 dB Versatz), dual-mono. **Sprechernamen
  aus Pegeln sind dann erfunden.** `transkript_lokal.py` verlangt jetzt ≥ 4 dB
  IQR und verweigert sonst die Zuordnung: *lieber kein Sprechername als ein
  erfundener.* Die Zuordnung kam am Ende aus der **Kameraführung**
  (Left = Aaronson, Right = Yannick, Middle = Totale).
  → betrifft: alle Content-Agenten
- **Whisper ist nicht deterministisch.** Dieselbe Stelle kam als „AI?", „AI."
  und „A I?" zurück. Feste Schreibweisen gehören in `video/korrekturen.txt`,
  nicht in die Hoffnung. Regel in `korrekturen_anwenden`: endet der Ersatz schon
  auf ein Satzzeichen, wird das des Originals **nicht** angehängt — sonst „AI??".
  → betrifft: alle Content-Agenten

### Umgebung und Werkzeuge
- **`SendMessage` erreicht die anderen Agenten nicht.** `ListAgents` zeigt nur
  Sessions auf dieser Maschine; das Team läuft in der Cloud. Der Weg ist
  `create_trigger` mit `persistent_session_id` + `run_once_at` — **der Prompt ist
  die Nachricht.** Am 21.10. geprüft, nachdem eine gespeicherte Anweisung diesen
  Weg um 03:40 Uhr still gescheitert wäre.
  → betrifft: alle
- **Der Container wird eingezogen, und das killt Hintergrundprozesse.** `nohup`
  und `setsid` helfen nicht. Lange Läufe müssen **wiederaufnehmbare Skripte**
  sein, die ihren Fortschritt an Dateien auf der Platte erkennen.
  → betrifft: alle
- **`cost_usd` ist der Listenpreis-Gegenwert der Token, kein Abbuchen von seinem
  Abo.** Abgerechnet wird über Nutzungsfenster (`rate_limit_info`,
  `isUsingOverage`). Er hat „96 Dollar" am 21.10. als Rechnung gelesen, und das
  war unser Formulierungsfehler. **Keine Dollarbeträge ohne diese Einordnung.**
  → betrifft: alle
- **`substack.com` ist durch den Egress-Proxy gesperrt** (403 auf CONNECT, auch
  über WebFetch), ebenso alle Spotify-Hosts. Er muss sie freischalten; bis dahin
  ist der Drive-Ordner der Weg. **403/407 sind Policy-Entscheidungen — nicht
  wiederholen, melden.** Nie die TLS-Prüfung abschalten, nie `HTTPS_PROXY`
  entfernen.
  → betrifft: head-of-content, youtube-manager
- **Keine Musik und keine Medien aus dem Netz** für etwas, das er
  veröffentlicht. Kommerzielle Aufnahmen holen sich einen Content-ID-Anspruch
  auf *seinem* Kanal.
  → betrifft: alle Content-Agenten
- **Kalender: immer `timeZone: Africa/Johannesburg` ausdrücklich mitgeben** und
  **beide** Kalender lesen — geschäftlich `ynb@yannick-noah.com`, privat
  `yannicknbernard@gmail.com`. Er ist seit 18.10. in Kapstadt, nicht in Austin.
  → betrifft: alle

### Arbeitsweise — die vier Regeln, die aus Fehlern kommen
- **Eine Messung, die den eigenen Plan bestätigt, ist kein Beleg.** Im selben
  Ausdruck standen −14,5 LUFS (was ich wollte) und der Rauschboden von −44,2 dB
  (was er hören würde). Ich habe das zweite als Fußnote behandelt. Beim nächsten
  Mal: zuerst die Zahl suchen, die gegen den Plan spricht.
  → betrifft: alle
- **Nie zwei Dinge am Ton in einer Runde ändern.** Sonst ist nicht feststellbar,
  welche davon er gehört hat.
  → betrifft: alle Content-Agenten
- **Sein Ohr schlägt jede Messung.** Auch wenn die Zahlen sagen, es sei besser.
  → betrifft: alle
- **Einen Weg selbst gehen, bevor er in eine gespeicherte Anweisung kommt.**
  Eine Anweisung, die nachts um 03:40 still scheitert, ist schlimmer als keine.
  → betrifft: alle

### Was ich heute über das Team selbst gemessen habe
- **Sechs von sieben Agenten haben eigene Commits — und keiner davon hat je
  etwas in einen gemeinsamen Kanal geschrieben, weil es keinen gab.** Gezählt
  am 21.10.: thumbnails **15**, youtube-manager **3**, content-cinematic **3**,
  head-of-content **2**, content-vlog **2**, guest-booking **1**; der
  Shorts-Assistent ist bereits in den Hauptzweig gemerged. Das sind 26 Commits
  echter Arbeit — Williamsons Bildsprache an 99 Standbildern gemessen, 438
  YouTube-Titel ausgewertet, die Thumbnail-Schrift gefunden, „die 71 sind 60
  Personen". **Jeder einzelne Befund davon war für jeden anderen Agenten
  unsichtbar.** Genau dafür ist diese Datei da.
  → betrifft: alle
- **Ungeholte Remote-Refs lügen.** Dieselbe Zählung ergab eine Stunde vorher
  „null eigene Commits bei allen sieben" — weil `git rev-list` gegen den alten
  Stand von `origin/...` lief, den dieser Container beim Klonen bekommen hatte.
  Das Ergebnis war ordentlich formatiert, eindeutig und komplett falsch. **Vor
  jeder Aussage über einen fremden Branch erst `git fetch`.**
  → betrifft: alle

### Nachtrag, 12:40 — zwei Befunde aus seiner Korrektur von eben
- **Der Ausschnittsplaner plant an einem Kameraschnitt nicht neu.** Im
  Aaronson-Short laufen **zwei** Einstellungen über 58 s, davon eine
  **56 Sekunden am Stück** mit festem Kasten `650:0:608:1080`. Solange die Regie
  auf Scotts Kamera bleibt, stimmt das. Schaltet das Studio auf die Totale,
  sitzt Scott woanders im 1920er Bild — und das Fenster zeigt Holzwand,
  Mikrofonarm und die Getränkedosen. Yannick hat es gesehen, ich nicht.
  **Jedes Short, das über einen Kameraschnitt läuft, hat diesen Fehler.** Der
  Plan muss an jedem Schnitt geteilt und der Kasten neu gemessen werden.
  Einfrieren (`tot: true`, wie bei Sutcliffe) ist hier **falsch** — der Gast ist
  ja zu sehen, nur an anderer Stelle. Seine Worte: *„Ich möchte, dass der Shot
  dann aber auf Scott bleibt."* Liegt beim Shorts-Assistenten.
  → betrifft: content-schlicht, content-cinematic, content-vlog
- **Short-Aufträge gehören dem Shorts-Assistenten, nicht mir.** Seine Korrektur
  am 21.10.: *„Diese Aufgabe hättest du eigentlich dem Short Manager übergeben
  sollen."* Ab jetzt: ich diagnostiziere, messe den Fehler so weit, dass die
  Übergabe präzise ist, und gebe ab. Ich rendere nicht selbst. **Das gilt
  sinngemäß für jedes Fach, für das es einen Agenten gibt** — wer einen Auftrag
  annimmt, für den jemand anderes zuständig ist, baut genau das Silo, das dieser
  Kanal auflösen soll.
  → betrifft: alle
- **ffmpeg ist heute aus meinem Container verschwunden** (die Dateien im
  Scratchpad liegen noch da, das Werkzeug nicht). Container werden eingezogen
  und neu gebaut; **was nicht im Repo oder in Drive liegt, ist weg**, und was
  installiert war, ist nicht wieder da. Kein Grund zur Panik, aber ein Grund,
  Zwischenstände zu committen statt im Scratchpad liegen zu lassen.
  → betrifft: alle
