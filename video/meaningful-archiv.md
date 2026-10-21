# „What makes life meaningful?" — das Archiv

**Sein Auftrag vom 21.10.2026:** die Abschlussfrage aus **allen** Folgen
schneiden und wegsortieren, damit bei Folge 100 ein Video daraus entsteht —
*„ich habe 100 verschiedene Menschen gefragt."*

**Diese Tabelle ist das eigentliche Ergebnis, nicht die Videodateien.** Aus ihr
lässt sich der Schnitt in einer Stunde bauen, auch wenn jede Datei neu gerendert
werden müsste — und das ist der realistische Fall: die sechs MP4s aus der Nacht
vom 20./21.10. sind mit dem Container weg, geliefert hat er sie, die Untertitel
liegen im Repo, die Dateien nicht.

**Der Drive-Ordner fehlt noch.** Drive-Schreibzugriffe sind nicht freigegeben
(einzige Ausnahme: das wöchentliche Protokolldokument). Bis er das freigibt,
kommen die Stücke über `SendUserFile` und das Archiv steht hier.

---

## Was geschnitten ist

Zeiten in **Masterzeit (Sekunden)**, Dauer **des fertigen Stücks** bei Tempo 1,2.
Die Untertitel liegen daneben unter `video/shorts/<datei>.srt`.

| # | Gast | Drive-ID des Masters | Frage/Antwort im Master | Dauer | Datei | geprüft |
|---|---|---|---|---|---|---|
| 1 | David Sutcliffe | `1oJjeQXjfIYtYph0gxfe8V1dhv17BBlPT` | 7222,0–7281,6 | 49,7 s | `01-sutcliffe-meaningful` | ja, von ihm abgenommenes Format |
| 2 | Scott Aaronson | `1C7CUI-B6_fBcdttR_zKIJBYraBMTtUvh` | 5894,3–5972,6 | 65,3 s | `02-aaronson-meaningful` | ja |
| 3 | Ken Stern | `1RGq-Mw0QEm5jE2WMthKPkP5OHrXvmotF` | 6150,1–6189,3 | 32,7 s | `03-ken-meaningful` | ja |
| 4 | Logan Gonzalez | `1ztggu2ua5-AntISFHHP9cBqjVhSn6Zmj` | 4957,1–5009,4 | 43,6 s | `04-logan-meaningful` | ja |
| 5 | Matt Defina | `1ubW-gMYb6_g0ZO-cOVyEFGQoKvIyGivj` | 6474,7–6513,1 | 32,0 s | `05-matt-meaningful` | ja |
| 6 | Rick Strassman | `1Hwt3_c_Ifhd7onXyC8nrHIdtjwJjxdjH` | **~7100–7160, ungenau** | 49,0 s | `06-rick-meaningful` | **nein — Ende offen** |

**Zwei Lücken in diesen sechs Zeilen, und beide sind echte Lücken:**

1. **Ricks Zeitmarke ist grob.** In `meaningful-serie.md` steht sie als
   `~7100–7160`; die anderen fünf sind auf eine Zehntelsekunde gemessen. Beim
   nächsten Zugriff auf diesen Master wird sie nachgemessen.
2. **Ricks Stück hat ein offenes Ende.** Der Vorgänger hat den kürzeren Bogen
   gewählt und das ausdrücklich ihm zur Entscheidung gelassen. Das bleibt seine
   Entscheidung.

**Das Aufnahmedatum fehlt in allen sechs Zeilen.** Drive liefert nur das
Hochladedatum, nicht das Aufnahmedatum — und die beiden liegen hier Wochen
auseinander. Die Aufnahmedaten stehen im Notion-Databank; sie kommen in die
Tabelle, wenn ich dort einmal durchgehe, nicht vorher geraten.

---

## Was in Frage kommt — alle Folgen, die aufgenommen sind

**17 aufgenommene Folgen**, gemessen am 21.10.2026 aus drei Quellen: die
veröffentlichten über `yt-dlp` vom Kanal, die Masterdateien über die Drive-Suche,
die Ordnerstruktur aus `YNB Podcast: Published` / `: In Progress` / `: Backlog`.

Nicht gezählt sind Gäste, von denen im Drive nur ein Vorbereitungsdokument liegt
und keine Aufnahme — **Bridget Woods, Cal Callahan, Cara West**. Die sind
Pipeline, keine Folge.

### Material liegt vor — das kann sofort laufen

| Gast | veröffentlicht | Länge | Master im Drive | Größe |
|---|---|---|---|---|
| Rob Bennett | `o9lM8i6XUWo` | 118:35 | `1K5E3SlIrEBL7aCM7Z-QvAeEsrXiQ5RW-` | 34,2 GB |
| Craig Makhosi | `FF-eRPgZI2k` (vermutlich) | 145:12 | `1JEWgIwIt1XIzwZphqsGnqLedKkYa9Dhm` | 27,4 GB |
| Curtis Crane | `ewgUIZGJaWQ` | 109:53 | `19S90VEL7LNfkwNCBZH6ZJDuVE3jRu6MG` (v1-Export) | **2,0 GB** |
| Eben Britton | `RG-K0fIA2-w` | 102:28 | `1lIFL8aUunQQPtTDp0vQNlaRc7of-4PfG` | 27,0 GB |
| Whitney Wheelock | `rFRIX4Yute0` (vermutlich) | 104:07 | `1iZy9XwHryVdCf3VBRM2Ya5oP_XIBjmdM` (Zweier-Kamera) | 5,0 GB |
| Kyle Kingsbury | — | — | `1mQjt0g5GVptvEDVY8w3mVN2Qa8NFlTnp` · LOW_RES `1NWMaIn8avpf0EVQvm2DhEQr73uhfioIq` | 17,0 / **1,3 GB** |
| Marian Goodell | — | — | `1LVM5nxvxjMuSmsQlz1Jys_O32y8eYe0A` · YNB-Kamera `1n4h-Qis-40e-cEcKd-hAhtyj_vgU4Hwk` | 18,5 / 10,4 GB |

**Curtis Crane und Kyle Kingsbury sind die billigsten der ganzen Liste** — von
beiden liegt ein kleiner Export vor (2,0 bzw. 1,3 GB). Die lassen sich ganz
laden, ohne das Tageslimit zu belasten. Der 33,2-GB-Rohschnitt von Curtis
(`1X9I3dODNz8RqdMml801Gk2a4E2SdmzM-`, im Drive des Cutters) wird dafür nicht
gebraucht.

**Whitney Wheelock liegt dreifach** — `(YNB)` 7,5 GB, `(Whit)` 7,5 GB,
`(Whit & YNB)` 5,0 GB. Für diese Frage ist die Zweier-Kamera die richtige: sie
zeigt beide, und das ist das Bild, das die Reihe braucht.

**Marian Goodell und Kyle Kingsbury sind unveröffentlicht.** Bei ihnen gibt es
kein YouTube-Transkript, also läuft die Suche rückwärts vom Ende — der Weg aus
`frage_am_ende.py`.

### Master noch nicht gefunden

| Gast | veröffentlicht | Länge | Stand |
|---|---|---|---|
| Francis Chouler | `swZGLesMb8Y` | 70:39 | Transkript-Doc da, **Short schon veröffentlicht** (1.300 Aufrufe), Videodatei nicht gefunden |
| Rob Paddock | `ud5kr_LoqU4` (vermutlich) | 92:13 | keine Videodatei im Gästeordner |
| Nathan Maingard | `cv-I2lkMebE` (vermutlich) | 114:41 | keine Videodatei im Gästeordner |
| Danny Miranda | `23NNT7aMgL4` (vermutlich) | 78:54 | nur zwei kurze Clips im Ordner, kein Master |

**Bei diesen vier liegt im Gästeordner keine Masterdatei.** Die veröffentlichte
Folge selbst ist keine Quelle: YouTube antwortet auf die Videobytes mit 403,
Metadaten und Untertitel gehen, die Mediendaten nicht. Zwei Wege bleiben — im
Drive des Cutters weitersuchen (dort lagen Rob Bennett und Curtis Crane), oder
ihn einmal fragen. **Das ist die einzige Stelle, an der es ohne ihn eventuell
nicht weitergeht.**

**Francis Chouler ist ein Sonderfall, und ein guter:** die Antwort ist als Short
*„What Makes Life Meaningful? (Francis Michael)"* **schon veröffentlicht** und
mit 1.300 Aufrufen sein viertstärkster. Das Stück existiert also — nur nicht als
Datei, an die ich herankomme. Wenn er die Exportdatei hat, ist diese Zeile in
fünf Minuten erledigt.

### Die Zuordnung ist teils erschlossen, nicht gemessen

Wo oben **„vermutlich"** steht, habe ich die Folge über Titel, Länge und
Gästeordner zugeordnet, nicht über eine Stelle im Video. Belegt sind Sutcliffe
(Transkript geprüft), Francis Chouler (Transkript 70:35 gegen Video 70:39) und
Curtis Crane (Dateiname). Die übrigen prüfe ich beim Schneiden mit — spätestens
dann fällt auf, wenn ein Master nicht zur Folge gehört.

---

## Ob die Frage überhaupt in jeder Folge steht

**Geprüft bei sieben von siebzehn.** Bei den sechs geschnittenen steht sie, bei
Francis Chouler belegt der veröffentlichte Short sie. Bei den übrigen zehn ist
sie **angenommen, nicht nachgewiesen** — er stellt sie als Abschlussfrage, und
bei sechs von sechs lag sie in den letzten Minuten. Es kann Folgen geben, in
denen sie fehlt; das fällt beim Suchen auf und wird dann hier als Fehlzeile
vermerkt, nicht verschwiegen.

**Und das Ziel liegt weit:** 17 aufgenommene Folgen gegen 100. Diese Tabelle
läuft also über Jahre weiter, und genau darum zählt sie mehr als die Dateien.

---

## Der Weg pro Folge

1. **Veröffentlichte Folge:** YouTube-Transkript (`video/yt-transkript.py`) gibt
   die Stelle wortgenau und kostenlos. Dann einen Anker in der Nähe suchen und
   den Versatz dort messen — **nie über eine Formel**, das Tempo 1,1 gilt nur
   lokal.
2. **Unveröffentlichte Folge:** rückwärts vom Ende in **210-Sekunden-Stücken**
   holen und transkribieren, bis das Muster trifft. Größere Fenster brechen
   vorzeitig ab und melden trotzdem Erfolg; `drive_fernzugriff.py` prüft
   inzwischen Status und Länge jedes Blocks.
3. **Schluss auf das letzte Satzende der Antwort**, nicht auf eine Sekundenzahl.
   Die automatische Wahl lief zweimal ins Outro, weil sie eine feste Ziellänge
   nahm.
4. **Format:** der abgenommene Sutcliffe-Stand — randlos, Versalien, gelbes
   Aktivwort, Logo 700 px auf 0,877, warmer Look, Tempo 1,2, `--laut aus`,
   `--dehnung atempo`. **Keine B-Rolls, keine Musik.**
5. **Zeile hier eintragen**, Untertitel nach `video/shorts/`, Datei über
   `SendUserFile`.

**Das Drive-Tageslimit hängt am Eigentümer, nicht an der Datei** — am 20.10.
waren nach rund 28 GB *alle* Dateien in seinem Ordner gesperrt. Ein Fenster
kostet 200–260 MB, eine Folge also unter einem Gigabyte. Elf Folgen sind damit
rechnerisch an einem Tag machbar; eingeteilt wird trotzdem über mehrere Tage,
weil ein Fehlversuch pro Folge zwei bis drei Fenster kostet und das Limit nicht
vorher sichtbar ist.
