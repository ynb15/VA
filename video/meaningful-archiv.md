# „What makes life meaningful?" — das Archiv

**Sein Auftrag vom 21.10.2026:** die Abschlussfrage aus **allen** Folgen
schneiden und wegsortieren, damit bei Folge 100 ein Video daraus entsteht —
*„ich habe 100 verschiedene Menschen gefragt."*

**Diese Tabelle ist das eigentliche Ergebnis, nicht die Videodateien.** Aus ihr
lässt sich der Schnitt in einer Stunde bauen, auch wenn jede Datei neu gerendert
werden müsste — und das ist der realistische Fall: die sechs MP4s aus der Nacht
vom 20./21.10. sind mit dem Container weg, geliefert hat er sie, die Untertitel
liegen im Repo, die Dateien nicht.

## Der Drive-Ordner — gefunden, und ich kann hineinschreiben

**`YNB Podcast: Claude Creation`** · `1N5i97R5byCWF57z23GuwoY1v5w6vX1ef` ·
von ihm am 21.10.2026 um 09:04 angelegt, in `YNB Podcast` neben
`: In Progress` und `: Published`.

**Am 21.10. um 09:22 getestet und es geht** — eine Textdatei hineingeschrieben,
sie liegt drin (`1bKrtpOk7iykn6KLR8KitxjSyFZeY6fF9`, kann gelöscht werden).
Der Stand im Handbuch („Drive-Schreibzugriffe nicht freigegeben") ist damit
überholt. **Dorthin gehen die Stücke ab jetzt**, je Folge drei Dateien:

```
<nr>-<gast>-meaningful.mp4    das geschnittene Stück
<nr>-<gast>-meaningful.srt    die Untertitel
<nr>-<gast>-meaningful.txt    das Transkript der Antwort
```

Das Archiv selbst bleibt hier im Repo — eine Tabelle in Git ist versionierbar
und durchsuchbar, eine im Drive nicht.

---

## Was geschnitten ist

Zeiten in **Masterzeit (Sekunden)**, Dauer **des fertigen Stücks** bei Tempo 1,2.
Untertitel unter `video/shorts/<datei>.srt`.

| # | Gast | Drive-ID des Masters | Frage/Antwort im Master | Dauer | Datei | geprüft |
|---|---|---|---|---|---|---|
| 1 | David Sutcliffe | `1oJjeQXjfIYtYph0gxfe8V1dhv17BBlPT` | 7222,0–7281,6 | 49,7 s | `01-sutcliffe-meaningful` | ja, von ihm abgenommenes Format |
| 2 | Scott Aaronson | `1C7CUI-B6_fBcdttR_zKIJBYraBMTtUvh` | 5894,3–5972,6 | 65,3 s | `02-aaronson-meaningful` | ja |
| 3 | Ken Stern | `1RGq-Mw0QEm5jE2WMthKPkP5OHrXvmotF` | 6150,1–6189,3 | 32,7 s | `03-ken-meaningful` | ja |
| 4 | Logan Gonzalez | `1ztggu2ua5-AntISFHHP9cBqjVhSn6Zmj` | 4957,1–5009,4 | 43,6 s | `04-logan-meaningful` | ja |
| 5 | Matt Defina | `1ubW-gMYb6_g0ZO-cOVyEFGQoKvIyGivj` | 6474,7–6513,1 | 32,0 s | `05-matt-meaningful` | ja |
| 6 | Rick Strassman | `1Hwt3_c_Ifhd7onXyC8nrHIdtjwJjxdjH` | **~7100–7160, ungenau** | 49,0 s | `06-rick-meaningful` | **nein — Ende offen** |

**Drei Lücken in diesen sechs Zeilen:**

1. **Ricks Zeitmarke ist grob** (`~7100–7160`); die anderen fünf sind auf eine
   Zehntelsekunde gemessen. Wird beim nächsten Zugriff auf diesen Master
   nachgemessen.
2. **Ricks Stück hat ein offenes Ende.** Der Vorgänger hat den kürzeren Bogen
   gewählt und das ausdrücklich ihm zur Entscheidung gelassen. Bleibt seine.
3. **Das Aufnahmedatum fehlt überall.** Drive liefert nur das Hochladedatum, und
   die beiden liegen hier Wochen auseinander. Die Aufnahmedaten stehen im
   Notion-Databank; sie kommen von dort, nicht geraten.

---

## Zeile fertig, Datei fehlt — Francis Chouler

**Das Muster für alle veröffentlichten Folgen ohne Master.** Die Antwort steht
wortgenau im Transkript, das am 19.10. geholt wurde
(`video/transkripte/swZGLesMb8Y.transkript.md`). Für die Archivzeile reicht das.

| Gast | Folge | Frage | Antwort | Dauer |
|---|---|---|---|---|
| Francis Chouler | `swZGLesMb8Y` · 70:39 | **01:08:29** | **01:08:36 – 01:09:31** | 55 s veröffentlicht |

Zeiten **veröffentlicht**, nicht Masterzeit — es gibt keinen Master mehr.

Seine Frage: *„I was thinking about renaming this podcast to Man's Search for
Meaning … so I would be curious, what does make life meaningful for you?"*

Francis' Antwort, gekürzt: *„All of the various episodes on the way, all of the
things we have to go through in order to get to where we're going … it's that
kind of unpredictable factor. I think that's the source of delight in a life,
and a source of meaning — from holding on to the kind of golden thread that you
know you need to keep following."* Und am Schluss, nach seinem Einwurf *„so live
for the uncertainty"*: **„Embrace the uncertainty. It is the source of
aliveness."**

**Das ist das stärkste Ende der sieben, die ich bisher gelesen habe** — und das
ist meine Einschätzung, nicht seine Vorgabe. Dazu passt, dass dieser Short mit
**1.300 Aufrufen** schon veröffentlicht und sein viertstärkster ist. Für die
Reihe bei Folge 100 wird er neu geschnitten werden müssen; der Schnittpunkt
steht jetzt fest.

---

## Was in Frage kommt

**17 aufgenommene Folgen**, gemessen am 21.10.2026 aus drei Quellen: der Kanal
über `yt-dlp` (10 lange Formate), die Masterdateien über die Drive-Suche, die
Ordnerstruktur aus `: Published` / `: In Progress` / `: Backlog`.

Nicht gezählt: Gäste, von denen nur ein Vorbereitungsdokument liegt —
**Bridget Woods, Cal Callahan, Cara West**, und **Vince Poscente** (Ordner vom
19.10., Dokument und ein Foto, keine Aufnahme im Drive). Falls Vince aufgenommen
ist, wird daraus Folge 18.

### Material liegt vor — das kann laufen

| Gast | veröffentlicht | Länge | Master im Drive | Größe |
|---|---|---|---|---|
| Rob Bennett | `o9lM8i6XUWo` | 118:35 | `1K5E3SlIrEBL7aCM7Z-QvAeEsrXiQ5RW-` | 34,2 GB |
| Craig Makhosi | `FF-eRPgZI2k` (vermutlich) | 145:12 | `1JEWgIwIt1XIzwZphqsGnqLedKkYa9Dhm` | 27,4 GB |
| Curtis Crane | `ewgUIZGJaWQ` | 109:53 | `19S90VEL7LNfkwNCBZH6ZJDuVE3jRu6MG` (v1-Export) | **2,0 GB** |
| Eben Britton | `RG-K0fIA2-w` | 102:28 | `1lIFL8aUunQQPtTDp0vQNlaRc7of-4PfG` | 27,0 GB |
| Whitney Wheelock | `rFRIX4Yute0` (vermutlich) | 104:07 | `1iZy9XwHryVdCf3VBRM2Ya5oP_XIBjmdM` (Zweier-Kamera) | 5,0 GB |
| Kyle Kingsbury | — | — | `1mQjt0g5GVptvEDVY8w3mVN2Qa8NFlTnp` · LOW_RES `1NWMaIn8avpf0EVQvm2DhEQr73uhfioIq` | 17,0 / **1,3 GB** |

**Curtis Crane und Kyle Kingsbury sind die billigsten** — von beiden liegt ein
kleiner Export vor (2,0 bzw. 1,3 GB), ganz ladbar, ohne das Tageslimit zu
belasten. Der 33,2-GB-Rohschnitt von Curtis
(`1X9I3dODNz8RqdMml801Gk2a4E2SdmzM-`, im Drive des Cutters) wird nicht gebraucht.

**Whitney Wheelock liegt dreifach** — `(YNB)` 7,5 GB, `(Whit)` 7,5 GB,
`(Whit & YNB)` 5,0 GB. Die Zweier-Kamera ist die richtige: sie zeigt beide, und
das ist das Bild, das die Reihe braucht.

**Dass fünf veröffentlichte Folgen den Master noch haben, ist kein Widerspruch
zu seiner Aufräumregel** — gelöscht hat er genau die vier unten, nicht alle.

### Marian Goodell — der Ton bricht ab

| Gast | Länge | Material |
|---|---|---|
| Marian Goodell | ~2 h | `1LVM5nxvxjMuSmsQlz1Jys_O32y8eYe0A` 18,5 GB · `1n4h-Qis-40e-cEcKd-hAhtyj_vgU4Hwk` (YNB-Kamera) 10,4 GB |

**Sein Befund vom 21.10.:** die Kamera, die den Ton aufgenommen hat, ist nach
etwa einer Stunde ausgegangen. Das Gespräch lief zwei Stunden, **und die Frage
steht am Ende** — also genau in dem Teil ohne Kameraton. Der Ton vom iPhone
muss darunter, so gut es geht.

**Im Drive-Ordner `00 YNB Podcast: Marian Goodell` liegt keine Tonspur** —
geprüft am 21.10., auch über eine Suche nach allen Audiodateien ab 01.10.: dort
stehen nur Scott Aaronsons MP3s und Logans vier CAM-WAVs. **Die iPhone-Aufnahme
fehlt, sie wird gebraucht.**

Wenn sie da ist, ist der Weg technisch unspektakulär und messbar: die beiden
Spuren über die **Kreuzkorrelation der Hüllkurve** im überlappenden ersten
Stück ausrichten (das gibt den Versatz auf wenige Millisekunden, und es zeigt
zugleich, ob das iPhone mit einer anderen Abtastrate gelaufen ist — dann driftet
es über zwei Stunden hörbar auseinander und muss gedehnt werden, nicht nur
verschoben). Danach Hochpass, Entzerrung, Pegel. **Was ich nicht verspreche:
dass es wie Kameraton klingt.** Ein iPhone im Raum ist ein iPhone im Raum.
Für ein Archivstück reicht es; ob es für die Reihe reicht, entscheidet sein Ohr.

### Master gelöscht — veröffentlicht, Platz gespart

| Gast | Folge | Länge | Stand |
|---|---|---|---|
| Francis Chouler | `swZGLesMb8Y` | 70:39 | **Zeile fertig** (oben), Transkript liegt im Repo |
| Rob Paddock | `ud5kr_LoqU4` (vermutlich) | 92:13 | kein Master, **kein Transkript** |
| Nathan Maingard | `cv-I2lkMebE` (vermutlich) | 114:41 | kein Master, **kein Transkript** |
| Danny Miranda | `23NNT7aMgL4` (vermutlich) | 78:54 | kein Master, **kein Transkript** |

**Seine Erklärung vom 21.10.:** die vier sind veröffentlicht, deshalb liegen sie
nicht mehr im Drive — Speicherplatz. Das ist nachvollziehbar und war nicht zu
erraten.

**Was daran hängt: der Umweg über YouTube ist seit heute zu.** Am 19.10. hat
`yt-transkript.py` die automatischen Untertitel ohne Anmeldung geholt — so
kamen Sutcliffes und Francis' Transkripte ins Repo. Am 21.10. antwortet YouTube
auf denselben Abruf mit **„Sign in to confirm you're not a bot"**. Vier
Abspielclients durchprobiert: `web_safari` und `mweb` liefern noch Titel und
Metadaten, aber **die Untertitelliste kommt leer zurück**; `android_vr` und der
Standardclient fallen auf die Botprüfung. Die Kanalliste über
`--flat-playlist` geht weiterhin — Metadaten ja, Untertitel nein.

**Damit sind Rob Paddock, Nathan Maingard und Danny Miranda die einzigen drei
Folgen, bei denen es ohne ihn nicht weitergeht.** Er besitzt die Videos; aus
YouTube Studio heruntergeladen und in `YNB Podcast: Claude Creation` gelegt,
sind sie in je zwanzig Minuten erledigt. **Eile hat es nicht** — geschnitten
wird frühestens bei Folge 100.

### Die Zuordnung ist teils erschlossen

Wo **„vermutlich"** steht, ist die Folge über Titel, Länge und Gästeordner
zugeordnet, nicht über eine Stelle im Video. Belegt sind Sutcliffe (Transkript
geprüft), Francis Chouler (Transkript 70:35 gegen Video 70:39) und Curtis Crane
(Dateiname). Die übrigen prüfe ich beim Schneiden mit.

---

## Ob die Frage überhaupt in jeder Folge steht

**Belegt bei acht von siebzehn:** die sechs geschnittenen, Francis Chouler über
das Transkript, und Marian Goodell, weil er es am 21.10. selbst gesagt hat.
Bei den übrigen neun ist sie **angenommen, nicht nachgewiesen.** Fällt eine
Folge aus, steht das hier als Fehlzeile, nicht verschwiegen.

**Und das Ziel liegt weit:** 17 aufgenommene Folgen gegen 100. Diese Tabelle
läuft über Jahre weiter, und darum zählt sie mehr als die Dateien.

---

## Der Weg pro Folge

1. **Veröffentlichte Folge mit Master:** Anker in der Nähe suchen, Versatz dort
   messen — **nie über eine Formel**, Tempo 1,1 gilt nur lokal. Das
   YouTube-Transkript als Vorsuche steht nicht mehr zur Verfügung (siehe oben),
   also läuft auch hier die Suche über den Master.
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
5. **Zeile hier eintragen**, Untertitel nach `video/shorts/`, die drei Dateien
   nach `YNB Podcast: Claude Creation`.

**Das Drive-Tageslimit hängt am Eigentümer, nicht an der Datei** — am 20.10.
waren nach rund 28 GB *alle* Dateien in seinem Ordner gesperrt. Ein Fenster
kostet 200–260 MB, eine Folge also unter einem Gigabyte. Eingeteilt wird
trotzdem über mehrere Tage, weil ein Fehlversuch zwei bis drei Fenster kostet
und das Limit nicht vorher sichtbar ist.
