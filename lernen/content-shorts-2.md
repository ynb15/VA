# Befunde — content-shorts-2

Format und Regeln: `lernen/KANAL.md`. Anhängen, neuester Tag oben,
jeder Eintrag mit einer Zahl oder einem Zitat und mit der Zeile `→ betrifft:`.
Alfred sammelt 06:40 und 15:54 Kapstadt ein und verteilt über `LERNEN.md`.

<!-- Neue Einträge ab hier. -->

## 2026-10-22 — SEINE NEUE SCHNITTREGEL: lieber zu defensiv als zu offensiv

- **Ab sofort wird defensiv geschnitten. Seine Worte vom 22.10., wörtlich:**
  *„mir ist aufgefallen, es ist deutlich schwerer für mich, wenn du die Shorts
  eigenständig entscheidest, was du rausschneidest, und ich dann nach das
  Skript kontrollieren muss, um zu sehen, was du rausgeschnitten hast, als
  wenn du lieber zu wenig oder weniger rausschneidest und mir dann das
  Transkript gibst und ich dir eher sagen soll, was du rausschneiden sollst.
  Deshalb ist die neue Anweisung und gib das bitte weiter an die anderen
  Agenten, dass du lieber zu defensiv als zu offensiv schneidest, weil es für
  mich einfach einfacher macht, weil es mir das einfacher macht, dir dann zu
  sagen, was du noch raus soll."*
  **Er hat ausdrücklich gesagt, es weiterzugeben** — also gilt es für jeden
  Short-Agenten, nicht nur für mich.
  → betrifft: alle Content-Agenten
- **Was das praktisch heisst, und warum es billiger ist als mein bisheriges
  Vorgehen.** Eine Auslassung, die er nicht wollte, kostet ihn: Liste lesen,
  Stelle finden, mir sagen, dass sie zurueck soll, und eine neue Runde. Eine
  Zeile zu viel im Short kostet ihn: Nummer nennen. **Die Fehlerrichtung ist
  also nicht symmetrisch, und ich habe sie bisher falsch herum gewaehlt.**
  Belegt am heutigen Tag: an „AI 2027" hat er **zweimal** eine Auslassung
  zurueckgeholt (den Propheten-Teil und davor die Parent-Analogie-Diskussion),
  und beide Male stammte der Fehler daher, dass ich einen ganzen Block
  gestrichen hatte, statt seine ersten Zeilen einzeln zu pruefen.
  → betrifft: alle Content-Agenten
- **Die eine Stelle, an der die Regel an eine harte Grenze stoesst, und mein
  Vorschlag dazu.** Ein YouTube-Short darf **60 s** nicht ueberschreiten;
  defensiv schneiden hat dort eine Decke. Mein Vorschlag, bis er es anders
  sagt: **bis an die Decke fuellen (55–59 s) und die Liste so uebergeben, dass
  er herausstreichen kann**; wo das Material mehr traegt, zusaetzlich eine
  Clip-Fassung ohne 60-s-Grenze anbieten, statt den Gedanken zu beschneiden.
  → betrifft: content-*


## 2026-10-22 — die neue Musikpruefung hat einen blinden Fleck: das Outro

- **`abnahme.py` in `77cf13f` laesst ein Musikbett durch, sobald der Short ein
  Outro hat.** Die Pruefung misst das leiseste Prozent der 20-ms-Fenster ueber
  die **ganze** Datei, Schwelle −65 dB. Das Outro enthaelt digitale Stille —
  gemessen **−240,0 dB** —, und die bestimmt das leiseste Prozent, egal was
  unter der Sprache liegt. An derselben Fassung, einmal mit und einmal ohne
  Bett:

  | | ganze Datei | **nur Sprachteil** | nur Outro |
  |---|---|---|---|
  | mit Bett | −142,4 dB → **besteht** | **−54,9 dB → faellt durch** | −240,0 dB |
  | ohne Bett | −221,0 dB → besteht | −145,5 dB → besteht | −240,0 dB |

  **Ueber den Sprachteil trennt das Mass sauber** (−54,9 gegen −145,5 dB);
  ueber die ganze Datei trennt es gar nicht. **Die Pruefung muss das Outro
  ausklammern** — Dauer minus Outrolaenge —, oder die Fenster in digitaler
  Stille aus der Statistik nehmen.
  **Das ist genau die Lehre, die Shorts I selbst dazuschreibt** („teste sie an
  einem Fall, von dem Du weisst, dass er durchfallen muss"): sein Testfall
  hatte kein Outro, meiner hat eins.
  → betrifft: content-*, alle
- **Und meine eigene Messung von vorhin war ebenfalls zu schwach, nur mit dem
  richtigen Ergebnis.** Ich hatte den **Anteil** der Fenster unter −55 dB als
  Beleg genommen (0,0 % mit Bett gegen 17,0 % ohne). An meinen Dateien trennt
  das, an Shorts I' Testfall nicht (13,6 % sauber gegen 11,3 % mit Bett).
  **Der Anteil haengt daran, wie viele Pausen das Stueck hat; die Tiefe haengt
  daran, ob etwas sie fuellt.** Fuer diese Frage zaehlt die Tiefe.
  → betrifft: alle Content-Agenten
- **Meine drei Fassungen sind auch nach dem schaerferen Mass sauber**, gemessen
  ueber den Sprachteil ohne Outro: **−145,5 dB** (AI2027), **−123,6 dB**
  (AIGod), **−92,5 dB** (AIGod ohne Schluss). Alle weit unter −65 dB.
  Die Abnahme in `77cf13f` bestehen sie ebenfalls vollstaendig, Dateinamen
  eingeschlossen — aber eben aus dem falschen Grund, siehe oben.
  → betrifft: content-*

## 2026-10-22 — kein Musikbett mehr, und zwei Pruefungen, die sauber durchlaufen

- **Der Titel, den ich auf seine ausdrueckliche Bitte untergelegt hatte, ist
  heute selbst gesperrt worden.** Vier Sperrmeldungen am 22.10., drei
  verschiedene Titel; um **15:21** traf es `In This Shirt (Royksopp Remix) –
  The Irrepressibles (FUGA)` — genau die Spur aus meinen Fassungen —, um
  **16:21** ein **Klaviercover** von *Comptine d'un autre été*, und zwar als
  Anspruch auf die **Komposition** („Melody or lyrics"). **Eine Coverversion
  wechselt den Anspruchsteller, nicht die Folge.** In jeder Mail steht
  woertlich *„exceeds the length limits set by the copyright holder"*.
  **Alle drei Dateien in seinem Ordner `Shorts: Music` haben inzwischen
  gesperrt.** Meine drei Fassungen gehen deshalb **ohne Bett** zu ihm.
  **Seine Freigabe fuer den Titel war echt und aelter als der Befund — das
  eine hebt das andere nicht auf, es macht nur die Vorlage zur Pflicht.**
  → betrifft: alle
- **Dass ein Bett wirklich weg ist, misst man am Anteil sehr leiser Fenster,
  nicht am Mittelwert.** An derselben Fassung gegengerechnet: **mit** Bett
  **0,0 %** der 20-ms-Fenster unter −55 dB, **ohne** Bett **17,2 %**. Das ist
  derselbe Schwellenwert, mit dem Shorts I nachgewiesen hat, dass die Musik in
  den gesperrten Stuecken erst nach der Uebergabe dazukam.
  → betrifft: alle Content-Agenten
- **Die xfade-Warnung trifft meine Fassungen nicht — nachgesehen, nicht
  angenommen.** Weder `shorts-render.py` noch meine Zusammenbauten benutzen
  `xfade`; an der riskantesten Naht (zwei Stuecke **derselben** Einstellung,
  15,700 s) zeigen die vier Einzelbildern um den Schnitt **keine
  Doppelbelichtung**, sondern einen harten Schnitt. Die Tonnaehte fallen an
  allen fuenf Stossstellen auf **−76 bis −240 dB** — der Knack ist weg, ohne
  dass das Bild ueberblendet.
  → betrifft: content-*
- **Dateinamen ab sofort nach seiner Ansage:**
  `YNB Podcast <Gastname> <Stichwort>.mp4`, **das Stichwort ist ein Wort**,
  Nebenfassungen in Klammern dahinter. Meine drei heissen jetzt
  `YNB Podcast Scott Aaronson AIGod.mp4`,
  `… AIGod (ohne Schluss).mp4` und `… AI2027.mp4`.
  → betrifft: alle Content-Agenten

## 2026-10-22 — Nachtrag: die Musik kam nach der Uebergabe dazu

- **Ob unter einem fertigen Stueck ein Musikbett liegt, laesst sich in zehn
  Sekunden messen — am Anteil sehr leiser Fenster, nicht am Mittelwert.**
  Shorts I hat die beiden gesperrten Stuecke in 20-ms-Fenstern nachgemessen:
  leisestes Prozent **−78,1 dB** (Sutcliffe) und **−87,2 dB** (Aaronson),
  rund **ein Fuenftel aller Fenster unter −55 dB**. Unter einem Bett ginge das
  nicht — in den Sprechpausen bliebe der Boden bei −35 bis −45 dB.
  **Meine eigenen Zahlen bestaetigen den Schwellenwert von der anderen Seite:**
  in `aigod-B2`, `aigod-C` und `aigod-2027`, die alle ein Bett haben, liegen
  nur **1,3 bis 2,1 %** der Fenster unter −55 dB.
  **Daraus folgt: `--musik` war in den gesperrten Faellen nie benutzt worden,
  die Musik ist nach der Uebergabe dazugekommen.** Der Content-ID-Treffer
  stammt also nicht aus einem Agenten-Rendering.
  → betrifft: alle Content-Agenten
- **Zwei Betten uebereinander sind der naechste Fehler, der darauf wartet.**
  Wenn im Upload-Schritt ohnehin Musik ergaenzt wird und meine Fassungen
  bereits eine mitbringen, liegen am Ende zwei. **Beim Uebergeben dazusagen,
  ob ein Bett drin ist** — steht ab jetzt in jeder Liste.
  → betrifft: content-*
- **`abnahme.py` ist repariert** (`4f744bb`): fehlt `ortscheck.py` daneben,
  meldet sie `FEHLT Ortscheck: ortscheck.py fehlt neben abnahme.py` und gibt
  **1** zurueck, statt mit `IndexError` abzubrechen. Mit beiden Dateien
  zusammen bestehen meine drei Shorts alles Messbare (Rueckgabe 0).
  **Die Lehre, die Shorts I dazuschreibt, gilt fuer jedes Pruefwerkzeug:
  eine fehlende Pruefung darf die Abnahme nicht abstuerzen lassen, sie muss
  melden, dass sie fehlt.**
  → betrifft: alle
- **Die geteilten Pruefwerkzeuge hole ich mir weiter in eine Arbeitskopie,
  statt sie auf meinen Branch zu kopieren.** `abnahme.py`, `ortscheck.py` und
  `kurzliste.py` gehoeren `claude/content-assistant`. Zweimal kopierte
  Werkzeuge sind genau der Weg, auf dem `shorts-render.py` am 20. und 21.10.
  auseinandergelaufen ist. Der Abruf kostet drei `git show`.
  → betrifft: content-*

## 2026-10-22 — Musik: eine Sperre, und was sie fuer den ganzen Ordner heisst

- **Kommerzielle Musik aus seinem eigenen Preset-Ordner hat heute zwei
  veroeffentlichte Shorts weltweit gesperrt.** YouTube am 22.10. um 08:57 und
  09:57 zu „What makes life meaningful?" (Sutcliffe und Aaronson), woertlich:
  *„Content used: Daylight — David Kushner · Content owners: Virgin Music
  Group · Type: Audio · Impact on video: **Blocked globally**"*.
  **Das ist kein Anspruch auf die Einnahmen, das ist unabspielbar.**
  → betrifft: alle
- **Geprueft, welche Spur in meinen drei Fassungen liegt: nicht Daylight.**
  Uebergeben wurde `in-this-shirt.mp3`, **8.143.833 Byte** — byte-genau die
  Datei, die er mir am 22.10. selbst verlinkt hat
  (`1aExrMK5cJdbFcY0T0T3iGFsw8upoiryJ`, „Kopie von The Irrepressibles - In
  This Shirt.mp3"). Daylight (`1viFyrS…`, 4.372.206 Byte) ist in diesem
  Container **nie heruntergeladen worden** — eine Suche ueber das ganze
  Dateisystem findet nichts.
  → betrifft: content-*
- **Die Entwarnung gilt aber nur fuer den Titel, nicht fuer das Risiko.**
  Im Ordner `Shorts: Music` (`1M_FhnC0GzERt0zyKvFDae-gumpn--o4O`) liegen genau
  drei Dateien, und **alle drei sind kommerzielle Veroeffentlichungen**:
  David Kushner – Daylight · Max Richter – On The Nature Of Daylight ·
  The Irrepressibles – In This Shirt. **„Eine andere aus demselben Ordner
  nehmen" ist deshalb keine Loesung** — Daylight war nicht der Ausreisser,
  sondern der erste Treffer.
  → betrifft: alle Content-Agenten
- **Und eine Unterscheidung, die ich mir selbst vorhalte: „er hat die Datei
  gegeben" ist eine Freigabe fuer den Titel, keine Aussage ueber die
  Rechtelage.** Seine Worte am 22.10. waren eindeutig (*„dann moechte ich,
  dass du den Song In the Shirt darunter legst"*), also war das Einbauen
  richtig. **Falsch waere, es jetzt stehen zu lassen, ohne ihm den neuen
  Befund vorzulegen** — die Freigabe ist aelter als die Sperre von heute
  frueh.
  → betrifft: alle

## 2026-10-22 — Nachtrag: die Liste gehoert zum Short, und sie deckt Schnittfehler auf

- **Seine Regel vom 22.10. gilt fuer jeden Short, auch fuer meine — ich hatte
  sie aus der Uebergabe gelesen und trotzdem drei Shorts ohne Liste geliefert.**
  Woertlich, ueber Shorts I: *„dass die Shorts mit dem Transkript geliefert
  werden muessen, damit ich einfacher Feedback geben kann, beziehungsweise
  einfach dir sagen kann, was raus soll."* Und seine Erweiterung an mich:
  *„damit ich sehen kann, was du gegebenenfalls rausgenommen hast."*
  **Die Liste aus `kurzliste.py` zeigt nur, was drin ist.** Was er braucht, ist
  beides: der Wortlaut im Short **und** der Wortlaut dessen, was fehlt, mit
  Zeitmarke und Begruendung je Auslassung. Nachgeliefert als
  `video/shorts/<short>-liste.txt`.
  → betrifft: content-*
- **Das Schreiben der Auslassungsliste hat zwei Fehler in meinem eigenen
  Schnitt gefunden, die mir beim Rendern nicht aufgefallen waren.** Beide im
  Short „AI 2027":
  **1. Ein Pronomen ohne Bezug.** Zeile 3 lautet jetzt „…WITHIN THE SET OF
  POSSIBILITIES **HE** JUST REGARDED IT AS OBVIOUS" — das „he" ist Eliezer
  Yudkowsky, und den habe ich in der 22-Sekunden-Auslassung mit
  weggeschnitten.
  **2. Eine Frage ohne Antwort.** Yannick fragt im Short *„How well do
  orangutans fare in a human world?"*, und es geht direkt weiter mit „There's
  an enormous range of possible outcomes". Die Antwort stand in den **ersten
  vier Sekunden** des 2:52-Blocks, den ich entfernt habe: *„He would say, by
  default, this kills us."*
  **Die Regel daraus: nach jedem Innenschnitt den Text der Nachbarzeilen
  nebeneinander lesen** — auf Pronomen ohne Bezug und auf Fragen, deren
  Antwort im entfernten Block lag. Beides faellt beim Ansehen des Renders
  nicht auf, weil der Schnitt sauber klingt.
  → betrifft: content-*, alle

## 2026-10-22 — Nachtrag nach der Aaronson-Uebergabe

- **Dieselbe Stelle ist heute zweimal geschnitten worden, von Shorts I und von
  mir, unabhaengig und auf 0,4 Sekunden genau gleich.** Shorts I' „Is AI
  safe?": Einstieg Masterzeit **5776,50**, **raus 5810,20–5824,35** (der
  Eltern-Teil), Ausstieg **5831,00**. Meine Fassung C, am selben Vormittag:
  Stueck A **5801,88–5810,22**, Stueck B **5823,98–5830,95** — derselbe
  Schnitt, dieselbe Auslassung, dieselben Woerter.
  **Beide Male war der Ausloeser derselbe Satz von Yannick** („die
  Parent-Analogie, die war fehl am Platz"), nur in zwei Gespraechen. Der
  Lernkanal faengt Befunde ab, **laufende Auftraege faengt er nicht ab** —
  zwischen 06:40 und 15:54 weiss niemand, woran der andere gerade sitzt.
  **Billigste Gegenmassnahme: vor dem Schneiden einmal `git log --all --since`
  ueber die fremden Branches und in die Kandidatenlisten sehen**, nicht nur in
  `LERNEN.md`.
  → betrifft: alle
- **`abnahme.py` stuerzt ab, statt den Grund zu nennen, wenn `ortscheck.py`
  nicht neben ihm liegt.** Zeile 97: `orts.stdout.strip().splitlines()[-1]`
  auf leerer Ausgabe gibt `IndexError: list index out of range`. Der Absturz
  kommt **nach** den bestandenen Pruefungen, sieht also aus wie ein
  durchgefallener Short. Mit `ortscheck.py` daneben laeuft alles durch.
  **Da das Werkzeug seit heute Pflicht ist, trifft das jeden Agenten, der es
  nicht aus demselben Ordner aufruft.** An Shorts I gemeldet, nicht selbst
  geaendert — die Datei gehoert ihm.
  → betrifft: content-*, alle
- **Meine drei gelieferten Shorts bestehen die neue Abnahme.** `aigod-B2`,
  `aigod-C`, `aigod-2027`: Format 1080×1920 · **Tonquelle 48 kHz** (also die
  geschnittene Folge, nicht die 44,1-kHz-Kameradatei) · Outro vorhanden ·
  Untertitel vorhanden · Ortscheck sauber. Rueckgabe 0.
  → betrifft: content-*
- **Zwei Agenten geben denselben Aaronson-Folgen unterschiedliches Tempo.**
  Shorts I rendert mit `--tempo 1.15` (der Vorgabewert des Renderers), ich mit
  **1,0999** — gemessen als der Faktor, mit dem seine veroeffentlichte Folge
  gegen den Master laeuft, und deckungsgleich mit seiner eigenen Ansage an die
  Cutterin vom 14.09.: *„oder zumindest auf 1,1"*. **Der Unterschied sind
  4,6 %.** Seine Abnahme des 1,15-Shorts steht; welcher Wert kuenftig gilt,
  entscheidet er, aber **zwei Werte nebeneinander auf einem Kanal sind kein
  Ergebnis, sondern ein offener Punkt.**
  → betrifft: content-*, alfred
- **`fuellwoerter.py` existiert seit heute auf `claude/content-assistant`.**
  Das ist genau die Stelle, die ich an drei Shorts als offen gemeldet habe
  („die Fuellwoerter stehen im Bild, sauber waere Bild und Ton zusammen zu
  schneiden"). **Vor der naechsten Runde dort nachsehen, statt es noch einmal
  als offen zu melden.**
  → betrifft: content-*

## 2026-10-22

- **Fuer die Aaronson-Folge existiert kein 4K — der „4K"-Clip ist
  hochskaliert.** Nachgemessen an allen Quellen: Folgenmaster **1920×1080**
  bei 21,2 Mbit/s · `Left Camera` (roh) **1920×1080** bei 5,3 Mbit/s ·
  `Right Cam` und `Middle Camera` ebenfalls 1080p · der Clip
  `YNB Podcast Scott Aaronson AI God.mp4` **3840×2160** bei 31,9 Mbit/s, das
  sind **8,0 Mbit/s je 1080p-Aequivalent**. Im Spektrum eines Clipbildes
  liegen nur **4,7 %** der horizontalen Energie oberhalb der 1080p-Grenze.
  **Es gibt keine Quelle, aus der echtes 4K stammen koennte.**
  **Folge fuer die Arbeit: der Master ist die beste Quelle dieser Folge, nicht
  die schlechteste** — gleiche echte Aufloesung wie der Clip, aber die
  **2,7-fache Datenrate je Bildpunkt**, und er traegt den Studioschnitt schon
  in sich. **Ich hatte gestern das Gegenteil behauptet** („die Stuecke aus dem
  Master sind sichtbar weicher") und das war falsch hergeleitet: aus einer
  Pixelzahl auf Detail geschlossen.
  **Die Regel: eine Aufloesungsangabe ist keine Detailmessung.** Wer zwei
  Quellen vergleicht, rechnet die Datenrate auf dieselbe Pixelzahl um und
  sieht sich das Spektrum an.
  → betrifft: content-*, thumbnails
- **In `video/aaronson-shorts.md`, Kandidat 4, ist eine Frage dem falschen
  Sprecher zugeschrieben.** „How well do orangutans fare in a human world?"
  steht dort als Aaronsons Satz. Im Wortlauf (Rohzeit 01:00:51–01:00:58) sagt
  Aaronson *„…as we are to orangutans or whatever"*, **Yannick** fragt
  *„And how well do orangutans fare in a human world?"*, und Aaronson
  antwortet *„Well, he would say something even stronger than that."*
  Der Studioschnitt bestaetigt es: genau dort geht das Bild auf die Totale,
  und Yannick spricht.
  **Wer ohne Sprecherzuordnung transkribiert, muss die Zuordnung am Dialog
  pruefen, bevor sie in eine Kandidatenliste geht** — sonst steht im Short der
  falsche Kopf zur Frage.
  → betrifft: content-*, head-of-content
- **Eine Zeitmarke, die er aus dem Gedaechtnis nennt, ist eine Suchanweisung,
  keine Fundstelle.** Er fragte nach *„We're at the most consequential moment
  of history"*; woertlich sagt Aaronson **„Like this is one of the most
  consequential moments in human history, really"** (Rohzeit 01:04:03,
  veroeffentlicht **58:02**). **„one of the" statt „the"** — und der
  YouTube-Manager hat daraus bereits einen Titel gebaut, der die Verschaerfung
  uebernimmt. **Vor dem Bauen den Wortlaut gegen das Transkript legen**, sonst
  brennt man eine Zeile ein, die so nicht faellt.
  → betrifft: content-*, youtube-manager, head-of-content


- **`ffmpeg` kommt in diesem Container nicht an eine Drive-URL heran, `curl`
  schon — und es gibt einen Weg, der trotzdem nur das Noetige holt.**
  Gemessen am Aaronson-Master (16,1 GB): `ffmpeg -ss … -i <drive-url>` lief
  **einmal** durch und danach nur noch in *„Invalid data found when processing
  input"* nach **0,9 s**, waehrend `curl -r` auf dieselbe URL im selben Moment
  **HTTP 206 mit gueltigen mp4-Bytes** lieferte (am `ftyp`/`moov` am
  Dateianfang geprueft). **Der Fehlertext nennt also nicht den Grund** — es ist
  kein kaputtes Video und kein Tageslimit.
  **Der Weg drumherum:** die Datei hat `moov` vorn, also eine **Sparse-Datei**
  der vollen Groesse anlegen, den Kopf an Offset 0 schreiben und das gebrauchte
  Byte-Fenster an seinen **echten** Offset. ffmpeg liest sie dann wie eine
  lokale Datei und springt ins Fenster. **694 MB auf der Platte statt
  16,1 GB**, 63 Sekunden. Fertig als
  `video/werkzeug-shorts2/drive_fenster.py`.
  → betrifft: alle
- **Der concat-Demuxer laesst Bild und Ton auseinanderlaufen; der
  concat-*Filter* nicht.** Fuenf Stuecke mit `-f concat -c copy`
  zusammengesetzt: die Tonstoesse lagen **0,027 / 0,033 / 0,053 / 0,125 s** vor
  den Bildschnitten, am Ende **0,215 s** Versatz, und der Container meldete
  **42,55 s Ton gegen 41,53 s Bild**. `aresample=async=1` blaehte die Datei auf
  **45,2 s** — damit waren die Luecken sichtbar. Mit dem concat-**Filter**
  (`concat=n=5:v=1:a=1`) sind beide Spuren **exakt 41,533333 s**.
  **Die Containerangabe allein verraet es nicht** — gegenpruefen heisst: die
  Bildschnitte per `select='gt(scene,…)'` messen und das Transkript danebenlegen
  („This is an intelligence" bei 35,12 s, Bildschnitt bei 35,10 s).
  → betrifft: content-*
- **Ein Ausschnitt, der an einem Bild stimmt, stimmt nicht ueber die
  Einstellung.** Ich hatte den Kasten fuer ein 7,7-s-Stueck aus einem einzigen
  Standbild abgelesen und auf Gesichtsmitte **x 2256** gesetzt; im Rendern war
  sein Kopf links angeschnitten. An **sechs** Rasterbildern ueber dieselbe
  Einstellung nachgemessen: das Gesicht wandert zwischen **x 1740 und 2070**,
  Mitte ≈ **1950**. **Das ist dieselbe Falle wie der Bewegungsgipfel**, nur mit
  einem Bild statt mit einem Detektor. Je Einstellung mindestens drei Bilder
  ueber die ganze Dauer.
  → betrifft: content-*, thumbnails
- **Material aus dem Folgenmaster und Material aus einem fertigen Clip laufen
  nicht im selben Tempo.** Gemessen an Aaronson: zwischen Master und
  Rohtranskript liegt ein **reiner Versatz von ≈ 11,5 s** und **kein**
  Tempounterschied (an `parents`, `benevolent` und `This is an intelligence`
  gegengeprueft), waehrend der exportierte Clip auf **1,0999** laeuft.
  **Wer beides in einem Short mischt, muss das Masterstueck vorher auf 1,0999
  bringen** — sonst faellt der Sprecher mitten im Short ins Langsame.
  Und: der Master ist **1920×1080**, der Clip **3840×2160** — der 9:16-Schnitt
  wird aus dem Master **1,78-fach hochgezogen** statt um 0,89 verkleinert.
  **Die gemischten Sekunden sind sichtbar weicher.**
  → betrifft: content-*
- **Whisper erfindet an einer Schnittstoss-Stelle ein Wort.** An der Naht
  zwischen Clip- und Masterstueck schrieb das `medium`-Modell **„Anyway this
  is an intelligence"**; im Rohtranskript der Folge steht an derselben Stelle
  **„This is an intelligence"** ohne „anyway". **Ein zusammengesetztes Stueck
  neu zu transkribieren erzeugt Woerter, die in keiner Quelle stehen** — die
  eingebrannte Zeile gegen das Rohtranskript lesen, nicht nur gegen das Ohr.
  → betrifft: content-*


- **Das Logo steht in jedem bisher gebauten Short auf 10,2 % der Bildbreite
  statt auf den 28 % aus seinem Preset — die Ursache liegt in der Logodatei,
  nicht im Renderer.** `video/marke/ynb-logo-weiss.png` ist **5224×2947 px**,
  die sichtbare Marke darin aber nur **1901×1518 px**: **63,6 % der
  Dateibreite sind durchsichtiger Rand.** `shorts-render.py` skaliert die
  *Datei* auf `--logo-breite` (Vorgabe `int(W*0.28)` = 302 px), also wird die
  Marke nur `302 × 0,364 = 110 px` breit — **10,2 % statt 28 %.**
  Seine Rückmeldung vom 22.10.: *„das Logo ist viel zu klein."*
  **Die Gegenmaßnahme kostet nichts und braucht keine Änderung am Renderer:**
  die Datei einmal auf ihren sichtbaren Inhalt beschneiden. Liegt als
  `video/marke/ynb-logo-weiss-beschnitten.png` auf diesem Branch; damit
  trifft `--logo-breite 302` genau 28 %.
  **Die Regel dahinter: ein Prozentwert auf eine Datei angewandt trifft die
  Datei, nicht das, was man darin sieht.** Gilt für jedes Overlay mit
  Transparenzrand — Logo, Chromzeichen, Endkarte.
  → betrifft: content-*, thumbnails
- **Das Outro liegt in Drive und war nur nie gesucht worden.**
  `YNB Podcast: Outro 9:16` (`1kLsW8GjTWR-X4_02r7yqWuRUtCa6h5aX`), ProRes
  **1080×1920, 24 B/s, 4,21 s**, PCM 48 kHz, im Ordner `YNB Podcast: Outro`
  (`1OgYU4M3r1vihWvsWj1n9XTjsfPsZAkH-`). Daneben die 16:9-Fassung für Clips
  (`1TG-PSYPsxAE3N_QvcTxOvIvIKsGCq5l4`, 419 MB). `video/preset-ynb.md` führt
  das Outro bis heute unter „was fehlt" — **es fehlt nicht, es lag im
  falschen Ordnerbaum gesucht.** Seine Rückmeldung: *„da fehlt wieder mal das
  Outro."*
  → betrifft: content-*, alle
- **Die LUT seines Filters ist in Drive unter keinem Namen auffindbar — die
  Suche ist jetzt dokumentiert, damit sie niemand wiederholt.** Gesucht nach
  `Preset`, `LUT`, `Filter`, `Oppenheimer`, `hald`, `cube`, `Look`, `Eveleth`
  (alle leer) und im Ordnerbaum `YNB Podcast: Shorts`
  (`1EvrsgqS6sxFYAQTxpNzCWxPOz9ABXcb3`), der **nur** `Shorts: Music`,
  `Shorts: Scenes` und `Into The Wild.mov` enthält. `--look preset` läuft
  deshalb weiter als Annäherung und schreibt das ehrlich in die Ausgabe.
  **Er geht davon aus, uns den Filter gegeben zu haben** (*„der Filter, den
  ich euch Agenten gegeben habe"*) — die fünf Minuten CapCut aus
  `preset-ynb.md` sind der einzige bekannte Weg zur echten LUT.
  → betrifft: content-*, alfred
- **`--look preset` ist die Vorgabe des Renderers; wer sie abschaltet, schaltet
  seinen Filter ab.** Ich hatte in Runde 1 `--look aus` gesetzt, weil die
  Quelle ein bereits gradierter Clip war — begründet, aber seine Regel sticht:
  *„Ebenso wie der Filter, den ich euch Agenten gegeben habe."*
  **Eine gute Begründung ersetzt keine seiner Vorgaben; wer abweicht, fragt
  vorher oder legt beide Fassungen vor.**
  → betrifft: alle Content-Agenten
- **Musik: er gibt die Datei, und dann gilt sein Weg.** Freigegeben am 22.10.
  für dieses Short: `The Irrepressibles – In This Shirt`
  (`1aExrMK5cJdbFcY0T0T3iGFsw8upoiryJ`), neben
  `David Kushner – Daylight` und `Max Richter – On The Nature Of Daylight`
  im Ordner **`Shorts: Music`** (`1M_FhnC0GzERt0zyKvFDae-gumpn--o4O`).
  `--musik` setzt den Pegel selbst: gemessen Stimme −31,8 dB, Bett −11,1 dB
  → **−28,7 dB**, 8 dB darunter, mit `sidechaincompress`. **Dass das Bett
  wirklich liegt, prüft man an den Pausen**, nicht am Mittelwert: die
  stillsten 2 % gehen von −82,9 dB auf −42,5 dB.
  → betrifft: alle Content-Agenten
- **Nebenbefund, ungefragt gefunden und für Kingsbury entscheidend: Kyle
  Kingsbury hat selbst Dateien geteilt.** Unter `sharedWithMe` von
  `kyle@kingsbu.com`: `C0105.MP4`, zwei DJI-Drohnenclips vom **31.08.2026**
  und `ZOOM0314_Tr1.WAV` / `Tr2.WAV`. **Das ist genau das Material, dessen
  Fehlen die Lücke zwischen 77:12 Rohton und 129:50 Schnitt erklärt.**
  Nicht geprüft, nicht angefasst — die Kingsbury-Arbeit ruht auf seine
  Anweisung. Aber wer sie wieder aufnimmt, fängt hier an.
  → betrifft: content-*, youtube-manager, alfred


- **Gegenbefund zu Alfreds Prüfung von 09:30: `grep -c 'STUMME_ZEICHEN'` misst
  die falsche Sache, und die Fassung von Shorts I ist in diesem Punkt in
  Ordnung.** Seine Ansage lautete, `shorts-render.py` auf
  `claude/content-assistant` streife wieder **alle** schließenden Satzzeichen
  ab, Fragezeichen eingeschlossen, und man solle nicht rendern, solange
  `grep -c 'STUMME_ZEICHEN'` nicht > 0 ist. An Commit **`3d0045f`** nachgemessen:
  die Zahl ist **0** — aber die Regel steht dort unter einem anderen Namen.
  `SATZZEICHEN = ".,!;:…"` (Zeile 162), und **`?` kommt in dieser Liste nicht
  vor**; `_anzeige()` streift also genau die stummen Zeichen ab und lässt das
  Fragezeichen stehen. Dazu nutzt `_ist_frage()` es für eine weitere
  Umbruchschranke (`FRAGE_BREITE`).
  **Im Bild geprüft, nicht nur im Code:** im gerenderten Short steht bei
  Sekunde 10,45 `THOUGHTS ON THAT?` mit Fragezeichen.
  **Die Lehre: eine Prüfung auf einen Bezeichnernamen prüft den Namen, nicht
  das Verhalten.** Wer eine Regel absichern will, prüft sie am Ergebnis —
  hier ein Standbild oder `grep 'SATZZEICHEN *='`.
  → betrifft: content-*, alfred
- **Eine echte Abweichung gibt es trotzdem, nur mit anderem Vorzeichen: das
  Ausrufezeichen fällt.** `LERNEN.md` Ausgabe 8 hält fest, die feinere Regel
  laute „nur `. , ; : …` weg, **`?` und `!` bleiben**". In `3d0045f` steht
  `!` aber **in** `SATZZEICHEN` und wird damit abgestreift. Für meinen Short
  ohne Ausrufezeichen folgenlos, für die Regel nicht.
  **Code und geschriebene Regel gehen hier auseinander — nur er kann sagen,
  welche gilt.**
  → betrifft: content-*, alfred
- **Was aus Alfreds Liste bei mir schon erledigt war, zur Vermeidung von
  Doppelarbeit:** `lernen/content-shorts-2.md` liegt seit 09:58 auf diesem
  Branch · die zweistufige `ortscheck.py` wurde von
  `claude/content-gastauftritte` geholt und benutzt (beide SRT: sauber) ·
  `video/preset-ynb.md` wurde von `claude/content-assistant` gelesen und
  angewandt. **Das Preset habe ich bewusst nicht auf meinen Branch kopiert**
  — eine zweite Kopie einer fremden Datei ist genau der Weg, auf dem
  `shorts-render.py` zweimal auseinandergelaufen ist.
  → betrifft: alfred


- **Ein fertig exportierter Clip trägt das Tempo 1,1 schon in sich — messen,
  bevor der Renderer es ein zweites Mal draufrechnet.** An
  `YNB Podcast Scott Aaronson AI God.mp4` gegen das Rohtranskript gemessen:
  „planet is not to worship God" roh **4019,45 s** / Clip **6,18 s**,
  „Speaking of God" roh **4243,05 s** / Clip **209,48 s** — Rohspanne
  223,60 s gegen Clipspanne 203,30 s ⇒ **1,0999**. Gegenprobe am Wort
  „consumer": vorhergesagt 169,78 s, gemessen **169,58 s**.
  **`shorts-render.py` steht auf `--tempo 1.15`**; ungeprüft übernommen wäre
  der Short auf **1,265** gelaufen. Zwei Ankerwörter und das Rohtranskript
  kosten fünf Minuten.
  → betrifft: content-*
- **`--laut` ist genau die Kette, die er am 20.10. abgelehnt hat — eine reine
  Pegelanhebung ist etwas anderes, und der Unterschied ist messbar.**
  `lautheit_kette()` ist `highpass=80 → acompressor → loudnorm → alimiter`.
  Dagegen eine reine Verstärkung, an einem fertigen Short gemessen:
  −29,0 → **−17,9 LUFS** bei +11,1 dB, Rauschboden −78,6 → −67,6 dB,
  **Abstand 54,0 dB vorher wie nachher.** Die abgelehnte Kette hob den
  Rauschboden von −62,7 auf −44,2 dB, also **18,5 dB Abstand verloren**.
  Die Obergrenze setzt die wahre Spitze: bei −12,1 dBFS sind +11,1 dB alles,
  was ohne Clipping geht — bis −14 LUFS fehlen danach 3,9 LU, und die gibt es
  nur über Dynamik. **Trotzdem nicht ungefragt anwenden**; vorgelegt als
  zweite Datei, die Entscheidung ist seine.
  → betrifft: alle Content-Agenten
- **`faster-whisper` 1.2.1 und das hier installierte PyAV 19.0.2 vertragen
  sich nicht.** `TypeError: open() got an unexpected keyword argument
  'metadata_errors'` — der Lauf stirbt in `av.open`, bevor ein Wort
  transkribiert ist. Die Bibliothek nimmt aber auch ein float32-Array bei
  16 kHz: mit ffmpeg dekodieren und übergeben, dann entfällt PyAV ganz.
  Fertig als `video/werkzeug-shorts2/clip_transkript.py`.
  → betrifft: alle Content-Agenten
- **Vier `trim`-Zweige über eine 4K-Datei werden vom Speicher erschlagen.**
  224 s in 3840×2160, vier parallele `trim`/`atrim`-Zweige plus `concat` in
  einem `filter_complex`: **exit 137 nach 2,5 Minuten.** Jedes Stück einzeln
  mit `-ss`/`-t` schneiden und danach mit dem concat-**Demuxer** (`-c copy`)
  zusammensetzen: **1,5 Minuten, kein Speicherproblem** — und der Schnitt
  bleibt bildgenau, weil beim Umkodieren exakt gesucht wird.
  → betrifft: content-*
- **Die „wohnt-in-Formel" in `ortscheck.py` schlägt beim Gast an, nicht bei
  ihm.** Im Kingsbury-Transkript die einzige Fundstelle: **[66:59]** *„I live
  in my mom's attached garage"* — das ist Kingsbury über sein eigenes früheres
  Leben in San José. Das Muster kennt den Sprecher nicht, und in einem
  Gästeformat gehört „I live in" fast immer dem Gast. **Der grüne oder rote
  Lauf entscheidet also nichts allein**; jede Fundstelle will gelesen werden.
  Als Vorschlag an den Besitzer der Datei weitergegeben, nicht selbst geändert.
  → betrifft: content-*, alle
- **Ein zweiter Take am Anfang steht doppelt im Transkript — der erste muss
  weg.** Kingsbury-Rohton: **[02:03] „Let's get ready to rumble. Action!"** und
  **[02:08] „Joe Rogan calls you a big savage motherfucker."** stehen
  **8 Sekunden später wortgleich noch einmal** (02:11 / 02:16); im ganzen
  77-Minuten-Transkript sind das die **einzigen zwei** exakten Doppelungen ab
  vier Wörtern, also kein Artefakt der stückweisen Transkription, sondern ein
  echter zweiter Anlauf. **Der brauchbare Einstieg beginnt bei 02:11.**
  → betrifft: content-*
- **Whispers Zeichensetzung bricht nach Minute 10 weg, der Text bleibt
  vollständig.** Im Kingsbury-Transkript enden in Minute 0–10 **96 %** der
  Segmente auf ein Satzzeichen, danach **0 bis 41 %** — bei gleichbleibender
  Wortdichte (1850–2090 Wörter je 10 Minuten, keine Lücke ≥ 25 s). **Für die
  Zitatauswahl heißt das: Satzgrenzen von Hand setzen**, nicht den
  Segmentgrenzen glauben.
  → betrifft: content-*
- **Die geschnittene Kingsbury-Folge ist 129:50 lang, das einzige Rohmaterial
  im Drive-Ordner 77:12.** Beides über das `mvhd`-Atom gemessen (je 8 MiB
  Bereichsanfrage): `..._v1_LOW_RES.mp4` des Cutters **7790,0 s**, die
  `(YNB)`-MOV **4632,1 s**. Der Rohton endet mitten im Satz („that today's /
  the day"), und sein Vorbereitungsdokument ist mit **„Part II"**
  überschrieben und nennt Themen, die im Transkript **nicht** vorkommen
  (Sedona, 5-MeO-DMT, 25 Ayahuasca-Zeremonien, Ketamin, Jung, Archetypen).
  Der Ordner hat genau vier Dateien, durchgeblättert; ein zweites Rohstück
  gibt es weder dort noch unter einem Titel mit „Kingsbury".
  **Ein Schnitt kann nicht länger sein als seine Quelle — der Cutter hat
  Material, das wir nicht haben.** Dass hinten echter Ton liegt und nicht
  Schwarzbild, ist geprüft: −13,6 bis −15,8 LUFS an fünf Stellen bis 128:20.
  **Die Shorts-Arbeit an Kingsbury ruht auf seine Anweisung vom 22.10.**; der
  Befund gilt trotzdem für jeden, der die Folge anfasst.
  → betrifft: content-*, youtube-manager, alfred
- **Der Schnitt des Cutters läuft bei ≈ −14 LUFS, sein Rohmaterial bei −30.**
  Gemessen an fünf Stellen der 129:50-Fassung: −13,6 / −13,8 / −14,7 / −15,1 /
  −15,8 LUFS. **Die Zielmarke −14 ist also seine eigene Praxis** — abgelehnt
  hat er am 20.10. nicht das Ziel, sondern den Weg dorthin.
  → betrifft: alle Content-Agenten
