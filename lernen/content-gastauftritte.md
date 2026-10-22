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
