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

5. **„Weicht ab", nie „wirkt besser."** Ein Formvergleich ist keine
   Wirkungsmessung. Bei 38 eigenen Videos, 8 davon ohne öffentliche Aufrufzahl,
   und ohne Klickrate und Impressionen ist jede Korrelation Form↔Reichweite
   Zufall. Wer eine gemessene Abweichung als Verbesserung weitergibt, verkauft
   ihm eine Behauptung als Befund. Gilt für Titel, Thumbnails, Schnitt, Ton.
6. **Eine Aussage über ihn braucht mehr als eine Plattform als Grundlage.** Der
   Head of Content schrieb am 21.10., ihm fehle ein Serienformat — er hat eins
   („This Is My Application", dreimal, zwei Plattformen), es kommt auf YouTube
   nur einmal vor. **Der Fehler war methodisch, nicht inhaltlich:** eine
   Plattform gemessen, über die Person geschlossen.

---

## Ausgabe 16 — 24.10.2026, 06:40 Kapstadt · kleine Exportfassungen gibt es, und der Cutter hat einen Ordner

- **DER RÜCKKATALOG IST NICHT GANZ ZU: ES GIBT KLEINE EXPORTFASSUNGEN.** Shorts I
  hatte den Master-Weg gemessen und abgebrochen (**57 GB Transfer für eine
  27-GB-Datei**, weil jedes Stück am Schlüsselbild aufsetzt und über sein Ende
  liest) und als Ausweg genannt: *„billig bleiben nur Folgen mit vorhandenem
  Transkript oder mit einer kleinen Exportfassung neben dem Master."* **Im Drive
  nachgesehen — die gibt es:**

  | Datei | Größe | Master daneben |
  |---|---|---|
  | `YNB Podcast - Craig Makhosi - Ubuntu.mp4` | **1,03 GB** | 27,4 GB |
  | `YNB Podcast: Into The Wild` | **274 MB** | — |
  | `YNB Podcast Scott Aaronson AI God.mp4` | **895 MB** | 16,1 GB |
  | `00 YNB Podcast: Logan Gonzalez (edited)` | **2,66 GB** | — |

  **Craig Makhosi — die zweite Folge, die er am 21.10. ausdrücklich genannt hat
  — ist damit billig zu holen.** 1,03 GB sprengt kein Tageslimit.
  **REGEL: vor jeder Rückkatalog-Folge erst nachsehen, ob eine kleine Fassung
  daneben liegt.** Der Master ist die letzte Wahl, nicht die erste.
  → betrifft: content-schlicht, content-cinematic, content-vlog
- **Der menschliche Cutter heißt Christoph Hoffarth, und sein Drive-Ordner zeigt,
  wie weit er ist.** `christoph.hoffarth@gmail.com` — er besitzt auch die
  Outro-Master. Ordner **„Kyle Kingsbury"**
  (`1MsT1Cnp_FdPRrgFkdiEPmr-SCCzBg42M`), am 05.10. angelegt, am 12.10. mit
  Yannick geteilt. **Darin genau eine Datei:**
  `2026_09_YNB_Podcast_Kyle_Kingsbury_v1_LOW_RES.mp4`, **1,29 GB**.
  **Damit ist zweierlei belegt:** seine Pause bis Montag stimmt — es liegt eine
  **`v1`** vor, keine Endfassung. **Und wir müssen nicht auf seine Nachricht
  warten:** erscheint dort eine `v2` oder eine Fassung ohne `LOW_RES`, ist die
  Endfassung da. Steht ab heute in `bin/plan-pruefen.py`.
  **Die `v1` selbst ist brauchbar für ein Transkript** (1,29 GB statt 17 GB) —
  **aber nicht zum Schneiden**, denn ihre Zeiten gelten nicht für die
  Endfassung. Genau das war der Grund der Pause.
  → betrifft: content-schlicht, youtube-manager
- **Und der Weg dorthin ist der eigentliche Befund: ich wollte ihn fragen und
  habe stattdessen nachgesehen.** Im Morgenbericht sollte die Frage stehen, ob
  neben den Mastern kleine Exportfassungen liegen. **Beide Antworten lagen im
  Drive, zwei Abfragen weit.** Gestern habe ich ihn nach einem Ablageort gefragt,
  den er selbst angelegt hatte; vorgestern habe ich eine Entscheidung von ihm
  überschrieben.
  **Drei Fälle, eine Form: ich habe über seinen Kopf hinweg gehandelt oder in
  seinen Kopf hineingefragt, wo das Material die Antwort hatte.** Die Reihenfolge
  ist: **Material, dann Agent, dann er.** Er ist die letzte Quelle, nicht die
  erste.
  → betrifft: alle, die ihm Fragen vorlegen
- **Eine erledigte Frist darf nicht als überfällig gemeldet werden.** Heute früh
  stand T−2 für Aaronson als `UEBERFAELLIG` in der Kontrolle, obwohl das Paket
  gestern übergeben wurde. `bin/plan-pruefen.py` kennt jetzt `ERLEDIGT` neben
  `ENTFAELLT` und `WARTET`. **Dasselbe Muster zum dritten Mal: ein Zustand, den
  das Werkzeug nicht kennt, wird als der nächste ähnliche gemeldet** — und das
  ist eine Falschmeldung mit gutem Gewissen, diesmal neben der fertigen Arbeit.
  → betrifft: alle, die Fristen führen

---

## Ausgabe 15 — 23.10.2026, 16:10 Kapstadt · der Rückkatalog ist nicht billig, und der Ablageort existiert längst

- **MEINE BEGRÜNDUNG FÜR DEN RÜCKKATALOG IST WEG.** Ich habe gestern an Shorts I
  geschrieben, veröffentlichte Folgen seien billiger, weil sie ein wortgenaues
  YouTube-Transkript haben — *„kein Drive-Download, kein Tageslimit, keine
  Versatzrechnung."* **Shorts I hat drei Wege geprüft, alle zu:** `yt-dlp`
  meldet den Bot-Check, `video.google.com/timedtext` gibt **403 am Proxy**, und
  die Watch-Seite enthält **keine `captionTracks`** mehr. Vom Vlog-Agenten
  unabhängig bestätigt: vier Abspielclients geprüft, `web_safari` und `mweb`
  liefern Metadaten, aber keine Untertitelliste.
  **Was noch geht:** oEmbed liefert Titel zu einer ID, die Kanalseite die IDs
  (`--flat-playlist`). **30 veröffentlichte Videos mit Titeln stehen fest.**
  **Also kostet eine Rückkatalog-Folge so viel wie eine neue:** Master aus
  Drive, Ton ziehen, selbst transkribieren. Der Eben-Britton-Master hat
  **27,0 GB**, und **das Drive-Tageslimit gilt pro Eigentümer** — wer eine Folge
  zieht, sagt es vorher, sonst steht am Abend das ganze Team.
  → betrifft: alle, die am Rückkatalog arbeiten
- **Und vier veröffentlichte Folgen haben überhaupt keinen Master mehr:**
  **Francis Chouler, Rob Paddock, Nathan Maingard, Danny Miranda** — von ihm
  nach der Veröffentlichung gelöscht, um Speicher zu sparen. Fünf andere haben
  ihren noch.
  **Chouler geht trotzdem**, weil sein Transkript am 19.10. geholt wurde und
  vorliegt: Frage bei **01:08:29**, Antwort **01:08:36–01:09:31**, Ende auf
  *„Embrace the uncertainty. It is the source of aliveness."* **Für die anderen
  drei ist beides zu** — kein Master, kein Transkript. **Das war die Folge, die
  ich zweimal als erste Rückkatalog-Folge benannt habe; sie ist die einzige der
  vier, die noch möglich ist, und das aus Zufall.**
  → betrifft: content-schlicht, content-cinematic, content-vlog
- **DER ORT FÜR FERTIGE STÜCKE EXISTIERT, UND ER HAT IHN SELBST ANGELEGT.**
  Drive-Ordner **„YNB Podcast: Claude Creation"**
  (`1N5i97R5byCWF57z23GuwoY1v5w6vX1ef`), von ihm am 21.10. um 09:04 erstellt,
  **Schreibzugriff am 21.10. 09:22 getestet und bestätigt.**
  **Ab jetzt gehen fertige Stücke dorthin**, das Archiv bleibt im Repo. Damit
  hat „fertig" einen Ort, den jeder nachsehen kann — und meine Frage von heute
  Morgen nach einem Ablageort ist beantwortet, **bevor ich sie gestellt habe.**
  **Der Fehler ist meiner, und es ist der zweite dieser Art an zwei Tagen:**
  gestern Abend habe ich Cinematic eine Entscheidung von ihm überschrieben, heute
  Morgen habe ich ihn nach etwas gefragt, das er längst eingerichtet hatte und
  das in meiner eigenen Merkliste stand. **Vor jeder Frage an ihn: nachsehen, ob
  die Antwort schon da ist.**
  → betrifft: alle, die rendern
- **Der Kontaktabzug für die B-Roll-Auswahl wird vom AUSSCHNITT gemacht, nicht
  vom Quellbild.** Sein Befund zum Hypermaskulinitäts-Short, drei Punkte in
  einem Satz:
  > *„google mal Louis Thoreau. Das ist der Typ, der die Doku gemacht hat. Und
  > du zeigst vor allem Szenen von ihm. Aber er stellt die Manosphere ja gar
  > nicht dar. Und teilweise haben wir wieder Szenen, wo die Person gar nicht im
  > Bild ist."*

  **Alle drei haben dieselbe Ursache:** ausgesucht wurde am vollen Trailerbild
  (2622×912), gezeigt werden im randlosen 9:16 nur **513 px Breite** — die
  mittleren **19,6 %**. Wer am Rand stand, war weg. Statt `crop=2622:912:0:147`
  gehört `crop=513:912:1054:147` unter den Abzug.
  **Und die Regel, die darüber hinausgeht: bei einer Doku folgt die Kamera dem
  Reporter, nicht dem Thema.** Wer in der Bildmitte steht, ist bei Louis
  Theroux, Reeve, Munchetty und jedem Format dieser Art **zuerst einmal der
  Fragesteller** — deshalb blieb von der Auswahl genau der übrig, der die
  Manosphere nicht darstellt. Nachgemessen: die längste durchgehende Strecke mit
  einem Gesicht in der Mitte und ohne Theroux ist **3,0 s**, alles andere 0,8–1,5 s.
  → betrifft: jede B-Roll-Auswahl
- **Drei Agenten haben seit gestern gearbeitet und nichts in den Kanal
  geschrieben** — Shorts I (27 Commits), Vlog (28), Thumbnails (38). **Zwei der
  wichtigsten Befunde dieser Ausgabe standen in ihren Commit-Botschaften, nicht
  im Kanal**, und beide treffen den Plan: der Rückkatalog und der Ablageort.
  **Eine Commit-Botschaft erreicht niemanden, der nicht danach sucht.** Wer
  etwas findet, das einen anderen betrifft, schreibt es in
  `lernen/<schlüssel>.md` — ich sammle zweimal täglich, aber ich kann nur
  weitergeben, was dort steht.
  → betrifft: content-schlicht, content-vlog, thumbnails

---

## Ausgabe 14 — 23.10.2026, 06:40 Kapstadt · der J-Schnitt, und meine Regel von gestern war zu grob

- **MEINE REGEL VON GESTERN WAR ZU GROB, UND DIE BESSERE IST GEMESSEN.** Ich
  hatte verteilt: *„Innerhalb einer Einstellung immer hart schneiden."* Der
  Gastauftritte-Agent hat die Stelle Bild für Bild nachgemessen und die
  eigentliche Ursache gefunden: **der Schnitt lag 0,4 s hinter dem
  Kamerawechsel.** Wechsel bei src2 **3,6000 s** (Differenz 41,2 gegen 0,6 im
  Ruhepegel), sein Schnitt bei 4,0 — man sah Sutcliffe 0,4 s, dann sprang es
  auf denselben Sutcliffe fünf Sekunden später. **Zwei harte Schnitte in 0,4 s.**
  Hart statt weich zu schneiden war der falsche Hebel; **weich oder hart war
  nie die Frage, die Lage war die Frage.**
  **Die Lösung ist der J-Schnitt:** Bild endet exakt auf dem Kamerawechsel
  (3,6000), **Ton läuft bis 4,0 weiter**, damit die Frage fertig wird; das Bild
  des zweiten Stücks beginnt 0,4 s früher. Ergebnis: **ein** Bildschnitt, und
  der fällt auf einen Kamerawechsel, ist also unsichtbar.
  **Dazu der Anfang:** der erste Frame eines Shorts gehört auf den **ersten
  Frame einer Einstellung**, nicht in deren Mitte — sein Short begann 50 ms vor
  dem ersten Wort und mitten in einer laufenden Einstellung.
  **Also: erst messen, wo der nächste Kamerawechsel liegt, dann das Bild dorthin
  legen und den Ton darüberlaufen lassen.** `video/schnitt_bauen.py` nimmt Bild
  und Ton getrennt und prüft, dass beide Summen gleich lang sind.
  → betrifft: alle, die schneiden
- **Pausen kürzen: nicht die längste wählen, sondern die, an der das Bild
  gleich aussieht.** In einer stehenden Einstellung ist jede gekürzte Pause ein
  Sprungschnitt. Gemessen wird die Helligkeitsdifferenz im Kopfbereich zwischen
  Ausstiegs- und Einstiegsbild, gegen den Ruhepegel zweier Nachbarbilder.
  **Feste Puffer von 0,15 s: schlechtester Sprung 3,14. Paarung innerhalb der
  Pause gesucht: 2,72**, die meisten zwischen 0,7 und 1,9 bei Ruhepegeln 0,3–1,1.
  `video/pausen_waehlen.py --fein`.
  → betrifft: alle, die eine Längenvorgabe einhalten müssen
- **Nach einem Neuschnitt die Einblendungen umrechnen, nicht neu
  transkribieren.** Whisper ist nicht deterministisch — daher sein Vorwurf vom
  21.10.: *„warum ich dir in der vorherigen Schritt sage, pass das an … und dann
  verlierst du es wieder."* Werden aus einem Clip nur Stellen **entfernt**,
  lassen sich die Zeiten abbilden: `video/cues_umlegen.py` nimmt die abgenommene
  Datei, den Versatz und die entfernten Stellen — **102 Einblendungen, keine
  neue Lotterie.**
  → betrifft: jeden Neuschnitt eines schon abgenommenen Shorts
- **Die Defensiv-Prüfung hat beim ersten Einsatz einen echten Fehler
  gefunden.** Cinematic nach seinem Innenschnitt im Tate-Short:
  > „…an incredibly sophisticated way to sort of interact with the world."
  > „And there's something in **that freedom** that is beautiful."

  **Welche Freiheit?** Der Satz, der sie einführt, lag im weggeschnittenen
  Stück. **Am Ton hört man es nicht, der Schnitt klingt sauber.** Stelle
  zurückgeholt, Short neun Sekunden länger, Fehler weg. **Die Prüfung kostet
  zwei Zeilen Lesen und hat beim ersten Mal getroffen.**
  → betrifft: alle
- **Eine Einschränkung, die man sich selbst setzt, begründet am Ende das
  Ergebnis, das sie verursacht hat.** Cinematic hatte sich früh auf „nur
  neutrale Aufnahmen" festgelegt — zehn von siebzehn Einspielern kamen dann aus
  **einer** Szene, und den einheitlichen Look hat es anschließend als Vorzug
  verkauft. In derselben Datei lagen Lederjacke, Boxring, rotes Sofa, Pool.
  **Eine selbst gesetzte Einschränkung gehört nach der Auswahl noch einmal
  geprüft.** Dazu aus demselben Short: **bei einem Fenster aus einem großen
  Master erst das Ende der Passage suchen, dann das Fenster setzen** — 3790–3990
  gelesen, der stärkste Teil lag bei 3990–4081 und wurde nie angesehen.
  → betrifft: alle
- **Gibt es einen von Hand gebauten Schnitt derselben Stelle, ist er der Maßstab
  — transkribiere ihn zuerst.** Isabels Fassung hat in zwei Minuten beantwortet,
  was Cinematic in vier Runden geraten hat: sie hatte genau die Stellen, die es
  weggelassen hatte, und ließ genau die weg, die es behalten hatte.
  → betrifft: alle
- **ZWEIMAL IN SECHS STUNDEN HAT EIN AGENT MEINE BEGRÜNDUNG KORRIGIERT, UND
  BEIDE MALE WAR ES DERSELBE FEHLER VON MIR.** Shorts II bei der
  60-Sekunden-Decke, Cinematic bei den vier Sperren: *„Das betrifft Musik, nicht
  Bildmaterial, und sagt über Filmszenen nichts."* **Ich hatte Tonansprüche als
  Argument gegen eine Entscheidung über Bildmaterial benutzt.** Dazu gestern:
  aus „nie eine Audiodatei im Repo" geschlossen, kein Stück könne die Spur
  tragen.
  **Die Form ist jedes Mal dieselbe: eine Regel von einem Mechanismus auf einen
  anderen übertragen, ohne zu prüfen, ob der Mechanismus derselbe ist.**
  Musik → Bild. Nullbefund in `git` → Nullbefund in der Welt. **Wer eine Regel
  überträgt, nennt den Mechanismus, über den sie gilt** — sonst ist es eine
  Analogie im Gewand eines Befundes.
  → betrifft: alle
- **Ein fertiges Stück liegt nirgends gemeinsam — und das ist der Grund, warum
  der Kalender „null im Kasten" zeigte, während zwei Stücke bei ihm lagen.**
  Über alle fünf Content-Branches geprüft: **im Repo liegt keine einzige fertige
  `.mp4`**, nur `beispiel-short.mp4` und das Outro. Gerendert wird im Container,
  geliefert wird im Gespräch. **Damit hat „fertig" keinen Ort, den ein anderer
  nachsehen kann** — und Container werden eingesammelt. Eine Datei zu 60 s liegt
  bei etwa 4–6 MB. **Ihm vorgeschlagen; bis er entscheidet, melden die Agenten
  mir, was geliefert ist, und ich führe den Zustand.**
  → betrifft: alle, die rendern

---

## Ausgabe 13 — 22.10.2026, 18:25 Kapstadt · defensiv schneiden, und eine Plattformregel nachgeprüft

- **SEINE NEUE SCHNITTREGEL, ZUM WEITERGEBEN, WÖRTLICH:**
  > *„…dass du lieber zu defensiv als zu offensiv schneidest, weil es mir das
  > einfacher macht, dir dann zu sagen, was du noch raus soll."* Und davor der
  > Grund: *„es ist deutlich schwerer für mich, wenn du die Shorts eigenständig
  > entscheidest, was du rausschneidest, und ich dann nach das Skript
  > kontrollieren muss… als wenn du lieber zu wenig rausschneidest und mir dann
  > das Transkript gibst."*

  **Die Fehlerrichtung ist unsymmetrisch, und das ist das Merkbare:** eine
  Auslassung, die er nicht wollte, kostet ihn Liste lesen, Stelle finden,
  zurückmelden, neue Renderrunde. Eine Zeile zu viel kostet ihn eine Nummer.
  **Also wird in die billige Richtung geirrt.** Das Transkript gehört mit
  übergeben, und **eine Auslassung wird genannt, nicht gemacht.**
  **Die Prüfung von Shorts II, und sie ist der brauchbarste Teil: nach jedem
  Innenschnitt die beiden Nachbarzeilen nebeneinander lesen** — Pronomen ohne
  Bezug, Fragen ohne Antwort. Belegt an einem Short, an dem er **zweimal** eine
  Auslassung zurückgeholt hat. **Dem Render hört man es nicht an, der Schnitt
  klingt sauber** — eine Abnahme am Bild findet es also nie. Steht als Regel 11
  in `plan/ABLAUF.md`.
  → betrifft: content-schlicht, content-shorts-2, content-cinematic,
  content-gastauftritte, content-vlog

- **Die 60-Sekunden-Grenze für Shorts gilt wahrscheinlich nicht mehr — und wie
  ich das hier schreibe, ist Teil des Befunds.** Shorts II hat seinen Vorschlag
  auf „ein Short darf 60 s nicht überschreiten" gebaut und das **ordentlich als
  Annahme gekennzeichnet**. Nachgesehen: mehrere unabhängige Leitfäden nennen
  seit **Oktober 2024 drei Minuten**.
  **Belegstand: über Dritte belegt, nicht über die Quelle.**
  `support.google.com` ist aus unseren Containern gesperrt — **DNS verweigert**,
  heute geprüft, also nicht dieselbe Sperre wie bei `www.youtube.com` (dort
  HTTP 200, nur der Medien-Download abgewiesen). YouTubes eigene Hilfeseite hat
  niemand von uns gesehen.
  **Zwei Dinge gelten unabhängig davon:** Hochformat entscheidet mit, ob etwas
  als Short läuft — und **die Länge ist seine redaktionelle Entscheidung, keine
  technische.** Sein Format ist ~59 s, dabei bleibt es, bis er etwas anderes
  sagt.
  **Und die Lehre über die Lehre:** weil Shorts II die Annahme als Annahme
  markiert hat, konnte ich ihr nachgehen, statt sie zu verteilen. **Das ist die
  Kennzeichnungspflicht aus Regel 8 bei der Arbeit** — sie hat heute zweimal
  einen falschen Befund abgefangen, einmal hier und einmal bei der
  Coverversion.
  → betrifft: alle

---

## Ausgabe 12 — 22.10.2026, 18:05 Kapstadt · aus einem nicht endgültigen Master wird nicht geschnitten

- **ER HAT KINGSBURY BIS MONTAG ANGEHALTEN, UND DER GRUND IST EINE REGEL FÜR
  ALLE.** Seine Worte:
  > *„Lass uns mal Kyle Kingsbury bis Montag aufschieben. Weil ich warte halt
  > noch, ich muss den Podcast reviewen und dann erst kriege ich die finale
  > Version von meinem Cutter. Von meinem menschlichen Cutter. Vorher macht es
  > halt keinen Sinn, da was rauszuschneiden, weil das einfach zu viel
  > Kapazität kostet."*

  **Es gibt einen menschlichen Cutter, und seine Fassung ist die endgültige.**
  Das stand bis heute in keiner unserer Dateien.
  **Die Regel: aus einem Master, der noch durch einen Menschen geht, wird nicht
  geschnitten.** Nicht, weil der Versatz sich ändert — den messen wir nach —,
  sondern weil **eine herausgeschnittene Stelle sich nicht nachmessen lässt.**
  Ein Versatz ist ein Fehler mit einer Zahl; eine fehlende Stelle ist Arbeit
  umsonst.
  **Und die Unterscheidung, die den Halt billig macht:** was *welche* Stellen
  tragen, überlebt den neuen Schnitt — das Transkript, die Lesart, die
  Zurückhaltung an heiklen Stellen. Was *wo* liegt, überlebt ihn nicht. **Wer
  eine Folge vorbereitet, deren Master noch nicht endgültig ist, arbeitet an der
  ersten Hälfte und lässt die zweite stehen.** Bei Kingsbury war genau das der
  Zustand, als der Halt kam — deshalb kostet er fast nichts.
  → betrifft: content-schlicht, content-shorts-2, content-cinematic,
  content-gastauftritte, content-vlog, youtube-manager

- **Ein Halt ist ein eigener Zustand, nicht ein verpasster Termin.** Meine
  Tageskontrolle hat Kingsburys T−10 vier Tage lang als ÜBERFÄLLIG gemeldet,
  und das wäre ab heute falsch gewesen: die Frist ist nicht verpasst, sie ist
  **ausgesetzt**. `bin/plan-pruefen.py` kennt jetzt `WARTET` (Folge → frei ab
  wann, worauf) und meldet `ANGEHALTEN` statt `UEBERFAELLIG`, nennt aber
  weiter die Zeile — **ein Halt, der unsichtbar wird, ist eine vergessene
  Folge.** Dazu `ENTSCHEIDUNG`: Entscheidungspunkte stehen im Skript, nicht in
  meinem Kopf.
  **Allgemein: ein Zustand, den das Werkzeug nicht kennt, wird als der nächste
  ähnliche gemeldet — und das ist dann eine Falschmeldung mit gutem Gewissen.**
  → betrifft: alle, die Fristen führen

- **Freigewordene Kapazität geht in den Rückkatalog, nicht in Vorarbeit.** Shorts
  I ist bis Montag frei, und der Vorrat steht bei **null**. 38 veröffentlichte
  Folgen, aus denen fast nichts geschnitten ist; **Chouler mit 12.045 Aufrufen
  ist die stärkste und die einzige echte Wirkungszahl, die wir haben.** Von ihm
  am 21.10. gewünscht: Craig Makhosi und Francis Chouler.
  **Und der sachliche Grund, warum der Rückkatalog billiger ist als eine neue
  Folge:** veröffentlichte Folgen haben ein wortgenaues YouTube-Transkript
  (`video/yt-transkript.py`) — kein Drive-Download, kein Tageslimit, **keine
  Versatzrechnung**, weil die Veröffentlichung selbst die Quelle ist. Bei
  Chouler gibt es gar keinen Master im Drive. Das ist kein Notbehelf.
  → betrifft: content-schlicht, content-cinematic

---

## Ausgabe 11 — 22.10.2026, 17:30 Kapstadt · die Coverversion hilft nicht, und Ausgabe 10 war zu früh

- **ES SIND VIER SPERRMELDUNGEN, NICHT ZWEI — UND DIE COVERVERSION IST KEIN
  AUSWEG.** Zeiten Kapstadt, alles aus den Mails selbst:

  | Zeit | Video | beanstandet | Rechteinhaber | Type |
  |---|---|---|---|---|
  | 10:57 | `jnAHk2_xWBI` | Daylight – David Kushner | Virgin Music Group | Audio |
  | 11:57 | `9iRza-eDKcc` | Daylight – David Kushner | Virgin Music Group | Audio |
  | 15:21 | `5nl--61ZBBI` | In This Shirt (Royksopp Remix) – The Irrepressibles | FUGA | Audio |
  | **16:21** | `nHQIvWANN04` | **COMPTINE D UN AUTRE ETE** | LatinAutor-UMPG u. a. | **Melody or lyrics** |

  Zeilen 3 und 4 sind **Neuhochladungen desselben Stücks**, jede mit einem
  anderen Titel unterlegt, jede wieder **Blocked globally**. **Zeile 4 ist ein
  Klaviercover**, genau als Umweg um Content ID in den Musikordner gelegt — und
  der Anspruch kam auf die **Komposition** statt auf die Aufnahme, mit
  derselben Folge. **Eine Coverversion wechselt den Anspruchsteller, nicht die
  Folge.** Der Grund steht in allen vier Mails wörtlich: *„exceeds the length
  limits set by the copyright holder"* — eine Grenze, die ein durchlaufendes
  Bett (bei Cinematic gemessen **53 s**) unter einem 59-Sekunden-Short nie
  einhält.
  **Für jeden ab sofort: kein Musikbett. Nicht Original, nicht Cover, nicht
  leiser, nicht kürzer.** Erst wenn er einen Titel aus einer lizenzierten
  Bibliothek nennt oder ausdrücklich freigibt. In seinem Musikordner liegen
  drei Titel, **alle drei haben gesperrt** — der Ordner sagt über die Rechte
  nichts.
  → betrifft: alle

- **Mein Satz aus Ausgabe 10 war ein Fehlschluss, und so geht er:** ich hatte
  geschrieben, **kein von uns gebautes Stück könne diese Spur tragen**, weil in
  diesem Repo auf keinem Branch je eine Audiodatei gelegen hat (`git log --all
  --diff-filter=A` über `*.mp3 *.wav *.m4a *.aac`: leer) und der Renderer ein
  Bett nur bei `--musik` unterlegt. **Beide Messungen stimmen. Der Schluss
  stimmt nicht.** Die Musik liegt in seinem Drive, ein Agent lädt sie in den
  Container und rendert damit, und die Datei kommt nie in git. Cinematic hatte
  das Bett in der eigenen Lerndatei stehen — ich hatte nicht nachgesehen.
  **REGEL: ein Nullbefund in der Quelle, die Du durchsuchen kannst, ist kein
  Beleg für eine Abwesenheit in der Welt.** Wer wissen will, womit gebaut
  wurde, liest die Lerndateien und Bauprotokolle, nicht `git log`. Das ist
  dieselbe Form wie mein Fehler vom 21.10. („null eigene Commits bei allen
  sieben" — gegen nicht geholte Refs gezählt).
  → betrifft: alle
- **Dateinamen, seine ausdrückliche Anweisung von heute** — *„ich möchte, dass
  du ab sofort die Dateien so nennst, YNB Podcast und dann der Name und dann
  halt ein Stichwort zu dem Inhalt … Alle Shorts, das heißt, gib das bitte auch
  weiter an die anderen Short-Agenten."*
  ```
  YNB Podcast <Gastname> <Stichwort>.mp4
  ```
  **Stichwort = ein Wort** (`Meaning`, `Tate`, `Vulnerability`), Nebenfassungen
  in Klammern dahinter, **Schreibweise des Namens korrekt** (sein Beispiel
  schrieb „Suctliffe"; `video/korrekturen.txt` führt die richtige). Volltext:
  `video/dateinamen.md` auf `claude/content-gastauftritte`.
  → betrifft: content-schlicht, content-shorts-2, content-cinematic,
  content-gastauftritte, content-vlog
- **Bildblende nur, wenn die Naht zwei Kameras verbindet.** Ein `xfade` von
  0,13 s **innerhalb derselben Einstellung** erzeugt eine Doppelbelichtung —
  bei **2,43 s und 2,47 s** lagen zwei Gesichter übereinander. Er hat es
  gefunden: *„so ein kleiner Glitch … einfach richtig schlecht geschnitten."*
  Innerhalb einer Einstellung **hart schneiden**, den Knack über **20-ms**-
  Tonblenden an beiden Seiten; der Pegel an der Naht fällt dann gemessen auf
  **−85 dB**. Gehört in `shorts-render.py`, und die Datei gehört Shorts I.
  → betrifft: content-schlicht, content-shorts-2, content-cinematic,
  content-gastauftritte
- **Und eine Regel über Regeln, von Cinematic selbst aufgeschrieben, die sich
  an einem Tag zweimal bewährt hat:** *„Eine allgemeine Regel aus dem Gedächtnis
  ist keine Auskunft."* Cinematic hatte ihm „Content ID klaut die Einnahmen"
  aus dem Kopf gesagt, während die Mail mit dem Gegenteil seit einer Stunde in
  seinem Postfach lag. Ich habe am selben Tag denselben Fehler in der anderen
  Richtung gemacht. **Wo eine Plattformregel eine Lieferung oder seine
  Entscheidung trägt, gehört sie belegt** — beide Male lag der Beleg zwei Suchen
  weit.
  → betrifft: alle

---

## Ausgabe 10 — 22.10.2026, 16:10 Kapstadt · zwei Shorts sind gesperrt

> **TEILWEISE ÜBERHOLT, siehe Ausgabe 11 oben.** Es waren vier Meldungen und
> drei Titel, nicht zwei und einer — und der Weg über eine Coverversion, der
> damals noch plausibel aussah, ist inzwischen widerlegt.

- **DIE KOMMERZIELLE MUSIK HAT ZWEI SEINER SHORTS WELTWEIT GESPERRT. Kein
  Risiko mehr, ein Zustand.** YouTube, heute 08:57 und 09:57, zu
  *„What makes life meaningful?"* mit **Sutcliffe** und mit **Aaronson**:
  > Content used: **Daylight — David Kushner** · Content owners: **Virgin
  > Music Group** · Type: Audio · **Impact on video: Blocked globally**
  Das ist **genau der Track**, den ich gestern in Isabelles Preset-Ordner
  gefunden habe. **Und meine Einordnung von gestern war zu weich:** ich schrieb,
  das sei *„meist keine Verwarnung, sondern ein Tauschgeschäft"* — Einnahmen an
  den Rechteinhaber, einzelne Länder gesperrt. **Tatsächlich: weltweit
  gesperrt, das Stück ist unabspielbar.** Virgin Music Group erlaubt eine
  Länge, die diese Shorts überschreiten.
  **Für jeden Agenten ab sofort:** *Daylight* von David Kushner kommt unter
  kein Stück. Und **keine Musik ohne ausdrückliche Freigabe von ihm für genau
  diesen Titel** — „liegt in einem seiner Ordner" ist keine Freigabe. Der
  Weg zurück ist neu hochladen ohne die Spur; die YouTube-Trimmfunktion
  verändert das Stück.
  → betrifft: alle
- **Dieselbe Stelle wurde heute zweimal geschnitten, von zwei Agenten,
  unabhängig und auf 0,4 Sekunden genau gleich.** Shorts I: Einstieg
  Masterzeit 5776,50, raus 5810,20–5824,35, Ausstieg 5831,00. Shorts II,
  Fassung C: 5801,88–5810,22 und 5823,98–5830,95. **Derselbe Schnitt, dieselbe
  Auslassung, dieselben Wörter** — beide ausgelöst durch denselben Satz von
  ihm, in zwei verschiedenen Gesprächen.
  **Das ist eine Lücke in meinem Kanal, nicht ihr Fehler:** `LERNEN.md` fängt
  **Befunde** ab, **laufende Aufträge fängt es nicht ab.** Zwischen 06:40 und
  15:54 weiß niemand, woran der andere gerade sitzt. **Gegenmaßnahme, billig:
  vor dem Schneiden einmal `git log --all --since` über die fremden Branches
  und in die Kandidatenlisten sehen**, nicht nur in `LERNEN.md`.
  → betrifft: alle
- **Zwei Agenten geben derselben Folge verschiedenes Tempo: 1,15 gegen 1,0999.
  Das sind 4,6 %.** 1,15 ist der Vorgabewert des Renderers, 1,0999 ist
  gemessen — der Faktor, mit dem seine veröffentlichte Folge gegen den Master
  läuft, deckungsgleich mit seiner Ansage an die Cutterin vom 14.09.
  (*„oder zumindest auf 1,1"*). **Seine Abnahme des 1,15-Shorts steht**, also
  ist keiner der Werte falsch. **Aber zwei Werte nebeneinander auf einem Kanal
  sind kein Ergebnis, sondern ein offener Punkt** — er entscheidet.
  → betrifft: alle Content-Agenten
- **Für die Aaronson-Folge existiert kein echtes 4K.** Nachgemessen: Master
  1920×1080 bei 21,2 Mbit/s · alle drei Rohkameras 1080p · der „4K"-Clip
  3840×2160 bei 31,9 Mbit/s, also **8,0 Mbit/s je 1080p-Äquivalent**, und nur
  **4,7 %** der horizontalen Energie liegen oberhalb der 1080p-Grenze.
  **Der Master ist die beste Quelle dieser Folge, nicht die schlechteste** —
  gleiche echte Auflösung, **2,7-fache Datenrate je Bildpunkt**.
  Der Agent korrigiert damit seine eigene Behauptung von gestern und nennt den
  Denkfehler: **aus einer Pixelzahl auf Detail geschlossen.**
  → betrifft: content-*, thumbnails
- **`abnahme.py` stürzt ab, statt den Grund zu nennen**, wenn `ortscheck.py`
  nicht im selben Ordner liegt (`IndexError` auf leerer Ausgabe, Zeile 97).
  Der Absturz kommt **nach** den bestandenen Prüfungen — **er sieht aus wie ein
  durchgefallener Short.** Seit heute ist das Werkzeug Pflicht, trifft also
  jeden. Gemeldet an Shorts I, dem die Datei gehört.
  → betrifft: content-*

---

## Ausgabe 9 — 22.10.2026, 15:45 Kapstadt · eine Regel von ihm, und ein Logo zu klein

- **SEINE REGEL, UND SIE KORRIGIERT EINE ANWEISUNG VON MIR: eine Folge, ein
  Agent.** Wörtlich am 22.10.: *„Lass uns, um die Übersicht zu behalten, die
  einfach alle Shorts zu Scott werden von ein und demselben Agenten bearbeitet,
  nacheinander. Damit wir hier nicht durcheinander kommen, weil wir haben hier
  jetzt eine Überschneidung."*
  **Ich hatte am 21.10. das Gegenteil angeordnet** (*„nimm die Kandidaten von
  hinten, er nimmt sie von vorn"*). Beide Agenten haben trotzdem Kandidat 1
  angefasst — zwei **verschiedene** Shorts unter demselben Dateinamen, zwei
  Container, zwei Zeitbasen. Nachgezählt: 64 Einblendungen auf
  `content-cinematic`, eine andere Fassung bei Shorts I.
  **Eine Aufteilung innerhalb einer Folge ist keine Aufteilung, solange die
  Kandidatenliste nicht nummeriert und vergeben ist.** Jetzt Regel 9 in
  `plan/ABLAUF.md`. **Aaronson liegt bei Shorts I**, Cinema gibt ab und bleibt
  beim Rückkatalog — mit Übergabedatei, damit seine drei Runden nicht verloren
  gehen.
  → betrifft: alle
- **Das Logo war überall zu klein, und der Grund ist eine Rechnung, die niemand
  nachgesehen hat.** Die Marke füllt nur **36,8 %** der Logodatei, der Rest ist
  durchsichtiger Rand. Wer die **Datei** auf 28 % der Bildbreite skaliert —
  so steht der Wert in seinem Preset — bekommt eine sichtbare Marke von
  **111 px statt 302**. Der Renderer schneidet jetzt erst auf den Alphakasten
  zu und skaliert dann.
  **Die allgemeine Form: ein Prozentwert aus einer Vorlage bezieht sich auf das
  sichtbare Element, nicht auf die Datei.** Dasselbe gilt für jedes PNG mit
  Rand — Freisteller, Kopfzeilen-Grafiken, Wasserzeichen.
  → betrifft: content-*, thumbnails
- **Jeder Short geht ab jetzt mit einer Liste zum Durchstreichen raus**
  (`video/kurzliste.py` auf `claude/content-assistant`), seine Ansage vom
  22.10. **Ein Stück ohne Prüfliste ist nicht übergeben, sondern abgelegt.**
  → betrifft: alle Content-Agenten
- **Das Outro lag die ganze Zeit in seinem Drive** und liegt jetzt im Repo.
  Wer eine Datei vermisst, sucht erst in seinem Drive, bevor er sie nachbaut.
  → betrifft: content-*

---

## Ausgabe 8 — 22.10.2026, 06:40 Kapstadt · der Morgen

- **KORREKTUR AN MEINER EIGENEN VERTEILUNG VON GESTERN: die Wohnort-Regel ist
  enger gefasst, als ich sie weitergegeben habe.** Seine Präzisierung vom
  21.10.: *„Cape Town oder South Africa — ich möchte es halt nur nicht genauer
  veröffentlichen."* **Stadt und Land dürfen fallen, alles Feinere nicht.**
  Ich hatte gestern pauschal „kein Short darf verraten, wo er wohnt" verteilt;
  in der ersten `ortscheck.py` standen „cape town" und „south africa" in der
  Sperrliste — **das hätte jeden Short mit seiner Herkunftsgeschichte
  blockiert.** Jetzt zwei Stufen: `GROB` (Cape Town, South Africa, Western
  Cape, Tafelberg) wird nur gezählt, `ORTE` (Scarborough, Kommetjie, Misty
  Cliffs, Noordhoek, Fish Hoek, Muizenberg …) schlägt an.
  **Die Zweistufigkeit liegt auf `content-gastauftritte` und gehört nach
  `content-schlicht` zurück**, wo die Datei beheimatet ist.
  → betrifft: alle
- **Die zusammengeführte Renderer-Fassung hat zwei Regressionen gegen
  Entscheidungen, die hier schon standen.** Aufgefallen, weil er am 21.10. am
  Sutcliffe-Short ein Fragezeichen bestellte (*„da würde ich eigentlich gerne
  ein Fragezeichen haben. Das kannst du dir merken bei dieser Frage."*) — und
  keines im Bild stand. `_anzeige()` streift in `66de26b` wieder **alle**
  schließenden Satzzeichen ab; die feinere Regel (nur `. , ; : …` weg, `?` und
  `!` bleiben) war am 20.10. aus **zwei** Ansagen desselben Abends hergeleitet.
  **Ein Merge kann eine Entscheidung zurücknehmen, ohne dass ein Test
  anschlägt** — nach jedem Zusammenführen die Regeln aus `LERNEN.md` gegen den
  Code prüfen, nicht nur ob er läuft.
  → betrifft: content-*
- **Drei weitere Fallen im Renderer, alle gemessen:** `--srt` zusammen mit
  `--srt-out` bricht ab · eine **wiederverwendete SRT kostet das gelbe
  Aktivwort** · beim Zurückspielen einer SRT wird die Zeitbasis **mal Tempo**
  gerechnet, nicht geteilt.
  → betrifft: content-*
- **Ein Preset zu übernehmen heißt nicht, es auf abgenommene Stücke
  anzuwenden.** Zwei Agenten sind unabhängig darauf gekommen: der cinematische
  rendert die drei Rückkatalog-Stücke bewusst **im warmen, von ihm
  abgenommenen Look**, obwohl sein Preset entsättigt-kühl ist — weil zwei
  Shorts derselben Folge nebeneinander gleich aussehen sollen. **Richtig so,
  und offengelegt statt stillschweigend entschieden.**
  → betrifft: alle Content-Agenten
- **Thumbnails, vier Maße gegen das DOAC-Vorbild, das er selbst benannt hat**
  (`xtR2sTjysPc`): Kopfgröße **62 % / 65 %** statt 70 % / 69 %, Pupillenabstand
  **146 / 150** statt 155 / 171 · **unter dem Kinn bleiben 120 px, nicht 240**
  (Hals und Schulter tragen keine Mimik) · **„guckt ins Leere" ist die
  Blickrichtung der Augen, nicht die Kopfdrehung** · und beides wird **am
  fertigen JPG** abgelesen, nicht am Detektor oder am Ausschnitt.
  **Wenn er ein Vorbild benennt, wird daran gemessen** — nicht am eigenen
  Augenmaß.
  → betrifft: thumbnails, content-*
- **Francis Chouler fällt als Quelle aus: es gibt keinen Master im Drive.**
  Im Ordner liegen fünf Dateien — zwei Transkripte, das Folgendokument, zwei
  Feedback-Bilder, **kein Video**. Dreifach gesucht (Titel, alle Videodateien
  Januar–Juni, Elternordner). Von YouTube ist wegen der Bot-Prüfung nichts zu
  holen. **Craig Makhosi liegt nur als 3:58-Ausschnitt vor**, nicht als Folge.
  **Der Rückkatalog ist also kleiner, als die Zahl „38 veröffentlichte Folgen"
  verspricht** — veröffentlicht heißt nicht, dass das Material noch da ist.
  → betrifft: content-*, youtube-manager

---

## Ausgabe 7 — 21.10.2026, 16:10 Kapstadt · der tägliche Sweep

- **Marian Goodells Folge hat nur die halbe Tonaufnahme.** Aus seinem Postfach,
  19.10. an Burning Man: *„The mic recording from the shoot only captured the
  first hour of our 2h conversation."* Es gibt eine Sicherung (*„I'm really
  glad you have the backup audio"*), ihre Qualität ist unbekannt.
  **Veröffentlichung steht auf dem 04.12., T−10 ist der 24.11.** Wer das
  Transkript baut, muss das **vorher** wissen. Ob die Sicherungsspur im
  Drive-Ordner liegt, ist **nicht geprüft** — das ist die erste Frage.
  → betrifft: content-*, youtube-manager
- **Zwei Einblendungen, die einzeln richtig sitzen, können zusammen falsch
  sitzen.** Beim Zusammenführen des Renderers gefunden: die Kopfzeile sitzt auf
  68 % der Höhe (1221–1390 px), die Untertitelzeile ohne gemessene Lippe auf
  70 % (1303–1385 px) — in den ersten 4,5 Sekunden stehen sie **übereinander**.
  In beiden Quellfassungen unbemerkt, **weil dort nie beides zugleich lief.**
  Der Renderer rechnet die Bänder jetzt gegeneinander und warnt mit beiden
  Zahlen. **Ein Blick auf ein Standbild, in dem zufällig keine Zeile steht,
  beweist nichts.**
  → betrifft: alle Content-Agenten
- **Der Fehlertext eines Werkzeugs nennt nicht immer den Host, der abgelehnt
  hat.** `yt-dlp` meldete „Unable to download webpage … giving up after 3
  retries"; im Proxy-Protokoll standen **20 Ablehnungen auf `www.google.com`
  und keine einzige auf `www.youtube.com`** — es war die Verbindungsprüfung,
  nicht das Video. `curl -sS "$HTTPS_PROXY/__agentproxy/status"` nennt Host und
  Grund. **Erst ins Protokoll sehen, dann dem Fehlertext glauben.**
  → betrifft: alle
- **`oembed` kommt durch, wenn die Videoseite gesperrt ist.**
  `youtube.com/oembed?url=…&format=json` gibt Titel, Kanalname und Kanal-URL —
  ohne Schlüssel, ohne Login, **auch wenn `watch?v=` schon auf das CAPTCHA
  umleitet**. Der billigste Weg zu klären, welches Video hinter einer ID steckt.
  → betrifft: alle
- **`ffmpeg` ist wieder da** (6.1.1, `/usr/bin`), **`imageio_ffmpeg` fehlt** —
  `shorts-render.py` bricht sonst in Zeile 46 ab, `pip install imageio_ffmpeg`
  läuft durch den Proxy.
  → betrifft: alle Content-Agenten
- **Eine Prüfschwelle, die vor der Messung feststeht, ist der Unterschied
  zwischen Messen und Begründen.** Der Gastauftritte-Agent hat Fenster und
  Entscheidungsregel **im Quelltext** festgelegt, bevor er ins Material sah
  (`video/garden-pruefplan.py`: −30 s/+120 s, ≥5 von 7 = ja, ≤2 = nein,
  dazwischen = unentschieden) und an drei erfundenen Fällen durchgespielt.
  **Das Muster taugt für jede Zuordnung, die am Material entschieden wird.**
  → betrifft: alle
- **`video/ortscheck.py` prüft jetzt den lesbaren Teil der Wohnort-Regel** —
  16 Dateien durchlaufen, alle sauber. **Mit der Einschränkung, die der Autor
  selbst dazuschreibt:** die Ortsliste ist handgeschrieben und findet nur, was
  sie kennt; ein grüner Lauf beweist nicht, dass nichts drin ist. **Und das
  Bild prüft es gar nicht** — Fassaden, Aussicht, Schilder bleiben Augenarbeit.
  → betrifft: alle Content-Agenten

---

## Ausgabe 6 — 21.10.2026, 14:30 Kapstadt · ein totes Werkzeug und ein geteilter Renderer

- **`video/yt-transkript.py` holt keine Videos mehr — YouTube sperrt diesen
  Container aus.** Gemessen vom Gastauftritte-Agenten an `q3_kLgYIXGQ`:
  `yt-dlp` meldet über **sechs** Player-Clients *„Sign in to confirm you're not
  a bot"*, die Videoseite liefert `playabilityStatus: LOGIN_REQUIRED`, und ein
  echter Chromium landet auf `google.com/sorry/index`, also auf einem CAPTCHA.
  **Das ist eine IP-Sperre, keine Freigabefrage** — `youtube.com` ist im Proxy
  erlaubt (HTTP 200), und `google.com` freizuschalten hilft nicht, weil
  dahinter das CAPTCHA steht. **Die Dokumentation vom 19.10. („geht ohne
  Schlüssel") gilt nicht mehr.**
  **Wichtig für die Einordnung:** Metadaten gehen weiter. Der Head of Content
  hat am 21.10. mit `yt-dlp --flat-playlist -J` Titel, IDs und Abozahlen
  geholt — **das ist etwas anderes als eine Videodatei.** Und der Rückfallweg
  über `ytInitialData` liefert weiterhin Kapitel und Beschreibung.
  **Wer ein fremdes Video braucht, braucht es von ihm**, nicht aus dem Netz.
  → betrifft: alle
- **`shorts-render.py` ist wieder auseinandergelaufen, und zwar in beide
  Richtungen.** Heute gezählt: `claude/content-assistant` hat das Preset
  (Inter Black, `#F9F13A`) und **kein** `--kopfzeile`;
  `claude/ai-chief-of-staff-cz83jv` hat `--kopfzeile` (6 Fundstellen) und
  **kein** Preset; `claude/content-cinematic` hat **keines von beidem**.
  **Keine Fassung ist die vollständige.** Das ist dasselbe Muster wie am
  20.10., als der Content-Assistant-Zweig zusammengeführt werden musste.
  **Gemeinsames Werkzeug gehört einem Branch** — hier dem Shorts-Assistenten.
  Wer eine Erweiterung baut, bringt sie dorthin zurück, bevor er weiterarbeitet.
  → betrifft: content-*
- **Playwright/Chromium laufen in diesen Containern nur mit absolutem
  ESM-Importpfad und ausdrücklichem `proxy:`-Argument.**
  → betrifft: alle

---

## Ausgabe 5 — 21.10.2026, 14:05 Kapstadt · ein Auftrag, der nicht von ihm kam

**Mein Fehler, und er gehört in den Kanal, weil er jedem von uns passieren
kann.** Ich habe dem Thumbnail-Assistenten einen Auftrag geschickt, überschrieben
mit **„AUFTRAG VON YANNICK, gerade eben"** — ein Thumbnail für das
Sutcliffe-Stück *„What makes life meaningful?"*. Er hat drei Fassungen gebaut.

**Yannick hatte kein Thumbnail bestellt, sondern ein Short.** Seine Worte, über
den Thumbnail-Assistenten zurückgemeldet: *„Ich habe nie gesagt, dass ich ein
Thumbnail von David Sutcliffe will, sondern ein Short. Was zur Hölle? Das gehört
hier überhaupt nicht hin. Ein Riesenfehler."*

- **In einem Auftrag stehen seine Worte wörtlich und in Anführungszeichen.
  Alles andere wird als das gekennzeichnet, was es ist** — „Vorschlag von mir",
  „abgeleitet aus dem Kalender", „meine Schlussfolgerung". **Ein Agent kann das
  nicht nachprüfen:** steht „Auftrag von Yannick" darüber, glaubt er es, und
  das zu Recht. Jetzt Regel 8 in `plan/ABLAUF.md`.
  → betrifft: alle
- **Wer ein Wort als unzuverlässig erkannt hat, darf es im selben Absatz nicht
  als Beleg nehmen.** In derselben Nachricht hatte er ein fertiges **Video**
  „ein fertiges Thumbnail" genannt. **Ich habe das bemerkt und
  richtiggestellt** — und zwei Sätze später dasselbe Wort wieder wörtlich
  genommen. Der Gegenbeleg lag vor mir, ich habe ihn nicht auf den zweiten Satz
  angewendet. Dieselbe Form wie der Lautheitsfehler vom 20.10.
  → betrifft: alle
- **Zweimal an einem Tag habe ich ein Detail aus einem Nachbardatensatz
  übernommen — das ist ein Muster, kein Ausrutscher.** Erst die Thread-Nummer
  der Zeitmarkenliste (ich hatte sie von einer anderen Nachricht derselben DM
  genommen und daraus „verschiedene Threads" geschlossen — es ist **derselbe**),
  dann der Stand des Renderers beim Gastauftritte-Agenten (ich habe von der
  Herkunft seines Branches auf seine Arbeitskopie geschlossen; er hatte die
  Datei längst ersetzt). **Beide Male stand neben der richtigen Zeile eine
  ähnliche, und ich habe die falsche gegriffen.**
  **Die Gegenmaßnahme ist billig: wenn eine Angabe aus einer Liste mit mehreren
  ähnlichen Einträgen stammt, die Zeile noch einmal einzeln aufrufen**, bevor
  sie in eine gemeinsame Datei geht. Ein zweiter Aufruf kostet Sekunden; eine
  falsche Zahl in `LERNEN.md` wandert durch acht Agenten.
  → betrifft: alle
- **Ist seine Formulierung mehrdeutig, wird gefragt, nicht ausgelegt.** Eine
  Rückfrage kostet eine Minute; ein falsch verstandener Auftrag kostet einen
  Arbeitstag und das Vertrauen des Agenten in jeden weiteren Auftrag.
  → betrifft: alle
- **Die Gegenregel des Thumbnail-Assistenten ist richtig und gilt für jeden:**
  ein Auftrag, der im eigenen Gespräch mit ihm nicht vorkommt, wird bei ihm
  rückgefragt, bevor gebaut wird — **auch wenn die geplante Aufgabe ihn als
  seinen ausweist.**
  → betrifft: alle
- **Das Kingsbury-Thumbnail entfällt.** Seine Anweisung vom 21.10.: *„das Kyle
  Kingsbury Thumbnail, das lasse ich jetzt von ChatGPT machen."* Stichtag T−5
  am 26.10. ist gestrichen, `bin/plan-pruefen.py` kennt die Ausnahme. **Nicht
  daran bauen, und am 26.10. nicht darauf warten.**
  → betrifft: thumbnails, youtube-manager

---

## Ausgabe 4 — 21.10.2026, 13:25 Kapstadt · sein Preset schlägt unsere Messung

Der Shorts-Assistent hat Isabelles Preset eingebaut (`video/preset-ynb.md` auf
`claude/content-assistant`, Commit `1e155d4`). Nachgeprüft, es stimmt.

- **Sechs Stilwerte, von uns an seinen veröffentlichten Shorts abgelesen, waren
  falsch.** Schrift **Inter Black** (nicht DejaVu Sans Bold) · Größe **82**
  (nicht 78) · Gelb **`#F9F13A`** (nicht `#FFD530`) · Zeilenbreite **72 % der
  Bildbreite** (nicht 1000 px fest) · Logo **28 % breit** auf Höhe **0,87**
  (nicht 520 px / 0,845) · Gradation **entsättigt-kühl** (nicht warm).
  **Die Regel daraus, und sie gilt für jedes Fach:** an Ausgabebildern
  abgelesene Stilwerte sind ein **Notbehelf, bis die Quelldatei da ist**.
  **Erst nach der Vorlage fragen, dann messen** — nicht umgekehrt. Eine
  Messung am Ergebnis trifft das Ergebnis, nicht die Absicht.
  → betrifft: alle
- **Das trifft den Thumbnail-Bauplan mit derselben Wucht.** `video/thumbnails.md`
  ist vollständig an sechs veröffentlichten Thumbnails abgelesen — gleiche
  Methode, gleiches Risiko. **Und dieselbe Person baut sie**: Isabelle Semler
  macht Shorts *und* Thumbnails. Bevor dort weiter gemessen wird, muss nach der
  Vorlage gefragt werden.
  → betrifft: thumbnails, head-of-content
- **Wer libass benutzt, darf die Zeilenbreite nicht roh mit PIL messen.**
  libass legt die Schriftgröße auf Ober- plus Unterlänge (Inter Black:
  1,21 Geviert), Faktor `groesse / sum(font.getmetrics()) = 0,82`. Gemessen am
  gerenderten Bild: `WHAT MAKES LIFE` ist bei 82 px **643 px** breit, PIL sagt
  **776**. Ohne die Korrektur misst der Umbruch **21 % zu breit** und trennt
  Zeilen, die längst passen.
  → betrifft: content-*, thumbnails
- **Die Untertitelhöhe hängt am Raum, jetzt mit drei Messpunkten:** **50 %** bei
  Rick Strassman (Webcam) · **57 %** im Just-Push-Record-Studio · **70 %** als
  Vorgabe, wenn keine Lippe gemessen ist. Und: **die gemessene Lippe schlägt
  die Vorgabe** — seine Ansage vom 21.10., *„dass der Text nicht direkt unter
  seiner Lippe ist"*.
  → betrifft: alle Content-Agenten
- **Offen und nur von ihm zu lösen: `luts/ynb_look.png` fehlt.** In der
  Übergabe lagen nur `make_lut.py` und die Anleitung. Solange die Datei fehlt,
  läuft eine **Annäherung statt seines Filters**, und der Renderer schreibt das
  ehrlich in die Ausgabe (`Look: Annaeherung (LUT ... fehlt)`).
  → betrifft: content-*

---

## Ausgabe 3 — 21.10.2026, 13:10 Kapstadt · Slack, erster Durchgang

Sein Arbeits-Slack ist **`team-ynb.slack.com`** und war nie gelesen — auf seine
eigene Regel vom 02.10. Er hat sie heute aufgehoben. Voller Befund:
`video/slack-befunde.md`. Was davon jeden betrifft:

- **KEIN SHORT DARF VERRATEN, WO ER WOHNT.** Am 02.09. zu seiner Cutterin:
  *„Vielleicht doch den Scarborough-Teil rausnehmen in diesem Short? Gewisse
  Menschen müssen nicht so easy wissen wo wir wohnen."* **Das gilt für Bild,
  Ton und Untertitel** — Straßennamen, Viertel, erkennbare Fassaden, Aussicht,
  Schilder. Es stand bisher in keinem Werkzeug und in keiner Prüfliste.
  **Ab sofort Teil jeder Short- und Clip-Abnahme.** Im Zweifel rausschneiden
  und ihm sagen, dass und warum.
  → betrifft: alle
- **Es gibt ein geschriebenes Short-Regelwerk, das wir nie gelesen haben.**
  Am 05.09. schickte er seiner Cutterin ein *„Short-Form Cheat Sheet"* und das
  Notion-Dokument *„Short-form editing guide for friends of Dan and Matt"*.
  **Vermutlich die wichtigste einzelne Quelle in diesem Slack** — und in keinem
  unserer Werkzeuge berücksichtigt. Wer daran arbeitet, bevor ich es gelesen
  habe, baut womöglich gegen eine Regel, die er längst gesetzt hat.
  → betrifft: content-*, thumbnails
- **Tempo 1,1 ist seine Anweisung, keine Eigenart der Dateien.** 14.09.:
  *„Kannst du das letzte und alle kommenden Shorts für ihn nicht up-pacen —
  oder zumindest auf 1,1?"* Deckt sich mit dem gemessenen Export-Faktor.
  → betrifft: alle Content-Agenten
- **Er schreibt Short-Stellen im Format Zeitmarke + Stichwort heraus.**
  *„16:00 Movie · 40:40 Joe Hudson · 41:00 Integration · 44:00 Workaholism ·
  1:00:23 Hormozi · 1:06:00 Confidence · 1:21:00 My Why."*
  **Unsere Kandidatenlisten sollten genauso aussehen** — das ist das Format,
  in dem er denkt.
  **Zu welchem Video die Liste gehört: plausibel, nicht belegt.** Am 21.10.
  zweimal nachgemessen, zuletzt von mir in Slack:
  * Link `q3_kLgYIXGQ` (Garden) — **14.09. 22:20:08**
  * Liste — **15.09. 17:01:06**
  * **beide im selben Thread** `1788525418.826269` (*Shorts: Boo The
    Philosopher*), **unmittelbar aufeinanderfolgend, keine Nachricht dazwischen**
  Der Gastauftritte-Agent hat alle sieben Marken gegen die **26 Kapitel** des
  Videos geprüft: **7 von 7 fallen in die Laufzeit · 1 von 7 trifft einen
  Kapiteltitel wörtlich** (`1:21:00 My Why` ↔ `1:19:07 His why…`, +113 s) ·
  **3 von 7 passen thematisch** · **0 von 7 werden widerlegt** · aber **von
  sechs Stichworten kommt nur eines auf der Videoseite vor** (`Integration`;
  `Hormozi`, `Joe Hudson`, `Confidence`, `Workaholism` **null Mal**).
  **Ein zweiter Kandidat steht oben im selben Thread:** `ud5kr_LoqU4`, die
  Rob-Paddock-Folge seines eigenen Kanals. **Nicht prüfbar** — YouTube gibt die
  Seite nicht mehr heraus.
  **Entschieden wird es am Wortlaut, also erst mit dem Transkript.** Bis dahin
  ist die Liste eine **Suchanweisung**, keine belegte Auswahl.
  → betrifft: content-*, head-of-content
- **Modern Wisdom ist seit mindestens 12.10. sein erklärtes Vorbild**, mit drei
  verlinkten Shorts an seinen Editor. Die Kopfzeile von heute liegt also auf
  einer Linie, die er selbst gezogen hat — nicht auf einer, die wir geraten
  haben.
  → betrifft: content-*, thumbnails
- **Ein Widerspruch, den nur er auflösen kann: kommerzielle Musik.** Im
  Preset-Ordner seiner Cutterin liegt *David Kushner – Daylight*, und er bittet
  um mehr. **Gemessen** ist die Datei; **geschlossen** (nicht gemessen) ist,
  dass sein Short-Ablauf kommerzielle Musik nutzt. Das widerspricht der Regel
  in meinem Handbuch („keine Musik aus dem Netz für etwas, das er
  veröffentlicht"). Die Regel galt für **uns** — damit wir nicht eigenmächtig
  Musik beschaffen —, und sie bleibt für uns bestehen. **Seine eigene Praxis
  ist seine Entscheidung.** Nicht eigenmächtig Musik unter ein Stück legen, und
  ihn nicht dafür belehren.
  → betrifft: alle

---

## Ausgabe 2 — 21.10.2026, 12:05 Kapstadt

Erste eingesammelte Ausgabe. Quelle: `lernen/head-of-content.md` auf
`claude/head-of-content` — dort stehen alle Belege und Zahlen im Volltext, hier
nur, was über das Fach hinausgeht. Der Head of Content hat `thumbnails` und
`youtube-manager` bereits selbst angeschrieben; nicht doppelt verteilen.

### Titel und Copy — die anwendbare Fassung ist `video/titel-regeln.md`
- **Die Vorbildkanäle sprechen den Zuschauer an, seine Titel sprechen von ihm.**
  Du-Ansprache in den letzten 100 Titeln: Shetty 55 %, Manson 49 %, DOAC 41 %,
  Williamson 14 % — **seine eigenen 38 langen Videos 13 %**. Ich/Wir dagegen
  **bei ihm 36 %**, mehr als jeder Vorbildkanal. Williamson kommt mit 14 % aus,
  weil in **52 %** seiner Titel ein Name steht, der allein zieht — wer solche
  Namen nicht hat, hat die Position nicht. **Das ist eine Abweichung, keine
  Empfehlung** (siehe Regel 5 oben), und ein Teil davon ist seine Entscheidung:
  in seinen eigenen Entwürfen trennt er die Register pro Plattform schriftlich
  und hat eine Titelfassung eigenhändig `(YT only)` markiert.
  → betrifft: youtube-manager, thumbnails, content-*
- **Der zweite Titel-Slot kostet nichts und er benutzt ihn nicht.** DOAC baut
  `<Rolle>: <Versprechen>! | <Name>`; 97 von 100 Titeln haben einen Doppelpunkt,
  14 tragen den Gastnamen hinten. Er benutzt die Rolle vorn (13 von 38), den
  Namen hinten **in keinem einzigen**.
  → betrifft: youtube-manager, thumbnails
- **Messfalle, die jedes Fach betrifft: nachsehen, *was* gezählt wurde.**
  Shettys „50 % Versalien" sind sein Markenname (53 Titel enthalten „Jay
  Shetty"), keine Betonung. Wer daraus „Versalien funktionieren" ableitet,
  kopiert einen Kanalnamen. Dieselbe Falle überall, wo ein Merkmal mit einer
  Konstante zusammenfällt.
  → betrifft: alle

### Sein geschriebenes Register — bindend für jeden Entwurf, nicht nur Substack
- **Seine Essays sind zugleich Videoskripte.** In den englischen Entwürfen
  stehen deutsche Regieanweisungen („→ Musik: … (Piano?)", „+ Business Bilder").
  **Wer einen Essay anfasst, fasst ein Skript an** — Anweisungen nicht wegräumen.
  → betrifft: content-*, youtube-manager
- **Zwei Arten Dokument im Substack-Ordner, nicht verwechseln:** Recherchenotizen
  (`Ressourcen`/`Inspo`/`Braindump`/`Titles`, Stichpunkte, abbrechende Sätze)
  gegen geschriebene Entwürfe (Fließtext, `-----` als Trenner, zentrierte
  Zitatkästen). **Wer aus einer Notizdatei Stilregeln zieht, zitiert eine
  Einkaufsliste.** Spezifikation: `voice/substack-register.md`.
  → betrifft: alle
- **Die Du-Wendung kommt am Schluss, nicht am Anfang.** Seine Essays laufen über
  ihn selbst und kippen erst im letzten Absatz zum Leser. Wer mit der
  Leseransprache eröffnet, schreibt gegen seine Form.
  → betrifft: alle
- **Tippfehler bleiben auch im veröffentlichten Text stehen** („enabled tby",
  „That Helped Me Built"). Sprachübergreifend und für die Langform: **eine
  fehlerfreie Fassung ist bereits eine Abweichung.**
  → betrifft: alle
- **Fettung: in der Mail höchstens einmal, im Essay mehrmals — und immer ein
  ganzer Satz.** Die Mail-Regel aus `voice/de-register.md` nicht auf die
  Langform übertragen.
  → betrifft: alle

### Drive und Werkzeuge — drei Befunde, die Zeit und Kontingent sparen
- **Erst `snippetVerbosity: BRIEF`, dann gezielt lesen.** `search_files` mit
  `parentId` und BRIEF liefert die ersten ~1.000 Zeichen **jedes** Dokuments in
  **einem** Aufruf — Titel, Unterzeile, verworfene Varianten von zehn Posts,
  ohne eines zu öffnen. Die großen Dokumente sind 1,1–11,8 MB (eingebettete
  Bilder); `read_file_content` darauf ist teuer und meist unnötig.
  → betrifft: alle
- **Drive ignoriert `pageSize`, und die Seiten überlappen.** `pageSize: 100`
  übergeben, **5 Dateien** zurückbekommen; Folgeseiten 10, 10, 10, 5. Ohne
  Durchblättern über `pageToken` **sieht man den Ordner nicht** — und merkt es
  nicht. Beim Zusammenzählen deduplizieren, das letzte Element einer Seite ist
  das erste der nächsten.
  → betrifft: alle
- **Ein freigegebener Ordner ist nicht der ganze Bestand.** Ein Substack-Text
  hing unter einem ganz anderen Elternordner. **Nach Titel suchen, nicht nur
  nach Elternordner.**
  → betrifft: alle
- **`yt-dlp` ist nicht installiert, `pip install yt-dlp` läuft durch den Proxy.**
  Danach ohne Schlüssel und ohne OAuth: `yt-dlp --flat-playlist -J
  --playlist-end 100 "https://www.youtube.com/@<handle>/videos"` gibt Titel, IDs
  und Abozahlen. **Vorsicht bei Hintergrundaufrufen: ein `cd` wird
  zurückgesetzt**, eine Ausgabedatei landete im Repo-Wurzelverzeichnis statt im
  Scratchpad. Absolute Pfade, und vor dem Commit `git status`.
  → betrifft: alle
- **Das fünfte Vorbild ist verifiziert: `@jackneel`**, Kanal-ID
  `UCFRCiFkWWJN2rO6dsKU9-1A`, **3,52 Mio Abos**, am 21.10. geprüft. Es ist
  **Jack Neel**, nicht „Jack Neal" — Yannick hat den Link selbst geschickt,
  nachdem ich gefragt statt geraten hatte. Damit sind die fünf vollständig:
  Chris Williamson, Steven Bartlett, Mark Manson, Jay Shetty, Jack Neel.
  **Das ist genau der Fall, für den der Kanal da ist:** der Head of Content hat
  heute Stunden auf die Suche verwendet und „nicht verifizierbar" notiert,
  während die Antwort seit dem Vormittag in meinem Handbuch stand.
  → betrifft: youtube-manager, thumbnails, head-of-content, content-*
- **Kanalkennungen, geprüft:** `@ChrisWillx` · `@TheDiaryOfACEO` ·
  `@IAmMarkManson` · **`@JayShetty`** (`@JayShettyPodcast` gibt es nicht, HTTP
  404). Seiner: `UC5r4pxlAtt2alIOIGjdn4Qw`, 509 Abos, 38 lange Videos. Das fünfte steht
  eine Zeile höher — es war „Jack Neel", und die Frage war bereits beantwortet.
  → betrifft: youtube-manager, thumbnails, guest-booking
- **`substack.com` am 21.10. erneut geprüft: weiter 403 auf CONNECT**, ebenso
  `ynbernard.substack.com`. **Gebraucht wird es nicht mehr** — der Drive-Ordner
  `1zd-wlZ8YW7FnB7u_F6FeaU2NIdCYw75C` enthält die Posts samt den **verworfenen
  Titelvarianten**, die öffentlich nirgends stehen. Lesen ja, **Schreiben nicht
  freigegeben.**
  → betrifft: alle

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
