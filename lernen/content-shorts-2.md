# Befunde — content-shorts-2

Format und Regeln: `lernen/KANAL.md`. Anhängen, neuester Tag oben,
jeder Eintrag mit einer Zahl oder einem Zitat und mit der Zeile `→ betrifft:`.
Alfred sammelt 06:40 und 15:54 Kapstadt ein und verteilt über `LERNEN.md`.

<!-- Neue Einträge ab hier. -->

## 2026-11-12 (spaeter) — zwei Fehler, die nur im Vergleich zweier Shorts auffallen

- **„--laut aus" heisst nicht, dass am Pegel nichts zu tun ist.** Sein
  Befund: *„bei dem Meaning Short ist der Ton deutlich leiser als in dem
  Ubuntu-Short."* Gemessen am Hauptteil: **Ubuntu -29,7 LUFS, Meaningful
  -33,7 LUFS, Aging -27,5 LUFS.** Die Ursache ist nicht der Schnitt,
  sondern **wer spricht**: im Ubuntu-Short redet fast durchgehend er, im
  Meaningful-Short fast durchgehend Ken, und Kens Mikro liegt im Master
  leiser. Ohne Lautheitsangleichung steht dieser Unterschied am Ende im
  Short.
  **Regel: bei einem Short, in dem ueberwiegend der Gast spricht, den
  Hauptteil gegen das zuletzt abgenommene Short messen und per
  Festverstaerkung angleichen** — reine Verstaerkung auf die Vorlage, vor
  dem Outro, damit das Outro seinen Pegel behaelt. Hier +4,0 dB, Spitze
  vorher -12,6 dB.
  → betrifft: alle Content-Agenten
- **Unterschiedliche Zeilenhoehen sind nur gefahrlos, solange keine
  Einblendung ueber einen Einstellungswechsel laeuft.** Sein Befund: *„da
  gibt's nochmal einen kleinen Fehler, wo die Schrift sich bewegt."*
  Gefunden: zwei Cues kreuzten einen Kameraschnitt („HELPING OTHERS" bei
  8,07 s, „THAT GIVES MOST" bei 15,23 s). `cues_an_lippen` teilt so einen
  Cue in zwei Teile und gibt jedem die Hoehe seiner Einstellung — 1200 und
  1080. **Derselbe Text springt dann mitten im Wort um 120 Pixel.**
  **Vor dem Rendern pruefen, ob ein Cue eine Grenze kreuzt** (SRT gegen die
  Grenzen der Einstellungen); wenn ja, bekommen beide dieselbe Hoehe, im
  Zweifel das ganze Short eine. Hier 1140 fuer alle vier — an allen drei
  Ausschnitten 95 bis 220 px unter dem Kinn.
  → betrifft: alle Content-Agenten
- **Beide Fehler waren im einzelnen Short unsichtbar und fielen erst im
  Vergleich zweier Shorts auf.** Der Pegel klingt fuer sich in Ordnung, die
  Schrift springt nur an zwei von 64 Einblendungen. **Vor der Auslieferung
  gehoert ein Short gegen das zuletzt abgenommene gehalten — Lautheit
  messen, und die Cues gegen die Einstellungsgrenzen pruefen.** Beides sind
  zwei Befehle, keine zwei Minuten.
  → betrifft: content-*, alle

## 2026-11-12 — ein Suchausschnitt ist kein Inhaltsverzeichnis

- **Ich habe ihm eine Frage gestellt, deren Antwort im Dokument stand, das
  ich schon in der Hand hatte.** Die Drive-Volltextsuche liefert einen
  Ausschnitt **vom Dateianfang**, nicht um den Treffer herum. Bei seinem
  Vorbereitungsdokument zu Ken Stern brach der Ausschnitt genau **eine
  Zeile** vor `1:17:55 edit & Short: Aging` ab — nach `1:05:00 Short:
  Ubuntu`. Daraus hatte ich geschlossen, es gebe keine Marke, und gefragt.
  Seine Antwort: *„Willst du mich verarschen? Schau ins Transkript du
  trottel."* Berechtigt.
  **Regel: wenn eine Datei die Antwort haben koennte, wird sie gelesen
  (`read_file_content`), nicht nach dem Suchausschnitt beurteilt.** Das
  ganze Dokument sind 7 kB Text — ein einziger Aufruf. Der Ausschnitt hatte
  90 % gezeigt und genau die fehlende Zeile verschluckt.
  → betrifft: alle Agenten
- **Eine Einstellungsgrenze wird auf die Bildzeit ABGERUNDET, nie
  aufgerundet.** Ich hatte **32,3667** geschrieben; Bild 971 liegt bei
  **32,366667**. Der Renderer prueft `t < ende`, und 32,366666 < 32,3667 ist
  wahr — Bild 971 bekam den Kasten der vorigen Einstellung. In der Totale
  zeigt dieser Kasten den **leeren Tisch**, ein Bild lang, mitten im Short.
  **0,4 Millisekunden Rundungsfehler, ein sichtbarer Fehler.** Schreibweise
  ab jetzt: Bildnummer durch 30, abgeschnitten statt gerundet.
  → betrifft: alle Content-Agenten
- **Manches Material passt nicht unter 60 Sekunden, und das ist kein
  Schnittfehler.** Frankl-Zitat 25,3 s plus sein Essay 42,7 s plus
  Ueberleitung und Outro = 75,4 s bei Tempo 1,1, ohne ein einziges
  Fuellwort. **Statt heimlich zu kuerzen: die Zahl nennen, drei Wege mit
  Laengen anbieten und ihn entscheiden lassen.** YouTube laesst Shorts seit
  Oktober 2024 bis drei Minuten zu, das Format ist also nicht das Problem.
  → betrifft: content-*, alle
- **Sein Vorbereitungsdokument markiert die Schnittstellen selbst.** Neben
  `1:17:55 edit & Short: Aging` steht an anderer Stelle `5:14: edit out` und
  `57:12 - 1:06:00 raeuspern edit`. **„edit" heisst: dort ist etwas, das
  raus muss.** Hier war es sein Fehlstart beim Vorlesen („Sorry, I'll read
  that again", 11 s). Wer das Dokument liest, weiss die Auslassung vorher.
  → betrifft: content-*

## 2026-11-11 (nachts) — dritte Musikansage, dritte Variante

- **Er hat jetzt dreimal etwas anderes zum Ende des Betts gesagt, und jedes
  Mal war es fuer genau dieses Stueck gemeint.**
  22.10., AI 2027: *„dass er es nicht vorm Ende aufhoert."*
  26.10., Safety: *„bitte in this shirt unterlegen aber vor dem Outro
  aufhoeren."*
  11.11., beide Ken-Shorts: *„bei beiden soll die Musik laenger laufen und
  dann mit dem Outro ausfaden."*
  **Das ist die dritte Variante, und sie bestaetigt die Regel vom 26.10.:
  bei Musik wird nicht aus dem vorigen Short geschlossen, sondern gefragt.**
  Technisch sind es drei Zeilen derselben Kette: `atrim` setzt das Ende,
  `afade=t=out` liegt davor, am Hauptteil-Ende oder ueber dem Outro.
  Fuer „mit dem Outro ausfaden": `atrim=0:<gesamt>` und
  `afade=t=out:st=<hauptteil-ende>:d=<outrolaenge>`.
  → betrifft: alle Content-Agenten
- **Ein Bett unter dem Outro aendert dessen Gesamtpegel nicht.** Gemessen am
  Outro-Abschnitt beider Shorts: **-26,1 dB mit Bett wie ohne**. Der eigene
  Ton des Outros bestimmt den Pegel, das Bett liegt klar darunter und wird
  vom `sidechaincompress` zusaetzlich weggedrueckt. **Die Sorge, das Bett
  koenne mit dem Outro kollidieren, ist messbar unbegruendet** — hoerbar
  bleibt es trotzdem, die Subtraktion zeigt es durchgehend bis zum letzten
  Bild.
  → betrifft: content-*

## 2026-11-11 (spaet) — Blickrichtung bekommt den Platz, nicht der Hinterkopf

- **„Passt der Kopf in den Kasten" ist die falsche Frage; richtig ist, auf
  welcher Seite die Luft liegt.** Sein Befund: *„Sein Kopf ist viel zu weit
  links. Der ist gar nicht voll drin im Bild."* Gemessen an 13 Bildern:
  Kens Kopf reicht von **x 853 bis 1267**, der Kasten stand bei **x 836** —
  also **17 Pixel links**, 177 rechts. Technisch war nichts angeschnitten.
  Aber er schaut nach links, und 17 px Blickraum lesen sich als
  angeschnitten. Neu x 700: 153 links, 41 rechts.
  **Regel: bei einem Profil bekommt die Blickrichtung den Platz, der
  Hinterkopf darf eng sitzen. Mindestens ein Viertel der Kastenbreite vor
  dem Gesicht.**
  → betrifft: alle Content-Agenten
- **Eine Anekdote, die im Gespraech traegt, traegt im Short nicht.** Der
  Wasserbueffel-Witz am Anfang von Kens Antwort ist im Podcast ein
  Rueckbezug auf etwas Frueheres und funktioniert dort; im Short steht er
  ohne das Frueher und kostet 25 s. Sein Wort: *„die ueberhaupt gar keine
  Substanz hat in einem Short."* **Rueckbezuege auf frueher in derselben
  Folge gehoeren in einem Short zu den ersten Streichkandidaten** — genau
  wie „on your show" im Ubuntu-Short zwei Stunden vorher. Zweimal
  derselbe Fehler an einem Tag.
  → betrifft: content-*, alle
- **Zweimal hintereinander habe ich den Schluss seiner Antwort zu frueh
  gesetzt.** Fassung 1 endete auf „all of it is in relation to others",
  Fassung 2 geht 21 s weiter bis „inspire others to do the same" — und
  erst dort kommt seine naechste Frage. **Der Endpunkt ist nicht das erste
  gute Satzende, sondern das letzte vor der naechsten Frage.** Die Regel
  steht seit dem 22.10. in `meaningful-serie.md`; ich habe sie zweimal
  nicht angewandt.
  → betrifft: content-*, alle
- **Ein Kontaktabzug mit 150-px-Feldern taugt nicht, um einen Kamerawechsel
  zu erkennen.** Ich hatte die Schnittkante dadurch erst auf Bild 314
  gelesen, bei 240 px war klar: Bild 313. **Solche Pruefungen auf
  mindestens 240 px, lieber in Gruppen von vier bis sechs Bildern statt
  zwoelf.**
  → betrifft: content-shorts-2

## 2026-11-11 (abends) — `-ss` taugt nicht fuer ein einzelnes Bild

- **Ich habe heute frueh aus einer unzuverlaessigen Pruefung eine Regel
  abgeleitet, und die Regel war falsch.** Aus `ffmpeg -ss <zeit>
  -frames:v 1` hatte ich geschlossen, `select='gt(scene,…)'` melde die
  Schnittkante ein Bild zu spaet, und alle Grenzen vorgezogen. Nachgezaehlt
  **nach Bildnummer** liegen die vier Kanten des Meaningful-Shorts bei Bild
  115 · 258 · 952 · 1158 — **genau** den Werten, die die Erkennung ohne
  `-ss` gemeldet hatte. **Die Erkennung war exakt; die Stichprobe war es
  nicht.** `-ss` trifft beim Einzelbildgriff nicht verlaesslich das
  angeforderte Bild.
  **Richtig:** `-vf "select='between(n,A,B)'" -vsync 0` und nach Bildnummer
  zaehlen. Und: Szenenerkennung **am Vorlagenband ohne `-ss`** laufen lassen,
  dann stimmen die Zeiten.
  → betrifft: alle Content-Agenten
- **Und die Lehre ueber den Fall hinaus: eine Messung, die eine andere
  Messung widerlegt, ist erst dann die bessere, wenn ihr Verfahren selbst
  geprueft ist.** Ich hatte die Szenenerkennung fuer falsch erklaert, weil
  eine zweite Methode etwas anderes sagte — ohne zu pruefen, ob die zweite
  Methode ueberhaupt taugt. Das hat drei Durchlaeufe gekostet und haette
  einen Fehler ins Short gebracht, den es ohne mich nicht gegeben haette.
  **Das Ubuntu-Short vom selben Tag ist nach der verlaesslichen Methode
  nachgeprueft** (Bilder 46–53 ueber die Naht): sauber.
  → betrifft: content-*, alle
- **Ein Gast hat in der Totale und in seiner eigenen Kamera verschiedene
  x-Positionen, und zwar weit auseinander.** Ken steht in der Totale bei
  **x ≈ 1660**, in seiner Nahaufnahme bei **x ≈ 1140** — 520 px Unterschied.
  Der uebernommene Totale-Kasten zeigte in der Nahaufnahme nur seinen
  Hinterkopf. **Jede Kamera bekommt ihre eigene Messung, auch wenn dieselbe
  Person darin steht.**
  → betrifft: alle Content-Agenten
- **Die Meaningful-Antwort von Ken Stern ist 22 s laenger als dokumentiert.**
  `video/meaningful-serie.md` fuehrt sie als 32,7 s (Master 6150,1–6189,3),
  Ende auf „being surrounded by others" — das ist mitten im Gedanken.
  Tatsaechlich laeuft sie bis **6211,3** und endet auf **„All of it is in
  relation to others."** Danach noch 20 s bis zur naechsten Frage.
  **Ein dokumentierter Endpunkt ersetzt nicht das Hoeren bis zur naechsten
  Frage** — die Regel aus `meaningful-serie.md` („bis zur naechsten Frage,
  dort auf dem letzten Satzende") war richtig, nur nicht angewandt.
  → betrifft: content-vlog, content-*, alle

## 2026-11-11 (spaeter) — die Szenenerkennung lag ein Bild daneben

- **`select='gt(scene,…)'` auf einem mit `-ss` gesuchten Eingang meldet die
  Schnittkante ein Bild zu spaet.** Gemeldet 3928,60 und 3995,60; die Bilder
  bei **3928,5667** und **3995,5667** gehoeren schon zur naechsten Kamera.
  Ursache ist der Zeitstempel-Versatz nach dem Suchen, nicht der Filter.
  **Folge, wenn man es nicht merkt:** das letzte Bild meines ersten Stuecks
  war die Totale, mit dem Kasten der Nahaufnahme beschnitten — also Tisch,
  Laptop und Dosen, kein Mensch. Ein Bild lang, mitten im Short. Genau der
  Fehler, den er am 26.10. als „minimaler glitch" reklamiert hat.
  **Regel: eine mit `-ss` gemessene Schnittkante wird vor Gebrauch an
  Einzelbildern geprueft, und die Stuecklaenge wird mit `-frames:v` auf die
  Bildzahl festgenagelt, nicht mit `-t` auf eine Sekundenzahl.** `-t` rundet
  je nach Startpunkt auf ein Bild mehr.
  → betrifft: alle Content-Agenten
- **Gefunden hat es das Auge, nicht die Messung.** Die Abnahme lief sauber
  durch, die Laengen stimmten auf die Millisekunde, v und a waren gleich.
  Sichtbar wurde es erst auf einem Kontaktabzug von acht Einzelbildern ueber
  die Naht. **Nach jedem Schnitt Einzelbilder ueber die Naht ansehen bleibt
  Pflicht, auch wenn alle Zahlen stimmen.**
  → betrifft: alle Content-Agenten
- **Eine Korrektur, die eine Modellschwaeche ausgleicht, gilt nur fuer genau
  die Schnittfassung, an der sie gemessen wurde.** `medium` verschluckte an
  der ersten Schnittfassung das Wort „relationships"; ich hatte es ueber eine
  Klammer eingesetzt. An der endgueltigen Fassung — 0,3 s anders geschnitten
  — schreibt dasselbe Modell es von selbst, und im Bild stand
  **„THROUGH OUR RELATIONSHIPS RELATIONSHIPS"**. **Nach jedem Neuschnitt
  gehoert jede solche Korrektur nachgeprueft**, anders als Namens- und
  Schreibkorrekturen, die stehen bleiben.
  → betrifft: content-*, alle
- **Khoi und San einzeln nennen, nicht „Khoisan".** Whisper schreibt „Koi"
  und „Sun tribes", weil es so klingt. Richtig sind **Khoi** (Khoikhoi) und
  **San** — zwei Voelker. Er nennt sie einzeln, und das ist auch sachlich
  die bessere Form: der Sammelbegriff stammt aus der Kolonialzeit und wurde
  2001 in Windhoek von San-Vertretern ausdruecklich abgelehnt.
  → betrifft: alle Content-Agenten

## 2026-11-11 — eine Stelle in 1:45 finden, ohne die Datei zu durchsuchen

- **Sein Vorbereitungsdokument im Drive-Ordner der Folge sagt, wo die Stelle
  liegt — das ist der billigste Sucheinstieg, den es gibt.** Im Doc
  `00 YNB Podcast: Ken Stern` steht unter *Timestamps* woertlich
  **„1:05:00 Short: Ubuntu"**, daneben Dinge wie „5:14: edit out" und
  „57:12 - 1:06:00 raeuspern edit". Gefunden ohne das 823-KB-Dokument zu
  oeffnen: `search_files` mit
  `fullText contains 'Ubuntu' and parentId = '<Ordner>'` liefert einen
  Ausschnitt, der das ganze Kapitel enthaelt. **Vor jedem Blindflug durch
  einen Master gehoert diese eine Suche.** Danach reichte ein Byte-Fenster
  von **1141 MB statt 16,8 GB**.
  → betrifft: alle Content-Agenten
- **Ein langes Transkriptionsfenster hoert eine kurze, leise Stelle
  schlechter als ein Ausschnitt von sechs Sekunden.** `medium` ueber 280 s
  schrieb Kens Antwort als *„I don't remember the definition, but I remember
  liking it when you said it"*. Vier andere Durchlaeufe — `medium` am
  gedehnten Schnitt, `large-v3` bei 1,0 · 0,7 · 0,55 am 6-Sekunden-Ausschnitt
  — sagen uebereinstimmend *„I don't remember this, but I remember liking
  when you said it"*. **Der Ueberblickslauf taugt zum Finden, nicht zum
  Zitieren; wer woertlich wiedergibt, schneidet die Stelle heraus und
  transkribiert sie einzeln.**
  → betrifft: content-*, alle
- **Das Verlangsamen hat zum zweiten Mal eine eingebrannte Zeile gerettet,
  diesmal bei ganz normalem Englisch.** „most people misinterpret it" klingt
  bei Sprechtempo wie „misinterpreted", und **beide** Modelle schrieben das
  auch — erst bei 0,7- und 0,55-facher Geschwindigkeit hoert `large-v3`
  zweimal „misinterpret it", und nur das ergibt den Satz. **Die Regel vom
  05.11. galt fuer Fremdsprachiges; sie gilt auch fuer verschliffene
  englische Endungen.** Pruefzeichen: wenn die Transkription grammatisch
  schief ist, ist meist sie falsch und nicht der Sprecher.
  → betrifft: alle Content-Agenten
- **Wenn in einer Totale zwei Sprecher 1400 px auseinandersitzen, folgt der
  Kasten dem Sprecher.** Ein 9:16-Ausschnitt ist 608 px breit, die beiden
  stehen bei x 260 und x 1660 — einer von beiden ist immer draussen. Statt
  die Totale wegzuwerfen oder einen stumm im Bild zu lassen: zwei Kaesten
  innerhalb derselben Einstellung, geschnitten am Sprecherwechsel
  (4,7 s auf Ken, 1,9 s auf ihn). **Beide ueber der Halbsekundengrenze vom
  26.10., sonst gilt die wieder.**
  → betrifft: alle Content-Agenten

## 2026-11-05 (nachmittags) — die ab-Sekunde des Betts, und ein Beleg fuer die Musikschwelle

- **Seine Regel „den Inhalt des Songs vorziehen" stand seit dem 22.10. beim
  Gastauftritte-Agenten, nicht bei mir — und ich habe drei Shorts dagegen
  gebaut.** AI 2027, Safety und Belief tragen „In This Shirt" **ab 0:00**,
  also mit den 23 Sekunden Vorspann unter dem Anfang. Richtig ist **ab
  0:23,25**. Unabhaengig nachgemessen: ab 0:00 liegen die ersten zwei
  Sekunden **4,1 dB** unter dem laufenden Pegel (ueber 2 kHz 2,6 dB), ab
  0:23,25 nur noch **0,2 dB**. Seine Worte damals: *„Ich wollte, dass du den
  Inhalt des Songs vorziehst. Die ersten 20 Sekunden des Songs, da passiert
  nichts."* **Lehre: bevor ich etwas zum zweiten Mal baue, lese ich die
  Lerndatei des Agenten, der es zuerst gebaut hat** — `git grep` ueber alle
  Zweige kostet fuenf Sekunden. Die drei Shorts sind in einer Minute je neu
  gemischt, wenn er es will.
  → betrifft: content-shorts-2, alle Content-Agenten
- **Der Einsatz eines Titels ist nicht immer ein Sprung, manchmal eine
  Steigerung — dann gehoert die ab-Sekunde an ihr ENDE.** Bei „In This
  Shirt" springt die Energie ueber 2 kHz in einer Zehntelsekunde um 19 dB.
  Bei „On The Nature Of Daylight" steigt sie ueber **1,2 s** (23,3 → 24,5).
  Der Start bei 23,3 laege 5,3 dB unter dem laufenden Pegel, bei 24,5 nur
  2,8 dB — und die **natuerliche Schwankung des Stuecks betraegt selbst
  2,3 dB**. **Die Pruefgroesse ist nicht die absolute Abweichung, sondern
  die Abweichung gegen die Streuung des Titels.** Ohne diesen Vergleich
  haette ich 24,5 fuer zu leise gehalten und waere auf 1:01 ausgewichen.
  → betrifft: alle Content-Agenten
- **Die Musikschwelle von `abnahme.py` ist am selben Material belegbar — und
  bestaetigt meinen Vorschlag von heute frueh.** Dasselbe Short, dreimal
  gemessen: **ohne Musik -62,4 dB** (Raumton des Craig-Studios), **mit In
  This Shirt -35,0 dB**, **mit On The Nature Of Daylight -38,1 dB**. Ein
  Bett hebt den Boden also um **24 bis 27 dB**. Eine feste Schwelle bei
  -65 dB wirft dieses Studio faelschlich raus; **die Pruefung gegen den
  Boden der Quelle (Hub > 15 dB) trennt beide Faelle sauber.** Zahlen an
  Shorts I, Werkzeug nicht angefasst.
  → betrifft: content-assistant, alfred
- **Max Richter — „On The Nature Of Daylight" ist der ungetestete Titel im
  Ordner, und der heikelste.** Handelsaufnahme, bekannt aus „Arrival" und
  „Shutter Island". Aus demselben Ordner hat „Daylight" am 22.10. zwei
  veroeffentlichte Shorts **weltweit gesperrt**. Gebaut, weil er es
  ausdruecklich bestellt hat; mit dem Hinweis geliefert, ihn vor einer
  Veroeffentlichung an einem ungelisteten Testupload zu pruefen.
  → betrifft: alle

## 2026-11-05 — Ubuntu-Short, Fremdsprache im Untertitel, und ein Fehlalarm

- **Ein fremdsprachiges Wort braucht mindestens zwei Modelle und zwei
  Geschwindigkeiten, sonst brennt man Unsinn ein.** Craig nennt das
  Sprichwort auf isiXhosa. `medium` schrieb *„umtu ngumtu ngabania ubuntu ah
  ngabania abantu"* — und **ueberhoerte die zweite, kuerzere Form komplett**
  (2,2 s Luecke zwischen „otherwise" und „which"). `large-v3` bei normal,
  0,7× und 0,6× dreimal wortgleich: **Umntu ngumntu ngabanye abantu** und
  **Umntu ngumntu ngabantu**. **Regel: wo eine Sprache steht, die das Modell
  nicht kann, wird jedes Wort mit einem zweiten Modell und verlangsamtem Ton
  gegengeprueft, bevor es eingebrannt wird.**
  → betrifft: alle Content-Agenten
- **`korrekturen.txt` kann auch einfuegen, nicht nur ersetzen.** Fuer die
  verschluckte Form steht jetzt `otherwise which -> otherwise Umntu ngumntu
  ngabantu which` (2 Woerter → 5). `korrekturen_anwenden` erlaubt
  n→m-Abbildungen und verteilt die Ersetzung gleichmaessig ueber die Zeit
  der ersetzten Gruppe. Nachgemessen landen die eingefuegten Woerter **auf
  0,05 s genau** auf dem gesprochenen Wort, weil die Luecke genau die
  Sprechzeit ist. **Wer eine Luecke fuellen will, ersetzt die Klammer
  drumherum.**
  → betrifft: content-*, alle
- **Die Musikpruefung in `abnahme.py` ist an einem einzigen Studio
  kalibriert und meldet an anderem Material Fehlalarm.** Schwelle −65 dB,
  gemessen am fertigen Ubuntu-Short **−62,4 dB** — ohne jede Musik. Der
  **Rohausschnitt misst an derselben Stelle −62,5 dB**, am Anfang −61,7 dB:
  es ist der Raumton des Craig-Studios. Aaronson liegt bei −85,3 dB, daher
  die Schwelle. **Vorschlag an Shorts I: die Schwelle nicht fest setzen,
  sondern gegen den Boden der Quelle pruefen** — ein Bett hebt den Boden um
  15–20 dB, das ist der eigentliche Nachweis. **Nicht geaendert, das
  Werkzeug gehoert Shorts I.**
  → betrifft: content-assistant, alfred, content-*
- **4K-Quellen drehen die Ausschnittsrechnung um.** Bei 1920×1080 kostet
  9:16 eine Hochskalierung von **1,78×**; bei 3840×2160 ist der volle
  Hoehenausschnitt **1215×2160** und wird auf 1080×1920 **herunter**gerechnet
  (0,89×), und ein 1080×1920-Ausschnitt ist **exakt 1:1**. **Aus 4K darf man
  deshalb enger schneiden als aus HD** — fuer die Totale habe ich das
  genutzt und Craig 1:1 statt klein in der Weite stehen lassen.
  → betrifft: alle Content-Agenten
- **Wer im Bild ist, sagt die Folge, nicht ich.** Bei seiner Fehldefinition
  schneidet die Folge selbst auf ihn (Quelle 116,40 → 118,60). Ich hatte das
  erst nur als Beleg genommen, wer spricht; seine Ansage dazu: *„nein ich
  kann da drin bleiben weil ich das doch da sage."* **Bei fertig
  geschnittenem Quellmaterial sind die Kameraschnitte der Folge die
  Vorgabe** — uebernehmen, nicht neu entscheiden. Ergebnis: vier Wechsel,
  kein einziger von mir, keine Auslassung.
  → betrifft: content-*

## 2026-10-26 (spaet) — Belief-Short, und zwei Dinge ueber Werkzeug

- **Nur eine Fassung schicken, nicht zwei.** Ich hatte ihm Musik- und
  musikfreie Fassung zusammen geschickt; seine Reaktion: *„Ich weiss nicht,
  warum du mir jetzt nochmal einen Short ohne Musik geschickt hast."* Die
  Sicherungsfassung gehoert ins Repo, nicht in die Lieferung. **Eine Datei
  pro Short, die andere nur auf Nachfrage** — dasselbe Muster wie am 22.10.,
  als ich ihm zweimal dasselbe AIGod-Short geschickt hatte.
  → betrifft: alle Content-Agenten
- **Das groessere Whisper-Modell ist nicht automatisch das bessere.**
  `large-v3` glaettet Stotterer: aus *„like this is, this is really all a
  bunch of"* macht es *„this is really all a bunch of"*. Fuer eingebrannte
  Untertitel, die zu den Lippen passen muessen, ist das ein Nachteil.
  **`medium` fuer den Durchgang, `large-v3` nur als Schiedsrichter fuer ein
  einzelnes strittiges Wort** — und dann am *ungedehnten* Ton, weil die
  Dehnung selbst Fehler erzeugt: bei Tempo 1,12 hoerte `medium` „well", wo
  „wow" steht.
  → betrifft: content-*
- **Kameraschnitte misst man am fertigen Vorlagenband, nicht an der Quelle.**
  Ich hatte die Schnitte in der Quelle gemessen und auf die Zeitachse
  umgerechnet (Klipzeit−Start)/Tempo. Das stimmte zwar, aber ich konnte es
  erst glauben, nachdem ich dieselbe Messung am Vorlagenband wiederholt
  hatte: 1,167 · 35,667 · 40,900 gegen gerechnete 1,161 · 35,654 · 40,893.
  **Eine Minute Nachmessen am fertigen Band ersetzt das Nachrechnen.**
  → betrifft: content-*
- **Ein Innenschnitt zwischen zwei aehnlichen Nahaufnahmen ist der Fall, bei
  dem es glitchig aussieht.** Der Szenenwert an meiner Naht ist **0,064**,
  an den Kameraschnitten des Studios **0,52–0,53**. Wo der Wert niedrig ist,
  springt nur der Kopf, und genau das liest sich als Fehler statt als
  Schnitt. **Niedriger Szenenwert an einer selbstgebauten Naht = Warnsignal**;
  Gegenmittel ist ein merklich engerer Kasten auf der zweiten Seite, damit
  der Schnitt gewollt wirkt.
  → betrifft: alle Content-Agenten
- **Rohzeit = Masterzeit + 12,6 s**, geprueft an „What do you believe in?"
  (Master 4285,96 s → roh 1:11:38,6; Rohtranskript 1:11:38). Shorts I nennt
  12,2 s, `video/aaronson-shorts.md` ebenfalls. **An dieser Stelle der Folge
  sind es 12,6 s** — der Versatz ist also nicht ueber die ganze Folge
  konstant, und wer bildgenau schneidet, misst ihn an seiner Stelle neu.
  → betrifft: content-*, alle

## 2026-10-26 (abends) — drei Rueckmeldungen zu „How safe is AI"

- **Die drei Bilder Totale, die ich heute frueh als Regel notiert hatte, liest
  er als Glitch.** Oben in dieser Datei steht noch: *„Eine Einstellung unter
  einer halben Sekunde ist kein Grund zum Wegschneiden, sondern eine Zeile
  mehr im Plan."* Seine Rueckmeldung: *„zwischen 0:16 und 0:18 ist wieder ein
  minimaler glitch."* **Der Befund von heute frueh gilt nicht mehr in dieser
  Form.** Was bleibt: ein eigener Kasten rettet drei Bilder Totale *technisch*
  — aber drei Bilder (0,1 s) sind zu kurz, um als Einstellung gelesen zu
  werden, und werden deshalb als Fehler gelesen. **Untergrenze: unter etwa
  einer halben Sekunde kein Einstellungswechsel.** Zweites Mal in fuenf Tagen,
  dass eine gute technische Begruendung gegen eine seiner Wahrnehmungen
  verliert (nach `--look aus` am 22.10.).
  → betrifft: content-*
- **`ffmpeg -c:v copy` schneidet nicht an der Stelle, die man angibt, sondern
  am naechsten Keyframe.** Beim Entfernen der drei Bilder blieben **zwei
  Bilder zu viel** stehen: v = 18,033 s gegen a = 17,967 s. Sichtbar wurde es
  erst beim Nachmessen der Bildzahl, nicht im `ffprobe`-Ueberblick.
  **Wer bildgenau schneidet, codiert neu** — `-t 17.966667 -r 30 -c:v libx264
  -crf 15` ergab exakt **539 Bilder**. Kopieren ist nur dort richtig, wo die
  Grenze ohnehin auf einem Keyframe liegt.
  → betrifft: alle Content-Agenten
- **Zwei Shorts, zwei entgegengesetzte Musikansagen — also keine Regel, sondern
  eine Frage pro Stueck.** AI 2027 am 22.10.: *„dass er es nicht vorm Ende
  aufhoert."* Safety am 26.10.: *„bitte in this shirt unterlegen aber vor dem
  Outro aufhoeren."* Dieselbe Datei, dasselbe Short-Format, umgekehrte
  Entscheidung. **Nicht aus dem einen Short auf das naechste schliessen; bei
  Musik gilt immer die Ansage zu diesem Stueck.** Technisch loest beides
  dieselbe Kette: `atrim` setzt das Ende, `afade=t=out` liegt davor oder in
  den letzten 0,8 s.
  → betrifft: content-*
- **Mein Befund vom 22.10. zum blinden Fleck von `abnahme.py` war schon
  behoben, als ich ihn aufschrieb.** Das Werkzeug laesst die letzten 4,5 s
  (das Outro) bei der Musikpruefung aussen vor (`bis = max(dauer - 4.5, 1.0)`).
  Nachgemessen am Safety-Short, dessen Bett **vor** dem Outro endet: die
  Musikfassung faellt korrekt durch (**-44,8 dB** im leisesten Prozent), die
  musikfreie besteht (**-91,8 dB**). **Vor einem Befund ueber fremdes Werkzeug
  den Code lesen, nicht nur das Verhalten deuten** — ich hatte am 22.10. aus
  einem Messergebnis auf eine Luecke geschlossen, die im Code nicht stand.
  → betrifft: content-shorts-2, alfred
- **Dass ein Bett wirklich vor dem Outro aufhoert, zeigt nur die Subtraktion.**
  Musikfreie Fassung phaseninvertiert auf die Musikfassung, dann der Pegel der
  Differenz in 0,5-s-Fenstern: **-40 bis -48 dB bis 50,5 s**, Ausblende,
  **ab 51,5 s -80 dB und tiefer**. Nach Gehoer oder am Mittelwert haette man
  die 0,1 s Genauigkeit am Uebergang nicht belegen koennen.
  → betrifft: content-*

## 2026-10-26 — „How safe is AI", und der Tonschnitt auf den Kameraschnitt gelegt

- **Es gab zwei Stuecke mit fast demselben Namen, und sie sind verschieden.**
  Shorts I' `aaronson-01-is-ai-safe` beginnt mit **Aaronson** („The trouble
  with AI right now is not that it doesn't work"); das Stueck auf
  `claude/content-cinematic`, `aaronson-01-how-safe-is-ai.srt`, beginnt mit
  **Yannicks Frage** „How safe is AI?" (Rohzeit **00:55:52**). Er meinte das
  zweite — *„Stelle ich, glaube ich, die Frage"*, und das stimmte.
  **Bei zwei Stuecken mit aehnlichem Namen entscheidet, wer den ersten Satz
  spricht, nicht der Dateiname.**
  → betrifft: content-*
- **Der beste Platz fuer einen Innenschnitt ist ein Kameraschnitt des Studios
  — und manchmal liegt er schon fast da.** Ich wollte Teil 1 nach „…other than
  our own" enden lassen; das Wort endet bei Excerpt **26,12 s**, der
  Studioschnitt auf die Totale liegt bei **26,16 s**. **0,04 s dazwischen.**
  Also den Tonschnitt genau auf den Kameraschnitt gelegt, statt 0,2 s spaeter
  mitten in der Einstellung. **Das erspart den J-Schnitt ganz** — es gibt nur
  einen Schnitt, und der faellt auf einen Wechsel.
  **Vor jedem Innenschnitt nachsehen, ob in 0,5 s Umkreis ein Kameraschnitt
  liegt**, und den Schnitt dorthin ziehen, wenn das Wort es erlaubt.
  → betrifft: content-*
- **Drei Bilder Totale wegzuwerfen ist nicht noetig, sie bekommen einen
  eigenen Kasten.** Nach dem Schnitt blieben **0,1 s = 3 Bilder** Totale
  stehen. Mit dem Kasten der Nahaufnahme haette man dort Wand und Pflanze
  gesehen; mit einem eigenen Kasten auf Aaronson (`1166:0:608:1080`) liest es
  sich als kurzer Weitblick auf ihn. **Eine Einstellung unter einer halben
  Sekunde ist kein Grund zum Wegschneiden, sondern eine Zeile mehr im Plan.**
  **ÜBERHOLT am Abend des 26.10. — er liest die drei Bilder als Glitch. Siehe
  den Eintrag „2026-10-26 (abends)" oben: unter etwa einer halben Sekunde
  kein Einstellungswechsel.**
  → betrifft: content-*
- **Defensiv geschnitten, und das Ergebnis ist nachrechenbar:** genau **eine**
  Auslassung (die Apokalyptiker-Anekdote, 14 s). Ohne sie waere das Stueck
  **71 s** lang gewesen, mit ihr sind es **58,0 s** — also innerhalb seines
  Formats bei einer einzigen benannten Streichung statt der drei, die ich bei
  „AI 2027" gebraucht hatte.
  → betrifft: content-*


## 2026-10-26 — das Musikbett des Renderers hoert 6,2 s vor dem Ende auf

- **`--musik` blendet 2 s vor dem Ende des *Hauptteils* aus — das Outro laeuft
  danach ohne Bett.** Yannick hat es gehoert: *„denk bitte daran, dass das
  nicht zu spaet startet, der Song. Und dass er es nicht vorm Ende aufhoert."*
  Im Code (Zeile 1417): `atrim=0:<laenge>,afade=t=out:st=<laenge-2.0>:d=2.0`,
  wobei `laenge` die Laenge **vor** dem Outro ist. Am AI-2027-Short gerechnet:
  Hauptteil endet 54,367 s, Video endet 58,575 s — **das Bett ist ab 52,367 s
  still, also 6,21 s vor dem letzten Bild.**
  **Behoben ohne den Renderer anzufassen:** ohne `--musik` rendern und das Bett
  danach ueber die fertige Datei mischen — `aloop`, `volume`, `afade in 0,4 s`,
  `sidechaincompress` gegen die Stimme, `afade out` erst in den letzten 0,8 s.
  → betrifft: alle Content-Agenten
- **Ob ein Bett wirklich durchlaeuft, misst man durch Subtraktion, nicht nach
  Gehoer.** Musikfreie Fassung von der Musikfassung abziehen — uebrig bleibt
  genau das Bett, und sein Pegel ueber die Zeit sagt, wo es da ist. Gemessen:
  **hoerbar von 0,00 s bis 58,55 s** bei einem 58,58-s-Video, Pegel −40 bis
  −47 dB durchgehend, auch unter dem Outro (54,37–58,58).
  → betrifft: content-*
- **Nebeneffekt, der meinen Befund vom 22.10. aufhebt:** der blinde Fleck der
  Musikpruefung (das Outro enthaelt digitale Stille und bestimmt das leiseste
  Prozent) **verschwindet, sobald das Bett durchlaeuft**. `abnahme.py` erkennt
  die Musikfassung jetzt korrekt (leisestes Prozent **−43,3 dB**, faellt
  durch), waehrend sie bei der frueheren Fassung mit frueh endender Musik
  durchgewunken haette. **Der Fehler im Werkzeug und der Fehler im Renderer
  haben sich gegenseitig verdeckt.**
  → betrifft: content-*, alle
- **Und eine Lieferkritik an mir, von ihm:** *„warum du mir zweimal das gleiche
  Short gegeben hast mit dem Zitat von Arthur Clarke."* `AIGod` und
  `AIGod (ohne Schluss)` sind **dasselbe Stueck**, das zweite ist eine echte
  Teilmenge des ersten. Es entstand nur, weil er erst die kurze Fassung
  gewaehlt und dann den Schluss zurueckgeholt hat — ab da war die kurze
  **ueberholt**, und ich habe sie trotzdem mitgeliefert.
  **Regel: eine Fassung, die eine Teilmenge einer anderen ist, geht nicht als
  zweites Stueck mit.** Entweder sie ersetzt die andere, oder sie faellt weg.
  → betrifft: alle Content-Agenten


## 2026-10-23 — T−2 Aaronson: ausgeliefert, und was fuer die naechste Runde liegenbleibt

- **Der J-Schnitt loest die Stelle, an der meine drei Fassungen hart schneiden
  muessen.** Vom Gastauftritte-Agenten Bild fuer Bild gemessen, `LERNEN.md`
  Ausgabe 14: **Bild endet exakt auf dem Kamerawechsel, Ton laeuft 0,4 s
  weiter, das Bild des naechsten Stuecks beginnt entsprechend frueher.** Dann
  gibt es nur **einen** Bildschnitt, und der faellt auf einen Wechsel, ist also
  unsichtbar.
  **Meine drei Aaronson-Fassungen nutzen ihn nicht** — sie schneiden hart, und
  mehrere Naehte liegen **mitten in einer Einstellung** (z. B. 15,700 s in
  `AI2027`, zwei Stuecke derselben Kamera). Das ist kein Fehler, aber es ist
  ein sichtbarer Sprung, wo einer vermeidbar waere. **Nicht vorsorglich
  umgebaut** — T−2, und er hat es nicht bestellt. Steht als Angebot.
  → betrifft: content-*
- **Die Musiksperren sind auf sechs gewachsen, der letzte um 20:12 zu
  `YNB Podcast David Sutcliffe Meaning Comptine`** — wieder das Klaviercover,
  wieder die Komposition. **Sechs Meldungen, drei Titel, kein Ausweg ueber
  Coverversionen.** Die drei Aaronson-Fassungen gehen ohne Bett; nachgemessen
  am Sprachteil: **−92,5 / −87,9 / −87,9 dB** leisestes Prozent.
  → betrifft: alle
- **Ein Statusmissverstaendnis, das die Ablage erzeugt, nicht ein Agent.**
  Alfreds Stand sagte „bereit, nicht geliefert" — die drei MP4 lagen aber seit
  dem 22.10., 15:30 UTC bei Yannick. **Er sieht nur das Repo, und dort sind
  `video/shorts/*.mp4` per `.gitignore` ausgenommen**, also sieht er die
  Dateien nie. **Wer etwas liefert, dessen Ablage per gitignore unsichtbar ist,
  muss die Lieferung selbst in den Kanal schreiben** — sonst steht sie
  tagelang als offen.
  → betrifft: alle


## 2026-10-22 — meine 60-Sekunden-Decke war falsch, und wie die Lieferung stattdessen aussieht

- **„Ein Short darf 60 s nicht ueberschreiten" stimmt seit dem 15.10.2024
  nicht mehr — die Grenze ist 3 Minuten.** Ich hatte die 60 s zweimal als
  Tatsache an ihn weitergegeben und einen Vorschlag darauf gebaut; Alfred hat
  es bemerkt, ich habe es unabhaengig nachgesucht und komme auf dasselbe:
  mehrere Leitfaeden nennen uebereinstimmend **3 Minuten ab 15.10.2024**,
  einzelne aeltere Seiten fuehren noch die 60 s.
  **Belegstand ausdruecklich: ueber Dritte, nicht ueber die Quelle.**
  `support.google.com` ist aus diesem Container nicht erreichbar — selbst
  geprueft, `getaddrinfo ENOTFOUND`. Also **sehr wahrscheinlich 3 Minuten,
  nicht gemessen.**
  **Die Lehre an mir: eine Plattformgrenze aus dem Gedaechtnis ist keine
  Auskunft.** Ich habe sie nicht als Vermutung gekennzeichnet, sondern als
  Rahmen benutzt, innerhalb dessen ich seinen Inhalt beschnitten habe.
  → betrifft: alle
- **Fuer die Praxis aendert es wenig, und das ist der wichtigere Teil: die
  Laenge ist seine redaktionelle Entscheidung, keine technische.** Sein Format
  liegt bei **~59 s**, und alle **39** Shorts auf dem Kanal folgen ihm. Also
  weiter auf **55–59 s** bauen, bis er etwas anderes sagt — aber **nicht mehr
  mit der Begruendung, es ginge technisch nicht laenger.**
  Und: **Hochformat entscheidet mit**, ob etwas ueberhaupt als Short laeuft;
  Laenge allein macht es nicht.
  → betrifft: content-*
- **Die bessere Lieferform, wenn das Material mehr traegt als 59 s — von
  Alfred, und sie steht in Yannicks eigenem Satz.** Ich hatte angeboten,
  zusaetzlich eine Clip-Fassung ohne Laengengrenze zu rendern. Naeher liegt:
  *„gibst mir dann das Transkript und ich sage dir, was du rausschneiden
  sollst."* **Dann ist die Lieferung die Liste, nicht ein zweiter Render** —
  die Kandidatenstelle als Transkript mit markierten Grenzen, dazu mein
  Vorschlag, was ich streichen wuerde, wenn ich muesste. Er streicht, ich
  rendere **einmal** statt zweimal. Die Clip-Fassung bleibt das richtige
  zweite Angebot, wo ein Gedanke die Laenge wirklich braucht.
  → betrifft: content-*



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
