# Ken Stern — seine ehrliche Meinung zu Trump (13.11., Fassung 5)

**Nicht veröffentlicht.** Liegt zur Abnahme, Yannick lädt hoch.

| Datei | Länge | Ton |
|---|---|---|
| `YNB Podcast Ken Stern Trump (Moms Got Work).mp4` | 51,9 s | Stimme + Bett ab 0:03,0 des Titels, bis zum letzten Bild |
| `YNB Podcast Ken Stern Trump.mp4` | 51,9 s | nur Stimme |

## Fassung 5 (13.11.) — Bettpegel am abgenommenen Short gemessen

*„Musik wieder mal viel zu leise, shaking my head."*

Ich hatte den Pegel dreimal aus der Formel `G = Stimme − Bett − 10 dB`
genommen und nie das Bett in den **abgenommenen** Shorts freigelegt. Das
geht in zwei Minuten: Musikfassung minus musikfreie Fassung, beide liegen
im Repo.

| Bett im Hauptteil | |
|---|---|
| Ubuntu | −45,4 dB |
| Meaningful | −44,8 dB |
| Aging | −43,4 dB |
| Fassung 4 | −44,1 dB |
| **Fassung 5** | **−42,2 dB** |

Der Mittelwert war richtig. **Der Verlauf nicht:**

| je 2 s | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fassung 4 | −48 | −48 | −48 | −51 | −53 | −53 | −43 | −42 | −43 | −42 | −44 |
| Fassung 5 | −45 | −44 | −42 | −44 | −43 | −43 | −43 | −41 | −43 | −42 | −43 |

Die ersten zwölf Sekunden lagen 8–10 dB unter dem Rest: die ruhige Stelle
des Titels (0:55–1:00), die ich in Fassung 3 bewusst an den Anfang gelegt
und in der Übergabe als „ein Atmen, kein Loch" verharmlost hatte.

**Fenster neu gewählt.** Jedes mögliche 52-s-Fenster auf Gleichmäßigkeit
gemessen (RMS je Sekunde, Spanne zwischen leisestem und mittlerem Punkt):

| Fenster | min | Spanne |
|---|---|---|
| **ab 0:03** | −21,5 dB | **3,0 dB** |
| ab 0:06 | −26,9 dB | 8,2 dB |
| ab 0:48 (Fassung 4) | −27,9 dB | 11,4 dB |

Das gleichmäßigste Fenster ist der **Anfang** des Stücks — genau der, den
die 2-kHz-Regel ausschließt. Für ein Bett 42 dB unter der Stimme zählt der
Pegel, nicht das Timbre. Bett jetzt **ab 0:03,0**, endet bei 0:54,9, also
vor der ruhigen Stelle und weit vor dem Song-Outro ab 1:41.

Verstärkung −23,8 dB. Ausblende unverändert 3,8 s ab 48,13 s über dem
Outro; Absenkung unverändert mit seiner Einstellung vom 21.10. (ratio 4,
release 250). Hauptteil −29,8 LUFS, Spitze −4,8 dB.

---

## Fassung 4 (13.11.) — sein Preset, statt meiner Messungen

*„Frag die anderen Agenten. Die Information liegt schon lange überall."*

Sie lag überall. Drei Fassungen lang habe ich an seinen fertigen Shorts
gemessen, statt die Quelle zu suchen.

**Die Quelle:** `claude/content-assistant:video/preset-ynb.md` — Isabelles
Preset-Ordner, den er am 21.10. übergeben hat. Und
`claude/content-gastauftritte:LERNEN.md` Zeile 54, seit dem 21.10.:
*„Schrift Inter Black (nicht DejaVu Sans Bold) · Größe 82 · Gelb #F9F13A ·
Zeilenbreite 72 % · Logo 28 % auf Höhe 0,87 · Gradation entsättigt-kühl."*

**Die Ursache:** `video/shorts-render.py` auf diesem Zweig hatte **1271
Zeilen**, die aktuelle Fassung auf `claude/content-assistant` hat **1608**.
Mein Abzug war der Stand vor dem 21.10. Die aktuelle Fassung trägt das
Preset als Vorgabewerte: `video/fonts/Inter-Black.otf`, Größe 82, sein
Gelb, Logo 28 %, Zeilenbreite 72 %, und `--look preset`. Mit ihr braucht
der Aufruf keinen einzigen Handwert mehr.

Geholt mit:
```
git checkout origin/claude/content-assistant -- \
  video/shorts-render.py video/fonts/Inter-Black.otf \
  video/luts/hald_identity_1080.png
```

**Warum keine installierte Schrift gepasst hat:** das Preset nimmt Inter
Black als Ersatz für Eveleth (CapCut, nicht exportierbar) und zieht sie auf
**112 % Breite plus 2 px Strich** in der Textfarbe (`SCALE_X = 112`,
`FETTER = 2`). Deshalb maß ich Füllgrad 0,667, den keine reine Schrift
erreicht. Durch Nachmessen ist das nicht zu finden.

Am Wort „OTHERS", das in beiden Shorts vorkommt:

| | Kasten | Strichstärke | Gelbton | Zeile | IoU |
|---|---|---|---|---|---|
| Meaningful (akzeptiert) | 313 × 54 | 0,667 | RGB(248,240,57) | 1154 | — |
| Fassung 2 (DejaVu 84) | 318 × 54 | 0,458 | RGB(253,211,46) | 1154 | 0,651 |
| Fassung 3 (Inter Display Black 87) | 290 × 52 | 0,562 | RGB(246,239,56) | 1158 | 0,783 |
| **Fassung 4 (Preset)** | **312 × 54** | **0,665** | **RGB(248,240,57)** | **1154** | **0,945** |

Logo 267 px auf Mitte y 1669 — wie Meaningful. Look jetzt `preset`
(entsättigt-kühl), nicht `warm`.

Die Fassungen 2 und 3 lieferten dadurch 52 Untertitel, Fassung 4 liefert
**62**: das Preset begrenzt die Zeile auf 72 % der Bildbreite (777 px statt
1000) und teilt längere Dreier.

**Weiter offen, nur von ihm zu lösen:** `luts/ynb_look.png` fehlt; der
Renderer meldet das selbst und nimmt die Annäherung aus dem Preset. Die
5-Minuten-Anleitung steht in `video/preset-ynb.md`. Liegt Eveleth als
Datei in `video/fonts/`, entfällt das Nachziehen und die Schrift ist exakt
seine.

### Die Musik, aus Fassung 3 übernommen

„Mom's Got Work" hat ab **1:41** sein eigenes Outro (−19 auf −47 dB). Das
erste Bett lief 1:00,75–1:52,68 und lag die letzten 11 s darauf, darüber
noch die eigene Ausblende. Jetzt **ab 0:48,50**, Bett endet bei 1:40,4.

| Bettpegel im Short | 38 s | 42 s | 44 s | 46 s | 48 s | 50 s |
|---|---|---|---|---|---|---|
| ab 1:00,75 | −44 | −49 | −56 | −62 | −58 | −65 |
| **ab 0:48,50** | −42 | −44 | −44 | −41 | −45 | −49 |

### Der Irrweg, zur Warnung

Fassung 3 lief auf einer **eigenen Kopie** des Renderers mit
Inter Display Black und handgesetztem Gelb. Die Datei
(`video/render-inter-shorts2.py`) ist gelöscht — sie war der Versuch, durch
Messen zu rekonstruieren, was in einer Datei stand.

---

## Fassung 3 (13.11.) — Schriftart und Musikfenster (Irrweg)

*„du hast Mom's Got Work an der völlig falschen Stelle eingesetzt. Man hört
die letzten 10 Sekunden gefühlt gar nichts mehr von dem Song. Und die
Schrift ist immer noch die falsche."*

### Die Musik: ein Bett braucht zwei Grenzen, nicht eine

„Mom's Got Work" hat ab **1:41** sein eigenes Outro — Abfall von −19 dB auf
−47 dB bis 1:52. Mein Bett lief von 1:00,75 bis **1:52,68**, die letzten
11 Sekunden also auf dem Ausklang des Songs, darüber noch meine eigene
Ausblende.

Mein Fehler war die Methode: der **Einsatz** war sauber gemessen (2-kHz-
Sprung), das **Ende** des Fensters nie geprüft.

Jetzt **ab 0:48,50**: das Bett endet bei 1:40,4, noch im vollen Teil, und
die dichteste Stelle des Titels (1:30–1:40) liegt unter dem Schluss des
Shorts. Bettpegel im fertigen Short, durch Subtraktion:

| | 38 s | 42 s | 44 s | 46 s | 48 s | 50 s |
|---|---|---|---|---|---|---|
| ab 1:00,75 | −44 | −49 | −56 | −62 | −58 | −65 |
| **ab 0:48,50** | −42 | −45 | −44 | −41 | −45 | −50 |

Preis: die ruhige Stelle des Titels (0:55–1:00) liegt jetzt bei Sekunde
7–12 des Shorts. Kein 52-s-Fenster vermeidet beides.

### Die Schriftart — nicht die Größe

Fassung 2 hatte die richtige Größe und die falsche Schrift. Am Wort
„OTHERS", das in beiden Shorts vorkommt:

| | Kasten | Strichstärke | Gelbton |
|---|---|---|---|
| Meaningful (akzeptiert) | 313 × 54 | 0,667 | RGB(248,240,57) |
| Trump Fassung 2 | 318 × 54 | 0,458 | RGB(253,211,46) |
| **Trump Fassung 3** | 290 × 52 | 0,562 | RGB(246,239,56) |

Gleiche Höhe, gleiche Breite, **43 % dünnere Striche** — eine andere
Schriftart. Ich hatte zwei Kennzahlen geprüft und die Form nicht angesehen.

**Ursache:** `FONT = "DejaVu Sans"` steht seit dem ersten Commit (19.10.)
unverändert im Renderer. Auf der Maschine, auf der Ubuntu, Meaningful,
Aging, Craig und die Aaronson-Shorts entstanden, war DejaVu Sans **nicht
installiert**; libass wich auf eine schwere Grotesk aus — und das ist der
abgenommene Look. Der Container wurde zwischen 11. und 12.11. neu gebaut,
seitdem ist DejaVu Sans da. Dass alle älteren Shorts RGB(248,240,57) zeigen
und nur die Trump-Fassungen RGB(253,211,46), den **reinen Stilwert** der
ASS-Datei, bestätigt es.

Alle 17 installierten Familien gegen die Buchstabenmaske geprüft:

| Familie | IoU |
|---|---|
| **Inter Display Black** | **0,794** |
| Inter Black | 0,774 |
| Inter Display ExtraBold | 0,745 |
| DejaVu Sans | 0,658 |

Fassung 3 läuft auf **Inter Display Black, Größe 87**, plus dem gemessenen
Gelbton. Es ist die nächstbeste, nicht dieselbe: Striche noch 16 % dünner,
Wort 7 % schmaler. Die Schrift der akzeptierten Shorts ist auf dieser
Maschine nicht mehr vorhanden.

**Gerendert mit einer eigenen Kopie:** `video/render-inter-shorts2.py`,
zwei Zeilen anders als `video/shorts-render.py` (FONT, GELB). Der geteilte
Renderer gehört Shorts I und ist unangetastet. Der dauerhafte Weg ist ein
Schalter `--font` dort plus die Schriftdatei im Repo statt auf der
Maschine — **Shorts I beschrieben, nicht gebaut.**


Plan: `video/plaene/ken-trump-plan.json`.
Korrekturen: `video/korrekturen-ken-shorts2.txt`.

## Der vollständige Aufruf

**Keine Handwerte mehr.** Mit dem aktuellen Renderer von
`claude/content-assistant` sind Schriftgröße 82, Logo 28 %, Gelb und
Zeilenbreite bereits die Vorgaben aus seinem Preset. Was bleibt, ist
`--look preset` statt `warm`.

```
python3 -I video/shorts-render.py \
  --src vorlage-trump2-laut.mp4 \
  --plan video/plaene/ken-trump-plan.json \
  --out "YNB Podcast Ken Stern Trump.mp4" \
  --tempo 1.1 --look warm --laut aus \
  --logo video/marke/ynb-logo-weiss-beschnitten.png --logo-breite 300 \
  --schriftgroesse 84 \
  --outro marke/ynb-outro-9-16.mp4 \
  --auto-captions --model medium --lang en \
  --korrekturen video/korrekturen-ken-shorts2.txt \
  --srt-out "YNB Podcast Ken Stern Trump.srt"
```

## Fassung 2 (13.11.) — Logo, Einstieg, erster Musikversuch

Seine Ansage: *„ich bin schockiert darüber, wie groß plötzlich das Logo ist
und wie du einfach die Schrift verändert hast … leg doch noch einen anderen
Song unter, und zwar Mom's Got Work. Und dann Intro starten bei ‚we're led
by a guy'."*

### 1. Logo und Schrift — gemessen, nicht geschätzt

| | Logo sichtbar | „OTHERS" | Zeilenhöhe |
|---|---|---|---|
| Ubuntu | 281 px | 313 × 54 px | 1140 |
| Meaningful | 267 px | 313 × 54 px | 1140 |
| Aging | 281 px | — | 1140 |
| **Trump, Fassung 1** | **481 px** | **294 × 49 px** | **1200** |
| Trump, Fassung 2 | 279 px | 317 × 54 px | 1140 |

Das Logo war 1,7-mal so breit, weil `--logo-breite` fehlte (Standard 520
statt 300). Die Schrift war **nicht größer, sondern 7 % kleiner** (78 statt
84) — was ins Auge sprang, war das Logo.

Gemessen wurde die Logobreite über weiße Pixel (`min(RGB) ≥ 250`) im Band
y 1540–1840, die Schriftgröße über die Höhe eines gelben Worts, gegen
Testsätze derselben ASS-Stilzeile auf Schwarz. Zwei unabhängige Wörter
(„OTHERS", „HELPING") ergeben beide **84**.

Bestätigung aus dem Code: die Umbruchgrenze ist `max_em=11.8`, und
11,8 × 84 = 991 px füllt die nutzbare Zeilenbreite von 1000 px genau aus.

### 2. Zeilenhöhe zurück auf 1140

Fassung 1 lag auf 1200, weil ich Kens Kinn in Kamera 2 auf Ausgabe-y 1124
geschätzt hatte. Am gerenderten Bild mit eingezeichneter Linie liegt es bei
**1115**; 1140 sitzt an der engsten Stelle 25 px darunter, auf dem Hals.

### 3. Neuer Einstieg bei „we're led by a guy"

Schnitt in der Sprechpause zwischen „that" und „we're", Rohzeit
**0:53:23,30** (Bild 96099). „we're" setzt bei 3203,36 ein; vom „that"
bleiben 0,05 s Ausklang bei −45 dB, unhörbar. Vorne fallen damit 3,1 s weg
und die 0,8 s Totale am Anfang entfallen mit — das Short öffnet direkt auf
der Nahaufnahme. Drei statt vier Einstellungen.

**Gelesen als: das Short beginnt dort.** Falls er den Musikeinsatz meinte,
ist das ein Durchlauf — in der Liste vermerkt.

### 4. Neue Musik: Mom's Got Work (Adam Taylor), ab 1:00,75

Drive `1z01tjaFm_tjUNelau9l9DTc3sjHbmsYo`, 117,8 s.

Der Einsatzpunkt war nicht eindeutig: das Stück hat helle Fills bei 0:14,
0:26 und 0:36, die jedes Mal abfallen. Geeicht an „In This Shirt", wo der
abgenommene Wert (0:23,25) bekannt ist — dort zeigt sich die Form: Senke,
Sprung, dann ein Niveau, das **hält**. Dieselbe Form liegt hier bei
**1:00,75**: von 4,3 auf 13,8 dB in einem Schritt, danach 25–35 dB bis
1:50. Kein Looping nötig.

Bett 0,00–51,93 s, Ausblende 3,8 s ab 48,13 s. Pegel: Stimme −33,5 dB,
Bett −15,4 dB, Verstärkung −28,1 dB. Hauptteil **−29,8 LUFS**, Spitze
−4,8 dB.

### 5. Zwei Untertitel-Korrekturen mussten nachgezogen werden

Am 3,1 s später beginnenden Ton hat `medium` anders gehört: „demonizing
others" statt „demon and demonizing those", „had gotten" statt „has
gotten". Whisper arbeitet in Kontextfenstern, ein verschobener Anfang
verschiebt jedes Fenster. Beide Varianten stehen jetzt in der
Korrekturliste.

---

## Fassung 1 (12.11.) — Grundlagen, weiter gültig

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

Rohzeit **0:53:20,30–0:54:30,40** = 70,1 s (Fassung 2: ab 0:53:23,30). Davon sind rund 20 s reine
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

Fassung 2, drei Einstellungen (Vorlage 1588 Bilder = 52,9333 s):

| # | Kasten | von–bis (Vorlage) | wer |
|---|---|---|---|
| 1 | `648:0:608:1080` | 0,0000–24,9333 | Ken, Nah (Kamera 1) |
| 2 | `1312:0:608:1080` | 24,9333–31,5666 | Totale, Kasten auf Ken |
| 3 | `548:0:608:1080` | 31,5666–52,9333 | Ken, Nah (Kamera 2) |

## Zeilenhöhe 1200, nicht 1140 — **in Fassung 2 zurückgenommen**

Beim Meaningful-Short war 1140 richtig. Hier nicht: in Kamera 2 reicht sein
Kinn bis Ausgabe-y **1124**, das wären 16 px Abstand gewesen. Nachgemessen
am gerenderten Ausschnitt, nicht am Vollbild — im Vollbild hatte ich das
Kinn erst auf 1199 geschätzt und lag um 135 px daneben.

**1200 für alle vier Einstellungen.** Der Renderer meldet
`Hoehen [1200]` — damit kann die Schrift nicht springen.

**Nachtrag 13.11.: falsch.** Auch 1124 war noch geschätzt. Am gerenderten
Bild mit eingezeichneter Linie liegt das Kinn bei 1115, und 1140 sitzt
25 px darunter, auf dem Hals. Fassung 2 läuft auf 1140 wie die anderen
drei Ken-Shorts.

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
