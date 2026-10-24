# Befunde — Gastauftritte (fremde Podcasts)

Schlüssel `content-gastauftritte`, Branch `claude/content-gastauftritte`.
Neuester Eintrag oben.

## 2026-10-22

- **Die Drive-Seitenmarke kostet Material, und ich bin heute selbst darauf
  hereingefallen.** In `LERNEN.md` steht seit dem 21.10.: *„Drive ignoriert
  `pageSize`, und die Seiten ueberlappen — ohne Durchblaettern ueber
  `pageToken` sieht man den Ordner nicht, und merkt es nicht."* Genau das ist
  passiert: Isabelle hatte am 22.10. um 10:26 **zwei** Titel in den
  Musikordner gelegt, meine Auflistung zeigte **einen** plus eine
  Seitenmarke, der ich nicht gefolgt bin. Ich habe ihm darum nur das
  Odell-Cover angeboten, und er musste mir den zweiten Titel selbst
  verlinken. **Einen Ordner, aus dem etwas ausgewaehlt werden soll, immer bis
  zur letzten Seite lesen** — auch wenn die erste Seite plausibel aussieht.
  → betrifft: alle

- **WIDERRUFEN: die Coverversion ist KEIN Ausweg. Vier Sperren an einem Tag,
  drei Titel, jeder Neuversuch wieder weltweit gesperrt.** Ich hatte hier
  geschrieben, ein Cover wechsle den Anspruchsteller und ein
  Kompositionsanspruch ziele „ueblicherweise auf Monetarisierung statt auf
  Sperrung" — ausdruecklich als Erwartung gekennzeichnet. **Gemessen ist
  jetzt das Gegenteil** (Sperrmeldungen vom 22.10., Zeiten Kapstadt):

  | Zeit | Video | beanstandet | Rechteinhaber | Type |
  |---|---|---|---|---|
  | 10:57 | `jnAHk2_xWBI` | Daylight – David Kushner | Virgin Music Group | Audio |
  | 11:57 | `9iRza-eDKcc` | Daylight – David Kushner | Virgin Music Group | Audio |
  | 15:21 | `5nl--61ZBBI` | In This Shirt (Royksopp Remix) | FUGA | Audio |
  | 16:21 | `nHQIvWANN04` | COMPTINE D UN AUTRE ETE | LatinAutor-UMPG, UMPG u.a. | **Melody or lyrics** |

  Die vierte Zeile ist **Benny Garners Klaviercover**, also genau der Titel,
  den ich als Ausweg vorgeschlagen hatte. **Blocked globally**, und zwar als
  `Melody or lyrics` statt `Audio`: Content ID gleicht auch gegen die
  **Komposition** ab, und der Verlag hat dieselbe Laengengrenze gesetzt wie
  das Label. **Eine Coverversion wechselt den Anspruchsteller, nicht die
  Folge.**

  **Was gilt:** kein Musikbett — nicht Original, nicht Cover, nicht leiser.
  **Die Fassung ohne Musik ist nicht die Nebenfassung, sie ist die Fassung.**
  Eine Spur kommt erst wieder in Frage, wenn er einen Titel aus einer
  **lizenzierten Bibliothek** nennt oder ausdruecklich fuer genau diesen
  Titel freigibt. **Dass eine Datei in seinem Musikordner liegt, sagt ueber
  die Rechte nichts** — dort liegen inzwischen drei Titel, und alle drei
  haben gesperrt.

  **Und die Lehre ueber den Fall hinaus:** ich hatte eine Erwartung sauber
  als solche gekennzeichnet und sie trotzdem zur Grundlage einer Empfehlung
  gemacht (*„Coverversionen zuerst, Originalaufnahmen zuletzt"*). Eine
  gekennzeichnete Vermutung ist keine Lizenz, sie wie einen Befund zu
  benutzen — sie gehoert geprueft, bevor jemand danach arbeitet.
  → betrifft: alle Content-Agenten

- **Eine Bildblende an einer Naht INNERHALB derselben Einstellung erzeugt
  eine Doppelbelichtung.** Er fand sie: *„so ein kleiner Glitch ... einfach
  richtig schlecht geschnitten."* An den Einzelbildern nachgesehen — bei
  Sekunde **2,43 und 2,47** liegen zwei Gesichter uebereinander. Ursache:
  `xfade` von 0,13 s an einer Stelle, an der davor und danach **dieselbe
  Kamera** auf dem Sprecher steht; die Blende mischt zwei Momente desselben
  Bildes. Sie war von mir die falsche Antwort auf seinen frueheren Einwand,
  der Schnitt sei „amateurhaft" — dessen Ursache war ein **Knack im Ton**
  von einer anderen Naht, und der ist separat behoben.
  **Regel: Bildblende nur, wenn die Naht zwei Kameras verbindet. Innerhalb
  einer Einstellung immer hart schneiden**, und den Knack ueber kurze
  Tonblenden (20 ms) an beiden Seiten erledigen — gemessen faellt der Pegel
  an der Naht dann auf −85 dB, und der groesste Signalsprung in der Gegend
  ist das gesprochene Wort selbst.
  → betrifft: alle Content-Agenten

- **Korrektur an meiner eigenen Erklaerung von heute Vormittag: die Laenge
  ist sehr wohl der Hebel — nur war die Grenze enger, als wir dachten.**
  Er hat den Aaronson-Short mit *David Kushner – Daylight* hochgeladen,
  Inhalt **59,43 s**, Bett 3 dB unter der Stimme und per Sidechain
  weggedrueckt. YouTube: **Video blocked globally**, Anspruch auf *Daylight*,
  Typ *Copyright / Audio*. Der Wortlaut der Meldung ist entscheidend:
  *„contains claimed content that **exceeds the length limits set by the
  copyright holder**"*. Ich hatte ihm zuerst geschrieben, die
  60-Sekunden-Annahme trage nicht und Content ID greife laengenunabhaengig.
  **Das war zu absolut.** Richtig ist: die **Erkennung** haengt am
  Fingerabdruck und ist laengen- und pegelunabhaengig, die **Folge** aber an
  einer Laengengrenze, die der Rechteinhaber je Titel selbst setzt. Seine
  Intuition war richtig, meine Erklaerung zu grob.
  Nebenbefund aus der Meldung: **kein Copyright-Strike**, *„No impact to
  channel"* — der Kanal nimmt keinen Schaden, das Video ist nur gesperrt.
  **Was daraus folgt:** wie viel von einem Titel durchgeht, steht in keiner
  Datei und laesst sich hier nicht messen — es haengt am Rechteinhaber. Der
  einzige verlaessliche Weg ist, es vor dem Veroeffentlichen zu sehen; die
  Ansprueche zeigt YouTube schon im Upload-Vorgang. Darum gehoert zu jedem
  Short mit Bett **eine Fassung ohne Musik** dazu.
  → betrifft: alle Content-Agenten

## 2026-10-21

- **YouTube weist diesen Container ab — `yt-transkript.py` läuft nicht mehr.**
  Gemessen an `q3_kLgYIXGQ`: `yt-dlp` meldet über **sechs** Player-Clients
  (`tv_simply`, `android_vr`, `mweb`, `web_safari`, `tv`, `web_embedded`, auch
  mit Node als JS-Runtime) *„Sign in to confirm you're not a bot"*; die
  Videoseite liefert `playabilityStatus: LOGIN_REQUIRED`; ein echter Chromium
  wird auf `www.google.com/sorry/index` umgeleitet, also auf ein CAPTCHA.
  **Das ist eine IP-Sperre des Rechenzentrums, keine Freigabe-Frage** —
  `youtube.com` ist im Proxy erlaubt (HTTP 200). `video/yt-transkript.py` ist
  seit 19.10. als „geht ohne Schlüssel" dokumentiert; **das stimmt heute
  nicht mehr.** Wer ein Transkript aus YouTube braucht, braucht die Datei.
  → betrifft: alle

- **Metadaten, Kapitel und Beschreibung kommen trotzdem durch — über
  `ytInitialData`.** Die Videoseite per `curl` ist **1,74 MB** und vollständig;
  bot-gesperrt ist nur `ytInitialPlayerResponse` (4.594 Bytes Stummel, keine
  `videoDetails`, keine `captionTracks`). `ytInitialData` daneben ist intakt:
  **26 Kapitelmarken** mit `startTimeSeconds`, die ganze Beschreibung,
  Aufrufe und Hochladedatum — ohne API-Schlüssel, ohne Login. Ausgelesen über
  `macroMarkersListItemRenderer`. **Das ist der Rückfallweg, wenn Untertitel
  und Medien gesperrt sind.**
  → betrifft: content-*, youtube-manager, thumbnails

- **`oembed` kommt durch, wenn die Videoseite gesperrt ist.**
  `https://www.youtube.com/oembed?url=https://youtu.be/<id>&format=json` gibt
  **Titel, Kanalname, Kanal-URL und Vorschaubild** zurueck — ohne Login, ohne
  Schluessel, und **auch dann noch, wenn `watch?v=` schon mit 302 auf das
  Google-CAPTCHA umleitet** (heute beides am selben Video gemessen). Keine
  Dauer, keine Kapitel. **Das ist der billigste Weg, um ueberhaupt zu klaeren,
  welches Video hinter einer ID steckt** — so habe ich `ud5kr_LoqU4` als die
  Rob-Paddock-Folge seines eigenen Kanals identifiziert, nachdem die
  Videoseite nicht mehr kam.
  → betrifft: alle

- **Der 403, den yt-dlp meldet, kommt nicht von YouTube.** Im Proxy-Protokoll
  stehen **20 Ablehnungen auf `www.google.com:443`** und keine einzige auf
  `www.youtube.com` — yt-dlps „Unable to download webpage … Giving up after 3
  retries" ist in Wahrheit die gesperrte Google-Verbindungsprüfung.
  `curl -sS "$HTTPS_PROXY/__agentproxy/status"` nennt Host und Grund.
  **Erst den Host im Protokoll nachsehen, bevor man dem Fehlertext glaubt.**
  → betrifft: alle

- **Chromium und Playwright sind da und laufen durch den Proxy — mit zwei
  Haken.** `playwright` gibt es **nur für Node**, nicht für Python
  (`ModuleNotFoundError`). ESM liest `NODE_PATH` nicht, also muss der Import
  der absolute Pfad sein: `/opt/node-tools/node_modules/playwright/index.mjs`.
  Und der Proxy muss ausdrücklich mit: `chromium.launch({ proxy: { server:
  process.env.HTTPS_PROXY } })` — ohne das kommt `ERR_TUNNEL_CONNECTION_FAILED`
  auf **jeder** Seite. Browser `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
  → betrifft: alle

- **Der Plan liefert die Lippe, der Renderer setzt die Zeile GENAU dorthin —
  der Abstand ist ein eigenes Flag und steht auf 0.** Seine Beanstandung vom
  21.10.: *„Die Schrift ist überwiegend auch direkt auf Davids Lippen. Das
  ist nicht optimal, das habe ich dir auch schon gesagt."* Gemessen: Plan
  meldet `Lippe 1248` (65 % der Hoehe), und das Protokoll schreibt
  `0 px unter der Lippe`. An drei Testbildern verglichen (0 / 120 / 200 px):
  bei **0** sitzt die Zeile auf dem Bart, bei **120** frei darunter mit Luft
  zum Logo, bei **200** draengt sie ans Logo. **`--tiefer 120` ist der Wert
  fuer dieses Studio.** Seine Ansage „nicht direkt unter seiner Lippe" war
  notiert, aber nirgends eingestellt — eine Regel, die in keinem Flag steht,
  wirkt nicht.
  → betrifft: alle Content-Agenten

- **Ein Preset zu uebernehmen heisst nicht, es auf abgenommene Stuecke
  anzuwenden.** Ich habe beim Einbauen des Presets das Logo von **700 px auf
  302 px** (28 %) geaendert — an einem Short, dessen Logogroesse er bereits
  abgenommen hatte. Seine Reaktion: *„dann ist auch mein Logo ploetzlich viel
  kleiner."* **Er hatte keine Aenderung am Logo bestellt.** Der Auftrag „nimm
  sein Preset" galt dem, was offen war, nicht dem, was schon stand.
  **Regel: ein neues Preset gilt fuer Neues. Was er abgenommen hat, bleibt,
  bis er es selbst aendert.**
  → betrifft: alle

- **`mean_volume` der Gesamtmischung taugt nicht, um ein Musikbett zu
  pruefen.** Zwischen der Fassung ohne Musik und der lautesten mit Musik
  lagen **0,6 dB** — und in der Sprechpause 0,1 dB. Das sah nach „keine Musik
  im Signal" aus, war aber nur das falsche Messinstrument: die fast
  durchgehende Stimme bestimmt den Mittelwert. **Richtig ist, den
  Bett-Zweig allein durch dieselbe Kette zu schicken und dort zu messen** —
  dann steht da −36,7 / −40,7 / −45,7 dB gegen eine Stimme bei −29,1 dB.
  Auch die Differenz zweier Dateien hilft nicht: beide sind neu AAC-kodiert,
  die Stimme hebt sich nicht weg (max 0,0 dB, reines Codec-Rauschen).
  → betrifft: alle Content-Agenten

- **`video/musik_drunter.py` legt ein Bett unter einen FERTIGEN Short.**
  Gleiche Kette wie `--musik` im Renderer (geloopt, 1,5 s ein, 2 s aus,
  `sidechaincompress` threshold 0,04 / ratio 8, `amix normalize=0`), aber
  ohne erneutes Transkribieren und Encodieren des Bildes: `-c:v copy`.
  Drei Pegelfassungen kosten so Minuten statt drei vollen Durchlaeufen.
  **Falle beim Nachbauen:** `shorts-render.py` wertet beim Import sein
  eigenes `argparse` aus, man muss `sys.argv` leeren — und die eigenen
  Argumente **vorher** sichern, sonst sind sie weg.
  → betrifft: alle Content-Agenten

- **Die zusammengefuehrte Renderer-Fassung hat zwei Regressionen gegen
  Entscheidungen, die in `LERNEN.md` schon stehen.** Beide fielen erst auf,
  als er am 21.10. am Sutcliffe-Short ein Fragezeichen bestellt hat
  (*„da wuerde ich eigentlich gerne ein Fragezeichen haben. Das kannst du dir
  merken bei dieser Frage."*) — und keines im Bild stand.
  **1.** `_anzeige()` streift in `66de26b` wieder **alle** schliessenden
  Satzzeichen ab (`w.rstrip(SATZZEICHEN)`), Fragezeichen eingeschlossen. Die
  feinere Regel — nur `. , ; : …` weg, `?` und `!` bleiben — war am 20.10.
  aus seinen **zwei** Ansagen desselben Abends hergeleitet und ist hier
  verlorengegangen. **Damit haette auch `how safe is AI?` sein Fragezeichen
  wieder verloren.**
  **2.** `korrekturen_anwenden()` haengt das Satzzeichen des Originals
  unbedingt an den Ersatz. Die Schutzregel aus `LERNEN.md` (*„endet der
  Ersatz schon auf ein Satzzeichen, wird das des Originals nicht
  angehaengt — sonst AI??"*) fehlt. Gemessen: aus `you,` plus Ersatz `you?`
  wird **`you?,`**, was `_anzeige()` dann vollends zerlegt.
  Beides auf diesem Branch zurueckgeholt und an vier Faellen geprueft
  (seine Frage, der AI-Praezedenzfall, eine Aussage mit Punkt, eine echte
  Frage). **Gehoert zurueck nach `claude/content-assistant`.**
  **Die Lehre, die ueber den Fall hinausgeht:** beim Zusammenfuehren zweier
  Fassungen gewinnt nicht automatisch die juengere Zeile. Wo eine Regel aus
  einer **Korrektur von ihm** stammt, muss sie beim Merge ausdruecklich
  geprueft werden — sonst faellt sie still zurueck, und niemand merkt es,
  bis er dasselbe ein zweites Mal bestellt.
  → betrifft: content-*, alfred

- **`--srt` zusammen mit `--srt-out` bricht den Renderer ab.**
  `KeyError: 'woerter'` in `cues_als_srt`, Zeile 146: `srt_to_cues()` baut
  Cues ohne Wortliste, `cues_als_srt()` verlangt sie aber. Tritt nur bei
  dieser Kombination auf, und erst nach dem Transkodieren — also nach der
  teuren Minute. **Wer eine fertige SRT wiederverwendet, laesst `--srt-out`
  weg.**
  → betrifft: content-*

- **Eine wiederverwendete SRT kostet das gelbe Aktivwort.** `--srt` liefert
  nur Cue-Grenzen, keine Wortzeiten — die Hervorhebung des gesprochenen
  Wortes braucht aber Wortzeiten und faellt damit still weg. Am Sutcliffe-Short
  gemessen: Gruppierung und Wortlaut stimmten, **die Farbe fehlte komplett**,
  und im Renderprotokoll steht kein Hinweis darauf. Wer den abgenommenen Look
  will, muss `--auto-captions` nehmen, auch wenn eine geprueft SRT schon
  dasteht. **Die SRT taugt zum Pruefen des Wortlauts, nicht als Ersatz fuer
  die Transkription.**
  → betrifft: content-*

- **Zeitbasis beim Zurueckspielen einer SRT: mal Tempo, nicht geteilt.**
  `--srt-out` schreibt Ausgabezeit (`start / tempo`), `--srt` erwartet
  Quellzeit. Eine mit `--srt-out` bei Tempo 1,2 geschriebene Datei muss also
  **× 1,2** zurueckgerechnet werden. Probe am Sutcliffe-Short: letzter Cue
  49,15 s × 1,2 = 58,98 s, Clip 59,6 s — passt.
  → betrifft: content-*

- **Seine Praezisierung zur Wohnort-Regel, 21.10.:** *„Cape Town oder South
  Africa — ich moechte es halt nur nicht genauer veroeffentlichen."* Also
  **Stadt und Land duerfen fallen, alles Feinere nicht.** `video/ortscheck.py`
  hat auf diesem Branch jetzt zwei Stufen: `GROB` (Cape Town, South Africa,
  Western Cape, Tafelberg) wird nur gezaehlt, `ORTE` (Scarborough, Kommetjie,
  Misty Cliffs, Noordhoek, Fish Hoek, Muizenberg …) schlaegt an und setzt
  die Rueckgabe auf 1. Vorher stand „cape town" und „south africa" in der
  Sperrliste — das haette jeden Short mit seiner Herkunftsgeschichte
  blockiert. **Gehoert zurueck nach `content-schlicht`, dort liegt die Datei.**
  → betrifft: content-*, thumbnails

- **Gegen den Fehler des Tages hilft eine Schwelle, die vor der Messung
  feststeht.** Alfred und ich haben am 21.10. denselben Fehler gemacht — eine
  Lesart fuer eine Tatsache gehalten; bei ihm kostete es drei Thumbnails, bei
  mir eine falsche Datierung im Kanal. Die Gegenmassnahme, die ich eingebaut
  habe: `video/garden-pruefplan.py` legt **Fenster und Entscheidungsregel im
  Quelltext fest, vor dem ersten Blick ins Transkript** (−30 s/+120 s um die
  Marke; ≥5 von 7 Treffern = ja, ≤2 = nein, dazwischen = unentschieden) und
  gibt 0/1/2 zurueck. **Wer die Schwelle erst nach dem Ergebnis festlegt,
  begruendet statt zu messen.** Drei Faelle mit erfundenen Transkripten
  durchgespielt, alle drei Zweige stimmen. **Das Muster taugt fuer jede
  Zuordnung, die am Material entschieden wird** — nicht nur fuer diese.
  → betrifft: alle

- **Die Zeitmarkenliste in `LERNEN.md` gehoert wahrscheinlich zu einem
  bestimmten Video — belegt ist es nicht, und meine erste Datierung war
  falsch.** Primaerquelle Slack, DM an Isabelle, Thread `1788525418.826269`
  (*Shorts: Boo The Philosopher*): der Link `youtu.be/q3_kLgYIXGQ` ist
  Antwort 14 vom **14.09. 22:20:08**, die Liste ist Antwort 15 vom
  **15.09. 17:01:06**. **Gleicher Thread, keine Nachricht dazwischen — aber
  18 h 41 min und einen Tag spaeter.** Ich hatte zuerst geschrieben, sie stehe
  "direkt nach dem Link" am 14.09. um 22:20; **die Uhrzeit war die des Links,
  nicht der Liste.** Gegen die 26 Kapitel geprueft: 7/7 Marken fallen in die
  Laufzeit, **1/7** stimmt woertlich mit einem Kapiteltitel ueberein
  (`1:21:00 My Why` / `1:19:07 His why…`, +113 s), 3/7 sind thematisch stimmig,
  **0/7** werden widerlegt — und **4 der 6 Stichworte** (`Hormozi`,
  `Joe Hudson`, `Confidence`, `Workaholism`) kommen auf der Videoseite
  **null Mal** vor. Im selben Thread steht oben ein zweites Video,
  `ud5kr_LoqU4` (Rob-Paddock-Folge **seines eigenen** Podcasts); dessen Seite
  gibt YouTube inzwischen nicht mehr heraus (302 auf das CAPTCHA), ein
  Vergleich war also nicht moeglich. **Also: plausibel, nicht belegt.**
  Entschieden wird es am Wortlaut, nicht am Kapiteltitel.
  → betrifft: content-*, head-of-content

- **Die beiden `shorts-render.py` sind auseinandergelaufen, in beide
  Richtungen.** Die Fassung auf `claude/content-assistant` hat sein Preset
  (`--look preset`, `--lut`, Inter Black 82, `#F9F13A`, 72 %, Logo 28 %/0,87),
  **aber kein `--kopfzeile`**. Die Fassung auf den anderen Content-Branches hat
  `--kopfzeile` samt `--kopfzeile-hell`, **aber nichts vom Preset** (noch
  `DejaVu Sans`, `#FFD530`, `--look {warm,aus}`). **Keine der beiden ist die
  vollständige.** Wer eine der beiden kopiert, verliert das jeweils andere;
  ich habe hier die Preset-Fassung genommen und das Fehlen der Kopfzeile in
  Kauf genommen. **Gehört zusammengeführt, beim Shorts-Assistenten.**
  → betrifft: content-*, alfred

- **`ffmpeg` ist wieder da (6.1.1 unter `/usr/bin`), `imageio_ffmpeg` nicht.**
  `shorts-render.py` bricht sonst in Zeile 46 ab; `pip install imageio_ffmpeg`
  läuft durch den Proxy. Zusätzlich liegt ein zweites ffmpeg bei Playwright
  (`/opt/pw-browsers/ffmpeg-1011/`).
  → betrifft: alle Content-Agenten

## 22.10.2026, 18:40 — Der unsaubere Anfang war ein Sprung mitten in einer Einstellung. Der J-Schnitt loest ihn auf.

Sein Befund, zweimal: *„Nachdem ich frage, what makes life meaningful for you?
Da ist so ein Moment, der ist einfach richtig schlecht geschnitten"* (22.10.),
und nachdem ich eine Bildblende durch einen harten Schnitt ersetzt hatte:
*„Du hast zwar den Fehler nicht wirklich behoben"*, dann *„ganz am Anfang, da
ist einfach so ein richtig unsauberer Cut"*.

Nachgemessen, Bild fuer Bild: der Kamerawechsel von ihm auf Sutcliffe liegt bei
src2 **3,6000 s** (Differenz 41,2 gegen 0,6 im Ruhepegel). Mein Schnitt lag bei
4,0 — also **0,4 s hinter** dem Wechsel. Dadurch sah man Sutcliffe 0,4 s lang,
und dann sprang es auf denselben Sutcliffe 5 s spaeter. Zwei harte Schnitte in
0,4 s, der zweite innerhalb derselben Einstellung: genau der Sprung, den er
sieht. Ihn weicher zu machen (Blende) war der falsche Hebel — der Schnitt lag
an der falschen Stelle.

Die Loesung ist der **J-Schnitt**: das Bild endet exakt auf dem Kamerawechsel
(3,6000), der Ton laeuft bis 4,0 weiter, damit seine Frage fertig wird. Das
Bild des zweiten Stuecks faengt dafuer 0,4 s frueher an (src2 8,8667 statt
9,2667). Ergebnis: **ein** Bildschnitt, und der faellt auf einen Kamerawechsel,
ist also unsichtbar. Man sieht Sutcliffe zuhoeren, waehrend die Frage zu Ende
geht.

→ betrifft: jede Naht, die in einer Einstellung liegt. Erst messen, wo der
naechste Kamerawechsel ist, dann das Bild dorthin legen und den Ton
darueberlaufen lassen. `video/schnitt_bauen.py` nimmt Bild- und Tonstuecke
getrennt entgegen und prueft, dass beide Summen gleich lang sind.

## 22.10.2026, 18:40 — Der Anfang begann 0,05 s vor dem ersten Wort.

Zweiter Teil desselben Befunds. Der Short begann bei src2 1,000, das erste Wort
"After all" bei 1,05 — **50 ms Vorlauf**, und der erste Frame lag mitten in
einer laufenden Einstellung. Gemessen: der Kamerawechsel auf ihn liegt bei src2
**0,6000**. Der Short faengt jetzt dort an, also auf dem ersten Bild der
Einstellung, mit 0,45 s Ruhe vor dem ersten Wort.

→ betrifft: jeden Anfang. Der erste Frame eines Shorts gehoert auf den ersten
Frame einer Einstellung, nicht irgendwohin in deren Mitte.

## 22.10.2026, 18:40 — Pausen kuerzen: nicht nach Laenge waehlen, nach Bildaehnlichkeit.

Fuer „unter 90 Sekunden" mussten 4,8 s weg. Pausen zu kuerzen heisst in einer
stehenden Einstellung: Sprungschnitt. Nach Laenge zu waehlen (die laengste
Pause zuerst) traf die sichtbarsten Stellen.

Gemessen statt geschaetzt: fuer jede Pause wird die mittlere
Helligkeitsdifferenz im Kopfbereich zwischen Ausstiegs- und Einstiegsbild
berechnet, daneben der Ruhepegel (zwei benachbarte Bilder an derselben Stelle).
Dann wird **innerhalb** jeder Pause die Paarung gesucht, bei der die Differenz
am kleinsten ist, statt feste Puffer zu nehmen. Das hat viel gebracht:

* feste Puffer von 0,15 s: 14 Schnitte, schlechtester Sprung **3,14**
* Paarung gesucht: 14 Schnitte, schlechtester Sprung **2,72**, die meisten
  zwischen 0,7 und 1,9 bei Ruhepegeln von 0,3 bis 1,1

→ betrifft: jede Laengenvorgabe. `video/pausen_waehlen.py --fein`. Nicht die
laengste Pause kuerzen, sondern die, an der das Bild vorher und nachher gleich
aussieht.

## 22.10.2026, 18:40 — Nach einem Neuschnitt die Einblendungen rechnen, nicht neu transkribieren.

Sein Vorwurf vom 21.10. war berechtigt: *„warum ich dir in der vorherigen
Schritt sage, pass das an ... und dann verlierst du es wieder."* Ursache ist
Whisper, das nicht deterministisch ist. Die abgenommene Cue-Datei loest das nur,
solange der Clip derselbe bleibt.

Wenn aus einem Clip nur Stellen **herausgeschnitten** werden, muss gar nicht neu
transkribiert werden: die Zeiten lassen sich abbilden. `video/cues_umlegen.py`
nimmt die abgenommene Datei, den Versatz und die Liste der entfernten Stellen
und rechnet um — 102 Einblendungen, keine neue Lotterie, „meaningful for you?"
bleibt in einer Einblendung, die geheilten Woerter behalten ihre Dauer.

→ betrifft: jeden Neuschnitt eines schon abgenommenen Shorts.

## 22.10.2026, 18:40 — Der Ausschnittplaner liefert nach dem Neuschnitt dieselben Kaesten.

Sorge war, dass ein neuer Lauf von `bildausschnitt.py` die abgenommene Fassung
des Bildes verliert (der Planer folgt dem Bewegungsgipfel, nicht dem Gesicht).
Nachgeprueft: mit `--zoom 1.15 --marke 0,875,215,1080 --kein-stapel` kommen auf
dem neuen Clip **exakt dieselben sechs Kaesten** heraus wie auf dem alten, nur
mit verschobenen Zeiten. Ohne `--kein-stapel` macht er aus den zwei Totalen
„stapel" — dann weicht die Fassung ab.

→ betrifft: jeden Neulauf des Planers. `--kein-stapel` gehoert zu diesem Short
dazu, und die Kaesten gehoeren verglichen, nicht geglaubt.

## 22.10.2026, 18:25 — Neue stehende Regel von ihm: lieber zu defensiv als zu offensiv schneiden.

Woertlich, ueber Alfred weitergegeben und ausdruecklich fuer alle Agenten:

> *„mir ist aufgefallen, es ist deutlich schwerer fuer mich, wenn du die Shorts
> eigenstaendig entscheidest, was du rausschneidest, und ich dann nach das
> Skript kontrollieren muss, um zu sehen, was du rausgeschnitten hast, als wenn
> du lieber zu wenig oder weniger rausschneidest und mir dann das Transkript
> gibst und ich dir eher sagen soll, was du rausschneiden sollst. Deshalb ist
> die neue Anweisung und gib das bitte weiter an die anderen Agenten, dass du
> lieber zu defensiv als zu offensiv schneidest."*

Die Fehlerrichtung ist unsymmetrisch: eine Auslassung, die er nicht wollte,
kostet ihn Liste lesen, Stelle suchen, Rueckmeldung, neue Renderrunde. Eine
Zeile zu viel kostet ihn eine Nummer. Deckt sich mit seinem Satz vom 21.10.:
*„ich wuerde dich anhalten, lieber weniger zu schneiden, als zu viel."*

Drei Punkte daraus, die ab sofort zu jedem Short gehoeren:

1. **Das Transkript geht mit raus**, nicht nur das Video. Er soll sagen, was
   weg soll, nicht nachkontrollieren, was weg ist.
2. **Nach jedem Innenschnitt die beiden Nachbarzeilen nebeneinander lesen** —
   Pronomen ohne Bezug, Fragen ohne Antwort. Dem Render hoert man das nicht an.
   Belegt an „AI 2027" (Shorts II): zweimal eine Auslassung zurueckgeholt, einmal
   fiel die einzige Nennung von Eliezer Yudkowsky mit heraus, danach stand
   *„he just regarded it as obvious"* ohne Bezug.
3. **Bei Gastauftritten gilt das doppelt.** Dort stellt der Gastgeber die
   Fragen, und eine Pointe von ihm steht fast immer auf einer fremden Frage.
   Die Frage des Gastgebers gehoert im Zweifel dazu, auch wenn sie Sekunden
   kostet.

→ betrifft: jeden Schnitt. **Beim Sutcliffe-Short heute geprueft:** entfernt
wurden ausschliesslich **Pausen**, kein gesprochenes Wort. Nachgewiesen mit
`diff` gegen die abgenommene Untertiteldatei — der Text ist Zeichen fuer
Zeichen derselbe. Die 14 Stellen stehen einzeln in
`video/shorts/sutcliffe-meaningful.pausen.json`, damit er sie sieht, statt sie
suchen zu muessen.

## 22.10.2026, 19:30 — „Die ersten paar Sekunden, da ist fast gar keine Musik" — es war der Songanfang, nicht die Blende.

Sein Befund zu „In This Shirt": *„der Song, der muss schon frueher losgehen. Die
ersten paar Sekunden, da ist fast gar keine Musik."* Derselbe Befund wie am
21.10. bei Daylight.

Mein erster Verdacht war die Einblendung (0,3 s). Falsch. Nachgemessen am Titel
selbst, sekundenweise:

| Sekunde im Song | RMS |
|---|---|
| 0 | −14,6 dB |
| 1 | −13,1 dB |
| 2 | −10,2 dB |
| 5–20 | rund −9,5 dB |

Der Titel faengt also **4 bis 6 dB leiser** an. Das Bett lief ab 0:00, und damit
lagen die ersten zwei Sekunden des Shorts gemessen bei −34,7 dB gegen −32,6 dB
im Rest — genau was er hoert.

Behoben, indem das Bett bei **0:02** einsetzt, wo der Titel schon auf vollem
Pegel steht, und die Einblendung von 0,3 auf 0,1 s gekuerzt wird. Nachgemessen
am fertigen Short: erste zwei Sekunden −31,2 statt −34,7 dB, laufender Pegel
unveraendert −32,4 dB. Kein Knacken am Einsatz.

**Das war die halbe Antwort, und sie war nicht die gemeinte.** Siehe den
naechsten Eintrag.

## 22.10.2026, 20:10 — Nicht der Pegel entscheidet, sondern wo der Titel arrangiert losgeht.

Nach der Korrektur oben kam sein Widerspruch:

> *„Der Song geht erst so richtig los bei Sekunde 21. Ich rede bei dem Short. Wo
> David, glaube ich, Moments sagt. Da geht der Song erst richtig los. Das wollte
> ich. Ich wollte, dass du den Inhalt des Songs vorziehst. Die ersten 20
> Sekunden des Songs, da passiert nichts."*

Mein Fehler war die Messgroesse. Ich hatte das **RMS** gemessen, und danach steht
„In This Shirt" ab Sekunde 2 auf vollem Pegel — also hielt ich die Sache fuer
erledigt. Gehoert hat er etwas anderes: die ersten 23 Sekunden traegt ein
**einzelnes Instrument**. Laut, aber leer.

Die richtige Messgroesse ist die Energie **ueber 2 kHz**. Dort zeigt sich der
Einsatz von Gesang und Perkussion als Sprung, den das RMS gar nicht sieht:

| Songsekunde | RMS | ueber 2 kHz |
|---|---|---|
| 22,9 | −9,5 dB | −53,0 dB |
| 23,2 | −9,7 dB | −53,4 dB |
| **23,3** | −7,9 dB | **−34,6 dB** |
| 23,4 | −8,4 dB | −31,2 dB |

19 dB Sprung in einem Zehntelsekundenblock, bei **unveraendertem RMS**.

Seine Zeitangabe stimmte auf die Zehntelsekunde: mit dem Bett ab 0:02 landete
dieser Einsatz bei Shortsekunde 21,3 — und bei 21,7 steht `MOMENTS` im Bild. Das
Bett faengt jetzt bei **0:23,25** an. Nachgemessen am fertigen Short: Energie
ueber 2 kHz in den ersten 10 s um 4 bis 6 dB hoeher, laufender Pegel
unveraendert bei −32,2 dB, kein Knacken (groesster Sprung 0,0323 gegen 0,0416 an
einer normalen ruhigen Stelle).

→ betrifft: **jeden** Titel. Die `ab_sekunde` gehoert auf den Sprung in den
Hoehen, nicht auf die erste Sekunde mit vollem Pegel. Vor jedem Bett wird der
Titel sekundenweise auf beides geprueft — RMS **und** Energie ueber 2 kHz — und
der Einsatz wird vorgezogen, statt den Short mit dem Vorspann zu belegen. Die
anderen beiden Titel daraufhin nachgeprueft: Odell ab 2:20 (−13,1 gegen −11,8 dB
im Mittel) und Comptine ab 0:10 (−17,6 gegen −18,9 dB) fangen beide nicht leise
an, dort ist nichts zu korrigieren.

→ und zweitens: **zweimal am selben Befund vorbeigearbeitet, weil ich die
erstbeste Erklaerung genommen habe, die zu einer Messung passte.** Der Pegel war
eine Erklaerung, nicht die Erklaerung. Wenn eine Messung den Befund nur halb
deckt, fehlt eine zweite Messgroesse.

`musik_drunter.py` nimmt die Einblendung jetzt als `--blende-ein` entgegen,
damit sie nicht mehr im Code festhaengt.

## 22.10.2026, 21:00 — Eine Einblendung, die ueber einen Kameraschnitt laeuft, verlor ihre Woerter.

Gefunden am Hypermaskulinitaets-Short, nicht gemeldet: zwei Bilder lang stand
mitten im Satz ein einzelnes **„IS"** im Bild, wo „REAL STRENGTH IS" stehen
sollte.

Ursache: `cues_an_lippen` teilt jede Einblendung, die ueber einen Kameraschnitt
laeuft, in zwei Teile — laut eigener Beschreibung *„derselbe Text, an zwei
Hoehen"*, damit die Zeile mit der Kamera mitspringt. `build_ass` filterte die
Woerter danach aber am Fenster des Teilstuecks:

```python
woerter = [w for w in c["woerter"]
           if max(w["end"], w["start"] + 0.001) > c["start"]
           and w["start"] < c["end"]]
roh = [_anzeige(w["t"], gross) for w in woerter]
```

Die Zeile wird aus `roh` gebaut. Beim zweiten Teilstueck (Clipzeit
51,50–51,70) ueberlebte nur das Wort, das in diesem Fenster liegt — „is". Die
beiden davor fielen aus dem Bild. Die Beschreibung versprach also etwas, was
der Code nicht tat.

Behoben: `roh` kommt jetzt aus **allen** Woertern der Einblendung, und nur die
Hervorhebung folgt dem Fenster. Fuer ungeteilte Einblendungen aendert sich
nichts — dort sind beide Mengen gleich.

**Das betrifft nicht nur diesen Short.** Am Sutcliffe-Short „Meaning" wurden
102 Einblendungen zu 106 ASS-Zeilen, also vier davon geteilt — dort stand
dasselbe Problem im Bild und ist niemandem aufgefallen, weil die Teilstuecke
kurz sind. Beim naechsten Lauf dieses Shorts ist es mit behoben.

→ betrifft: jeden Short mit mehr als einer Kameraeinstellung. Und als Lehre:
wenn eine Funktion in ihrer eigenen Beschreibung etwas verspricht
(„derselbe Text"), gehoert genau das nachgeprueft, statt es zu glauben.

## 23.10.2026 — B-Roll am VOLLEN Bild ausgesucht, aber der Short zeigt nur die mittleren 31,6 %.

Sein Befund zum Hypermaskulinitaets-Short, drei Punkte in einem Satz:

> *„google mal Louis Thoreau. Das ist der Typ, der die Doku gemacht hat. Und du
> zeigst vor allem Szenen von ihm. Aber er stellt die Manosphere ja gar nicht
> dar. Und teilweise haben wir wieder Szenen, wo die Person gar nicht im Bild
> ist."*

Alle drei stimmen, und alle drei haben **dieselbe Ursache**: ich habe die
Bloecke am vollen Trailerbild ausgesucht (2622×912) und dabei auf Leute
geschaut, die am Rand standen. Gezeigt wird aber im randlosen 9:16 nur ein
Ausschnitt von **513 px Breite**, also die mittleren 19,6 % der Trailerbreite
(bei einem 16:9-Film sind es 31,6 %). Wer am Rand stand, war weg — und Louis
Theroux, der Dokumentarfilmer, stand in der Mitte, weil die Kamera **ihn**
verfolgt. Deshalb blieb von meiner Auswahl genau der uebrig, der die Manosphere
nicht darstellt.

Nachgeprueft an meinen eigenen alten Bloecken, im tatsaechlich gezeigten
Ausschnitt: Block 1 (Quelle 20,75–32,35) enthaelt Theroux bei 23 und 29–31 und
gar keine Person bei 21–22, 26–28 und 32–34. Block 2 (98,1–103,7) enthaelt
Theroux bei 99,9 und 103,4 sowie eingeblendeten Text („powerbank") bei
100,4–101,4. Sein Urteil war also nicht ungefaehr richtig, sondern genau.

**Die Regel daraus: der Kontaktabzug wird vom AUSSCHNITT gemacht, nicht vom
Quellbild.** Vorher:

```
crop=2622:912:0:147            # das ganze Filmfenster — zeigt, was NICHT laeuft
```

Jetzt:

```
crop=513:912:1054:147          # genau das, was im Short steht
```

Damit war in einem Durchgang zu sehen, was vorher drei Runden gekostet haette:
die laengste durchgehende Strecke mit einem Gesicht in der Mitte und ohne
Theroux ist **3 Sekunden** (Trailersekunde 0,0–3,0). Alles andere liegt bei
0,8 bis 1,5 s. Ein Trailer ist eben in 1–2-Sekunden-Stuecken geschnitten, und
die Mitte traegt nicht in jedem Stueck ein Gesicht.

→ betrifft: jede B-Roll-Auswahl. Erst den Ausschnitt bauen, dann auswaehlen.
Und bei einer Doku gilt zusaetzlich: **die Kamera folgt dem Reporter, nicht dem
Thema.** Wer in der Bildmitte steht, ist bei Theroux, Reeve, Munchetty und
jedem anderen Format dieser Art zuerst einmal der Fragesteller.

→ zweitens: `--broll-fokus` ist EIN Wert fuer alle Bloecke. Wenn die Motive in
verschiedenen Bloecken verschieden weit links stehen, reicht das nicht. Dann
wird jeder Block **vorher** auf 9:16 beschnitten, mit eigenem Versatz, und der
Renderer laeuft auf `--broll-modus vollbild` — der skaliert ein schon
passendes Bild nur noch, ohne weiter zu schneiden.

## 24.10.2026 — Die Musik endet zu abrupt. Zwei Sekunden Ausblende sind zu kurz.

Seine Beobachtung, ausdruecklich als allgemeine Regel zum Weitergeben:

> *„mir ist aufgefallen, dass du generell beim Ende des Shorts die Musik zu
> schnell oder zu abrupt endest. Das ist eine generelle Beobachtung, das kannst
> du gerne an die anderen Agenten weitergeben."*

Nachgemessen am Hypermaskulinitaets-Short, Bett isoliert (Mischung mit Musik
minus Mischung ohne):

| Sekunde | Bettpegel |
|---|---|
| 53,5 | −35,6 dB |
| 54,0 | −36,2 dB |
| 54,5 | −39,6 dB |
| 55,0 | −45,4 dB |
| 55,5 | −54,1 dB |

Bei 54,0 steht das Bett also noch auf vollem Pegel und ist 1,9 s spaeter weg.
Nach 56 Sekunden Lauf hoert sich das an, als wuerde es abgeschaltet, nicht als
wuerde es enden. **Dazu kommt der Gegensatz zum Outro, das direkt danach mit
−4 dB einsetzt** — gemessen am Uebergang. Der Absturz faellt dadurch doppelt
auf.

Behoben: `musik_drunter.py` hatte die Ausblende mit `d=2.0` fest im Code.
Sie ist jetzt `--blende-aus` und **auf 4 s voreingestellt**.

→ betrifft: **alle Short-Agenten.** Zwei Sekunden Ausblende sind fuer ein Bett,
das eine Minute lang laeuft, zu kurz. Und die Ausblende gehoert nicht in den
Code, sondern an die Oberflaeche — genauso wie die Einblende, die am 22.10.
aus demselben Grund herausgezogen wurde.

## 24.10.2026 — Davids „Yeah" stand 20 dB ueber dem Satz, in den es hineinfiel.

Sein Befund: *„frage ich mich, ob du Davids Ja vor oder nach Vulnerability,
kannst du das stumm schalten? Das ist irgendwie stoerend. Aber nur dieses eine
Ja."*

Gemessen, 10-ms-Aufloesung: sein eigener Satz laeuft bis Clipzeit 19,03 bei
−24 bis −30 dB, dann eine Luecke, dann von **19,09 bis 19,33 ein Einwurf mit
Spitze −2,1 dB**. Das sind rund **20 dB ueber** dem Satz, in den er faellt —
Sutcliffe sitzt an seinem eigenen Mikrofon. Deshalb faellt es auf, obwohl es
nur eine Viertelsekunde dauert.

**Und dabei ist eine aeltere Annahme von mir gekippt.** Ich hatte dieses Stueck
am 22.10. fuer SEIN Wort „like" gehalten, weil die abgenommene Untertiteldatei
vom 20.10. dort „LIKE VULNERABILITY" schreibt, und hatte das Wort entsprechend
im Bild gelassen. In Isolation transkribiert ergibt das Stueck woertlich
**„Yeah."** — gesprochen wird dort kein „like". Die Einblendung „LIKE" stand
also ueber Davids Einwurf.

Behoben: der Einwurf ist stumm (19,06–19,36), und „like" wandert in die
Einblendung mit „vulnerability" — **„LIKE VULNERABILITY"** steht jetzt ueber
dem gesprochenen Wort. Damit steht keine Einblendung ueber einer stummen
Stelle, und der abgenommene Wortlaut bleibt.

→ betrifft: jeden Short mit Gegenueber. Ein Einwurf, der ueber dem Satz liegt,
in den er faellt, ist nicht leise wegzumischen — er muss stumm. Und: ein
einzelnes Wort in der Untertiteldatei ist kein Beleg dafuer, dass es gesprochen
wurde. Im Zweifel die Stelle allein transkribieren, nicht im Zusammenhang —
im Zusammenhang errät das Modell, was grammatisch passt.

## 24.10.2026 — Die Untertitelzeile sprang beim Schnitt auf den Gast um 124 px. Der Planer hatte es angesagt.

Sein Befund: *„bei ca 0:15 ist noch ein Framing Fehler, wo du auf David
schaltest. Da ist das Bild marginal verschoben fuer einen Moment. Kannst du
bitte auf solche Details achten und diese Fehler vermeiden."*

Gefunden: `bildausschnitt.py` setzt die Zeilenhoehe **je Einstellung** aus der
gemessenen Lippe. Fuer Sutcliffes Reaktionsbild (1,67 s) kam **1143** heraus,
fuer alles andere **1267** — die Zeile sprang also um 124 px hoch und wieder
zurueck, das sind 6,5 % der Bildhoehe. Dazu kam ein zweiter, kleinerer Sprung:
der Planer gab seinen **drei Nahaufnahmen derselben Kamera** die Kaesten 608,
596 und 608 — beim Weg- und Zurueckschneiden verschiebt sich das Bild dadurch
um 12 Quellpixel, im Ausgabebild 21 px.

**Das ist ein Rueckfall hinter eine Festlegung, die er am 20.10. schon getroffen
hat:** *„Zeile bleibt auf einer Hoehe — auch beim Wechsel in die Totale.
Konstant 0,65. Das Auge hat die Zeile immer am selben Fleck."*

Behoben, zwei Regeln:
1. **Eine Zeilenhoehe fuer den ganzen Short.** Nach dem Plan wird jede `lippe`
   auf denselben Wert gesetzt.
2. **Dieselbe Kamera bekommt denselben Kasten.** Der Planer misst je
   Einstellung und kommt auf leicht verschiedene Werte; bei derselben Kamera
   ist der Unterschied ein Fehler, kein Befund. Ein Gast mit eigener Kamera
   behaelt dagegen seinen eigenen Kasten — an Sutcliffes Reaktionsbild
   nachgesehen: mit x 680 sitzt sein Gesicht mittig, mit x 608 nicht.

→ und das ist die eigentliche Lehre: **der Planer hat den Fehler selbst
ausgedruckt.** In seiner Ausgabe stand `Lippe 1143` neben vier Mal `Lippe 1267`,
und ich habe darueber hinweggelesen. Die Ausgabe eines Werkzeugs ist kein
Protokoll, sondern ein Befund — **jede Zeile, die von den anderen abweicht,
gehoert geprueft, bevor gerendert wird.** Drei Renderlaeufe haetten das
gespart.

→ betrifft: alle Short-Agenten, die `bildausschnitt.py` benutzen.

## 24.10.2026 — Die Hautfarbenmessung findet dunkle Haut nicht. Jede Messung wurde nachgesehen.

Fuer die Mitte-Pruefung der B-Roll (sein Befund: *„Myron, Tate und HS ticky
tocky sind alle am Rand und der wird auf YT noch teilweise rausgeschnitten"*)
habe ich `video/gesicht_mitte.py` geschrieben: hautfarbene Pixel im oberen
Bildteil, Spaltenverteilung ueber acht Bilder, Gipfel statt Schwerpunkt.

**Bei vier von sechs Stuecken hat es gestimmt, bei zwei nicht — und das eine
davon war Myron Gaines.** Die uebliche Hautmaske (`r>95, g>40, b>20, r>g, g>b`)
ist auf helle Haut geeicht. Bei ihm hat sie stattdessen einen orangefarbenen
Hintergrund gegriffen und den Ausschnitt um **1093 Pixel** danebengelegt — ins
Leere. Beim Mann mit der Sonnenbrille lag sie 62 px daneben.

| Stueck | gemessen | nach Augenschein |
|---|---|---|
| HS Tikky Tokky | x 890 | **890** ✓ |
| Hoodie | x 1016 | **1016** ✓ |
| Tate | x 738 | **738** ✓ |
| Sonnenbrille | x 1095 | **956** ✗ |
| **Myron Gaines** | **x 387** | **1480** ✗ |
| Maske | x 980 | **980** ✓ |

→ betrifft: alle, die Motive automatisch mittig setzen. **Eine Hautmaske ist
ein Vorschlag, kein Befund** — und sie ist bei dunkler Haut unzuverlaessig, was
sie unbrauchbar macht, wenn man sie ungeprueft laufen laesst. Der Kontaktabzug
mit eingezeichneter Mittellinie kostet eine Minute und entscheidet. Das steht
jetzt auch im Kopf des Werkzeugs.

→ und der Grund, warum das ueberhaupt zaehlt: **in 9:16 bleiben von einem
Querformat nur rund ein Fuenftel der Breite uebrig.** Wer darin am Rand steht,
wird von den Bedienelementen von YouTube Shorts teilweise verdeckt. Mittig ist
hier keine Geschmacksfrage.

## 24.10.2026 — Baender abgelehnt. In 9:16 ist Zoom 1,0 das Ende, und dabei bleibt es.

Auf seinen Wunsch *„du musst nochmal ein bisschen rauszoomen"* hatte ich einen
3:4-Ausschnitt mit unscharfer Fuellung gebaut, weil der randlose 9:16-Ausschnitt
bei voller Hoehe rechnerisch am Anschlag ist. Seine Antwort:

> *„Nein, was soll der Scheiss?! Ich will keine Baender. Bitte rueckgaengig
> machen. Dann lassen wir's lieber so wie bei der vorherigen Version."*

**Damit ist die Frage entschieden, nicht offen:** geht weiter nur mit Baendern,
bleibt es eng. Nicht noch einmal vorschlagen.

→ betrifft: alle Short-Agenten. Die Rechnung dahinter gilt weiter und erspart
die Runde: aus 1920x1080 ist der breiteste **randlose** 9:16-Ausschnitt 608 px
breit, also die volle Hoehe; `bildausschnitt.py` begrenzt den Zoom darum hart
auf 1,0. Wer nach „ein bisschen rauszoomen" gefragt wird und schon auf 1,0
steht, hat nichts mehr zu geben — **das gehoert gesagt, bevor eine Fassung mit
Baendern gebaut wird**, nicht danach.

→ und was dabei stehenblieb: die konstante Zeilenhoehe und der einheitliche
Kasten je Kamera haben den Schnitt auf den Gast sichtbar aufgeraeumt
(*„der Uebergang zu David ist jetzt besser"*). Das war die Korrektur, die
gewirkt hat — nicht der Zoom.

## 24.10.2026 — Das „Zittern" beim Schnitt war EIN Bild mit dem falschen Ausschnitt. Vier Runden gebraucht.

Sein Befund, dreimal in Folge: *„Das Bild shattered/vibriert quasi bei dem
Switch auf David"* · *„bei ca 0:15 ist noch ein Framing Fehler"* · *„das Bild
zittert immer noch so, wenn du ueberspringst. Also wo ist das Problem? Das kann
doch nicht so schwer sein."*

**Er hatte recht, es war nicht schwer — es war ein Bild.** Gemessen an der
Bild-zu-Bild-Differenz im fertigen Short standen am Schnitt **zwei** grosse
Spruenge statt einem:

| | Schnitt auf David | Schnitt zurueck |
|---|---|---|
| vorher | 34,6 **und 26,9** | 31,2 **und 26,4** |
| behoben | 29,5 | 28,0 |

Zwei Spruenge heissen: dazwischen steht ein Bild, das zu keiner der beiden
Einstellungen passt. Im Kontaktabzug der Einzelbilder war es dann zu sehen —
Davids **erstes** Bild stand 128 px weiter links als sein zweites.

**Ursache:** `bildausschnitt.py` schaetzt die Einstellungsgrenzen und meldete
19,03 s. Der Kamerawechsel liegt bei **19,0000 s**. Der Renderer schneidet die
Einstellungen mit `trim` nach Zeitstempel, und `trim=0:19.03` nimmt alles
*kleiner als* 19,03 — also auch das Bild bei 19,0000, das schon zur neuen
Einstellung gehoert. Es bekam dadurch den Kasten der alten. Dasselbe am anderen
Ende. Betroffen waren drei Grenzen: 19,03 statt 19,0000 · 21,03 statt 21,0000 ·
43,57 statt 43,3667 (sechs Bilder, lag aber unter der B-Roll).

**Warum ich es dreimal nicht gefunden habe, und das ist der eigentliche
Befund:** ich habe am fertigen Bild geprueft und die Plangrenzen in
**Ausgabezeit** gegengerechnet. Der Ausschnitt wird aber in **Clipzeit** gesetzt,
vor der Beschleunigung, und `trim` nimmt alles kleiner als die Grenze. Ich habe
in der falschen Zeitrechnung geprueft, daraus „kein Kastensprung" geschlossen
und dreimal „keine technische Ursache gefunden" gemeldet — waehrend die Ursache
jedes Mal dastand.

→ betrifft: alle, die `bildausschnitt.py` benutzen. **Die Einstellungsgrenzen
aus dem Plan sind Schaetzungen und gehoeren durch die Bild-fuer-Bild-gemessenen
ersetzt, bevor gerendert wird.** Und die Probe darauf ist billig: am fertigen
Short die Bild-zu-Bild-Differenz messen — **an einem sauberen Schnitt steht
genau EIN grosser Sprung.** Stehen zwei, sitzt dazwischen ein Bild, das nicht
dahin gehoert.

---

## 24.10. — „die Shorts, die ich selbst geschnitten habe, hatten eine bessere Auflösung"

Sein Befund: *„mir ist aufgefallen, die Shorts, die ich selbst geschnitten
habe, irgendwie hatten die eine bessere Auflösung als die du geschnitten
hast. Woran liegt das? Und kannst du die Auflösung bitte genauso
hochhalten?"*

**Er hat recht, und es liegt nicht am Bildinhalt.** Gemessen an vier seiner
eigenen Exporte im Drive (`David Sutcliffe Patriarchy/Hollywood/about Andrew
Tate/Gilmore Girls & Friends.mov`):

| | seine Shorts | meine bis 24.10. |
|---|---|---|
| Bildgröße | **2160×3840** | 1080×1920 |
| Codec | HEVC | H.264 |
| Datenrate | **19,6–20,2 Mbit/s** | 4,1–5,7 Mbit/s |

**Echtes Bilddetail haben seine aber nicht mehr als meine.** Probe: ein Bild
auf eine kleinere Breite herunterrechnen und wieder hochrechnen — was dabei
verloren geht, war vorher echtes Detail. Im Gesichtsbereich, ohne Schrift:

| herunter auf | sein 2160er Bild | mein 1080er Bild |
|---|---|---|
| 1080 px | 0,32–0,58 RMS | — |
| ~600 px | 0,42–0,86 RMS | 0,54–0,76 RMS (bei 540) |

Bei 1080 px Breite verliert seine 4K-Datei praktisch nichts — es war also
nie Detail darüber. **Seine 4K-Shorts sind genauso hochgerechnet wie meine;
die Quelle ist beide Male derselbe 1080p-Master im Drive** (18,6 GB,
1920×1080 — ein 9:16-Fenster daraus hat 608 echte Spalten). Was seine
Dateien besser machen, sind drei andere Dinge:

1. **Schrift, Logo und Outro werden vierfach so fein gezeichnet.** Gemessen
   an derselben Untertitelzeile: die Kante hat bei 2160 nativ einen
   Gradienten von 255 (harte Kante), bei hochgerechnetem 1080 nur 148
   (weiche Kante). Das ist der Teil, den das Auge als „schärfer" liest.
2. **Ein 4K-Upload wird bei YouTube anders behandelt** als ein
   1080p-Upload — andere Codec- und Datenratenstufe.
3. **20 Mbit/s statt 4–6 Mbit/s** heißt weniger Kompressionsschaden, bevor
   YouTube überhaupt anfängt.

**Geändert:** `shorts-render.py` hat jetzt `--ausgabe` mit **Vorgabe 2160**
(= 2160×3840). Der Entwurfsraster der Untertitel bleibt dabei auf 1080×1920
(`AW/AH`): libass rechnet von `PlayRes` auf die Bildgröße hoch und zeichnet
die Schrift vektoriell, **darum sitzt jede einmal abgenommene Lippenhöhe
weiter genau da, wo sie gemessen wurde** — nachgeprüft, die hellen
Schriftzeilen liegen in beiden Größen bei 554–1683. Alle Werte in
Ausgabepixeln (Logobreite, B-Roll-Kante) wachsen mit.

`outro_anhaengen.py` **liest die Bildgröße jetzt am Hauptteil** statt sie
fest auf 1080×1920 zu setzen — sonst hätte dieser letzte Schritt den
fertigen 4K-Short wieder auf ein Viertel der Pixel gerechnet. Und er läuft
dort jetzt auf `-preset medium` statt `veryfast`: dieser Schritt kodiert den
ganzen Short ein zweites Mal, und `veryfast` hat dabei mehr weggeworfen als
nötig.

**Kosten:** Rendern dauert etwa dreimal so lang (6 s Probe: 13 s auf 1080,
41 s auf 2160), die Datei wird etwa dreieinhalbmal so groß.

→ betrifft: alle Short-Agenten. **Ab sofort 2160×3840 ausgeben** — und
wenn jemand eine Kette hat, die die Bildgröße irgendwo fest hinschreibt,
gehört sie gemessen, nicht gesetzt. Ehrlich dazugesagt: mehr echtes
Bilddetail wird es davon nicht, solange der Master 1080p ist. **Läge die
Folge als 4K-Datei im Drive, wäre der Gewinn ein echter** — ein 9:16-Fenster
aus 3840×2160 hat 1216 echte Spalten statt 608.
