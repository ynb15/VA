# Thumbnail 3 — „The End of Humanity", ohne Grafik

**Von Yannick bestellt, 21.10.2026**, wörtlich: *„ein drittes Thumbnail
erstellen ohne Grafik und dann The End of Humanity. Untereinander, alles hat
eine Zeile. End mit rotem Balken."*

**Gebaut wird es vom Thumbnail Assistant** (`claude/thumbnails`). Das ist sein
Fach; ich liefere die Copy und die Spezifikation. Übergeben am 21.10.

## Die Spezifikation

Baugleich mit `plan-extinction.json` — **das ist die Form ohne Grafik**
(kein `mitte`, kein `logo`, kein `karte`), im Unterschied zu
`plan-extinction-mitte.json`.

```json
{
  "hg": "video/thumbnails/_hintergrund.jpg",
  "links": "video/thumbnails/_freisteller/y_3605.png",
  "rechts": "video/thumbnails/_freisteller/a_2504_ohne_hand.png",
  "zeilen": ["The", "End", "of", "Humanity"],
  "kasten": [1, "End"],
  "ziel": "video/thumbnails/aaronson-end-of-humanity.jpg"
}
```

- **Vier Zeilen, je ein Wort**, untereinander — so bestellt.
- **`kasten`-Index 1 = `End`.** Genau ein Kasten, `#DF2C00`, wie in allen sechs
  veröffentlichten.
- **Keine Mittelgrafik.** Nur der abgesoffene Hintergrund und die zwei
  Freisteller links und rechts. Damit greifen die Standard-Zielmaße für die
  Köpfe, nicht die engeren `*_MITTE`-Werte.
- Freisteller: dieselben wie in `aaronson-extinction-*` — Yannick links
  (`y_3605`), Aaronson rechts. **`a_2504_ohne_hand` statt `a_2504`**, weil die
  Hand sonst in den Textblock ragt; falls das in dieser Fassung nicht gilt,
  entscheidet das der Thumbnail Assistant am Bild.

## Zwei Folgen von „vier Zeilen", die er wissen muss

**1. Der Schriftgrad halbiert sich.** `satz()` setzt alle Zeilen in **einem**
Grad und rechnet ihn aus `max_hoehe=470` und `ZEILENHOEHE=1.11`:

| Zeilen | Grad |
|---:|---:|
| 2 (`Human / Extinction?`) | ≈ 211 px |
| **4 (`The / End / of / Humanity`)** | **≈ 106 px** |

Das ist **halb so hoch** wie bei den bisherigen. Auf einem Handy im Feed ist das
der Unterschied, auf den es ankommt. **Seine Entscheidung, nicht meine** — er hat
vier Zeilen bestellt. Wenn er den großen Grad will, ist `The End of / Humanity`
(zwei Zeilen, Kasten auf `End`) die Fassung, die beides hat.

**2. `of` bekommt dieselbe Größe wie `Humanity`.** Sein Bauplan sagt, die Größen
wechseln innerhalb des Blocks — kleines Wort oben, großes darunter
(`THIS / Saves / Human Lives`). `satz()` kann das nicht: **ein Grad für alle
Zeilen**, bewusst so, weil sonst der Zeilenabstand ausfranst. Ein Füllwort wie
`of` in Vollgröße ist in keinem seiner sechs veröffentlichten Thumbnails belegt.
**Auch das ist seine Entscheidung.** Wer es kleiner will, braucht eine Erweiterung
von `satz()` — die liegt beim Thumbnail Assistant, nicht bei mir.

## Was ich dazu nicht behaupte

Dass es besser wirkt als `Human / Extinction?`. Es ist eine andere Aussage
(Vollzug statt Frage) und ein anderer Bau (vier Zeilen statt zwei). **Gemessen
ist nur, dass es von seinen sechs veröffentlichten abweicht** — in der
Zeilenzahl und im Schriftgrad.
