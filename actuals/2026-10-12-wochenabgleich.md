# Wöchentlicher Abgleich — Montag 12.10.2026, Austin

Ausgelöst vom wöchentlichen Trigger um 08:15 Austin, fertiggestellt um
13:02. Vier Teile: Gäste-Abgleich, Sent-Mail-Pattern, Wochendokument in
Drive, Board.

Abgleichszeitraum für die Mails: `in:sent newer_than:8d` = **04.–12.10.**

---

## TEIL 1 — PODCAST-GÄSTE: OUTREACH-DOC vs. DATABANK vs. POSTFACH

### Die drei Quellen, exakt gezählt

| Quelle | Umfang | Was drinsteht |
|---|---|---|
| Outreach-Doc (Drive `1R11m4Lt…`) | **87** nicht-leere `### Name`-Überschriften (90 `### `-Zeilen, drei davon leer), 204.157 Zeichen | nur Pitch-Texte, kein Status, kein Datum |
| Databank (Notion `collection://4aa27609…`) | **234 Zeilen**, davon **100 mit Kontaktstatus**, 125 *Not Started*, 8 *Researching*, 1 ohne Status | `Outreach Status`, `Datum`, `Location`, `Approval`, `Why`, `Contact`, `Notes` |
| Postfach | — | die Wahrheit über das, was rausgegangen ist |

**Zwei eigene Zahlen von letzter Woche korrigiert, nicht verglichen:**
- „~200 Zeilen" war eine Schätzung. **Es sind 234.**
- „87 Überschriften" war richtig. Mein erster Zählbefehl heute sagte 90,
  weil er leere `### `-Zeilen mitzählt. **87 bleibt die Zahl**, und das
  Doc hat sich in der Woche **nicht** verändert.

**Nichts in der Databank hat sich in der Woche bewegt.** Jüngste Zeile
angelegt `2026-10-03 20:24Z`. Keine neue Zeile, kein geänderter Status.

### 1a) Das Outreach-Doc kann ich weiter nicht beschreiben

Unverändert: der Drive-Connector hat für eine **bestehende** Datei nur
`update_file`, und das ändert ausschließlich Titel und Ordner. Ein
Inhalts-Write gibt es nur über `create_file`, also nur für eine **neue**
Datei. Die 204.157 Zeichen Pitch-Arbeit neu anzulegen und die alte zu
ersetzen wäre genau das Überschreiben, das verboten ist.

→ Die Zeilen, die der Trigger ins Doc haben will, stehen deshalb **hier
und im Wochendokument**. Einfügen muss er.

### 1b) Namen in der Databank ohne Pitch im Doc — 26

Von 37 Treffern sind elf nur **anders geschrieben** (siehe 1e). Es
bleiben **26 Namen mit Kontaktstatus, für die im Doc kein Pitch steht:**

*Confirmed (5):* Amy May · Amy Nelson · Drew Birch · Jamie Elkon ·
Megan de Beyer — **alle fünf Cape Town.**
*Follow-up (5):* Jack Kornfield · Jim Collins · Mikhaila Peterson ·
Timothy Olson · Tommy Caldwell
*In Conversation (1):* Chris Taylor (Red Fridge Society)
*Reached Out (11):* Angie Lee · Dean Karnazes · Francisco Medina ·
Kyle Buller · Maverick Maltin · Staffan Taylor · Steve Adler ·
T.D. Jakes · TD (Yes Theory) · Charles Nemeroff¹ · Kirk Watson¹
*Recorded (4):* Bridget Woods · Craig Makhosi · Nathan Maingard ·
Whitney Wheelock
*Declined (1):* Sarinia Bryant [DUPLICATE – delete, merged]

¹ *stehen im Doc nur mit Titel davor — siehe 1e, zähle ich unten nicht
doppelt.*

**Die fünf Cape-Town-Zeilen sind der Fund dieser Woche.** Sie stehen auf
*Confirmed*, haben kein Datum, keinen Pitch — **und er ist seit dem
10.10. in Kapstadt, bis 04.11.** Das stelle ich nebeneinander. **Kein
Vorschlag.**

### 1c) Pitches im Doc ohne Outreach — vier geschrieben, nie raus

Namen mit fertigem Pitch im Doc und Databank-Status *Not Started*:

| Name | Approval |
|---|---|
| **Matthew McConaughey** | **Yes** |
| **Wes Huff** | Pending |
| **yung pueblo (Diego Perez)** | Pending |
| **Andy Weir** | Pending |

### 1d) Neun Pitches im Doc ohne jede Databank-Zeile

Alon Matar · Codie Sanchez · Dr. Mark Gafni · Elliott Bisnow ·
Joe Lonsdale · John Wineland · MJ DeMarco · Mark Kaplan · Stephen West

*Einzeln per `LIKE` gegengeprüft, keiner ist unter abweichender
Schreibweise vorhanden.* **Fertige Pitch-Arbeit, die in keiner Liste
auftaucht.**

### 1e) Dieselbe Person, zwei Schreibweisen — elf Paare

| Databank | Doc |
|---|---|
| Blake Mycoskie | Blake Mykosy |
| David Perell | David Perrel |
| Dr. Daniel Amen | Dr. Dan Amen |
| Ian Gardner | Ian Garden |
| Charles Nemeroff | Prof. Charles Nemeroff |
| Kirk Watson | Mayor Kirk Watson |
| Thomas Brag | Thomas Barg |
| Aubert Batistat | Aubert Bastiat |
| Enfold – Steve Rio & Austin | Austin & Steve Rio |
| Paul | Paul Austin |
| **Angie Lee + Mike Lee (zwei Zeilen)** | **Angie & Mike Lee (eine Überschrift)** |

*Aubert ist unabhängig geklärt: die Adresse lautet
`aubert@aubertbastiat.com`, also ist **Bastiat** richtig und die
Databank-Zeile falsch geschrieben.* **Ich benenne es, ich benenne nicht
um** — Umbenennen heißt bei Notion den Titel überschreiben, und bei
elf Zeilen in einem Durchgang will ich dafür sein Wort.

### 1f) Bestätigte und aufgenommene Gäste ohne Datum

**Geschrieben in dieser Runde (ein Write):**
- **Whitney Wheelock** — Status war *Recorded*, Datum leer. Belegt über
  den Kalender: *„Man's Search for Meaning: Whitney Wheelock"*,
  **So 27.09., 17:00–19:00 −05:00 (`America/Chicago`)**, Eintrag vom
  17.08., zuletzt geändert 29.09. → **Datum `2026-09-27T22:00:00Z`.**
  *Die Zone des Orts kenne ich weiter nicht; der Offset im Kalender legt
  den Zeitpunkt fest, und genau den trägt das Feld.*

**Nicht geschrieben, mit Grund:**
- **Ian Gardner** — *Confirmed*, kein Datum. **Hier korrigiere ich mich
  selbst:** mein eigenes Wochendokument vom 05.10. nannte ihn „den Fund"
  und schlug *Recorded* mit `2026-09-17 17:00Z` vor. **Das war falsch.**
  In der Notiz derselben Zeile steht seit dem 21.09.: *„DER 17.09. HAT
  NICHT STATTGEFUNDEN. Yannick hat die Aufnahme am 13.09. selbst
  verschoben."* Und im Handbuch steht seit dem 14.09., dass ich den
  Status hier **nicht** ändere. **Ich habe am 05.10. gegen meine eigene
  belegte Korrektur argumentiert, ohne sie zu lesen.** Datum bleibt
  leer, Status bleibt. Offen ist sein eigenes Versprechen: *„I'll follow
  up as soon as I've got firmer dates."*
- **Marian Goodell** — *Confirmed*, Datum `2026-10-06 18:00Z`. **Das
  Datum ist vorbei.** Was ich sehe: alle drei Teilnehmer stehen jetzt auf
  `accepted` (seine Antwort kam bis 30.09. 13:47 Austin — damit ist der
  Punkt „Deine Antwort fehlt" **zu**), Ort 660 Alabama St, keine Absage,
  und er hat den Block *California 03.–08.10.* am 11.10. nachträglich
  selbst eingetragen. **Trotzdem habe ich keinen Beleg, dass aufgenommen
  wurde** — keine Mail danach, keine Statusänderung. *Ich setze nicht
  auf Recorded. Das kann nur er bestätigen.*
- **Matt Defina** — *Confirmed* mit Datum 04.09., Aufnahme hat
  stattgefunden. Status veraltet. **Dasselbe Muster wie bei Goodell**,
  nur älter; auch hier kein Nachweis in Mail oder Kalender, dass ich
  „Recorded" belegen könnte. Vorgelegt, nicht gesetzt.
- **Logan Gonzalez** — Notion `2026-09-11 20:00Z` (= 15:00 Austin),
  Kalender **14:30**–17:00 −05:00 (= 19:30Z). **Weiter eine halbe Stunde
  auseinander**, unverändert seit dem 05.10. Der Kalender wurde am 12.09.
  nachträglich geändert, Notion nicht nachgezogen. *Ich ziehe nicht
  nach, solange ich nicht weiß, welche Seite stimmt.*
- **Confirmed ohne Datum, fünf Cape-Town-Zeilen:** Amy May, Amy Nelson,
  Drew Birch, Jamie Elkon, Megan de Beyer. Kein Datum findbar.
- **Recorded ohne Datum, drei:** Bridget Woods, Craig Makhosi,
  Nathan Maingard.
- **Scott Aaronson** — *Confirmed*, Datum 21.08. vorbei, `Approval`
  steht auf *Pending*. Heute hat er die **Veröffentlichungsmarke** für
  Aaronson auf Sa 17.10. gelegt; das sagt über den Aufnahmestatus
  nichts.

### 1g) Der Kingsbury-„Widerspruch" war mein Kategorienfehler

Seit dem 06.10. führe ich: *Databank 31.08. gegen Kalender Sa 17.10.
ganztägig.* **Falsch zusammengestellt.** Ganztägige, durchsichtige
Einträge mit dem Vorsatz „Podcast:" sind **Veröffentlichungsmarken**,
keine Aufnahmetermine — das steht wörtlich in meinen eigenen Regeln. Ein
Veröffentlichungsdatum widerspricht einem Aufnahmedatum nicht.

Sichtbar wurde es, weil er die Marke **heute um 10:02 von Sa 17.10. auf
So 25.10. geschoben** und eine Minute später Aaronson auf Sa 17.10.
gelegt hat. Hätte ich recht gehabt, wäre der „Widerspruch" damit einfach
weitergewandert — ein Zeichen, dass die Gegenüberstellung nie eine war.

**Offen bleibt die echte Frage:** Databank *Confirmed*, **31.08.
15:00Z**, und für den 31.08. keine Aufnahme im Kalender. **Kein Datum
erfunden.**

### 1h) Zeitzonen-Prüfung September-Roadtrip

Unverändert gegenüber dem 05.10., und beide Fälle stehen schon im
Handbuch: Phoenix (Ian Gardner, 17.09.) ist **UTC−7 ohne Sommerzeit**,
Albuquerque (Strassman, 18.09.) **UTC−6**. Beide Einträge stehen auf
Offset −05:00 mit Label `America/Chicago`. Umrechnung bleibt:
`12:00 Austin = 10:00 Phoenix`, `11:30 Austin = 10:30 ABQ`. Neu zu
beachten: seit dem 11.10. tragen viele Einträge das Label
`Africa/Johannesburg` — **der Offset ist weiter der Moment, das Label
ist Dekoration.**

---

## TEIL 2 — SENT-MAIL-PATTERN

### Die Woche hatte genau eine ausgehende Mail

`in:sent newer_than:8d` → **ein Thread, eine eigene Nachricht.** Den
Thread vollständig gelesen (13 Nachrichten, nicht die fünf der
Suchvorschau). Keine Entwürfe von mir umgeschrieben — `DRAFT` steht
unverändert bei 16. **Kein Delta zu diffen.**

Damit ist die Woche für die Registeranalyse zu dünn. Ich nehme deshalb
die **drei Nachrichten desselben Verhandlungsbogens** dazu (30.09.,
02.10., 09.10.) — ausdrücklich außerhalb des Acht-Tage-Fensters, und
nur, weil das Register erst im Verlauf sichtbar wird.

### Englisch, derselbe Empfänger, drei Register in zehn Tagen

| | 30.09. 13:05 | 02.10. 13:00 | 09.10. 12:57 |
|---|---|---|---|
| Anrede | „Howdy Ryan," | **keine** | „Howdy Ryan," |
| Eröffnung | eigener Zustand (*„getting back on my feet"*) | **die Position des anderen** (*„you've got a firm policy and I hear you"*) | Entscheidung (*„I'll have to bite the bullet"*) |
| Bitte | beiläufig (*„Any chance you could…"*) | **ausbuchstabiert** (*„as honestly and humbly as I can"*) | keine, nur Auftrag |
| Schluss | „Thanks a lot, YNB" | **keiner, Satz endet auf „…"** | „Thanks, Yannick" |
| Länge | kurz | längster der drei | kürzester |

**Die Regel, die daraus folgt (nicht die Anekdote):**

> **„Howdy <Vorname>," ist seine normale englische Anrede für eine
> transaktionale Mail. Wenn er um eine Ausnahme bittet, lässt er Anrede
> und Grußformel weg und beginnt mit dem Zugeständnis an die Gegenseite.
> Der Bittmodus ist am Fehlen der Rahmung erkennbar, nicht an einem
> Signalwort.**

Zweitens, und unabhängig davon:

> **Seine Unterschrift schwankt mit der Nähe: „YNB" an jemanden, mit dem
> er schon im Austausch ist · „Yannick" bei einer sachlichen
> Entscheidung · gar keine, wenn er bittet. Ein Entwurf von mir setzt
> keine Unterschrift, die ich nicht aus derselben Mailkette belegen
> kann.**

Drittens, aus dem 09.10. und schon in der Manual-Stimme angelegt:

> **Wenn er nachgibt, nennt er es so. „I'll have to bite the bullet on
> this one then" — keine Rechtfertigung, kein Rückblick auf die Bitte,
> die abgelehnt wurde. Ein Entwurf, der an dieser Stelle die Ablehnung
> noch einmal aufgreift, klingt nicht nach ihm.**

### Deutsch: diese Woche nichts von ihm, aber ein Befund aus dem Eingang

Keine deutsche ausgehende Mail im Fenster. Dafür steht im
Brandlift-Faden sein deutsches Register vom 28.08./03.09. neben Luis'
heutiger Mail — und daraus ein Punkt für `voice/german-register.md`:

> **In seinen deutschen Arbeitsmails steht die Absage mitten im Text,
> nicht am Ende, und sie wird mit dem eigenen Anspruch begründet, nicht
> mit Zeitmangel allein: *„Wenn ich mich zu etwas committe, dann nur zu
> 100%."* Dann folgt ein konkreter neuer Zeitpunkt. Das ist dieselbe
> Bewegung wie im englischen Bittmodus — Position der Gegenseite
> anerkennen, eigene Lage benennen, einen Termin liefern — nur ohne das
> Weglassen der Rahmung.**

---

## TEIL 3 — WOCHENDOKUMENT IN DRIVE

Neu angelegt im Ordner `YNB x Claude`
(`1ioemsCTuhs-mdrRMdEWC1CHFzQCdI9dq`), Titel
**„Alfred — Actuals Log · Woche 5.–12. Oktober 2026"**,
`fileId` **`1Zr_k9hD5hSx2MUmZXMpcHDoQvIXTNKCNyvhKLcqzUNk`**, angelegt
`2026-10-13T08:51:53Z`. Nichts überschrieben, nichts in den Papierkorb.
`fileSize` meldet wie immer `1` — das ist der bekannte Artefaktwert bei
Google Docs und **kein Hinweis auf einen Fehlschlag**; Inhalt
zurückgelesen.

---

## TEIL 4 — BOARD

`SWEPT` 13:02. Zeilen `glass-nachfrage-1210`, `brandlift-onhold-1210`,
`marken-getauscht-1210`. Lede, Uhrenzeile, `EV` und `why` Punkt 1 und 6
auf den heutigen Stand. Zwei eigene Fehler behoben (doppelte
Uhrenkette, mitgedrehte Zeitmarke), ein dritter von der
Wochentagsprüfung gefangen („Sa 25.10." → **So**).

---

## WAS DIESER DURCHGANG NICHT KONNTE

- **Das Outreach-Doc beschreiben.** Siehe 1a — unverändert eine
  Connector-Grenze, keine Entscheidung.
- **Elf Schreibweisen zusammenführen.** Das wäre elf Titel in Notion
  überschreiben; dafür will ich sein Wort.
- **Goodell und Defina auf *Recorded* setzen.** Kein Beleg, nur starke
  Indizien. Vorgelegt.
- **Den Kingsbury-31.08. auflösen.** Keine Aufnahme im Kalender, kein
  Datum erfunden.
- **Logans halbe Stunde entscheiden.** Zwei Quellen, keine dritte.
