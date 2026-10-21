# Befunde — guest-booking

Format und Regeln: `lernen/KANAL.md`. Anhängen, neuester Tag oben,
jeder Eintrag mit einer Zahl oder einem Zitat und mit der Zeile `→ betrifft:`.
Alfred sammelt 06:40 und 15:54 Kapstadt ein und verteilt über `LERNEN.md`.

<!-- Neue Einträge ab hier. -->

## 2026-10-21

- **Ein Faden ist keine Person, und eine Person ist keine Beziehung.**
  `podcast/outreach-unbeantwortet.md` führte **71 „unberührte" Fäden**. Pro Person
  zusammengelegt sind es **62**, zwei davon haben längst geantwortet, also
  **60 wirklich stille Personen** — plus 6, deren Mail nie ankam.
  **Woran die Dubletten erkennbar sind, drei Muster, alle belegt:**
  1. **Zwei Adressen desselben Menschen in zwei Zeilen** — `dengle@doterra.com`
     und `dan@drdanengle.com` (beide 09.07.), `timothyallenolson@gmail.com` und
     `timothy@timothyallenolson.com` (beide 22.07.), zwei UT-Adressen für
     McConaughey (beide 15.08.). **Gleicher Tag plus gleicher Betreff ist das
     Erkennungszeichen.**
  2. **Zwei Anläufe derselben Person an Tagen hintereinander** — Zach Leary
     **3×** (07.07., 09.07., 15.07.), Paul Austin, Kim (rappid.run),
     Justin Lovato, Yung Pueblo je 2×. Der zweite Anlauf steht als eigener Faden
     und sieht aus wie ein eigener Mensch.
  3. **Person und Vertretung getrennt geführt** — `info@yungpueblo.com` gegen
     `diego@yungpueblo.com`. Dagegen sind `thomas@` und `ammar@yestheory.com`
     **zwei verschiedene Menschen**: dieselbe Firma heißt nicht dieselbe Person.
     Nicht pauschal nach Domain zusammenlegen.
  **Zählregel: erst pro Mensch zusammenlegen, dann zählen** — vorher ist jede
  Quote um den Faktor der Doppelanläufe zu pessimistisch.
  → betrifft: alfred, head-of-content

- **„Unbeantwortet" prüft man pro Adresse über das ganze Archiv, und das kostet
  fünf Abfragen statt achtundachtzig.** `in:anywhere from:{a b c …}` nimmt
  **18 Adressen in einem Aufruf** (geschweifte Klammern = OR), mit
  `includeTrash: true`. Alle **88 Adressen** der Liste geprüft: **14 Treffer,
  null menschliche Antworten** — zwei bekannte Fehleinträge, zwei Autoreplies,
  zehn Rundbriefe.
  **Was die Abfrage nicht kann:** eine Antwort von einer *anderen* Adresse
  derselben Person finden (Agentur, Assistenz, zweites Postfach). Das gehört an
  jede Zahl dazu, die mit ihr belegt ist.
  **Und ein Autoreply ist keine Antwort, kann aber eine Adresse korrigieren:**
  Carhart-Harris' Abwesenheitsnotiz vom 07.08. nennt **UCSF statt Imperial** und
  die Assistenz `buglova.kat@ucsf.edu`. Die Adresse in der Liste ist die falsche.
  → betrifft: alle

- **Vier veröffentlichte Folgen haben keine korrekte Databank-Zeile.** Heute den
  Kanal (`UC5r4pxlAtt2alIOIGjdn4Qw`, 38 lange Videos) gegen alle 262
  Databank-Zeilen gestellt:
  · **Robert Paddock** steht auf *Researching* — Folge läuft, 5.533 s, 537 Aufrufe
  · **Francis Chouler** hat **keine Zeile** — 4.239 s, **12.000 Aufrufe**, das
    stärkste lange Video des Kanals
  · **Rob Bennett** hat **keine Zeile** — 7.115 s, 334 Aufrufe
  · **Curtis Crane** hat eine Zeile, aber **`Outreach Status` ist leer** (das
    einzige Status-NULL in 262 Zeilen) — Folge läuft, 6.593 s, 1.300 Aufrufe
  **Regel: eine Databank-Lücke wird nicht im Postfach gesucht.** Gäste tauchen an
  drei Orten auf, die alle außerhalb der Mail liegen — veröffentlichte Folgen auf
  dem Kanal, Kalenderblöcke mit Personennamen, und die Gästeliste in seinen
  eigenen Pitches. Beispiel aus der dritten Quelle: **Sean Meyersfield** steht auf
  *Not Started* und wird in beiden Sponsoring-Pitches als Gast geführt.
  → betrifft: alfred, youtube-manager, head-of-content

- **Die Databank hat 262 Zeilen, nicht „~90 aktive Kontakte".** Heute gezählt:
  Not Started 153 · Reached Out 51 · Follow-up 16 · Recorded 11 ·
  In Conversation 9 · Confirmed 9 · Researching 8 · Declined 4 · ohne Status 1.
  Die Zahl „~90" im Handbuch stammt vom 26.08. **Eine Abfrage ohne Namensfilter
  zeigt nur die erste Seite** — wer so prüft, ob jemand drinsteht, findet ihn
  nicht. Immer gezielt filtern oder `COUNT(*)` rechnen.
  → betrifft: alfred, head-of-content

- **Ein Videotitel ohne Gastnamen ist keiner Zeile zuzuordnen, und Raten ist
  hier teuer.** Zwei Langfolgen bleiben offen: *„The SHOCKING Truth About The
  Crisis in South Africa… (4K)"* (8.712 s) und *„Federal Reserve Banker Turned
  Tantra Guru…"* (6.247 s). Gleichzeitig stehen **Bridget Woods** und
  **Craig Makhosi** auf *Recorded* ohne Datum. Dass das zusammengehört, ist
  **Vermutung** — ich habe es nicht eingetragen. Wer Folgen gegen Gäste zählt,
  braucht die Video-ID, nicht den Titel.
  → betrifft: youtube-manager, head-of-content

- **`yt-dlp` ist aus diesem Container verschwunden, `pip install yt-dlp` holt es
  in einem Aufruf zurück** (2026.08.19 installiert, lief sofort). Dieselbe
  Gattung wie Alfreds Befund „ffmpeg ist heute verschwunden": **Container werden
  neu gebaut, installierte Werkzeuge sind dann weg.** Kein Grund, einen Befund
  aufzugeben — die Netzwerkfreigabe vom 19.10. gilt weiter, der Kanalabruf über
  `extract_flat` braucht keinen API-Schlüssel.
  → betrifft: alle
