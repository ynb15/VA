# Der Ablauf — wie eine Folge rausgeht

Seine Bitte vom 21.10.2026: *„Es geht gerade auch vor allem darum, so einen
Flow, einen Prozess zu entwickeln, weil gerade beim Aufsetzen merke ich, ist es
noch sehr chaotisch, und wir brauchen klare Regeln."*

Das hier sind die Regeln. **Eine Seite, nicht zehn.** Wer sich daran hält,
produziert keine Rückfragen.

---

## 1 · Eine Folge hat zu jedem Zeitpunkt genau einen Zustand

Der Zustand steht in **`plan/folgen.md`**, nirgends sonst. Nicht in einem Chat,
nicht im Kopf eines Agenten, nicht in Drive.

```
geplant → Transkript → Auswahl → Text → Bild → Shorts → bei ihm → raus
```

**Ein Schritt ist fertig oder er ist es nicht.** Es gibt kein „fast". Wer einen
Schritt als fertig meldet, meldet damit: der nächste kann sofort anfangen.

## 2 · Jeder Schritt hat einen Besitzer, ein Datum und ein Fertig-Kriterium

| Frist | Schritt | Besitzer | Fertig heißt |
|---|---|---|---|
| **T−10** | Transkript | Shorts-Assistent | Transkript mit Zeitmarken liegt im Repo, Länge gegen die Datei geprüft |
| **T−8** | Clip- und Short-Auswahl | Shorts-Assistent | 3–5 Clips und alle Short-Kandidaten, je mit Rohzeitmarke, Zitat, einem Satz Begründung |
| **T−6** | Titel · Beschreibung · Tags | YouTube-Manager | 15 Titel mit **einer** Empfehlung, 15 Thumbnail-Zeilen mit **einer** Empfehlung, Beschreibung als `.txt` zum Einsetzen in einem Zug, ~20 Tags, angepinnte Kommentare |
| **T−5** | Thumbnails | Thumbnail-Assistent | Fertige JPGs, 1280×720, aus gemessenen Gesichtspositionen |
| **T−3** | Shorts gebaut | Shorts- und Cinematic-Assistent | Gerendert **und einmal nachgebessert** — das war bisher jedes Mal nötig |
| **T−2** | Paket bei ihm | Alfred | Alles an einem Ort, nichts fehlt, offene Entscheidungen benannt |

**T−x heißt Tage vor der Veröffentlichung.** Die Fristen stehen in
`bin/plan-pruefen.py` und feuern von selbst im täglichen Lauf.

## 3 · Der Besitzer meldet, bevor er reißt — nicht danach

Wer sieht, dass eine Frist nicht hält, sagt es **an dem Tag, an dem er es
sieht**, nicht am Stichtag. Eine Frist, die rutscht, verschiebt keine Aufgabe,
sondern eine Veröffentlichung.

**Eine Meldung besteht aus drei Sätzen:** woran es hängt · was ich stattdessen
liefern kann · was ich dafür brauche. Keine Entschuldigung, kein Bericht.

## 4 · Keine Rückfrage ohne Vorschlag

Ein Agent fragt ihn nie „was möchtest du?". Er legt **zwei Fassungen** vor, oder
eine Fassung mit einer benannten Alternative, und sagt, welche er nehmen würde
und warum. Offene Fragen kosten ihn Zeit; Entscheidungen zwischen zwei fertigen
Dingen kosten ihn Sekunden.

**Und eine Entscheidung von ihm blockiert nie mehr als einen Schritt.** Wenn die
Kopfzeile noch nicht entschieden ist, werden beide Fassungen gebaut und alles
andere läuft weiter.

## 5 · Was nicht im Repo liegt, existiert nicht

Container werden eingezogen. Am 21.10. waren sechs über Nacht gerenderte MP4s
weg, und ffmpeg war aus einem Container verschwunden. **Zwischenstände
committen, nicht im Scratchpad liegen lassen.** Eine Tabelle in Git, aus der
sich etwas neu bauen lässt, ist mehr wert als die Datei selbst.

## 6 · Eine Änderung pro Runde

Nie zwei Dinge gleichzeitig ändern — sonst ist nicht feststellbar, worauf er
reagiert hat. Das gilt für Ton, Bild, Schnitt und Text gleichermaßen.

## 7 · Drei Stücke im Kasten, immer

Er nimmt täglich ab. In der Abnahme liegt damit kein Puffer, also muss er davor
liegen: **mindestens drei fertige Stücke, bevor der Tag kommt.** Fällt die Zahl
darunter, wird nicht weitergebaut, sondern aufgefüllt — notfalls aus dem
Rückkatalog. Eine Lücke im Kanal ist das Einzige, was ein Takt nicht verzeiht.

## 8 · Nichts geht raus

Kein Upload, keine Veröffentlichung, keine geplante Veröffentlichung, kein
Kommentar, keine Mail — von keinem Agenten, auch nicht in seinem Namen. Wir
bauen, legen vor, **er lädt hoch.** Von ihm am 21.10. bestätigt: *„Regel bleibt,
Agenten entwerfen."*

---

## Was er bekommt, und wann

**T−2, an einem Ort**, je Folge:

```
Beschreibung .txt            einsetzen in einem Zug
15 Titel                     mit einer Empfehlung
15 Thumbnail-Zeilen          mit einer Empfehlung
Thumbnails                   fertige JPGs
Tags                         eine Zeile
Angepinnter Kommentar        Folge und Clips
Clip-Beschreibungen
Shorts + Clips               fertig gerendert
```

Dazu **eine** Zeile von mir: was offen ist und was er entscheiden muss. Wenn
nichts offen ist, steht da „nichts offen".

**Short-Beschreibungen entfallen** — seine Entscheidung vom 21.10.

## Die eine Zahl, auf die es ankommt

Nicht wie viele Folgen im Vorrat liegen (acht, das reicht bis Februar). Sondern
**wie viele fertige Stücke im Kasten liegen.** Steht die bei null, ist alles
andere Beschäftigung.
