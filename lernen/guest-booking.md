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

- **„Not Started" in der Databank beweist nicht, dass nichts rausgegangen ist.**
  Beim Abgleich seines Outreach-Docs (87 Pitches) gegen die Databank stand
  **Matthew McConaughey auf *Not Started* nach sechs gesendeten Mails** (vier
  Bounces, zwei zugestellt am 15.08.), **yung pueblo auf *Not Started* nach
  zwei**. Mein Abgleich lief zuerst nur gegen die aktiven Status und hat beide
  als „fehlende Zeile" gemeldet, obwohl sie existieren.
  **Regel: ein Status-Abgleich schließt `Not Started` mit ein**, sonst meldet er
  Lücken, die keine sind, und übersieht die Fehler, die es gibt.
  → betrifft: alfred, head-of-content

- **Fünf gesendete Pitches haben gar keine Databank-Zeile** — Dr. Mark Gafni
  (gesendet und **binnen eines Tages persönlich beantwortet**), John Wineland,
  Codie Sanchez, MJ DeMarco, Alon Matar. Und **eine Zeile heißt nur „Paul"**,
  gemeint ist Paul Austin (The Third Wave) — wer nach dem Nachnamen sucht,
  findet sie nie.
  **Das Outreach-Doc in Drive ist damit eine eigene Quelle über seine Pipeline,
  nicht eine Kopie der Databank.** Beim Zählen gehört es dazu.
  → betrifft: alfred, head-of-content

- **Sein Betreff-Trick, von ihm am 21.10. ausgesprochen:** *„wenn ich Personen
  kenne, die irgendwie mit meinem Prospect connected sind, dann mache ich so in
  eckigen Klammern via Scott Aronson … das erhöht die Chance deutlich, dass die
  Personen auch reagieren."* Gemessen über alle 111 Fäden liegt `[Via <Name>]`
  bei 3 von 12 (25 %) und der nackte Podcastname bei 10 von 17 (59 %) — die
  Zahlen sind mit der Temperatur des Kontakts konfundiert und widerlegen ihn
  nicht. **Seine Ansage schlägt meine Quote; beides nebeneinander nennen.**
  → betrifft: alle

- **Seine Ortsrecherche ist eine Google-Frage, und er hat sie mir gesagt:**
  *„Ich gebe oft bei Google ein, Scott Aronson, where does he live?"* Für Ilya
  Sutskever ergibt das **Palo Alto** (Sitz von Safe Superintelligence, zweites
  Büro Tel Aviv). **Firmensitz, nicht Wohnadresse** — nach einer privaten
  Adresse wird nicht gesucht, und für „in-person only" reicht der Firmensitz.
  → betrifft: alle

- **Ein Kalenderblock mit einem Gastnamen ist nicht automatisch eine Aufnahme.**
  Von ihm am 21.10. über Bridget Woods: *„Bridget ist auch eine persönliche
  Freundin von mir. Deshalb wirst du die wahrscheinlich im Kalender noch öfter
  mal sehen."* Ich hatte den zweistündigen Block „Bridget" am Sa 24.10. als
  mögliche Aufnahme hingestellt. **Die Person war richtig, die Sache falsch.**
  Dazu: ihre Folge ist aufgenommen, aber *„die Audio absolut katastrophal …
  vermutlich eher nicht"* veröffentlichen — an diese Zeile gehört keine
  Veröffentlichungsmarke.
  → betrifft: alfred, youtube-manager, head-of-content

## 2026-10-22

- **Seine Signatur endet bei `Dreaming Big,` — Name und Firma stehen in Gmail.**
  Wörtlich am 21.10.: *„meine Unterschrift Dreaming Big, die sollte eigentlich
  da enden und mein Name und die das Business das habe ich ja in meiner Signatur
  in Gmail."* **Damit ist die Handbuchregel von 27.08. überholt** („full name
  plus YNB Ventures LLC if they don't know him"). Wer den Block in einen Entwurf
  schreibt, erzeugt ihn doppelt. Das kurze `YNB` in Antworten an Lieferanten
  bleibt davon unberührt.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Fünf Bullet Points, immer.** *„dass ich immer 5 Bullet Points mache.
  Dahinter steckt neuropsychologische Muster."* Meine Fassung hatte vier. Nicht
  kürzen, weil eine Liste lang wirkt.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Eine Aufzählung wird pro Empfänger ausgewählt, und ein Bekannter wird nicht
  erklärt.** Für Ilya Sutskever: Scott Aaronson nicht als „former OpenAI safety
  researcher" (*„weil Ilya Scott kennt. Das ist irgendwie so ein bisschen
  dumm."*), sondern als **„our mutual connection"** — dieselbe Form wie *„our
  mutual friend, my mentor and living legend Rob Paddock"* in seinem eigenen
  Brendan-Kane-Pitch. **Der Twist erklärt den Menschen für Fremde und die
  Beziehung für Bekannte.** Dazu: Namen aus dem Feld des Empfängers wählen
  (Strassman als Professor rein, Rob Bennett und Whitney Wheelock raus),
  statt die Liste aus dem Outreach-Doc zu kopieren.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Der Reisebogen im Betreff ist Absicht, nicht Gewohnheit:** *„from South
  Africa to San Francisco … Das nutze ich immer, um eine gewisse globale
  Reichweite darzustellen."* Meine Auswertung hatte dieses Muster als das
  schwächste gemessen (6/37 = 16 % gegen 10/17 = 59 % beim nackten
  Podcastnamen). **Die Zahl widerlegt ihn nicht** — sie ist mit der Temperatur
  des Kontakts konfundiert, und genau so stand es auch in der Auswertung.
  **Eine Quote, die nicht nach Kontakttemperatur geschichtet ist, taugt nicht
  als Einwand gegen eine Absicht.**
  → betrifft: alfred, head-of-content
- **Ein Entwurf im Repo ist nicht seine Stimme — auch wenn er nach ihm klingt.**
  Ich habe Rick Strassman als *„DMT researcher, UNM professor and author of The
  Spirit Molecule"* in einen Pitch geschrieben. Seine Korrektur: *„du hast die
  Beschreibung geändert. So habe ich es Rick Strassman nie vorgestellt"* — er
  sagt **„the world's leading DMT and consciousness researcher, Professor Rick
  Strassman"**. Meine Fassung kam aus `drafts/2026-10-18-mushroom-cowboy.md`,
  einem **Agenten-Entwurf, den er nie gesendet hat**. Gegenprobe danach: im
  Outreach-Doc hat Strassman **keine** Roster-Zeile, und „consciousness
  researcher" kommt im ganzen Doc nicht vor.
  **Belegte Formulierungen stehen in gesendeten Mails und im Outreach-Doc.
  Repo-Entwürfe sind Herleitungen von uns und dürfen nie als seine Sprache
  weiterverwendet werden** — das ist die Regel vom 09.09. eine Ebene tiefer.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **`(upcoming)` am Gastnamen ist eine Aussage über den Sendezeitpunkt, keine
  Eigenschaft des Gastes.** *„nimm dieses Upcoming aus … die Nachricht wird
  rausgehen, wenn alle Podcasts veröffentlicht sind."* Wer die Marke aus dem
  Outreach-Doc mitkopiert, datiert die Mail unbemerkt. Vor jedem Pitch den
  geplanten Versand gegen die Veröffentlichungsmarken im Geschäftskalender
  halten (Aaronson So 25.10., Strassman Fr 13.11., Goodell Fr 04.12.).
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Bei einem Auftrag ohne Uhr wird für den Zustand gebaut, in dem er rausgeht
  — nicht für heute.** *„das jetzt nur als Testdurchlauf … die Nachricht wird
  dieses Jahr nicht mehr rausgehen."* Dadurch fielen drei Fragen weg, die ich
  ihm vorgelegt hatte (Unfall erwähnen, MRT abwarten, Jahreszahl 2027). **Einmal
  nach dem Zeitpunkt fragen, bevor Einschränkungen in einen Text kommen, die nur
  heute gelten.**
  → betrifft: alle
- **Ein sechstes Register, das in keinem Voice-Dokument stand: die warme DM an
  einen Peer.** Am 22.10. über einen Screenshot seiner eigenen Nachricht an Jon
  Savage sichtbar geworden — gelaufen über Instagram/WhatsApp, **im Postfach
  steht dazu nichts**. Aufbau: `Howdy <Name>,` · Vermittler als erster Satz ·
  `Quick intro:` als eigene Zeile · der Aufhänger in einer Zeile mit
  Ethos-Spiegel · die Reise als Rahmen für die Gästeliste · **`AND:`-Zeile** ·
  Unfall als ein Satz · **Kaffee statt Mikrofon** als Bitte · `Dreaming Big,`.
  **Was ich daraus mitnehme und was auch für andere gilt: sein Betrieb läuft
  über Kanäle, die wir nicht lesen, und die Register, die dort entstehen,
  fehlen in unseren Dateien, bis er sie zeigt.**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Der Motorradunfall ist für ihn Material, nicht Tabu.** In derselben
  Nachricht: *„On top of that, I survived a motorcycle accident 3 weeks ago…
  just landed back in SA on Friday night in one piece."* Ein Satz, kein zweiter
  Satz Rechtfertigung, und das gegenüber jemandem, den er nicht kennt. **Die
  Regel „nicht nachfragen, nichts ableiten" gilt weiter für uns** — aber ihm zu
  raten, ihn aus einem Text zu lassen, war meine Vorsicht, nicht seine.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Die `AND:`-Zeile schlägt die `(upcoming)`-Klammer.** Marian Goodell steht
  in seiner DM nicht in der Bullet-Liste, sondern als eigener Satz darunter —
  und als **Einladung ins BMHQ**, nicht als Folge. Dadurch altert die Zeile
  nicht, egal wann die Folge erscheint. **Seine Lösung, besser als meine.**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Wenn eine ausgesprochene Regel und ein gefundener Text sich widersprechen,
  zuerst beide datieren.** Seine DM hat **sieben** Bullets, seine Ansage vom
  21.10. sagt **fünf**. Die DM sagt *„3 weeks ago"* und *„landed back in SA on
  Friday night"*, ist also um den 10.10. geschrieben — **älter als die Ansage,
  also gilt die Ansage.** Ohne Datierung wäre daraus „Praxis schlägt Regel"
  geworden, und das wäre hier falsch gewesen.
  **Dazu: eine Zeitangabe aus einem fremden Text wird nie übernommen** —
  „3 weeks ago" war am 10.10. richtig und ist heute falsch.
  → betrifft: alle
- **„A motorcycle accident", nie „I came off a motorcycle".** *„das hört sich
  viel zu undramatisch an."* Belegt in drei seiner eigenen Mails (an Ryan
  24.09., an Joe Moore 21.09., in der DM an Jon Savage). **Verharmlosen ist
  genauso eine Abweichung von seiner Stimme wie Übertreiben.** Derselbe Fehler
  stand in einem zweiten, ungesendeten Entwurf und ist dort mitkorrigiert —
  **eine als falsch erkannte Formulierung wird über alle liegenden Entwürfe
  gegrept**, denn ein ungesendeter Entwurf wird irgendwann gesendet.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Die Form des neuen Textes bestimmt die Regeln, nicht die Form der Vorlage.**
  Ich hatte in eine Mail `Howdy Jon,` als erste Zeile gesetzt, weil **seine
  eigene DM** so anfängt. Seine Korrektur: *„eine E-Mail, die mit Hi Howdy,
  Hello anfängt, hat ungefähr 90-prozentige schlechtere Erfolgsquote … Warum
  nimmst du das jetzt plötzlich weg?"* Beat 1 ist der Cold Open **ohne Anrede**,
  so machen es alle 87 Pitches im Outreach-Doc. **In einer DM ist man schon im
  Gespräch, in einer Mail an einen Fremden noch nicht.** Wer aus einer DM eine
  Mail baut, übernimmt den Inhalt und nicht den Aufbau.
  **Und: wenn wir bewusst von einer seiner Regeln abweichen, gehört die
  Abweichung in den Entwurfskopf** — sonst ist es kein Vorschlag, sondern ein
  stiller Regelbruch.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Woran „zu wenig Tiefe" bei ihm konkret liegt**, dreimal nachvollzogen an
  einem Entwurf, den er genau so beanstandet hat:
  1. **Die beste Anekdote ist nicht der beste Mensch.** Mein Cold Open sass auf
     den zwei Millionen Rand, die Jon Savage zurückzahlte. Stärker ist seine
     *Heartbreak-Chart* — ein Mann plottet seine Niederlagen, weil die
     Erfolgskurve zu dünn zum Hinsehen war. **Beat 1 sucht die Stelle, an der
     der Mensch sichtbar wird, nicht das beeindruckendste Ereignis.**
  2. **Ohne Geständnis keine Tiefe.** Beat 3 hatte eine Parallele statt etwas,
     das ihn kostet. Das Geständnis ist der Motor seiner Essays und fehlt in
     einem Pitch genauso auffällig.
  3. **Eine der Fragen muss den Preis berühren**, nicht die Methode.
  **Prüfung vor der Übergabe: steht ein Satz drin, der ihn etwas kostet, und
  eine Frage, die den Preis des anderen berührt?**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Ein Satz aus seinem Archiv trägt die Lage mit, in der er stand.** Ich hatte
  in einen Erstkontakt *„I like to meet people properly before we ever switch a
  mic on"* geschrieben — hergeleitet aus seiner Mail an Scott Aaronson vom
  04.08. (*„One thing I like to do before every podcast: grab a quick coffee in
  person"*). **Nur hatte Scott da längst zugesagt**: das ist eine Logistikzeile
  an einen gebuchten Gast. Seine Reaktion: *„Was ist das für ein Bullshit,
  Alter? Wo hast du diese Formulierung gesehen?"*
  **Vor jeder Übernahme zwei Fragen: an wen ging der Satz, und in welchem
  Stadium?** Und: **wo sein Text für genau diesen Empfänger existiert, wird er
  übernommen, nicht verbessert** — seine eigene DM an Jon hatte den Schlusssatz
  bereits, und ich hatte ihn durch meinen ersetzt.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Über eine Beziehung, die es noch nicht gibt, wird nichts behauptet.** Mein
  *„He was right"* über den Vermittler: *„wie kann ich sagen, dass er recht
  hatte, wenn ich noch gar nicht mit Jon zusammengekommen bin?"* Zulässig ist
  nicht die Bestätigung, sondern **die eigene Hälfte** — warum der Absender
  glaubt, dass der Vermittler das gesagt hat.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Jeder Satz muss etwas tun, nicht nur stimmen.** *„I had a motorcycle
  accident in Colorado and flew home to the Mother City to start my rehab"* —
  beide Tatsachen richtig, der Satz trotzdem funktionslos (*„Das ist so, hä?
  Was soll der kommunizieren?"*). Mit der Verknüpfung **unterbrochen → deshalb
  zu Hause → deshalb jetzt möglich** trägt dieselbe Information die Bitte, die
  danach kommt.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Eine nicht erreichbare Website beendet die Recherche nicht.** Ich hatte
  einen Pitch auf einem TEDx-Talk von **2014** gebaut und zur Gegenwart nur
  notiert, dass `jonsavage.com`/`.co.za` und `instagram.com` von hier
  `ENOTFOUND` sind. Eine einzige Websuche ergab dann: **Africa Podcast Network**
  (Gründer), **InBroadcasting** (CEO), **AMPD Studios** (Mitgründer), Bühnen
  bei **Podcast Movement** (USA) und **The Podcast Show** (London). **Erst
  damit wurde der richtige Spiegel sichtbar** — Yannicks Redaktionslinie
  Europa–Afrika–Amerika gegen einen Mann, der Afrika in diese Räume trägt.
  **Und: bevor ein Spiegel aus Yannicks Biografie gebaut wird, muss belegt
  sein, dass das Thema beim Empfänger überhaupt vorkommt** — seine Korrektur:
  *„die Vipassana macht bei ihm gar keinen Sinn, du siehst doch gar keine
  spirituelle Referenz in seiner Story."*
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Bevor ich recherchiere, lese ich seine eigenen Felder zu dem Menschen.**
  Ich habe den Jon-Savage-Auftrag behandelt, als käme er von Null, habe
  Instagram und zwei Websites angelaufen, und am Ende in meinem Entwurf eine
  Einschränkung notiert: dass der Podcast-Mann und der TEDx-Filmemacher
  derselbe seien, sei **meine Schlussfolgerung**, nirgends ausgeschrieben.
  **Es stand ausgeschrieben, bei ihm.** Die Databank-Zeile „Jon Savage" trägt
  seit **01.07.2026** im Feld *Platform* vier Kanäle, darunter
  `africapodcastnetwork.com` und `x.com/jonsavagerocks` — von ihm eingetragen,
  vier Monate vor der Vermittlung. Dazu ein Vorbereitungsdoc in Drive vom
  **02.08.** mit seinem Arbeitstitel **„The Podcast Genius"**. **Drei Felder
  lesen hätte eine Websuche und eine falsche Einschränkung gespart.**
  → betrifft: alle, die für ihn recherchieren
- **Ein leerer Gmail-Entwurf ist eine Quelle.** Zu Jon lag seit **16.10.** ein
  Entwurf im Postfach: Körper leer, kein Empfänger, aber **Betreff gesetzt** —
  `[Via Denver Burgess] Man's Search for Meaning`. Daraus kommen zwei Dinge,
  die ich sonst geraten hätte: **der Nachname des Vermittlers** (Burgess), und
  **seine Betreff-Wahl für diesen Fall** — voller Nachname in der Klammer, und
  der nackte Podcastname **ohne** Reisebogen, weil beide in derselben Stadt
  sind. Die Betreff-Suche in `in:drafts` gehört damit neben `in:sent`.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **„Teilweise angepasst" heißt nicht, dass der Text irgendwo liegt.** Seine
  angepasste Fassung war weder in diesem Chat noch in den 18 Gmail-Entwürfen,
  im Outreach-Doc (letzte Änderung 21.10.), in den Drive-Dateien von heute, im
  Alfred-Inbox-Ordner oder in Notion. **Erst suchen, dann fragen** — die Suche
  hat hier mehr gefunden als die Frage gekostet hätte; aber ohne seinen Text
  gibt es keine Analyse, und das sage ich in einer Zeile statt zu raten.
  → betrifft: alle Agenten
- **Seine Ortsrecherche hat zwei Schritte, ich kannte nur den ersten.** Am
  21.10. hatte er gesagt: *„Ich gebe oft bei Google ein, Scott Aronson, where
  does he live?"* Am 26.10. kam der Rest: *„Und dann gucke ich gegebenenfalls
  bei LinkedIn und oder bei Twitter, weil da oft auch die Locations stehen."*
  **Ich war bei Jon Savage und bei Craig Mundie nach Schritt 1 stehen
  geblieben** und habe das Ortsfeld leer gelassen; bei Mundie hat er die
  Antwort dann selbst geliefert (Seattle, Washington). **Wichtig für alle:
  `linkedin.com`, `x.com` und `instagram.com` sind aus dem Container gesperrt**
  — Schritt 2 geht nur über ihn. Dann aber als konkrete Bitte („schau bei
  LinkedIn"), nicht als Leerstelle im Feld.
  → betrifft: alle, die für ihn recherchieren
- **Ein fehlender Wert und ein fehlender Feldtyp sind zwei verschiedene
  Blockaden.** Bei Craig Mundie war erst der Ort unbekannt; als er ihn
  lieferte, stellte sich heraus, dass die `Location`-Auswahlliste **kein
  „Washington" als Bundesstaat** kennt — nur „Washington DC", also die
  Hauptstadt. Einen Wert eintragen ist Routine; **eine Option anlegen ändert
  die Struktur seiner Datenbank** und wird vorgelegt. Notion lehnt einen
  unbekannten Select-Wert von sich aus ab, legt ihn also nicht still an.
  → betrifft: alle, die an der Databank arbeiten
- **Vor einem Pitch wird der Faden des Vermittlers gelesen, nicht nur die
  Databank-Zeile.** Beim Boyd-Varty-Auftrag lagen vier Empfehler auf dem Tisch,
  einer davon Cal Callahan. Im Postfach steht aber, dass Yannick Cal am
  **01.09.2026** genau darum gebeten hat — *„any chance you could also connect
  me with Boyd?"* — und am **08.09.** zurückrudert: *„all good on Boyd, I get
  it. No stress at all, whenever the timing feels right."* **Cal hat nicht
  vermittelt.** Hätte ich nur die Databank gelesen (dort steht Cal als „der
  produktivste Referrer im ganzen Netzwerk"), wäre `[Via Cal Callahan]` in den
  Betreff gewandert — eine Empfehlung behauptet, die ausdrücklich nicht gegeben
  wurde. **Regel: bevor ein Name in die eckige Klammer kommt, wird der Faden mit
  diesem Menschen gelesen, ganz, mit `get_thread`.**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Sein Postfach enthält die Begeisterung, die ein Pitch braucht — datiert und
  wörtlich.** Zu Boyd lag seit 08.09. in einer Mail an Cal: *„listened to your
  episode with Greg, Chase and Boyd… I swear I felt like I was right there in
  the bush with you guys… Ordered Boyd's book right away."* Dazu seine eigene
  Lage aus dem 20.08.-Pitch: *„that's exactly what brought me to the US on the
  last of my savings, all-in on this podcast."* **Beides ist belegtes Material
  für Beat 3 und muss nicht erfunden werden.** `in:sent` ist die Quelle für sein
  Geständnis, nicht nur für seinen Ton.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Zwei von ihm überarbeitete Pitches nebeneinander ergeben mehr als zehn
  Einzelkorrekturen.** Jon Savage (raus 22.10.) und Boyd Varty (seine Fassung
  26.10.), beide an Südafrikaner, vier Tage auseinander. Unangetastet blieben
  in beiden Fällen **Cold Open, Anrede, Fragenblock und Beat 6**. Geändert hat
  er jedes Mal **die Gästeliste** — und zwar nicht nach dem Feld des
  Empfängers, sondern nach dessen Maßstab: der Podcast-Unternehmer bekam eine
  rein amerikanische Liste (Reichweite), der Wildnis- und Männerarbeiter eine
  südafrikanisch grundierte (Verwandtschaft). **Rolle vor Name, durchgehend.**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Der Vermittler steht zuletzt, mit „and of course", und wird nicht
  erklärt.** *„and of course our mutual connection, Professor Scott Aaronson"*
  (Ilya) und *„and of course living legend Rob Paddock"* (Boyd) — bei Rob ohne
  IronMan und ohne $100M, obwohl beides sonst seine Standardzeile ist. Zweimal
  belegt, damit Regel.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Die Einleitung über der Gästeliste ist eine Tatsachenbehauptung.** Ich
  hatte *„I just got back from that trip with some wyld characters in the
  bag"* über eine Liste gesetzt, in der drei Namen nicht von dieser Reise
  waren. Er hat es gefangen: *„I've already had some wyld characters on."*
  **Erst die Liste bauen, dann den Satz darüber prüfen.**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Er trackt seine Cold Pitches.** Der Link in der gesendeten Jon-Savage-Mail
  läuft über `streak-link.com`. **Er sieht Öffnungen und Klicks, wir nicht.**
  Über die Wirkung einer Anfrage wird nicht spekuliert; das ist eine Frage an
  ihn.
  → betrifft: alle Agenten
- **Eine Zusage kann an einem Vertrag sterben, nicht am Interesse.** Brendan
  Kane hat am 09.07. zugesagt und am 28.10. bestätigt — aber inzwischen die
  Firma verlassen und ein **Wettbewerbsverbot für Social Media**. Damit ist
  genau das Thema weg, auf dem der Pitch stand (*„the untold stories behind
  building the most famous people alive"*). **Vor jedem Nachfassen nach langer
  Pause prüfen, ob die Grundlage des Pitches überhaupt noch existiert** — die
  Firmenadresse antwortete bereits mit *„Hook Point is winding down its
  business."*
  → betrifft: alle, die Entwürfe für ihn schreiben
- **„Let me give it some thought" heißt: nicht schreiben.** Wenn der Ball beim
  Empfänger liegt, ist der nächste Entwurf kein Fortschritt, sondern Druck.
  Und **kein Thema vorschlagen, solange kein Satz des Empfängers eines
  belegt** — er hat selbst gesagt, dass er noch sucht.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Zwei Schreibweisen desselben Namens ergeben zwei Zeilen.** In der Databank
  stehen „Brendan Kane" (Reached Out, der echte Faden) und „Brandon Kane"
  (California, Not Started, leer). Dieselbe Verwechslung stand in Yannicks
  Auftrag vom 27.10. **Beim Anlegen einer Zeile gegen Namensvarianten prüfen,
  nicht nur gegen die exakte Schreibweise.**
  → betrifft: alle, die an der Databank arbeiten
- **Zwei echte Sätze von ihm zu einem dritten zu verschmelzen ist erfinden.**
  Ich hatte den Treffen-Satz aus der Scott-Mail (*„grab a quick coffee in
  person"*) mit dem Schluss aus der Sutcliffe-Mail kombiniert. Er hat sofort
  gefragt: *„habe ich das wirklich genauso geschrieben?"* **Der kanonische Satz
  ist der aus der Sutcliffe-Mail vom 15.08., wörtlich.**
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Verbotsliste, von ihm am 29.10.:** „because that's the other thing",
  „no rush at all", „whatever you land on". Dazu: **er ist nie indifferent** —
  ein offenes Thema heißt bei ihm „ich sage Dir meine Gedanken persönlich",
  nicht „mir egal". Und **sein Wort für Kaffee ist „Black Gold"**.
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Jede Mail braucht einen CTA mit konkretem Fenster**, auf den man mit einem
  Tag antworten kann: *„What works for you in the week of the 9th–13th?"*
  → betrifft: alle, die Entwürfe für ihn schreiben
- **Nur Bindestriche: `-`, nie `–` oder `—`.** Von ihm am 29.10. zum zweiten
  Mal gesagt, sichtbar genervt. Gilt für jeden Text, den wir für ihn
  schreiben.
  → betrifft: alle Agenten
- **Wenn er einen Text zur Prüfung schickt, will er die Fehlerliste, keine
  neue Fassung.** *„Ich weiß nicht, warum du manche Sachen einfach so
  anpasst."* Ungefragtes Umformulieren nimmt ihm seine Stimme aus dem Text.
  → betrifft: alle Agenten
