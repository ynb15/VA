# Shorts I — Messungen und Lehren

## Renderschleife beschleunigt: gemessen, nicht geschaetzt (26.11.2026)
→ betrifft: content-*

Anlass, seine Worte: *„Das kann nicht sein, dass ich mit jeder Verbesserung,
dass jedes Mal das Ding neu gerendert werden muss. Also das frisst ja
Stunden."* An einem einzigen Short (Kingsbury, Pilze, 1:14,6) waren es an
diesem Tag vier volle Durchlaeufe, drei davon nur wegen eines Wortes in
`korrekturen.txt`.

### Die Zahlen, am selben Short, derselben Maschine

| | vorher (einstufig) | nachher |
|---|---|---|
| voller Durchlauf, nichts im Speicher | **206 s** | 258 s (Stufe A 45 s + B 151 s) |
| Textrunde, nur ein Wort geaendert | **206 s** | **150 s** |
| Vorschau zum Hinsehen | – | **46 s** |
| drei Standbilder | – | **2 s** |

### Mein Befund war falsch, und das ist die eigentliche Lehre

Die Vermutung war: das 4K-Master frisst die Zeit, also eine Zwischendatei
dazwischen. Gemessen stimmt das nicht. Die Aufteilung der 206 s:

    Stufe A (Fenster, Hochformat, Tempo, Ton)          45 s
    Stufe B gesamt                                    151 s
      davon nackter Encode (x264 preset medium, crf 20) 102 s
      davon Look (eq, colorbalance, vignette)            45 s
      davon Untertitel brennen (115 Zeilen, 290 Woerter)   4 s

Der Encode allein ist zwei Drittel jeder Runde — und der ist sein Preset,
also unantastbar. Eine Zwischendatei kann daran nichts aendern. Sie hilft
genau 56 s je Runde, mehr nicht.

Der wirkliche Hebel ist, **gar kein Video zu rechnen**: ob die Schrift auf
der Lippe sitzt, beantworten drei Standbilder in 2 s statt eines Videos in
206 s. Das ist der Faktor 100, nicht die Zwischendatei.

### Gleichheit mit der alten Kette — nachgewiesen

* **Bild, ohne Untertitel, ueber alle 2238 Bilder: PSNR y 48,15 dB,
  Minimum 44,56 dB, kein einziger Ausreisser.** Zum Vergleich: die
  einstufige Kette selbst liegt 48,8 dB von einer verlustfreien Referenz
  entfernt. Die zweistufige ist der einstufigen also so nah wie die
  einstufige dem Verlustfreien.
* **Ton: Versatz 0 Samples.** Beide Fassungen liegen gleich weit vom
  verlustfreien Ton der Zwischendatei (27,9 und 27,8 dB) — die Differenz
  zwischen ihnen ist das Eigenrauschen des AAC-Encoders, nicht die Kette.
* Mit Untertiteln liegen rund 100 der 2238 Bilder auseinander: dort
  schaltet die gelbe Hervorhebung ein Bild (33 ms) frueher. Das Bild selbst
  ist identisch, der Unterschied sitzt ausschliesslich im Schriftband.

### Drei Fallen, alle teuer bezahlt

**1. Der Look gehoert NICHT in Stufe A.** Dort kostete er 8,7 dB PSNR
(40,1 statt 48,8) — bei fast unveraendertem SSIM, also strukturell dasselbe
Bild und trotzdem systematisch verschoben. Nicht die Quantisierung: crf 6
und crf 12 ergaben 40,08 und 40,07 dB, und selbst eine verlustfreie
ffv1-Zwischendatei brachte nur 41,41 dB. Es ist ein Farbraum-Umweg —
`colorbalance` und libass rechnen in RGB, und mit einer Zwischendatei laeuft
das Bild einmal mehr durch yuv420p und zurueck. Steht der Look in Stufe B,
macht die neue Kette dieselben Umrechnungen wie die alte, und der Verlust
ist weg.

**2. Ein Zwischenspeicher, der unter demselben Schluessel Verschiedenes
ablegt, ist schlimmer als keiner.** `--vorschau` halbierte die Bildgroesse
VOR Stufe A. Damit rechnete Stufe A selbst auf 540x960 und legte das unter
einem Schluessel ab, der von der Vorschau nichts weiss. Die naechste
Endfassung haette diese verkleinerte Datei gelesen und waere unscharf
geworden, ohne dass irgendetwas davon gemeldet haette. Gerettet hat nur,
dass der Lauf abbrach, weil Logo und Outro nicht mehr zur Bildgroesse
passten. In den Schluessel gehoert ALLES, was die Stufe beeinflusst, und
nichts, was sie nicht beeinflusst.

**3. Was zwischengespeichert wird, muss das Rohe sein, nicht das Fertige.**
Der Transkript-Speicher legt die ROHE Wortliste ab — nicht die fertigen
Einblendungen. Korrekturen, Gruppierung und Lippenhoehe aendern sich ja
gerade zwischen zwei Runden; eine fertige Einblendungsliste haette das
falsche Wort festgeschrieben. Genau dafuer gibt es daneben `--cues-in`:
eine ABGENOMMENE Liste einzufrieren ist etwas anderes als einen teuren
Rechenschritt zu sparen. Beides nebeneinander, mit verschiedenen Aufgaben.

### Was jetzt vor jeder Auslieferung laeuft

    python3 video/shorts-render.py ... --standbild 5,20,40     # 2 s
    python3 video/shorts-render.py ... --vorschau              # 46 s
    python3 video/nahtprobe.py fertig.mp4 <grenzen>            # Einstellungsgrenzen
    python3 video/schriftlage.py fertig.mp4                    # Schrifthoehe
    python3 video/abnahme.py fertig.mp4 --srt fertig.srt

### Zusammengefuehrt mit Shorts III

Die beiden Fassungen des gemeinsamen Werkzeugs waren auseinandergelaufen und
haben **keinen gemeinsamen Vorfahren** — `git merge` gibt es also nicht, es
war Handarbeit. Von dort uebernommen: `ohne_ueberlappung`, `--cues-in`,
`--cues-out`, `--ass-out`, `--ausgabe 1080|2160` samt der Trennung von
Ausgabegroesse (W,H) und Entwurfsraster der Schrift (AW,AH). Dort fehlten:
`_ist_frage`, `_ganze_frage`, `_logo_kasten` — ohne das letzte wird die
Marke auf 111 statt 302 px skaliert, sein Einwand vom 22.10.

Das Entwurfsraster ist dabei mehr als ein Detail: weil die Untertitel in
1080x1920 entworfen und von libass hochskaliert werden, bleibt jede einmal
abgenommene Lippenhoehe gueltig, egal in welcher Groesse ausgegeben wird.
Genau das hat die Vorschau in halber Groesse ueberhaupt erst moeglich
gemacht.

OFFEN, nicht von mir zu entscheiden: Shorts III gibt auf Wunsch 2160x3840
aus, weil seine eigenen Exporte so liegen. Vorgabe bleibt bis zu seiner
Antwort 1080x1920 — das Format, in dem er bisher alles abgenommen hat.
