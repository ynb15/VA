# Shorts in Eigenregie — Stand 19.10.2026

**Was geprüft wurde, nicht behauptet.** Alle Angaben unten sind in dieser
Maschine ausgeführt worden, nicht geschätzt.

## Läuft, ohne dass Yannick irgendetwas tut

| | |
|---|---|
| **ffmpeg** | 7.0.2 static, über `pip install imageio-ffmpeg` von pypi — kein apt nötig |
| **Encoder** | libx264, aac |
| **Filter** | `crop`, `scale`, `zoompan`, `subtitles`, `ass` (`drawtext` fehlt, wird nicht gebraucht) |
| **Schrift** | DejaVu Sans Bold vorhanden |
| **Maschine** | 4 Kerne, 15 GB RAM, ~30 GB frei, **kein GPU** |
| **Tempo** | 11 s Short in **6,9 s** gerendert — schneller als Echtzeit |

`video/shorts-render.py` nimmt eine Langfassung, Start/Ende, einen
Bildausschnitt und Untertitel und gibt einen fertigen **1080×1920 H.264/AAC**
mit `+faststart` aus. Belegt durch `video/beispiel-short.mp4`.

```
# einfachster Fall: ein fester Ausschnitt
python3 video/shorts-render.py --src folge.mp4 --start 00:12:04 --end 00:12:48 \
        --out short.mp4 --focus 0.45 --srt clip.srt

# der volle Weg: Einstellungen erkennen, dann rendern
python3 video/bildausschnitt.py clip.mp4 --json plan.json
python3 video/shorts-render.py --src clip.mp4 --plan plan.json \
        --tempo 1.1 --auto-captions --out short.mp4
```

`--focus 0..1` schiebt den 9:16-Ausschnitt horizontal durchs Breitbild.
`--tempo` beschleunigt wie beim Export (seine Folgen laufen auf **1,1**).

## Nicht mehr blockiert

Die drei Hosts, die hier am 18.10. als gesperrt standen, sind seit der
Freischaltung am 19.10. erreichbar:

| Host | wofür | Stand |
|---|---|---|
| `huggingface.co` | Whisper-Modell für wortgenaue Untertitel | **läuft** |
| `youtube.com` | Kanal lesen, Abrufe messen, Auto-Captions | **läuft, ohne API-Schlüssel** |
| `greymattermedia.capetown` | Mark Kaplans Seite | **läuft** |

**Kein API-Schlüssel, kein OAuth, kein Google-Cloud-Projekt** — `yt-dlp` liest
Metadaten, Abrufzahlen und automatische Untertitel ohne Anmeldung.
**Was nicht geht:** die Mediendaten selbst. YouTube antwortet auf die
Videobytes mit **403** — das kommt von YouTube, nicht vom Proxy (geprüft gegen
`$HTTPS_PROXY/__agentproxy/status`, dort steht kein Fehlschlag für den
Medienhost). Deshalb wird aus dem **Drive-Master** geschnitten, nicht aus der
veröffentlichten Folge.

## Die Arbeitsteilung, ehrlich aufgeschrieben

**Ganz ohne ihn:** Clipauswahl aus einem Transkript · Hook, Titel, Beschreibung,
Hashtags · Untertitel setzen und einbrennen · vertikal zuschneiden und rendern ·
Datei zurückgeben.

**Einmal pro Folge von ihm:** die Masterdatei in `[Alfred] Inbox` auf Drive
(`1BTFS3WpV2XbTMDz0knlSMOPjNOziRzO9`) — oder ein Drive-Link. Mehr nicht.

**Einmal überhaupt:** die drei Hosts freischalten — **am 19.10. erledigt.**

## Die Grenze, die bleibt

**Seit dem 19.10. kleiner als vorher.** `bildausschnitt.py` entscheidet selbst,
ob eine Einstellung eine Nahaufnahme oder eine Totale ist, und stapelt die
Totale (beide übereinander, 1080×960 je Hälfte) statt auf die Tischplatte
zwischen den beiden zu schneiden. Die Untertitel sitzen an der gemessenen
Mundhöhe und springen mit dem Kameraschnitt mit.

**Was weiterhin fehlt:** echtes Umschneiden auf den jeweils Sprechenden. Im
Stapel weiß das Werkzeug nicht, wer gerade redet — dafür bräuchte es
Lippenbewegung je Person, und bei zwei Personen in einer Totale ist die zu
klein für das Bewegungsmaß, mit dem hier gearbeitet wird. Echtes Multicam geht
nur, **wenn getrennte Kameradateien vorliegen** — das ist die offene Frage an
Cory/JPR aus `youtube/ai-editor.md`, und sie entscheidet, ob dieses Werkzeug
AutoPod ($29/Monat) ersetzt oder nur ergänzt.

## Warum das diesmal nicht im Leerlauf endet

Die drei Gerüste vom August (`youtube/README.md`, `shorts-elements.md`,
`ai-editor.md`) stehen still, weil alle drei auf einen Upload von ihm warten —
von einem Mann in der Reha. Hier ist der Zuschnitt umgekehrt: **alles, was
Denkarbeit ist, läuft ohne ihn.** Er legt eine Datei ab, sonst nichts.
