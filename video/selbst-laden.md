# Szenen selbst holen, ohne Bildschirmaufnahme

**Seine Ansage vom 21.10.:** *„Es muss eine Alternative geben. Du musst einen
Weg finden, wie du eigenständig diese Szenen aus den Filmen bekommst."*

## Woran es heute hängt — gemessen, nicht vermutet

**Nicht am Netz.** Der Proxy dieses Containers ist nicht selektiv
(`"selective": false`), YouTube-Seiten antworten mit HTTP 200, Vorschaustreifen
kommen durch.

**Sondern an YouTubes eigener Bot-Prüfung.** Sobald die *Videodaten* verlangt
werden, antwortet YouTube: *„Sign in to confirm you're not a bot."* Am 21.10.
mit sieben Player-Zugängen geprüft — `default`, `visionos`, `tv`,
`web_safari`, `web_embedded`, `mweb`, `android_vr`. Alle abgewiesen.
`android_vr` liefert Metadaten und Vorschaustreifen, aber keine Videodaten.

**Die Fehlermeldung nennt die Lösung selbst:** *„Use --cookies-from-browser or
--cookies for the authentication."* YouTube will eine angemeldete Sitzung
sehen.

## Der Weg: einmal eine Cookie-Datei, danach hole ich alles selbst

**Was das heißt, ehrlich:** eine Cookie-Datei *ist* eine angemeldete Sitzung.
Wer sie hat, ist bei Google eingeloggt — nicht nur für YouTube. Und YouTube
kann Konten sperren, die automatisiert Videos laden.

**Deshalb: nicht Dein Hauptkonto.** Ein eigenes, leeres Google-Konto nur dafür.
Wird es gesperrt, ist nichts verloren.

### Die Schritte, einmalig

1. **Ein neues Google-Konto anlegen** (oder ein leeres, das Du nicht brauchst).
2. In einem Browser **mit diesem Konto auf youtube.com einloggen** und ein, zwei
   Videos ansehen, damit das Konto nicht ganz frisch wirkt.
3. **Die Erweiterung „Get cookies.txt LOCALLY"** installieren (Chrome und
   Firefox, quelloffen, lädt nichts hoch — die Daten bleiben auf Deinem
   Rechner, bis Du sie selbst ablegst).
4. Auf **youtube.com** die Erweiterung anklicken → **Export** → es entsteht
   `youtube.com_cookies.txt`.
5. Die Datei in den **Drive-Eingang** legen.
6. **Im Browser von diesem Konto abmelden** — sonst wird die Sitzung beim
   nächsten Seitenaufruf erneuert und die exportierte Datei ungültig.

### Was ich dann tue
* Die Datei liegt **nur im Scratchpad**, nie im Repo — `.gitignore` schließt
  jedes `*cookies*` aus, auch bei einem versehentlichen `git add -A`.
* `yt-dlp --cookies` lädt **nur die Minuten, die gebraucht werden**
  (`--download-sections`), nicht ganze Filme.
* **Ich teste es in dem Moment, in dem die Datei da ist**, und sage Dir
  innerhalb von Minuten, ob es geht. Garantieren kann ich es vorher nicht:
  YouTube prüft auch die Herkunft der Anfrage, und dieser Container sitzt in
  einem Rechenzentrum.
* **Cookies laufen ab** — nach Wochen, manchmal früher. Dann einmal neu
  exportieren.

## Was das ändert

| | Bildschirmaufnahme | mit Cookie-Datei |
|---|---|---|
| wer holt die Szenen | **Du**, Film für Film | **ich**, selbstständig |
| Bildqualität | was der Bildschirm zeigt, mit Player-Resten | die Originaldatei, bis 4K |
| Zeitangaben | Du musst sie treffen | ich schneide sie selbst |
| neue Quelle | wieder eine Aufnahme | eine Zeile |

## Was sich nicht ändert
Es ist dasselbe Material wie bei der Bildschirmaufnahme. Die Entscheidung,
Filmszenen zu verwenden, hat er am 21.10. getroffen; der Weg, auf dem sie in
den Container kommen, ändert daran nichts.
