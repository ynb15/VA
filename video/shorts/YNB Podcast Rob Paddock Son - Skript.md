# Rob Paddock — „Ich habe meinen Sohn getroffen" (Skript)

**Datei:** `YNB Podcast Rob Paddock Son.mp4` · Tempo 1,15 · 2160×3840 ·
75,5 s Inhalt + 4,21 s Outro
**Quelle:** `$100M Exit, Psychedelic Fatherhood & The Truth About Masculinity –
Millionaire Rob Paddock (4K).mp4` (Drive, `1lGUE0j…`), 92:12 lang.
Alle Zeiten unten sind **Zeiten dieser Datei**.

**Die ganze Stelle mit dem Namen ist raus** — beide Male, dazu die Reaktion
seiner Frau, die ja nur wegen des Namens komisch ist.

---

## Was drin ist

| # | ab | bis | Dauer | Text |
|---|---|---|---|---|
| **1** | 782,033 | 796,200 | 14,17 s | **YNB:** „How did psychedelics impact the relationship to your children?" — **Rob:** „Sure. One of my first psychedelic experiences was actually — and I've certainly never spoken about this publicly — but I did a hero's journey mushroom dose." |
| **2** | 800,200 | 825,600 | 25,40 s | „So I did it in the October of what would have been 2019. And my wife and I had been trying for kids for ages. We were on all sorts of fertility treatments, and the anticipation every month of *is it gonna happen or isn't it* — this was just up and down. It's very hectic. For anyone who's gone through that experience, it's actually incredibly challenging." |
| **3** | 846,400 | 875,500 | 29,10 s | „**I met my son.** He told me his name. He told me his deep desire to come into the world. And he was also clear that he wasn't going to come in until I had transcended certain behavior patterns with my father that he didn't want repeated in our relationship. And he literally told me the date he was gonna come in: third of September, the next year. And remember, this is the October the year before. And he told me he was a boy, he told me his name, like everything." |
| **4** | 883,300 | 890,267 | 6,97 s | „I remember I went over to my wife that night and I was like: *Love, I've met our son. He's so beautiful.*" |
| **5** | 906,800 | 918,000 | 11,20 s | „But guess what? Early the next year we found out that she was pregnant. And then a couple of weeks later we found out it was a boy — and the due date was the tenth of September. I was like: *well, that's kind of close.* **Born on the third of September.**" |

Zusammen **86,83 s = 2605 Bilder**, bei Tempo 1,15 **75,5 s**.
Schluss: „Born on the third of September." Danach erzählt er nur noch, wem er
davon erzählt hat.

## Was raus ist

| ab | bis | Dauer | was |
|---|---|---|---|
| 796,200 | 800,200 | 4,00 s | „Well, this is the only way to podcast. Yeah, there we go. All the way." — Zwischenruf |
| 825,600 | 846,400 | 20,80 s | „I had thought for various reasons that it's more likely on Ash's side, my wife's side…" plus der Stotterer „I think it was my first — was my second mushroom experience ever" und das zweite „October 2019" |
| **875,500** | **883,300** | **7,80 s** | **„And the name he told me was Chadwick Graham Paddock."** |
| **890,267** | **906,800** | **16,53 s** | **„…and his name's Chadwick."** · ihre Reaktion („Shut the f\*\*\* up, we're not calling our son Chadwick") · „So we didn't end up calling him Chadwick. We ended up calling him Grey Kahn Paddock." |

Nach dem Herausnehmen fällt in Block 3 das Satzende so: *„…he told me his
name, like everything."* — und weiter mit *„I remember I went over to my wife
that night."* Der Name wird **kein einziges Mal** genannt.

## Schnitte im Bild

Vier Nähte. Zwei davon fallen auf einen Kamerawechsel, den das Material
selbst hergibt (mit `schnittgrenzen.py` Bild für Bild nachgemessen):

| Clipzeit | was dort passiert |
|---|---|
| 3,433 | Kamerawechsel aus dem Material (YNB → Rob) |
| **14,167** | **Naht 1 — liegt auf einem Kamerawechsel** (Unterschied 58,6 gegen Ruhepegel 1,2) |
| 15,300 | Kamerawechsel aus dem Material (Totale → Nahaufnahme) |
| **39,567** | **Naht 2 — sichtbarer Sprung.** Von 801,3 bis 865,1 läuft im Master **eine einzige Einstellung**; hinter einen Wechsel lässt sich dieser Schnitt nicht legen |
| 58,300 | Kamerawechsel aus dem Material (Nahaufnahme → Totale) |
| **68,667** | **Naht 3 — sichtbarer Sprung**, aus demselben Grund, aber in der Totale, wo er kleiner im Bild steht |
| **75,667** | **Naht 4 — liegt auf einem Kamerawechsel** (Unterschied 60,9 gegen Ruhepegel 0,5) |

Keine Blende, nirgends — harte Schnitte, wie festgelegt. Jede Naht ist eine
ganze Zahl von Bildern lang (425 / 762 / 873 / 209 / 336).

## Einblendungen

112 Stück, drei Wörter. **Drei habe ich von Hand nachgebessert:**

1. Whisper hatte das erste Wort **„psychedelics"** und das gedehnte „your"
   verschluckt — die erste Zeile hätte mit „IMPACT THE" angefangen.
2. **„first"** war als Einzelwort durch die Mindeststandzeit herausgefallen;
   aus „one of my first psychedelic experiences" wäre „one of my psychedelic
   experiences" geworden.
3. Am Ende von Block 4 stand **„IN HIS NAME"** im Bild. Das ist eine
   Halluzination des Modells über die Schnittkante hinweg — im Ton steht es
   nicht (an drei verschiedenen Endpunkten geprüft, es erfindet die Zeile
   jedes Mal). Es wäre ausgerechnet der Hinweis auf den Namen gewesen.
   Gelöscht.

## Zwei Dinge, die Du wissen solltest

1. **Die Datei ist 720p, nicht 4K.** Im Namen steht „(4K)", im Bild sind
   **1280×720 bei 0,96 Mbit/s**. Der 9:16-Ausschnitt daraus ist 405×720 und
   wird auf 2160×3840 hochgerechnet — das Bild ist sichtbar weicher als bei
   den Sutcliffe-Shorts (dort 1920×1080). Wenn es den echten Master gibt,
   schneide ich es daraus neu; der Plan oben bleibt dann Bild für Bild gültig.
2. **Keine Musik** — Grundfassung ohne Bett.

## Geprüft

- **Ortscheck:** die Stelle nennt keinen Ort. „Cape Town, South Africa" fällt
  früher in der Folge (01:22), nicht hier.
- **Name:** kommt im Ton und in den Einblendungen null Mal vor.
