# Befunde — alfred

Format und Regeln: `lernen/KANAL.md`. Anhängen, neuester Tag oben,
jeder Eintrag mit einer Zahl oder einem Zitat und mit der Zeile `→ betrifft:`.
Alfred sammelt 06:40 und 15:54 Kapstadt ein und verteilt über `LERNEN.md`.

<!-- Neue Einträge ab hier. -->

## 27.10. — ein Datum aus dem Contentplan ist nicht automatisch von ihm

**Shorts I hat fünf Logan-Shorts unter dem Termin Fr 30.10. gebaut — den
Termin hatte ich gesetzt, nicht Yannick.** Seine Worte heute: *„Den Pod mit
Logan plane ich erst im Januar oder so zu veröffentlichen."* Vier Slots im Plan
sind dadurch leer, und mein Vorratszähler stand drei Tage zu hoch.

**Der Fehler liegt bei mir, nicht beim Agenten.** In der Plantabelle sieht ein
Datum, das ich zur Füllung des Takts gesetzt habe, genauso aus wie eines, das
er zugesagt hat.

**Für Euch heisst das zweierlei:**
1. **Nur die fünf Podcast-Termine sind von ihm** (21.10. gesetzt: Aaronson
   25.10., Kingsbury 31.10., Strassman 13.11., Defina 27.11., Goodell 04.12.).
   Jedes andere Datum im Plan ist meine Taktfüllung. **Ab jetzt steht die
   Herkunft in der Quellspalte**, und in jedem Auftrag von mir steht, woher der
   Termin kommt.
2. **Wenn ein Termin Euch komisch vorkommt, fragt — bei ihm oder bei mir.**
   Shorts I hat genau das getan, und deshalb wissen wir es jetzt. Fertige
   Stücke verfallen nicht; auf einen falschen Termin gebaute Arbeit ist aber
   Arbeit, die anderswo gefehlt hat.
→ betrifft: alle

## 29.10. — kurz. Keine Romane.

**Seine Worte:** *„Es ist mir viel zu viel Blabla. Du schreibst mir einfach
einen Roman."* Er hat es **einem anderen Agenten schon gesagt** — es betrifft
also nicht nur mich.

**Ein Satz pro Punkt, maximal drei Punkte, nur was er anfassen muss.** Keine
Begründungen, keine Fortschrittsmeldungen, keine Selbstkorrekturen an ihn.
Begründung gehört ins Repo, Entscheidung in den Chat.
→ betrifft: alle


## 03.11.2026 — wenn Ihr liefert, schreibt es in Euren Kanal

Drei fertige Aaronson-Shorts lagen vom **26.10. bis zum 03.11.** ungenutzt,
weil sie in meinem Kalender nicht standen. Gebaut waren sie um **08:54, 09:35
und 10:27**; geliefert auch — seine Antwort darauf steht in
`lernen/content-shorts-2.md`.

**Der Eintrag in den Plan ist meine Pflicht**, und ich habe sie versaut. Was
Ihr tun könnt, damit es nicht wieder passiert: **eine Zeile in
`lernen/<euer-schlüssel>.md`, sobald ein Stück ausgeliefert ist** —
Dateiname, Dauer, Datum, und was noch offen ist. Ich sammle den Kanal zweimal
täglich ein; was dort steht, kommt in den Plan. Was nur in Eurer Chat-Antwort
steht, erreicht ihn nicht.

## Erst über alle Zweige suchen, dann bauen (16.11.2026)
Shorts II hat vor dem ersten Handgriff `git grep` über alle Zweige laufen
lassen und dabei eine fertige B-Roll-Implementierung und eine komplette
Trailer-Sichtung gefunden, die auf einem fremden Zweig lagen. **Die Suche
kostet eine Minute.** Sie gehört vor den ersten Handgriff.

## Fremdes Werkzeug importieren, nicht kopieren (16.11.2026)
Eine Kopie veraltet. `importlib.util.spec_from_file_location` lädt auch eine
Datei mit Bindestrich im Namen; `if __name__ == "__main__"` sorgt dafür, dass
beim Import nichts anläuft.

## Viele Dateien gehen in Blöcken raus (17.11.2026)
Seine Beanstandung: „Ich habe gesagt 25 Screenshots und ich kriege immer nur
einen Teil davon geliefert." Alle 31 Dateien waren gebaut und committet — es
lag an der Übergabe. **Mehr als etwa acht Dateien: mehrere `SendUserFile`-
Aufrufe, je sechs, Bildunterschrift „x von y" mit den enthaltenen Nummern.**
So sieht er selbst, ob etwas fehlt, statt es zählen zu müssen.
