# Kontowechsel — was am Claude-Konto hängt und was nicht

**Stand 18.10.2026.** Anlass: das Konto läuft auf `info@yannickbernard.com`,
die Adresse soll gewechselt werden. **Anthropic erlaubt das Ändern der
E-Mail-Adresse derzeit nicht** — der einzige Weg ist ein neues Konto.
Quelle: https://support.claude.com/en/articles/8452276-how-do-i-change-the-email-address-associated-with-my-account

Dieses Dokument existiert, damit der Wechsel **kein Datenverlust** ist.

---

## 1. Überlebt den Wechsel ohne Zutun — liegt auf GitHub

`ynb15/VA`, Branch `claude/ai-chief-of-staff-cz83jv`. **88 Dateien, alles
gepusht.** Das Konto besitzt davon nichts.

| Datei | Umfang | was es ist |
|---|---:|---|
| `OPERATING-MANUAL.md` | **7.387 Zeilen** | das Gedächtnis. Jede Regel, jeder Fehlschluss, jede Messung |
| `dashboard/command-center.html` | 2.193 Zeilen | **das Board im Quelltext** — neu veröffentlichbar, siehe §3 |
| `actuals/` | 55 Dateien | jedes Tageslog seit Beginn |
| `voice/` | 7 Dateien | de-register, en-podcast-outreach, beide Blindtests samt Auswertung |
| `podcast/` | 2 Dateien | Outreach-Auswertung und Rohliste |
| `video/` | 3 Dateien | Shorts-Pipeline, README, Beispielrender |
| `drafts/` | 8 Dateien | offene Entwürfe, u.a. Mediclinic und Mushroom Cowboy |
| `trigger-prompt.md` | — | **der gespeicherte Sweep-Auftrag im Wortlaut** |

**Ebenfalls außerhalb des Kontos:** Gmail, Google Calendar, Google Drive,
Notion (inkl. der ganzen `Databank`), Slack, Trello. Das sind fremde Dienste.
Ein neues Claude-Konto bedeutet dort **einmal neu anmelden**, keine Migration.

---

## 2. Hängt am Konto und muss neu angelegt werden

| | Wert | Aufwand |
|---|---|---|
| **Geplante Aufgabe** „Alfred — hourly sweep" | `trig_01FnmMyeG9ynGwbzNxwnSQLu`, stündlich. Wortlaut steht in `trigger-prompt.md`. **Zeitzone dabei auf `Africa/Johannesburg` umstellen** | Minuten |
| **Board-Artefakt** | `claude.ai/code/artifact/36c602cc-f6a8-46a7-89c3-937111cd431d` | neu veröffentlichen, **neue URL** |
| **Connectors** | Gmail · Google Calendar · Google Drive · Notion · Slack · Vibe Prospecting · (Canva braucht ohnehin Reconnect) · **neu: YouTube, Trello** | je ein Login |
| **Cloud-Umgebung** | GitHub-Zugriff auf `ynb15/VA`; Netzfreigaben für `youtube.com`, `huggingface.co`, `themushroomcowboy.com`, `greymattermedia.capetown` | einmal einrichten |
| **Abo / Zahlung** | auf dem alten Konto kündigen, falls dort eins läuft | |

---

## 3. Der einzige echte Verlust

**Der Gesprächsverlauf.** Chats lassen sich nicht übertragen. Alles, was nur
im Chat stand und nie ins Repo ging, ist dann weg.

**Deshalb ist das Handbuch so geschrieben, wie es geschrieben ist.** Jede
Messung, jede Regel und jeder widerlegte Verdacht steht dort im Volltext, nicht
als Verweis auf ein Gespräch. Der Verlauf ist Protokoll, das Handbuch ist das
Gedächtnis.

**Das Board ist kein Verlust.** Der Quelltext liegt im Repo; es wird auf dem
neuen Konto einmal neu veröffentlicht. Nur die URL ändert sich.

---

## 4. Reihenfolge, falls gewechselt wird

1. **Nichts löschen, solange das neue Konto nicht steht.** Löschen ist bei
   Anthropic endgültig und nimmt die Chats mit.
2. Neues Konto auf der neuen Adresse anlegen.
3. Connectors verbinden, Umgebung einrichten, `ynb15/VA` anbinden.
4. Board aus `dashboard/command-center.html` neu veröffentlichen, neue URL ins
   Handbuch eintragen.
5. Geplante Aufgabe aus `trigger-prompt.md` neu anlegen, Zeitzone Kapstadt.
6. Erst **danach** entscheiden, was mit dem alten Konto passiert.

**Das alte Konto muss nicht gelöscht werden.** Es stillzulegen bewahrt den
Gesprächsverlauf. Löschen lohnt nur, wenn ein Abo gekündigt oder **dieselbe
Telefonnummer** am neuen Konto gebraucht wird — die muss der Support vorher
entkoppeln.

**Support läuft nur schriftlich**, über den In-App-Messenger und per Mail.
Kein Telefon.
