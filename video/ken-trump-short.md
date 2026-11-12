# Ken Stern — seine ehrliche Meinung zu Trump (12.11.)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

| Datei | Länge | Ton |
|---|---|---|
| `YNB Podcast Ken Stern Trump (In This Shirt).mp4` | 54,7 s | Stimme + Bett bis zum letzten Bild |
| `YNB Podcast Ken Stern Trump.mp4` | 54,7 s | nur Stimme |

Plan: `video/plaene/ken-trump-plan.json`.
Korrekturen: `video/korrekturen-ken-shorts2.txt`.

---

## Wo es stand

Sein Vorbereitungsdokument führt es als
`53:25 Short & Clip: Ex-NPR Boss: My Honest Opinion about Trump`.
Die Marke stimmt: bei **0:53:20,58** kommt er von selbst darauf, mitten in
der Antwort auf eine ganz andere Frage (nach seinen Eltern und dem
DC-Umfeld). Deshalb braucht dieses Short keine Frage als Einstieg — der
erste Satz trägt sich allein.

> „I think a lot of my views today are colored by the fact that we're led by
> a guy — we're led, it's not the right term — **the president is a guy who
> is the embodiment of political polarization, who lives to demonize others**,
> who gets value and strength and energy from everything I sort of detest
> about American politics: not listening and demonizing the other side. When
> I wrote the book in 2016, I thought we were reaching sort of the peak of
> polarization — and little did I know that everything has gotten worse and
> worse and spiraled. When I talk about politics, I talk about what
> polarization and demonization is doing to us and what it is wrecked on
> American society, and how to think about putting that back. **Hopefully
> elections will step us away from a precipice that is very dangerous.**"

## Der Schnitt

Rohzeit **0:53:20,30–0:54:30,40** = 70,1 s. Davon sind rund 20 s reine
Denkpause; die Rede selbst ist knapp 45 s. Drei Stücke raus, zusammen 14,2 s:

| # | im Short | roh | was | s |
|---|---|---|---|---|
| 1 | 0:21.6 | 53:44,10–53:48,53 | „So I'm, you know, my views are now, I thought we were sort of," | 4,4 |
| 2 | 0:31.4 | 53:59,30–54:04,43 | „So I think my concerns," + 3,2 s Pause | 5,1 |
| 3 | 0:46.1 | 54:20,60–54:25,20 | „And hopefully," + 3,4 s Pause | 4,6 |

Alle drei sind Anlauf ohne Inhalt. Bleiben 55,93 s roh, bei **Tempo 1,1**
noch 50,85 s, mit Outro **54,7 s**.

**Schnitt 2 liegt genau auf einem Kameraschnitt (Bild 97179 = 3239,300)
und ist dadurch unsichtbar.** Die Pause nach „spiraled" und der
Kameraschnitt fallen zusammen — das war Glück, aber nur zu sehen, weil die
Kameraschnitte vor der Schnittentscheidung gemessen waren.

Schnitt 1 und 3 liegen innerhalb einer laufenden Einstellung, sind also
Sprungschnitte, beide auf einer Satzgrenze. Ein leichtes Nachzoomen
(540×960 statt 608×1080) hätte sie kaschiert — verworfen, weil er sich an
beiden Stellen vorlehnt und die Kopffreiheit dann auf 86 px fällt. In der
Liste als Angebot.

## Kameraschnitte und Kästen

Vier Kameraschnitte im Block, bei 0,08 **und** bei 0,035 Schwelle dieselben
vier — keine weichen übersehen:

| Bild | Zeit | nach |
|---|---|---|
| 96033 | 3201,100 | Ken, Nah (Kamera 1) |
| 96980 | 3232,667 | Totale |
| 97179 | 3239,300 | Ken, Nah (Kamera 2) |
| 98118 | 3270,600 | (hinter dem Schluss) |

**Die zwei Nahaufnahmen sind nicht dieselbe Kamera.** Kopfmitte an je fünf
Stellen gemessen: Kamera 1 bei Quell-x ≈ 1000, Kamera 2 bei ≈ 900. Mit
einem Kasten für beide säße er in einer der beiden schief — genau sein
Einwand vom Meaningful-Short. Darum **648** und **548**.

| # | Kasten | von–bis (Vorlage) | wer |
|---|---|---|---|
| 1 | `1312:0:608:1080` | 0,0000–0,8000 | Totale, Kasten auf Ken |
| 2 | `648:0:608:1080` | 0,8000–27,9333 | Ken, Nah (Kamera 1) |
| 3 | `1312:0:608:1080` | 27,9333–34,5666 | Totale |
| 4 | `548:0:608:1080` | 34,5666–55,9333 | Ken, Nah (Kamera 2) |

## Zeilenhöhe 1200, nicht 1140

Beim Meaningful-Short war 1140 richtig. Hier nicht: in Kamera 2 reicht sein
Kinn bis Ausgabe-y **1124**, das wären 16 px Abstand gewesen. Nachgemessen
am gerenderten Ausschnitt, nicht am Vollbild — im Vollbild hatte ich das
Kinn erst auf 1199 geschätzt und lag um 135 px daneben.

**1200 für alle vier Einstellungen.** Der Renderer meldet
`Hoehen [1200]` — damit kann die Schrift nicht springen.

## Sechs Korrekturen an den Untertiteln

`medium` hat an fünf Stellen daneben gehört. Jede am ungedehnten Ton mit
large-v3 bei 1,0 **und** 0,6 gegengeprüft:

| falsch | richtig | Befund |
|---|---|---|
| „THINK A LOT OF" | „I THINK A LOT OF" | large-v3 hört „I" zweimal; Pegel der Vorlage setzt bei 0,34 s ein, vor „think" |
| „DEMONIZE OTHER" | „DEMONIZE OTHERS" | zweimal „others" |
| „ENERGY FROM?" | „ENERGY FROM" | Fragezeichen mitten im Satz |
| „DEMON AND DEMONIZING THOSE" | „AND DEMONIZING THE OTHER SIDE" | sein „uh" wird zu „demon" |
| „AND LOADED WE HAVEN'T LITTLE DID I KNOW WE HAVEN'T" | „AND LITTLE DID I KNOW THAT" | Fehlstart „little did we ha—" |

Das Fragezeichen geht nur weg, weil `korrekturen_anwenden` die Gruppe neu
aufbaut und den Satzzeichenschwanz **nur ans letzte Wort** hängt. Deshalb
`from everything -> from everything`: identische Wörter, aber „from" wird
neu geschrieben und verliert sein „?". Eine Ein-Wort-Korrektur hätte es
nicht geschafft.

**Stehengeblieben:** „and what it is wrecked on American society". Er sagt
dort wörtlich „and what it is — uh — wrecked on — um — American society".
Grammatisch schief, aber so gesagt. Geglättet hieße: ihm Worte in den Mund
legen. In der Liste mit zwei Auswegen angeboten.

## Lautheit

Vorlage roh **−31,7 LUFS**. Mit **+2,0 dB** auf die Sprachspur vor dem
Outro auf **−29,7**, Spitze danach −4,9 dB.

Der fertige Mix mit Bett maß dann −30,2 statt −29,8 — die Gatterung des
ebur128 verschiebt sich, wenn ein leises Bett die stillen Blöcke anhebt.
Mit **+0,4 dB** auf den Mix auf **−29,8 LUFS**, exakt wie Ubuntu und
Meaningful. Spitze −5,0 dB.

| Short (Hauptteil) | Lautheit |
|---|---|
| Ubuntu | −29,8 LUFS |
| Meaningful | −29,8 LUFS |
| **Trump** | **−29,8 LUFS** |
| Aging | −27,7 LUFS |

## Musik und Abnahme

**Musik war nicht angesagt.** Gelegt wie bei den drei anderen Ken-Shorts,
weil das zuletzt so abgenommen war — „In This Shirt" ab 0:23,25, Bett
0,00–54,67 s, Ausblende 3,8 s ab 50,87 s, also genau über dem Outro.
Durch Subtraktion geprüft: −44 dB während der Rede, −48,7 bei 51 s,
−54,2 bei 53 s, −72,6 bei 54,5 s. Pegel: Stimme −33,6 dB, Bett −11,6 dB,
Verstärkung −32,0 dB (= Stimme − Bett − 10).

1080×1920 · 48 kHz · 54,7 s · Outro da · 56 Untertitel · Ortscheck sauber.
Alle vier Übergänge bildweise geprüft, keine Fremdbilder. „Kein Musikbett"
schlägt bei der Musikfassung erwartungsgemäß fehl (−43,9 dB); die Fassung
ohne Musik besteht alle Prüfungen (−76,6 dB).

## Offen

- Das Short danach: Deine Frage „In a country living in bubbles with
  thicker and thicker walls, what still gives you hope and what actually
  scares you?" mit seiner Antwort ab 0:54:42. Eigenes Short, angeboten.
- Aging auf −29,8 LUFS ziehen (steht seit dem Meaningful-Short offen).
