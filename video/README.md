# Shorts in Eigenregie — Stand 18.10.2026

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
python3 video/shorts-render.py --src folge.mp4 --start 00:12:04 --end 00:12:48 \
        --out short.mp4 --focus 0.45 --srt clip.srt
```

`--focus 0..1` schiebt den 9:16-Ausschnitt horizontal durchs Breitbild.

## Blockiert — und zwar genau hier

| Host | Fehler | wofür |
|---|---|---|
| `huggingface.co` | **403 durch den Proxy** | Whisper-Modell für wortgenaue Untertitel |
| `youtube.com` | DNS nicht aufgelöst | seinen Kanal lesen, Abrufe messen, Auto-Captions |
| `greymattermedia.capetown` | DNS nicht aufgelöst | Mark Kaplans Seite |

Alle drei über **Cloud-Umgebung → Edit → Network access → Allowed domains**
(Haken bei den Paketmanagern drin lassen).
Doku: https://code.claude.com/docs/en/cloud-environments#network-access

## Die Arbeitsteilung, ehrlich aufgeschrieben

**Ganz ohne ihn:** Clipauswahl aus einem Transkript · Hook, Titel, Beschreibung,
Hashtags · Untertitel setzen und einbrennen · vertikal zuschneiden und rendern ·
Datei zurückgeben.

**Einmal pro Folge von ihm:** die Masterdatei in `[Alfred] Inbox` auf Drive
(`1BTFS3WpV2XbTMDz0knlSMOPjNOziRzO9`) — oder ein Drive-Link. Mehr nicht.

**Einmal überhaupt:** die drei Hosts oben freischalten.

## Die Grenze, die bleibt

Ein **fester** 9:16-Ausschnitt ist nicht dasselbe wie automatische
Sprechererkennung. Bei einem Zweiergespräch in einer Totale schneidet AutoPod
besser, weil es auf den jeweils Sprechenden umschneidet. Was hier geht:

- fester Ausschnitt mit frei wählbarer Position (`--focus`) — gut bei einer
  Person oder enger Kameraführung,
- **Umschnitt pro Clip-Abschnitt**, wenn die Sprecherwechsel aus dem Transkript
  bekannt sind — damit kommt man nah an AutoPod heran,
- echtes Multicam, **wenn getrennte Kameradateien vorliegen**. Genau das ist
  die offene Frage an Cory/JPR aus `youtube/ai-editor.md`, und sie entscheidet,
  ob dieses Werkzeug AutoPod ($29/Monat) ersetzt oder nur ergänzt.

## Warum das diesmal nicht im Leerlauf endet

Die drei Gerüste vom August (`youtube/README.md`, `shorts-elements.md`,
`ai-editor.md`) stehen still, weil alle drei auf einen Upload von ihm warten —
von einem Mann in der Reha. Hier ist der Zuschnitt umgekehrt: **alles, was
Denkarbeit ist, läuft ohne ihn.** Er legt eine Datei ab, sonst nichts.
