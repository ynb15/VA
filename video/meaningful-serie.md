# „What makes life meaningful?" — die Serie, sechsmal geschnitten

**Auftrag vom 20.10.2026:** die Abschlussfrage, die er in jedem Podcast
stellt, aus sechs Folgen schneiden. Über Nacht, ohne ihn.

## Was dasteht

| # | Gast | Länge | Master | der Kern seiner Antwort |
|---|---|---|---|---|
| 1 | David Sutcliffe | 49,7 s | 7222,0–7281,6 | „other people… to see yourself reflected through the other" |
| 2 | Scott Aaronson | 65,3 s | 5894,3–5972,6 | „my kids, my family, my students" — und die Mathematik |
| 3 | Ken Stern | 32,7 s | 6150,1–6189,3 | „we get meaning from others. Helping others, being with others" |
| 4 | Logan Gonzalez | 43,6 s | 4957,1–5009,4 | „doing things for others… for the team, for the greater good" |
| 5 | Matt Defina | 32,0 s | 6474,7–6513,1 | „it's experiences… finding the joy in the mundane" |
| 6 | Rick Strassman | 49,3 s | ~7100–7160 | die Genesis-Übersetzung — „a case of the unconscious becoming conscious" |

**Fünf von sechs landen auf demselben Kern — andere Menschen.** Nur Rick
bricht damit: bei ihm ist es die Arbeit am Text, das Verstehen selbst. Als
Kontrast neben die anderen gesetzt trägt das eine ganze Reihe.

**Format:** der abgenommene Sutcliffe-Stand — randlos, Versalien, gelbes
Aktivwort, Logo 700 px auf 0,877, warmer Look, Tempo 1,2. **Keine B-Rolls.**
Das B-Roll-Verfahren war an dem Abend noch nicht abgenommen; Ungeklärtes
wird nicht sechsmal weitergetragen.

---

## Wie die Frage gefunden wird — drei Wege, nach Aufwand sortiert

**1. Sein eigenes Vorbereitungsdokument.** Neben jedem Podcast liegt im
Drive ein Google-Doc. Bei Sutcliffe stand dort eine Kapitelliste mit
`1:40:00 What makes life meaningful?`. **Achtung: die Zeitmarken sind grob.**
Tatsächlich lag die Stelle bei veröffentlicht 01:52:04 — zwölf Minuten
daneben. Als Hinweis brauchbar, als Zeitmarke nicht.

**2. Das veröffentlichte YouTube-Transkript** (`video/yt-transkript.py`).
Kostet nichts und ist wortgenau — aber nur für veröffentlichte Folgen. Von
den sechs war nur Sutcliffe veröffentlicht; die anderen fünf liegen genau
deshalb noch im Drive.

**3. Rückwärts vom Ende transkribieren.** Der Weg für alles Unveröffentlichte.
Die Frage steht am Schluss, also: letzte 210 s holen, transkribieren, suchen;
wenn nicht drin, das Stück davor. Bei Ken Stern brauchte es zwei Anläufe, bei
Rick auch.

**Umrechnung veröffentlicht → Master:** nie über eine Formel. Einen Anker in
der Nähe suchen (bei Sutcliffe „in the tornado and in the lightning strike",
veröffentlicht 01:45:06 ↔ Master 6763,1 s), den Versatz dort messen und mit
Tempo 1,1 weiterrechnen. So kam Master 7223 heraus, tatsächlich waren es
**7222,31** — 0,7 s daneben.

---

## Zwei Fehler, die Arbeit gekostet haben

### Der Bereichsabruf bricht bei großen Fenstern vorzeitig ab

Bei Ken Stern 600 s bestellt, **192 s bekommen** — und das Werkzeug meldete
sauberen Abschluss. Die Frage lag deshalb außerhalb, und ich habe im Leeren
gesucht.

**Regel: nach jedem Fensterabruf die tatsächliche Dauer messen, nicht die
bestellte annehmen.** In Stücken von **210 s** lief es durchweg zuverlässig
(bekommen: 210,3 / 210,4 / 210,6 / 210,8 s).

### Die automatische Endpunktwahl lief zweimal ins Outro

Ken endete mitten im Satz, Logan und Matt liefen bis „wo findet man dich /
Instagram / Spotify". Ursache: eine feste Ziellänge. **Die Antwort auf diese
Frage ist bei jedem unterschiedlich lang** — Ken 39 s, Logan 52 s, Matt 38 s,
Aaronson 78 s.

**Richtig ist zweierlei zusammen:** bis zur **nächsten Frage** schneiden
(Muster: Satz auf `?`, beginnend mit how/what/where/when/why/who/can/do/…)
und dort auf dem **letzten Satzende** landen. Beides steckt in
`schluss_waehlen()` in `video/frage_am_ende.py`.

---

## Der Container wird eingesammelt — und was dagegen hilft

**Der härteste Befund der Nacht.** Dreimal ist mitten im Lauf alles
weggewesen: `uptime` meldete `up 0 min`, Prozesse tot, kein OOM
(621 MB von 16 GB belegt), Platte frei, nichts im Fehlerprotokoll.
**Der Container wird neu gestartet, sobald ein Zug endet und eine Weile
nichts passiert.** Dateien überleben, Prozesse nicht — und zwar auch mit
`nohup` und `setsid` nicht. Beides wurde versucht.

**Was trägt, sind zwei Dinge zusammen:**

1. **Nichts auf einen laufenden Prozess stützen.** `frage_am_ende.py` erkennt
   an den Dateien, was fertig ist, und macht nur den nächsten offenen
   Schritt. Beliebig oft aufrufbar. Nach dem dritten Neustart hat es in
   **acht Sekunden** erkannt, dass fünf Shorts stehen, und mit dem sechsten
   weitergemacht — vorher hätte derselbe Neustart den ganzen Lauf gekostet.
2. **Eine geplante Aufgabe, die die Sitzung selbst weckt.** Stündlich (das
   ist das Minimum), bindet an diese Sitzung, startet das Skript. Damit
   überlebt ein Nachtlauf das Einsammeln des Containers.

**Regel für jeden langen Lauf ab jetzt: erst wiederaufnehmbar bauen, dann
starten.** Nicht umgekehrt.

---

## Nachtrag 21.10.2026 — Sutcliffe neu gebaut, mit seinem Preset

Auf seine Bitte („den Short, den ich aus dem David Sutcliffe-Podcast ziehen
moechte, What Makes Life Meaningful") noch einmal gerendert, diesmal **mit
seinem Preset** statt mit den abgelesenen Werten der Nacht: Inter Black 82,
Gelb `#F9F13A`, Zeilenbreite 72 %, Logo 28 % auf 0,87, `--look preset`.
Laenge unveraendert **49,70 s**, 1080x1920.

**Der Weg, nachvollziehbar:** Fenster 7221–7283 aus dem Drive-Master geholt
(62,04 s bekommen von 62 bestellt, geprueft — 176 MB statt 18,6 GB), exakt auf
7222,0–7281,6 geschnitten, Ausschnittsplan neu gemessen.

**Vier Einstellungen, an jedem Kameraschnitt geteilt** — und einzeln im Bild
nachgesehen, weil der feste Kasten genau hier schon einmal die Wand gezeigt
hat:

| Einstellung | im Quellbild | wer zu sehen ist |
|---|---|---|
| 0,0–2,6 s | `768:141:528:939` | Yannick, stellt die Frage |
| 2,6–29,7 s | `732:98:528:939` | Sutcliffe, nah |
| 29,7–37,1 s | `1332:141:528:939` | **Totale** — Kasten korrekt auf Sutcliffe |
| 37,1–59,6 s | `708:86:528:939` | Sutcliffe, nah |

**Zwei Befunde, die Arbeit gekostet haben** (ausfuehrlich in
`lernen/content-gastauftritte.md`):

1. **`--srt` zusammen mit `--srt-out` bricht ab** (`KeyError: 'woerter'`), und
   zwar erst nach dem Transkodieren.
2. **Eine wiederverwendete SRT kostet das gelbe Aktivwort.** `--srt` liefert
   keine Wortzeiten, die Hervorhebung faellt **still** weg — kein Hinweis im
   Protokoll. Erst der zweite Lauf mit `--auto-captions` hat sie zurueckgeholt.
   Der Wortlaut war in beiden gleich, nur die Gruppierung weicht an einer
   Stelle ab (`MEANINGFUL FOR YOU` gegen `MEANINGFUL FOR` + `YOU`) — Whisper
   ist nicht deterministisch.

**Ortscheck auf den Untertiteln: sauber**, kein Hinweis auf den Wohnort.

**Was ich noch aendern wuerde, aber nicht ohne ihn:** die Totale bei Sekunde
25–31 traegt die Pointe (*„to see yourself reflected through the other"*), und
dort ist er klein und im Profil. Einfrieren waere falsch — er ist ja zu sehen.
Moeglich waere, die Totale enger zu fassen; das ist eine Aenderung am Bild und
gehoert vor seine Augen, nicht in denselben Durchgang.
