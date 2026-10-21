# Der Lernkanal — wie das Team Befunde austauscht

Angelegt am 21.10.2026 auf Yannicks Bitte: *„Ich möchte, dass deine Agenten
einmal täglich mindestens oder zweimal täglich ihre Learnings miteinander
austauschen … oder dass du derjenige bist, der den Progress und die Learnings
der unterschiedlichen Agenten kontrollierst und sie dann immer gegenseitig
miteinander teilst."*

**Vorher passierte das nicht.** Jeder Agent hat seinen eigenen Branch und sein
eigenes Kontextfenster. Nichts überquert diese Grenze von allein. Ein Befund,
den der Shorts-Assistent am Montag messt, ist für den Cinematic-Assistenten am
Dienstag nicht existent — er macht denselben Fehler nochmal.

## Zwei Richtungen, eine Datei je Agent

**Du schreibst** nach `lernen/<dein-schlüssel>.md` auf **deinem eigenen**
Branch. Nur Du schreibst diese Datei — deshalb gibt es nie einen Merge-Konflikt.
Anhängen, nie umschreiben, neuester Eintrag oben unter dem Datum.

**Du liest** `LERNEN.md` vom Chief-of-Staff-Branch. Ohne Checkout, ohne Merge:

```
git fetch origin claude/ai-chief-of-staff-cz83jv
git show origin/claude/ai-chief-of-staff-cz83jv:LERNEN.md
```

**Das liest Du am Anfang jedes Arbeitsblocks**, vor der ersten Messung. Zwei
Werkzeugaufrufe. Billiger als jeder Fehler, der dort schon steht.

## Was ein Eintrag ist — und was keiner

Ein Eintrag ist **ein nachgemessener Befund, der auch für jemand anderen gilt**.

| Gehört hinein | Gehört nicht hinein |
|---|---|
| Eine Messung, die eine Annahme widerlegt | Fortschrittsmeldungen („Short 3 fertig") |
| Ein Werkzeug, das jetzt existiert, samt Flag | Was Du als nächstes vorhast |
| Eine Korrektur von ihm, wörtlich | Deine Einschätzung ohne Messung |
| Ein Weg, der nicht funktioniert, und warum | Was nur Deinen Auftrag betrifft |
| Eine Grenze (Quota, Freigabe, Token) | Lob, Zusammenfassungen, Füllsätze |

Der Test: **würde ein anderer Agent ohne diesen Satz einen Fehler machen oder
Arbeit doppeln?** Nein → nicht in den Kanal, nur in Dein eigenes Log.

## Format

```markdown
## 2026-10-21
- **Kurztitel.** Was gemessen wurde, mit Zahl. Was daraus folgt.
  → betrifft: content-*, thumbnails   (oder: alle)
```

Die Zeile `→ betrifft:` ist Pflicht. Sie ist der Grund, warum der Kanal nicht
zumüllt: ich verteile nach Adressat, nicht per Rundruf.

**Eine Zahl oder ein Zitat gehört in jeden Eintrag.** „Der Ton klang besser" ist
kein Befund. „−31 LUFS unbearbeitet, Shorts laufen bei −14, er hat die
Angleichung trotzdem abgelehnt weil der Rauschboden von −62,7 auf −44,2 dB
steigt" ist einer.

## Wer sammelt

Alfred, zweimal täglich, auf zwei Läufen, die es schon gibt — kein neuer Timer:

* **06:40 Kapstadt**, im Morgenbericht der Nachtschicht — was nachts gelernt wurde.
* **15:54 Kapstadt**, im täglichen Sweep — was am Tag gelernt wurde.

Dazwischen passiert nichts automatisch. Wenn etwas eilt — ein Befund, der einen
anderen Agenten gerade jetzt in die falsche Richtung laufen lässt — dann schreib
es in Deine Datei, committe, pushe und **sag es Alfred sofort**: eine geplante
Aufgabe mit `persistent_session_id: session_01ELkvmWEvz5X1QNTjj2ucia` und
`run_once_at` zwei Minuten in der Zukunft. `SendMessage` erreicht ihn nicht —
am 21.10. geprüft, die Sessions laufen in der Cloud, `ListAgents` zeigt nur
diese Maschine.

## Die Schlüssel

| Schlüssel | Agent | Branch |
|---|---|---|
| `alfred` | Chief of Staff | `claude/ai-chief-of-staff-cz83jv` |
| `content-schlicht` | Content Assistant — Shorts, schlicht | `claude/content-assistant` |
| `content-cinematic` | Content Assistant — cinematisch | `claude/content-cinematic` |
| `content-vlog` | Content Assistant — Vlog / Archiv | `claude/content-vlog` |
| `content-gastauftritte` | Content Assistant — seine Gastauftritte | `claude/content-gastauftritte` |
| `thumbnails` | Thumbnail Assistant | `claude/thumbnails` |
| `head-of-content` | Head of Content | `claude/head-of-content` |
| `youtube-manager` | YouTube Manager | `claude/youtube-manager` |
| `guest-booking` | Guest Booking | `claude/guest-booking` |
