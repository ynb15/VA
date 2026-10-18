# Drive-Benennung — aus seinen eigenen Dateien gelesen, nicht erfunden

**Stand 18.10.2026.** Methode wie bei der Stimme: erst messen, was er tut, dann
als Regel aufschreiben. Nichts hiervon ist mein Vorschlag — alles sind Belege.

## Die Grammatik

**`<Präfix>: <Spezifikum>`** — Doppelpunkt plus Leerzeichen, auf **jeder** Ebene.
Ordner und Dateien benutzen dieselbe Regel.

| Element | Beleg |
|---|---|
| **Präfix = Ort** | `SF: Flywheel Coffee` · `SF: Golden Gate Bridge` · `ATX: Jibran` |
| **Präfix = Person** | `Jibran: waffling in the car` · `Jibran: slumped` · `Bella: Pistachio Milk` |
| **Präfix = Projekt** | `YNB Podcast: David Sutcliffe` · `Vegan Boos: Cali` · `USA Roadtrip: New Mexico` · `Coffee: Rosetta` |
| **Präfix = fremde Quelle** | `Steven Bartlett: Empty Success` · `Simon Sinek: High-Achiever Identity Fallacy` |
| **Reihe → römische Ziffer** | `SF: YNB Journaling Cafe I / II / III` · `SF: YNB Fencing I / II` |
| **Variante → Klammer** | `(YNB)` = seine Kamera · `(Marian Goodell)` = Gastkamera · `(edited)` · `(Whit)` = Spitzname |
| **`00 ` = nach oben sortieren** | `00 YNB Podcast: Rick Strassman` · `00 US Journey` |
| **Monatsschnitte** | `02 February 26` · `03 March 2026` … `09 September 2026` |

**Kein Datum im Dateinamen.** Das Datum steht in den Drive-Metadaten. Einzige
Ausnahme sind die Monatsschnitte, bei denen das Datum *der Inhalt* ist.

**Der Ordner trägt den Kontext, der Dateiname die Unterscheidung.** In
`USA 2026 / California / SF: Golden Gate Bridge` muss der Dateiname nicht noch
einmal sagen, dass es San Francisco ist — er muss sagen, was *dieser* Clip zeigt
und die anderen acht nicht.

**Der Ton ist trocken und menschlich, nicht katalogartig:** *waffling in the car*,
*slumped*, *Pistachio Milk*, *Empty Success*. Keine Unterstriche, keine
Versalien, keine Codes.

## Der Rückstand, gemessen

**Mindestens 100 Dateien heißen noch `IMG_####`** (weitere Seiten vorhanden):
**95 Videos, 7,2 GB**, verteilt auf **22 Ordner**.

| Anzahl | Ordner |
|---:|---|
| 15 | `USA 2026 / California / SF: Cruise` |
| 12 | `USA 2026 / USA Roadtrip: TX-NM-CO / USA Roadtrip: New Mexico` |
| 11 | `… / USA Roadtrip: Texas` |
| 11 | `… / USA Roadtrip: Texas / USA Roadtrip: Palo Duro State Park` |
| 10 | `USA 2026 / Vegan Austin / Mission Burger` |
| 9 | `USA 2026 / California / SF: Golden Gate Bridge` |
| 5 | `Bewerbungen / THE Application / Modern Wisdom x YNB` |
| 4 | `… / Vegan Boos: Cali / SF: Angela's Ice Cream` |

## Was ich kann und was nicht — geprüft, nicht geschätzt

**Ich bin blind für den Inhalt.** Belegt am 18.10.:
- `download_file_content` liefert die Datei als **base64 in den Kontext**. Beim
  Versuch an der *kleinsten* Datei (7 MB) **brach die Verbindung zum
  Drive-Server ab** — „a message from the server was too large".
- `get_file_metadata` liefert **keinen Thumbnail-Link, keine Laufzeit, kein
  Aufnahmedatum** — nur Titel, Größe, Ordner, Upload-Zeit.
- Es gibt keinen zweiten, authentifizierten Weg an die Bytes.

**Was damit geht, ohne ihn:**
1. **Ordner + Reihenfolge → Name.** Die `IMG_`-Nummer ist die Aufnahmereihenfolge.
   Aus `IMG_3595…3598` in `SF: Angela's Ice Cream` wird
   `SF: Angela's Ice Cream I–IV`. Das ist exakt seine Konvention und ersetzt den
   stumpfen Teil vollständig.
2. **Das `description`-Feld füllen.** `update_file` kann es, und **Drive
   durchsucht es**. Dorthin gehören Datum, Ort, Kalenderkontext des Tages — der
   Name bleibt kurz, die Auffindbarkeit steigt deutlich. Das ist eine Erweiterung
   seines Systems in seiner eigenen Grammatik, kein Ersatz.

**Was nur er kann:** das eine unterscheidende Wort — *slumped*, *waffling in the
car*. Ein Satz pro Ordner reicht: „die vier aus Baker Beach: Surfer, Sonnenuntergang,
Isabelle im Wasser, Brücke im Nebel." Daraus baue ich die Namen.

## Offen — braucht seine Freigabe

**Umbenennen ist ein Schreibzugriff auf sein Drive. Notion-Schreibzugriff ist
seit 27.08. freigegeben, Drive nicht.** Nichts anfassen, bevor er es sagt.
Umbenennen ist umkehrbar; trotzdem erst fragen.

## Nebenbefund für die Shorts-Arbeit

`yannick_bernard_09-11-26_1 CAM 1 01.mp4` bis `CAM 4 01.mp4` liegen in
`YNB Podcast: In Progress` — **vier getrennte Kameradateien einer Aufnahme.**
Das ist genau die offene Frage aus `video/README.md`: echtes Multicam-Umschneiden
im Short ist damit für mindestens diese Session möglich. Ob das bei jedem
Studio so herauskommt, ist weiter offen.
