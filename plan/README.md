# Der Contentplan — wie er läuft

**Sein Auftrag vom 21.10.2026:** *„Ich habe mir vorgenommen, dieses Jahr noch
zwei Podcasts pro Monat zu veröffentlichen … jetzt scheint es mir, als gäbe es
die Möglichkeit, dass ich jeden Tag ein Content-Piece veröffentliche … behalte
die Übersicht, erstelle einen Contentplan, achte darauf, dass wir den Plan
einhalten, und löse die Aufgaben aus."*

Seine Vorgaben, im selben Gespräch: **sieben Stücke pro Woche angestrebt, fünf
die Untergrenze** · **Hauptpodcast am Wochenende** („da sind die meisten Leute
auf YouTube"), Shorts und Clips unter der Woche drumherum · **Rückkatalog
mitnutzen**, vor allem Craig Makhosi und Francis Chouler · **Short-Beschreibungen
braucht er nicht** · **er nimmt täglich ab, Stück für Stück.**

## Die vier Dateien

| | |
|---|---|
| **`plan/ABLAUF.md`** | **Die Regeln.** Wer macht was, bis wann, und wann ist es fertig. Auf seine Bitte vom 21.10.: *„wir brauchen klare Regeln."* Wer eine Frage zum Vorgehen hat, liest zuerst hier. |
| `plan/folgen.md` | Der Bestand. Was aufgenommen ist, was davon schon existiert, welche Vorlaufzeiten gelten. Von Hand gepflegt. |
| `plan/kalender.md` | Der Kalender, Tag für Tag. **Erzeugt** von `bin/kalender-bauen.py` — nicht von Hand ändern, sonst ist er beim nächsten Lauf weg. |
| `bin/plan-pruefen.py` | Die Kontrolle. Was geht heute raus, welche Frist greift, wie tief ist der Vorrat. |

## Der tägliche Lauf

Im Sweep um 15:54 Kapstadt, nach dem Lernkanal:

1. `python3 bin/plan-pruefen.py`
2. **Jede Frist, die heute greift, wird heute ausgelöst** — geplante Aufgabe an
   den zuständigen Agenten, mit Folge, Datum und dem, was er vorfindet.
   `SendMessage` erreicht die Agenten nicht; der Weg ist `create_trigger` mit
   `persistent_session_id` und `run_once_at`.
3. **Überfällige Fristen sind die eigentliche Arbeit.** Eine Frist, die rutscht,
   verschiebt keinen Auftrag, sondern eine Veröffentlichung.
4. Zustand im Kalender nachziehen (`offen` → `in Arbeit` → `fertig` → `bei ihm`),
   committen, pushen.
5. **Ist der Vorrat unter drei Tagen, ist das die Meldung des Tages.**

## Der Vorrat ist das Sicherheitsnetz

Er nimmt täglich ab — das hat er so entschieden. Täglich heißt: **kein Puffer
in der Abnahme.** Also muss der Puffer davor liegen: **mindestens drei fertige
Stücke im Kasten, bevor der Tag kommt.** Fällt die Zahl darunter, wird nicht
weitergebaut, sondern aufgefüllt — ein leerer Kasten ist eine Lücke im Kanal,
und eine Lücke ist das Einzige, was ein Takt nicht verzeiht.

## Die Vorlaufzeiten

Stehen mit Besitzer und Fertig-Kriterium in **`plan/ABLAUF.md`**, Abschnitt 2.
Kurz: T−10 Transkript · T−8 Auswahl · T−6 Text · T−5 Bild · T−3 Shorts ·
T−2 Paket bei ihm.

**T−3 trägt eine Nachbesserungsrunde ein**, weil bisher **jedes** Short eine
gebraucht hat. Eine Frist ohne Nachbesserungsrunde ist eine Frist, die reißt.

## Was er bekommt

Das Paket steht in `youtube/veroeffentlichung.md` (YouTube Manager).
**Eine Streichung seit 21.10.: Short-Beschreibungen entfallen** — *„die ist
jetzt nicht wirklich relevant."*

## Die Grenze, die bleibt

**Nichts geht raus.** Kein Upload, keine Veröffentlichung, keine Planung in
YouTube durch einen Agenten. Wir bauen, legen vor, **er lädt hoch.** Von ihm am
21.10. bestätigt: *„Regel bleibt, Agenten entwerfen."*
