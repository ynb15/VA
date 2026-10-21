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

- **Korrektur an `LERNEN.md`: die Zeitmarkenliste ist nicht allgemein, sie
  gehört zu einem bestimmten Video.** In Ausgabe 3 steht sie als Beleg für
  „sein Format" mit Datum 15.09. Gemessen: er hat sie am **14.09.2026 um
  22:20 Kapstadt** in der DM an Isabelle geschickt, **direkt nach dem Link
  `youtu.be/q3_kLgYIXGQ`** — dem Garden-Gastauftritt. Die Zuordnung hält an den
  Kapiteln: `1:21:00 My Why` gegen Kapitel `1:19:07 His why: giving a voice to
  people who don't usually get one`, `16:00 Movie` gegen `16:19 what would the
  hero do`. **Für dieses Video existiert seine Auswahl also schon** — wer hier
  neu anfängt, doppelt seine Arbeit.
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
