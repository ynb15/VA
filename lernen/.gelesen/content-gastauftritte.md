# Befunde — Gastauftritte (fremde Podcasts)

Schlüssel `content-gastauftritte`, Branch `claude/content-gastauftritte`.
Neuester Eintrag oben.

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
