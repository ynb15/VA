# Chris Williamson essay — outreach cards

31 PNGs for the video montage in the **Wanted** chapter
("dozens of cold emails, then fifties, then hundreds").

Real sent mail, `ynb@yannick-noah.com` / `info@yannickbernard.com`,
May–Nov 2026. 402 outreach threads in total; 201 share the "Man's Search
for Meaning" subject line.

**No email addresses on any outreach card.** Each card carries recipient,
subject and the opening of the real mail. The boilerplate ("my name is
Yannick, host of…") is skipped on every card — it is near-identical in all
30 mails.

Transparent background, 3000 px wide, @2x (CSS width 1500).

## One paragraph or two

Every card used to carry two paragraphs, which made the long ones twice
the height of the short ones. Since 20.11.2026 the length of the first
paragraph decides:

- **three or more rendered lines → paragraph one stands alone.** It is a
  closed thought and already in Yannick's voice; the second would only
  double the card.
- **two lines or fewer → both paragraphs.** Paragraph one is an opener
  (a quote, a blog title, a one-liner); alone the card would be thin.

The threshold is measured in the browser, not estimated: `render.js` puts
a Range around paragraph one and counts its client rects.

`src/measure.json` records the line count and the decision per card.
Yannick named eight cards himself; the rule reproduces all eight:

| Card | Lines in ¶1 | Paragraphs | His call |
|---|---|---|---|
| 01 Matthew McConaughey | 4 | 1 | 1 ✓ |
| 02 Lex Fridman | 1 | 2 | 2 ✓ |
| 03 Tim Ferriss | 1 | 2 | 2 ✓ |
| 04 Brené Brown | 3 | 1 | 1 ✓ |
| 05 Michael Pollan | 6 | 1 | 1 ✓ |
| 06 Peter Attia | 3 | 1 | |
| 07 Ryan Holiday | 1 | 2 | |
| 08 Mark Manson | 2 | 2 | 2 ✓ |
| 09 Jim Collins | 2 | 2 | |
| 10 Jon Krakauer | 3 | 1 | |
| 11 Steven Pressfield | 2 | 2 | |
| 12 Sebastian Thrun | 3 | 1 | |
| 13 Alex Banayan | 4 | 1 | |
| 14 Lance Armstrong | 3 | 1 | 1 ✓ |
| 15 T.D. Jakes | 3 | 1 | |
| 16 Codie Sanchez | 4 | 1 | |
| 17 MJ DeMarco | 5 | 1 | |
| 18 Blake Mycoskie | 4 | 1 | |
| 19 Dean Karnazes | 3 | 1 | |
| 20 Arthur Brooks | 3 | 1 | |
| 21 Greg McKeown | 3 | 1 | |
| 22 Aubrey Marcus | 2 | 2 | |
| 23 Jack Kornfield | 2 | 2 | |
| 24 Mikhaila Peterson | 2 | 2 | |
| 25 Andrew Huberman | 4 | 1 | 1 ✓ |
| 26 Yung Pueblo (Diego Perez) | 3 | 1 | |
| 27 Thomas Brag (Yes Theory) | 2 | 2 | |
| 28 Kirk Watson | 2 | 2 | |
| 29 MacKenzie Price | 3 | 1 | |
| 30 Marian Goodell | 4 | 1 | |

Lance Armstrong is the boundary case: three lines, and he called it one
paragraph. So the cut runs between two and three lines.

Card heights now run 812–1218 px instead of 948–1582 px.

**Open question — card 10, Jon Krakauer.** Its first paragraph is a
quotation from *Into the Wild*, three lines long, so the rule drops the
second. What is left is a Krakauer quote with no Yannick in it; the line
that makes it an outreach mail ("You wrote that not about a character, but
about yourself…") sits in paragraph two. It is the only quote-led card the
rule strips. Setting `"force": 2` on that entry in `src/cards.json` would
be the fix — not done, because the rule as stated says one.

## Rebuilding

    node src/render.js            # the 30 cards, by the rule
    node src/render.js --both     # calibration run: always two paragraphs
    node src/render.js --both --calib   # ...into src/calib/, for diffing

The calibration run reproduces the heights of the previous card set
exactly, all 30 — that is how the layout values in `render.js` were fixed.

`R0-goodell.png` is not rebuilt: the reply card has one block only.

## Source data

`src/cards.json` — recipient, subject, date, status tag, both paragraphs.
Transcribed from the sent mail and checked against the earlier card set.

| # | Recipient | Status |
|---|---|---|
| 01 | Matthew McConaughey | never delivered (bounced 3x) |
| 02 | Lex Fridman | no reply, no bounce |
| 03 | Tim Ferriss | no reply, no bounce |
| 04 | Brené Brown | no reply, no bounce |
| 05 | Michael Pollan | replied personally, declined |
| 06 | Peter Attia | no reply, no bounce |
| 07 | Ryan Holiday | no reply, no bounce |
| 08 | Mark Manson | no reply, no bounce |
| 09 | Jim Collins | no reply, no bounce |
| 10 | Jon Krakauer | delivery delayed |
| 11 | Steven Pressfield | replied personally |
| 12 | Sebastian Thrun | no reply, no bounce |
| 13 | Alex Banayan | replied personally |
| 14 | Lance Armstrong | 2 of 3 addresses bounced |
| 15 | T.D. Jakes | no reply, no bounce |
| 16 | Codie Sanchez | no reply, no bounce |
| 17 | MJ DeMarco | no reply, no bounce |
| 18 | Blake Mycoskie | no reply, no bounce |
| 19 | Dean Karnazes | no reply, no bounce |
| 20 | Arthur Brooks | bounced |
| 21 | Greg McKeown | no reply, no bounce |
| 22 | Aubrey Marcus | no reply, no bounce |
| 23 | Jack Kornfield | no reply, no bounce |
| 24 | Mikhaila Peterson | no reply, no bounce |
| 25 | Andrew Huberman | auto-reply after 52 seconds |
| 26 | Yung Pueblo (Diego Perez) | no reply, no bounce |
| 27 | Thomas Brag (Yes Theory) | no reply, no bounce |
| 28 | Kirk Watson | no reply, no bounce |
| 29 | MacKenzie Price | reply from her office, signed Mary |
| 30 | Marian Goodell | replied personally — and it led to the recording |

`R0-goodell.png` — Marian Goodell's reply in full, as a dark card. It is
the one card that shows an address (hers, in the header). It was approved
that way and is left untouched; say the word and it comes off.

## Suggested cut

Run 20 of the silent ones fast (≈0.8s each, long enough to read the first
line). Hold **01 McConaughey** (never arrived). Then the failures:
14 Armstrong, 20 Brooks, 10 Krakauer, 25 Huberman's 52-second robot.
Then the four human noes: 05 Pollan, 11 Pressfield, 13 Banayan, 29 Price.
End on 30 Goodell and hold **R0** longest — it is the only one in the
stack that turned into something.

## Held back

The paragraph that was Mark Manson's natural second beat names a pregnancy
loss. It is deliberately NOT in `src/cards.json`, not on any card and not
in this folder; card 08 uses the lighter paragraph instead. YNB decides
whether it is ever used.
