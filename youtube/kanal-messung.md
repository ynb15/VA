# Kanalmessung @yannick-noah — 24.11.2026

Grundlage: 116 sichtbare Uploads (57 lang, 59 Shorts), Abrufe am 24.11.2026 abgerufen,
Uploaddatum fuer 104 davon. Werkzeug: yt-dlp ohne API-Key, Thumbnails von i.ytimg.com.
Rohdaten und Messskripte liegen im Scratchpad, nicht im Repo.

Klassen: **Folge** (Laufzeit >= 2000 s, n=13) — **Clip** (lang, < 2000 s, n=44) — **Short** (n=59).

## 1. Geliehene Namen

Eigenname mit eigenem Publikum im Titel (OpenAI, UFC, NFL, Andrew Tate, Hormozi,
Gary Vee, Gilmore Girls, Burning Man, Into The Wild, German School System):

| | mit Name | ohne |
|---|---|---|
| Shorts, Upload <= 120 d | n=9, Median 1.300 | n=24, Median 444 |
| Clips, Upload <= 120 d | n=9, Median 531 | n=13, Median 146 |

## 2. Politik als Ausnahme davon

Politischer Begriff im Titel (Trump, Bobby Kennedy/RFK, NPR, White House,
Democrats/Republicans, Divided, Political, Gun Rights):

n=8, Median 100 — alles andere n=107, Median 475.

Einzelwerte: 1.300 / 479 / 146 / 125 / 74 / 70 / 58 / 30.
Medianalter der politischen Titel 41 d gegen 91 d sonst; vier der acht sind
juenger als 10 Tage. Damit ist das eine Beobachtung, keine gesicherte Zahl.

## 3. Thumbnail-Layout

36 Clips und Folgen haben ein gestaltetes Cover (Markenorange ueber 0,4 % der Flaeche).
**30 davon tragen dasselbe Layout**: Hautflaeche links > 10 %, Hautflaeche rechts > 10 %,
Text in der Mitte. Gemessen ueber den Hautton-Anteil je Bilddrittel.

Die sechs Abweichler: Hormozi (2.300), NFL (1.100), Into The Wild (124),
Ketamine (57), UFC Fighter (36), Judaism (1, heute). Median rund 90 —
das Layout zu brechen hat bisher nichts eingebracht.

Keine gemessene Thumbnail-Eigenschaft trennt die Spitze vom Boden.
Spearman gegen Abrufe, Clips (n=38): Orange-Anteil +0,02, Hautanteil -0,10,
Helligkeit +0,05, Kontrast -0,25, Kantendichte -0,16. Staerkster Zusammenhang
im Datensatz ist das Alter (+0,30).

Shorts: 1 von 50 hat ein gestaltetes Cover (`His Last Fight In The UFC`).
Die uebrigen 49 sind Videoframes mit eingebrannten Untertiteln.

## 4. Rollen-Praefix (`NFL Star:`, `Millionaire:`)

Upload <= 120 Tage:
- Shorts: mit Praefix n=10, Median 281 — ohne n=23, Median 621
- Clips: mit Praefix n=6, Median 124 — ohne n=16, Median 228

Auf Folgen zeigt sich nichts: ohne die zwei Ausreisser 548 gegen 507.

## 5. Titellaenge bei Shorts

ueber 48 Zeichen: n=8, Median 243 — darunter: n=43, Median 621.
Fragezeichen im Short-Titel: n=14, Median 419 — ohne: n=37, Median 716.

## 6. Zwillinge — gleicher Moment, andere Verpackung

| Clip | Short |
|---|---|
| `Millionaire: I Met My Unborn Son on Mushrooms – Then It Came True` 35 (185 d) | `The Day He Met His Unborn Son` 1.200 (17 d) / `He Met His Unborn Son` 1.000 |
| `Into The Wild: What Chris McCandless Really Died For` 124 (103 d) | `Into The Wild: What He Really Died For` 1.600 (31 d) |
| `Why Feminism Is A BIG Mistake` 368 (170 d) | `Feminism Is A BIG Mistake` 797 (176 d) |
| `OpenAI Insider REVEALS: We created God` 192 | `OpenAI Insider: We created God` 27 (29 d) |

Vier von vier Paaren sind der kuerzere Titel; drei von vier gehen zum Short.
Das vierte geht in die andere Richtung.

## Was hier nicht steht

Ein Short-Abruf und ein Longform-Abruf sind nicht dieselbe Einheit — YouTube zaehlt
den Short frueher. Jeder Vergleich Shorts gegen Clips in dieser Datei ist deshalb
kein Reichweitenvergleich. Der Vergleich innerhalb einer Klasse ist einer.
