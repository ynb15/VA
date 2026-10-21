# Lernen — Cinematic Content Assistant

Schreibt nur dieser Agent. Anhängen, neueste Einträge unten.
Lesen: `git show origin/claude/ai-chief-of-staff-cz83jv:LERNEN.md`

---

## 21.10.2026 — Nachtrag der drei Commits, um die Alfred gebeten hat

### Es gibt drei Standbilder je Short, nicht eines
`i.ytimg.com/vi/<id>/` liefert neben `oardefault.jpg` auch **`oar1.jpg` und
`oar3.jpg`**, alle HTTP 200 ohne Anmeldung, alle 1080×1920. `oar2` ist
bitgleich mit `oardefault`. Damit sind **drei über die Laufzeit verteilte
Zeitproben** je Short messbar statt einer.

Für Langvideos gilt dasselbe Muster mit `maxresdefault`/`hq720`.
→ betrifft: content-*, thumbnails, head-of-content

### YouTubes Vorschaustreifen ist offen, die Mediendaten sind zu
**Der wichtigste Zugang, den ich heute gefunden habe.** Zu jedem Video gibt es
ein `storyboard`: ein Gitter kleiner Einzelbilder (160×90) über die volle
Laufzeit, auf `i.ytimg.com`, ohne Anmeldung. **Damit lässt sich jedes Video als
Kontaktabzug ansehen, ohne es zu laden** — und der Download ist gesperrt
(*„Sign in to confirm you're not a bot"*, am 21.10. erneut geprüft).

* Werkzeug: **`video/vorschaustreifen.py`** (auf `claude/content-cinematic`).
* **Nur der Player-Zugang `android_vr` kommt durch.** `visionos`, `tv`,
  `web_safari`, `web_embedded`, `mweb` werden abgewiesen — am 21.10. alle sechs
  durchprobiert.
* **Die Abweisung ist mengenabhängig, nicht videoabhängig.** Nach zwei bis
  vier Abrufen in Folge blockt YouTube für Minuten. Pause von 10 s zwischen
  Videos, kurze Wiederholungskette, und **wiederaufnehmbar bauen** — der
  Container wird ohnehin zwischen den Zügen eingesammelt.
* **Grenze, die dazugehört:** der Takt (Abstand zweier Vorschaubilder) skaliert
  mit der Laufzeit — 4,9 s bei 9 Minuten, 9,9 s bei 18. Liegt die Sättigung
  (Anteil unterschiedlicher Nachbarbilder) nahe 1,00, schneidet das Video
  schneller als der Takt und **die Einstellungslänge ist nicht messbar.**
  Gemessene Werte lagen bei 0,88 und 0,89, also am Anschlag. Nicht behaupten.

→ betrifft: alle Content-Agenten, thumbnails, head-of-content

### Williamson: zwei Formate, die innerhalb eines Shorts nie wechseln
33 Shorts × 3 Zeitproben = 99 Bilder, `video/williamson-bildsprache.md`.

| | |
|---|---|
| randlos 1080×1920 | **26 Shorts (79 %)** |
| 980×980-Kasten auf Schwarz (x=50, y=470) | **7 Shorts (21 %)** |

Der Kasten steht in **allen drei** Zeitproben derselben Shorts (`KKK`, nie
`KRK`). **Er ist der Rahmen des ganzen Shorts, nicht die Einblendung darin** —
im Kasten wird zwischen Film und Sprecher geschnitten. Die frühere Lesart
„randlos = Sprecher, Kasten = B-Roll" stammte aus je einem Bild und ist falsch.

**Lehre, die über den Fall hinausgeht: dass etwas gut messbar ist, macht es
nicht zum Inhalt.** Der Kasten ließ sich auf das Pixel messen und wurde deshalb
für die Sache gehalten; Kleinschreibung und weißes Aktivwort wurden im selben
Bild richtig als fremde Handschrift erkannt.
→ betrifft: content-*, thumbnails

### Williamsons Schrift ist viermal schmaler als unsere
| | Williamson randlos | Williamson Kasten | unser Stand |
|---|---:|---:|---:|
| Zeilenhöhe Median | 48 px | 50 px | — |
| **Zeilenbreite Median** | **220 px** | **342 px** | **861 px (breiteste)** |
| Zeilenmitte Median | 0,550 | 0,499 | 0,65 |
| Wörter je Einblendung | 1–2 | 1–2 | genau 3 |

Nicht die Schriftgröße macht den Unterschied — die Zeilenhöhen liegen
beieinander — sondern **drei Versalienwörter gegen ein bis zwei
kleingeschriebene**. **Befund, keine Empfehlung:** Versalien, Gelb und drei
Wörter sind sein abgenommener Stil.
→ betrifft: content-*

### Die Titelkarte: Maße für `--kopfzeile`
**13 von 33 Williamson-Shorts (39 %)** tragen eine fette zweizeilige Titelkarte
zusätzlich zur laufenden Einblendung (*How To Spot A Liar*, *The Sign Of A
Deteriorating Marriage*, *The Winter Arc Mindset*).

| | gemessen |
|---|---|
| Lage | **0,585 der Bildhöhe** — also **unter** der laufenden Zeile (0,550) |
| Breite | Median **840 px** |
| Satz | zwei Zeilen, fett, Versalanfänge, **weiß** |
| Dauer | in **1 von 3** Zeitproben sichtbar — steht einen Teil der Laufzeit |

Alfred meldet, `--kopfzeile` sei gebaut und die Entscheidung hell/dunkel stehe
noch aus. **In allen 15 gemessenen Bildern ist die Karte weiß auf dem Bild,
nicht dunkel** — das entscheidet die Frage aber nicht, denn es ist Williamsons
Handschrift und nicht seine. Die Maße oben sind brauchbar, die Farbe ist seine
Wahl.
→ betrifft: content-*, head-of-content

### Geprüfte Quellen und die Rechtefrage
`video/aufnahmeliste-hypermaskulinitaet.md`. Jede Kennung, jeder Kanal, jede
Laufzeit am 21.10. über `yt-dlp ytsearch` geprüft — nichts aus dem Gedächtnis.

**Die Rechtelage, weil sie jeden von uns betrifft:** er sagte, YouTube erlaube
die Übernahme fremder YouTube-Inhalte. **Das trifft nicht zu.** YouTube vergibt
keine Nutzungsrechte an fremden Inhalten; die Nutzungsbedingungen untersagen
das Herunterladen sogar. Was es gibt, ist **Fair Use bzw. § 51 UrhG** — eine
Schranke, über die im Streitfall ein Gericht entscheidet, keine Plattform-
freigabe. Praktisch läuft es über **Content ID**: Regelfall ist kein Strike,
sondern ein Anspruch, der die Monetarisierung dieses Videos abzieht — **auf
seinem Kanal**. *Er hat es am 21.10. so entschieden, und damit ist es
entschieden* — der Eintrag steht hier, damit niemand die falsche Begründung
weiterträgt.

**Unverändert und ohne Ausnahme: Musik und Medien für Veröffentlichtes holen
wir nicht aus dem Netz.** Er legt die Dateien in den Drive-Eingang.

**Technisch am 21.10. nachgemessen:** `www.youtube.com` HTTP 200;
Medien-Download abgewiesen; `archive.org` und `commons.wikimedia.org` keine
Verbindung. Im Drive liegt **kein** Filmmaterial, nur sein eigenes.
→ betrifft: alle

### Quellenart schlägt Messung bei der Einstellungslänge
Aus seiner Rückmeldung vom 20.10. (*„gefühlt eine Sekunde da und störend"*) und
dem Vorschaustreifen zusammen:

* **Ganze Szenen** (Miramax, Sony Pictures, Movieclips-Einzelszenen) haben die
  Einstellungen des Films.
* **Szenen-Zusammenschnitte** („TOP 3 BEST SCENES", „Best Moments at The
  Garrison") reihen ganze Szenen — **viel Abwechslung, trotzdem lange
  Einstellungen. Die richtige Form.**
* **Moment-Zusammenschnitte** („Funny Moments", TikTok-Compilations) schneiden
  im Sekundentakt. Unbrauchbar.
* **Trailer** sind die schlechteste Quelle: 1–2-Sekunden-Stücke mit Blenden,
  und eine Szenenerkennung sieht eine Überblendung nicht.

**Eingebrannte Zeichen sieht man nur am Kontaktabzug, in keiner Zahl.**
Binge Society brennt sein Logo oben links ein. Bei einem randlosen
9:16-Ausschnitt aus der Mitte fällt das heraus (es bleiben 31,6 % der Breite) —
**oben oder unten mittig wäre es drin.** Je Quelle nachsehen.
→ betrifft: content-*, thumbnails

### Die Rechnung, die Aufnahmearbeit spart
Er fürchtete hunderte Bildschirmaufnahmen. Gegengerechnet: 5 Blöcke × 2–4
Einstellungen = **rund 15 Einstellungen für den ganzen Short**. Eine einzige
18-Minuten-Aufnahme enthält **97 verschiedene Bilder** (gemessen,
`LwG6aia2vn0`). **Sechs Aufnahmen reichen.**
→ betrifft: content-*

### Beschnitt und Auflösung bei fremdem Material
| Film im Bild | Aufnahme | 9:16-Ausschnitt | Hochskalierung |
|---|---|---|---|
| 16:9 | 1080p | 608×1080 | 1,78× |
| **2,39:1** (Wolf of Wall Street, Batman) | 1080p | 452×803 | **2,39×, sichtbar weich** |
| 2,39:1 | 2160p | 903×1606 | 1,20× |

`--broll-modus unschaerfe` löst das ohne vierfachen Speicherplatz: der Film
steht quadratisch und fast unskaliert scharf in der Mitte (803→1080 = 1,34×),
dahinter füllt er sich selbst vergrößert und unscharf das Hochformat.
→ betrifft: content-*

### Zwei Regeln aus dem Into-the-Wild-Lauf, die allgemein gelten
* **Wenn die Automatik dreimal falsch liegt, ist es kein
  Schwellenwert-Problem.** Vier Anläufe, Trailerschrift automatisch zu finden,
  maßen an einer bekannten Schriftstelle 0,0000 und an einer sauberen 0,0064 —
  genau verkehrt herum. Ein Kontaktabzug über die volle Länge, ein Bild je
  Sekunde, kostet eine Minute und beantwortet die Frage endgültig.
* **Variable Bildrate macht Zeitmarken unzuverlässig.** Eine Datei meldete
  „29,70 fps bei 60 tbr"; erst nach `fps=30, -g 30` stimmten alle Zeiten. Das
  vorher zu tun hätte zwei von vier Anläufen erspart.
* **`ffmpeg` frisst `stdin`.** In einer Schleife gehört `-nostdin` in jeden
  Aufruf, sonst verliert die Schleife nach dem ersten Durchlauf ihre Liste.
* **`gblur=sigma=42` auf 1080×1920 kostete 25 Minuten für einen 33-s-Short.**
  Verkleinern auf ein Viertel, `sigma=11`, wieder vergrößern: kein sichtbarer
  Unterschied, ein Sechzehntel der Rechenzeit.
→ betrifft: alle Content-Agenten

### Aufgenommen aus Ausgabe 1, mit Folgen für meine nächste Runde
* **Der Ausschnittsplaner plant an einem Kameraschnitt nicht neu** (Alfreds
  Befund, Aaronson-Short, 56 s fester Kasten). **Ich prüfe das am
  Hypermaskulinitäts-Short, bevor ich die B-Roll rechne** — er läuft 55,9 s und
  wechselt zwischen Nahaufnahme und Totale.
* **Drive liefert Fehler als HTTP 200 mit 2040 Byte.** Beim Neuholen des
  Master-Fensters Statuscode **und** Blocklänge prüfen.
* **`ZEILE_FEST = 0,65` gilt für das Sutcliffe-Studio** — für diesen Short also
  richtig, nicht ungeprüft auf andere Räume übertragen.
