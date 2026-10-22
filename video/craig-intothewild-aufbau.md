# Craig / Into the Wild — Aufbau der Vollbild-Fassung

Stand 22.10. Die Fassung, die aus Variante A hervorgeht, nachdem vier Dinge
beanstandet waren: Rand an den Einspielern, zu später Einstieg, doppelt
benutztes Material, Tagebuch nicht beim Zitat.

## Quelle

Bildschirmaufnahme des Trailers, 2622x1206, 185 s.
Das Filmbild darin: **2138x917 bei x=242, y=153.**

Die 917 statt 961 sind Absicht: in den unteren 43 Pixeln des Filmfeldes
stehen die eingebrannten Trailer-Untertitel — jedes Mal an derselben Stelle.
Weggeschnitten ist der **ganze** Trailer brauchbar statt 36 von 185 Sekunden.
Kosten: 4,5 Prozent der Bildhöhe. Siehe `untertitel_finden.py`.

Gegengeprüft am fertigen Short: 105 Proben im Abstand 0,5 s über das untere
Fünftel — kein einziger eingebrannter Untertitel mehr im Bild.

## Die neun Einspieler

Jeder aus einer anderen Stelle des Trailers. **Nichts wird zweimal benutzt.**
Bei 171 brauchbaren Sekunden gibt es dafür keinen Grund.

| Name | Trailer ab | Dauer | Bild                        | im Short     |
|------|-----------:|------:|-----------------------------|--------------|
| n1   |       24,0 |  7,7s | Wald, Rucksack am Wasser    | 0,00–6,40    |
| n2   |       64,5 |  4,7s | Lesen im Gegenlicht         | 6,40–10,30   |
| n3   |      148,0 |  4,5s | **das Tagebuch**            | 10,30–14,00  |
| n4   |       37,5 |  4,8s | Silhouette am Meer, Vögel   | 14,00–18,00  |
| n5   |       43,5 |  4,8s | Pferde                      | 18,00–22,00  |
| n6   |       96,0 |  7,2s | Wüste, Gehen                | 25,00–31,00  |
| n7   |      116,0 |  6,6s | Schnee, Berge               | 31,00–36,50  |
| n8   |       68,0 |  5,4s | Wasserfall                  | 39,50–44,00  |
| n9   |      124,5 |  7,9s | Bus im Schnee, Lagerfeuer   | 44,00–50,60  |

**n3 liegt auf dem Zitat.** Bei 12,5–13,5 s sagt Craig „happiness … when
shared", und im Bild steht die Tagebuchseite. Das war die Vorgabe.

Craig selbst ist noch bei 22,0–25,0, 36,5–39,5 und 50,6–52,5 zu sehen:
7,9 von 52,5 Sekunden. **85 Prozent B-Roll.**

## Was dabei nicht zu haben ist

`--broll-modus vollbild` schneidet aus dem 2,33:1-Feld ein echtes 9:16
heraus: von 2138 Pixeln Breite bleiben 516. Hochgerechnet auf 1080x1920 ist
das **Faktor 2,09** — die Einspieler sind weicher als das Interviewbild.

Daran ist mit dieser Quelle nichts zu ändern; mehr Pixel hat die Aufnahme
nicht. Wer es schärfer will, nimmt den Film im Vollbild eines größeren
Monitors auf, nicht im Browserfenster.

Die Alternative `--broll-modus unschaerfe` bleibt randlos **ohne** zu
beschneiden (scharfe Mitte, unscharf vergrößerte Kopie dahinter) und
rechnet nur 1,18-fach hoch. Sie kostet dafür das echte Vollbild.

## Zweiter Punkt am Rande

In der gestapelten Zwei-Personen-Einstellung (z. B. 37,5 s) steht das
YNB-Zeichen zweimal im Bild: einmal eingebrannt in der Aufnahme unten links,
einmal vom Renderer mittig. Das ist nicht neu und nicht von dieser Fassung
gemacht — es steckt im Master. Wegzubekommen wäre es nur, indem der
Stapel-Ausschnitt die untere linke Ecke meidet.
