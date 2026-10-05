# Wöchentlicher Abgleich — Montag 05.10.2026, 08:15–09:00 Austin

Ausgelöst vom wöchentlichen Trigger. Vier Teile: Gäste-Abgleich,
Sent-Mail-Pattern, Wochendokument in Drive, Board.

Abgleichszeitraum für die Mails: `in:sent newer_than:8d` = 27.09.–05.10.2026.

---

## TEIL 1 — PODCAST-GÄSTE: OUTREACH-DOC vs. DATABANK vs. POSTFACH

### Was die drei Quellen sind

| Quelle | Umfang | Was drinsteht |
|---|---|---|
| Outreach-Doc (Drive, `1R11m4Lt…`) | **87** `### Name`-Überschriften, 204.157 Zeichen | **Nur Pitch-Texte.** Kein Status, kein Datum, keine Statuszeile — nirgends im ganzen Dokument. |
| Databank (Notion, `collection://4aa27609…`) | **~200** Zeilen, davon **100** mit Kontakt-Status | `Outreach Status`, `Datum`, `Location`, `Approval`, `Why`, `Contact` |
| Postfach | — | die Wahrheit über das, was tatsächlich rausgegangen ist |

### Der Befund, der alles andere einordnet

**Das Outreach-Doc kann ich nicht beschreiben.** Der Drive-Connector hat für
bestehende Dateien nur `update_file`, und das ändert ausschließlich **Titel und
Ordner** — keinen Inhalt. Ein Inhalts-Write existiert nur über `create_file`,
also nur für ein **neues** Dokument. Das Doc ist 204.157 Zeichen Pitch-Arbeit;
ein Neuanlegen-und-Ersetzen wäre genau das Überschreiben, das verboten ist.

→ Die Zeilen und Daten, die der Trigger ins Doc haben will, stehen deshalb
**hier und im Wochendokument** — zum Einfügen vorbereitet, einfügen muss er.

### 1a) Bestätigte Gäste brauchen ein Datum

Elf Databank-Zeilen tragen überhaupt ein `Datum`. Gegen den Geschäftskalender
geprüft:

| Gast | Databank | Kalender (Austin) | Urteil |
|---|---|---|---|
| **Marian Goodell** | Confirmed · 2026-10-06 18:00Z | Di 06.10. 13:00–15:00 −05:00 | **stimmt auf die Minute** (= 11:00 San Francisco) |
| **Logan Gonzalez** | Recorded · 2026-09-11 20:00Z | Fr 11.09. **14:30**–17:00 −05:00 | **halbe Stunde auseinander.** Kalender am 12.09. nachträglich geändert (`updated 2026-09-12T14:06:17Z`), Notion nicht nachgezogen. |
| **Kyle Kingsbury** | Confirmed · 2026-08-31 15:00Z | am 31.08. **nichts**; Geschäftskalender hat **Sa 17.10. ganztägig** | **Datum veraltet.** Kein Beleg, dass am 31.08. etwas war. |
| **Matt Defina** | **Confirmed** · 2026-09-04 14:00Z | Fr 04.09. 09:00–11:00 −05:00, *Just Push Record Studios* | Instant stimmt. **Status veraltet** — die Aufnahme hat stattgefunden, steht aber noch auf Confirmed. |
| **Ken Stern** | Recorded · 2026-09-14 13:30Z | Mo 14.09. 08:30–10:30 −05:00 | stimmt |
| **Rick Strassman** | Recorded · 2026-09-18 16:30Z | Fr 18.09. 11:30–13:30 −05:00, Ort *Albuquerque* | Instant stimmt — **aber siehe Zeitzonen** |
| **Joe Moore** | Follow-up · 2026-09-22 16:00Z | Di 22.09. 11:00–13:00 −05:00, *Let's Do Podcast* | **stimmt so, wie es ist.** Die Aufnahme fand nicht statt (seine Absage vom 21.09. 16:15 nach dem Motorradunfall); *Follow-up* und das stehengelassene Datum sind die Korrektur vom 28.09., nicht ein Versehen. |
| Danny Miranda | Recorded · 2026-08-17 | — | past |
| Eben Britton | Recorded · 2026-08-24 17:00Z | — | past |
| David Sutcliffe | Recorded · 2026-08-26 16:00Z | — | past |
| Scott Aaronson | Confirmed · 2026-08-21 18:00Z | — | past, Status vermutlich veraltet |

**Und eine Bewegung, die ich beinahe als eigenen Rechenfehler verbucht hätte:**
Im Wochendokument vom 28.09. steht Marian Goodell mit **Di 06.10., 17:00–19:00
Austin**. Heute steht sie auf 13:00–15:00. Beide Einträge — Walkers Einladung
*und* Yannicks eigene Kopie — tragen `updated 2026-09-30T18:29:45Z` bzw.
`18:47:09Z`, also **Mi 30.09., 13:29 und 13:47 Austin**. Der Termin ist nach dem
letzten Abgleich um zwei Stunden nach vorn gezogen worden, und die Databank ist
mitgezogen. Das Dokument vom 28.09. war an seinem Tag richtig.

**Bestätigt ohne jedes Datum** (sechs): Amy May, Amy Nelson, Drew Birch,
Jamie Elkon, Megan de Beyer (alle Cape Town — kein Datum findbar, er ist nicht
dort) und **Ian Gardner**.

**Ian Gardner ist der Fund.** Status *Confirmed*, kein Datum — aber die Aufnahme
hat stattgefunden: **Do 17.09. 12:00–14:00 −05:00, `112 N Central Ave #M18,
Phoenix, AZ 85004`**, davor Mi 16.09. 20:00 *Dinner Ian & Yannick*.
→ Datum `2026-09-17 17:00Z`, Status *Recorded*.

**Aufgenommen ohne Datum** (vier): Bridget Woods, Craig Makhosi, Nathan
Maingard, **Whitney Wheelock** — bei Wheelock liegt das Datum vor:
So 27.09. 17:00–19:00 −05:00, also `2026-09-27 22:00Z`.

### 1b) ZEITZONEN-PRÜFUNG SEPTEMBER-ROADTRIP

Alle **73** September-Termine des Geschäftskalenders stehen auf Offset
**−05:00**, fast alle mit dem Label `America/Chicago`. Kein einziger Termin im
ganzen September steht auf einem Mountain-Offset. Zwei davon waren aber
körperlich außerhalb von Central:

1. **Ian Gardner, Do 17.09., Phoenix AZ.** Eintrag `12:00:00-05:00`.
   Arizona ist **MST ohne Sommerzeit, UTC−07:00** — im September also **zwei
   Stunden** hinter Austin. 12:00 Austin = **10:00 Phoenix**.
   Das Abendessen am Vortag, 20:00 −05:00, = **18:00 Phoenix**.
2. **Rick Strassman, Fr 18.09., Ort im Termin: „Albuquerque".** Eintrag
   `11:30:00-05:00`. Albuquerque war im September **MDT, UTC−06:00**.
   11:30 Austin = **10:30 Albuquerque**. Verabredet war mit ihm
   **10–12 lokale Zeit**. Der Termin lief also 10:30–12:30 lokal — eine halbe
   Stunde hinter dem Fenster. Wäre 10:00 lokal gemeint gewesen, müsste der
   Eintrag `2026-09-18T11:00:00-06:00` lauten (= 12:00 Austin).

**Gegen das letzte Wochendokument gehalten.** Am 28.09. habe ich geschrieben:
*„Zeitzonen auf dem September-Roadtrip geprüft — alle drei stimmen: Strassman
10:30 Albuquerque (Mountain), Joe Moore 10:00 Boulder (Mountain), Matt Defina
08:00 Austin (Central). Kein Central/Mountain-Fehler."* Daran sind zwei Dinge
zu berichtigen:

- **Ich habe nur drei Termine geprüft und Phoenix nicht darunter.** Ian Gardner
  am 17.09. war der einzige Fremdzonen-Termin mit **zwei** Stunden Abstand und
  stand in der Prüfung überhaupt nicht drin.
- **„Matt Defina 08:00 Austin (Central)" ist falsch gerechnet.** `14:00Z` minus
  fünf ist **09:00** Austin, nicht 08:00 — 08:00 wäre die Mountain-Lesart. Der
  Termin selbst steht richtig (09:00–11:00 −05:00, Studio in Austin); nur meine
  Umrechnung war um eine Stunde daneben. Am Befund „kein Central/Mountain-
  Fehler bei Defina" ändert das nichts.

**Boulder: kein Beleg.** Kein September-Termin trägt Boulder oder Colorado als
Ort. Whitney Wheelock steht in der Databank unter *Colorado*, der Kalendereintrag
vom 27.09. hat aber **gar keinen Ort** — die Zone ist daraus nicht prüfbar.
Ich behaupte nicht, dass das Boulder war.

**Und die Gegenprobe, die die Vermutung halbiert:** Matt Defina (Databank
*Colorado*) und Ken Stern (DC) wurden **beide in Austin aufgenommen** —
`Just Push Record Studios, 908 East 5th Street #114C, Austin, TX 78702`.
Bei beiden ist Central also richtig.

→ **Regel:** `Location` in der Databank ist der **Wohnort des Gastes**, nicht
die Zone der Aufnahme. Als Zeitzonen-Prüfung ist das Feld unbrauchbar. Es zählt
das `location`-Feld des Kalendertermins.

### 1c) Wer angeschrieben wurde, braucht eine Zeile

**24 Namen haben in der Databank einen Kontakt-Status, aber keine
`### `-Überschrift im Outreach-Doc:**

Amy May (Confirmed) · Amy Nelson (Confirmed) · Bridget Woods (Recorded) ·
Chris Taylor / Red Fridge Society (In Conversation) · Craig Makhosi (Recorded) ·
Dean Karnazes (Reached Out) · Drew Birch (Confirmed) · Francisco Medina
(Reached Out) · Jack Kornfield (Follow-up) · Jamie Elkon (Confirmed) ·
Jim Collins (Follow-up) · Kyle Buller (Reached Out) · Logan Gonzalez (Recorded) ·
Maverick Maltin (Reached Out) · Megan de Beyer (Confirmed) · Mikhaila Peterson
(Follow-up) · Nathan Maingard (Recorded) · Staffan Taylor (Reached Out) ·
Steve Adler (Reached Out) · T.D. Jakes (Reached Out) · TD / Yes Theory
(Reached Out) · Timothy Olson (Follow-up) · Tommy Caldwell (Follow-up) ·
Whitney Wheelock (Recorded).

### 1d) Fünf fertige Pitches, zu denen ich keine Mail finde

Diese Namen haben einen **ausgearbeiteten Pitch-Text im Doc**, aber weder eine
Databank-Zeile noch einen Mail-Thread unter dem Namen
(`in:anywhere`, inkl. Trash):

**Elliott Bisnow · Joe Lonsdale · John Wineland · Mark Kaplan · Stephen West.**

Fertige Arbeit, die nie rausgegangen ist. Das ist eine Beobachtung, keine
Aufforderung — ich weiß nicht, ob er sie zurückgehalten hat.

### 1e) Drei Outreaches ohne Databank-Zeile — belegt durch Mails

1. **Marc Gafni.** Doc-Überschrift „Dr. Mark Gafni" — richtig ist **Marc**
   (`drmarcgafni@gmail.com`, `marc@centerforintegralwisdom.org`). Kontakt lief
   **über Kyle Kingsbury**. Seine Antwort 21.08.: *„Let's do it Yannick! A friend
   of Kyle's is a friend of mine. I am copying Suzette who will set us up."*
   Dann Suzette am 26.08.: *„Marc lives in Vermont so as much as he would like to,
   doing an in-person session in Austin would not be possible."* Yannicks letzte
   Mail 26.08.: *„let's just wait for when the timing aligns."*
   → Ein Thread, der bis zur Terminsuche kam und an **in-person** scheiterte.
   Keine Databank-Zeile.
2. **MJ DeMarco.** Pitch raus 18.08. 20:54 an `mjdemarco@viperionpublishing.com`,
   `mj@viperionpublishing.com`, bcc `mj.demarco@yahoo.com`. Keine Antwort.
   Keine Databank-Zeile.
3. **Codie Sanchez.** Pitch raus 18.08. 19:28 an `codie@contrarianthinking.co`;
   zweiter Anlauf 19:41 **über Danny Miranda** an `lindsey@contrarianthink.com`.
   Autoantwort von `codie.sanchez@gmail.com`, Betreff „No response Re: …":
   *„Sorry, this email doesn't get checked. SO if you want to catch me, subscribe
   to Contrarian Thinking (see what I did there) and hit me up in the comments
   section on any social platform."*
   → Die Adresse ist tot. Ein weiterer Mail-Anlauf ist verbrannte Zeit.
   Keine Databank-Zeile.

### 1f) Sechs Namen, die in beiden Quellen anders geschrieben sind

Deshalb lassen sich Doc und Databank nicht maschinell abgleichen:

| Outreach-Doc | Databank | Richtig |
|---|---|---|
| Aubert Bastiat | Aubert Batistat | **Doc** — `aubert@aubertbastiat.com` |
| Blake Mykosy | Blake Mycoskie | **Databank** (TOMS-Gründer) |
| David Perrel | David Perell | **Databank** |
| Dr. Dan Amen | Dr. Daniel Amen | Databank |
| Ian Garden | Ian Gardner | **Databank** |
| Thomas Barg | Thomas Brag | **Databank** (Yes Theory) |
| Dr. Mark Gafni | *(keine Zeile)* | **Marc** Gafni — beide falsch |

Dazu: die Databank-Zeile **„Paul" (Reached Out)** ist mit hoher
Wahrscheinlichkeit **Paul Austin** (Third Wave) — das Doc hat eine
`### Paul Austin`-Überschrift. **Das ist meine Vermutung, nicht belegt.**

### 1g) Was ich nicht angefasst habe

- Die drei **Brendan-Kane-Nahduplikate**, die **Christian-Angermayer-Dreifachzeile**,
  die **Andy-Frisella-Doppelzeile**, die beiden **David-Nutt-** und
  **Stanislav-Grof-Zeilen** und die zwei Zeilen mit
  `[DUPLICATE – delete, merged]` (Sarinia Bryant, Walter Isaacson).
  **Nichts gelöscht, nichts zusammengeführt** — das ist seine Entscheidung.
- **Kein Datum erfunden.**

---

## TEIL 2 — SENT-MAIL-PATTERN, 27.09.–05.10.

`in:sent newer_than:8d` → `resultCountEstimate: 9`. Alle neun Threads, die ER
geschrieben hat, vollständig gelesen (Aubert nur MINIMAL — 27 MB Anhänge).

### Die zwei Befunde über die Woche selbst

1. **Kein einziger neuer Cold Pitch.** Alle neun sind Follow-ups in bestehenden
   Threads. Zwischen 27.09. und 05.10. ist keine neue Erstansprache rausgegangen.
2. **Alle neun auf Englisch.** Diese Woche ist **keine deutsche Mail**
   rausgegangen — `voice/german-register.md` bekommt deshalb keine neue Regel.
   Das Fehlen ist der Befund, nicht eine Lücke in meiner Prüfung.

Dazu die Verteilung: **neun Mails am 01.10. zwischen 12:30 und 15:xx**, danach
fast nichts. Die Woche hatte einen Schreibtag, nicht sieben.

### Der Widerspruch — in seinen eigenen Worten, zwei Tage auseinander

- **01.10., an Enfold (Steve Rio & Austin):** *„I'm now omw back in Germany to
  get my rehab done and it'll be a while before I'm back in ATX, or in North
  America at all"*
- **03.10., an Ken Stern:** *„I'm now heading back to South Africa earlier than
  planned to do my rehab over there"*

Zwei Ziele, zwei Tage auseinander, beide von ihm selbst geschrieben. **Ich löse
das nicht auf** — ich stelle es hin. Für alles, was von „wo ist er ab wann" abhängt
(Gäste, Studios, Reisekosten), ist das die offene Frage der Woche.

### Media Pouch — meine eigene Rahmung war falsch

Ich habe das bisher als „Frist bei Ryan" geführt. Ryans Mail vom 30.09. sagt
genauer: *„Recovery within 30 days of the session is available at our standard
$250 recovery fee, and not guaranteed. Your 09/11 session is still within that
window, so if you'd like me to attempt recovery, let me know and I'll send an
invoice."*
Yannicks Antwort vom 02.10. 13:00 hat **um Nachsicht beim Honorar gebeten und
die Recovery nicht beauftragt.** Also: das Fenster schließt am **11.10.**, und
in Auftrag gegeben ist nichts. Nicht „Frist", sondern „nicht beauftragt".

### Weitere Funde aus den neun Threads

- Er hat **https://chriswillx.netlify.app/** für Chris Williamson gebaut und ein
  CMS angeboten.
- Beim Montagsshow war er **auf Krücken** und hat mit Gabby gesprochen —
  *„the door's still open"*.
- **Brendan Kane** nennt er wieder *„my next podcast guest"*.
- **Zac vom ATX Writing Club ist Zac Solomon** (Namensgleichheit mit dem
  Luma-Handle `zacsolomon`); die Databank hat ihn als *Zac Solomon ·
  In Conversation · Austin* — **die Zuordnung ist damit bestätigt.**
- Die **ATX-Mitgliedschafts-Rückerstattung** vom 01.10. ist offen, begründet mit
  Arztrechnungen; Zac ist bis **13.10.** weg.

---

## TEIL 3 — WOCHENDOKUMENT IN DRIVE

**Neu angelegt, nichts überschrieben, nichts in den Papierkorb:**

- Titel: **„Alfred — Actuals Log · Woche 28. Sep – 4. Okt 2026"**
- Ordner: `YNB x Claude` (`1ioemsCTuhs-mdrRMdEWC1CHFzQCdI9dq`)
- `fileId` `1aRQSMZDewf0pzD2sT8f3aAwRQ2_y0so_vjOgppJzAj8`
- https://docs.google.com/document/d/1aRQSMZDewf0pzD2sT8f3aAwRQ2_y0so_vjOgppJzAj8/edit

**Vorher geprüft**, dass es kein Dokument dieser Woche schon gibt: der Ordner
enthielt sechs Wochendigests, das jüngste war
*„Alfred — Actuals Log · Woche 21.–27. September 2026"*.

`create_file` hat wie immer `fileSize: 1` gemeldet. **Zurückgelesen** — der
vollständige Text ist drin, alle Abschnitte. Die Regel aus
`actuals/README.md` hat zum siebten Mal gegriffen: `fileSize: 1` heißt nicht,
dass der Schreibvorgang gescheitert ist.

---

## TEIL 4 — BOARD

Vier Änderungen, eine davon eine Korrektur an einer stehenden Board-Aussage:

1. **Neue Zeile `wochenabgleich-0510`** oben in *Still open* — die sieben
   Befunde aus Teil 1, die beiden Selbstkorrekturen und die Drive-Grenze.
2. **Punkt 6 im Right-now-Block korrigiert.** Dort stand *„So 11.10. — die
   Frist bei Ryan, 250 $ … der Ball liegt bei ihm."* Das war ungenau. Richtig:
   Ryan hat am 30.09. 17:00 um eine Freigabe gebeten
   (*„if you'd like me to attempt recovery, let me know and I'll send an
   invoice"*); Yannicks Antwort vom 02.10. 13:00 bittet um Nachsicht beim
   Honorar (*„Is there any chance you might be able to help me out on the
   recovery this one time?"*, *„hoping for a little grace…"*) und bestätigt den
   Auftrag nicht. **Die Wiederherstellung ist nicht beauftragt**, und seit
   30.09. 17:00 ist von Ryan keine Antwort und keine Rechnung gekommen.
   Die Leadzeile entsprechend von „Frist bei Ryan" auf „30-Tage-Fenster bei
   Ryan — nicht beauftragt" geändert.
3. **Zeile `abreise-widerspruch` ergänzt** um das Paar 01.10. (Deutschland, an
   Enfold) / 03.10. (Südafrika, an Ken Stern).
4. **Altersangabe derselben Zeile korrigiert**: sie stand seit dem 17.09. auf
   `heute` mit der Klasse `hot` — jetzt `17.09.–03.10.`. Eine stehengebliebene
   Altersangabe ist eine falsche Aussage wie jede andere.

`var SWEPT` auf `2026-10-05T08:45:00-05:00`.

---

## WAS DIESER DURCHGANG NICHT KONNTE

- **Das Outreach-Doc beschreiben.** Siehe 1a. Der Drive-Connector kann an einer
  bestehenden Datei nur Titel und Ordner ändern.
- **Den Aubert-Thread vollständig lesen** (`19e9290f4ebc35d1`, letzte Nachricht
  `1a0f8b81f9c62d1c`) — 27 MB Anhänge, nur MINIMAL gelesen. Die Namensfrage ist
  trotzdem geklärt: `aubert@aubertbastiat.com`.
- **Die Zone des Wheelock-Termins vom 27.09. bestimmen** — der Kalendereintrag
  hat kein Ortsfeld.
