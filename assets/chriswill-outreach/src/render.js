// Outreach-Karten -> transparente PNGs, 3000 px breit (@2x, CSS-Breite 1500).
//
// Regel (von YNB am 20.11.2026 angesagt, hier als Zeilenmass umgesetzt):
// Traegt Absatz 1 DREI oder mehr gerenderte Zeilen, steht er allein - Absatz 2
// wuerde die Karte nur verdoppeln. Bleibt er bei ZWEI oder weniger (ein Zitat,
// ein Blogtitel, ein Einzeiler), waere die Karte allein zu duenn: dann beide.
//
//   node src/render.js            baut die 30 Karten nach der Regel
//   node src/render.js --both     Kalibrierlauf: immer zwei Absaetze
//   node src/render.js --calib    schreibt nach src/calib/ statt ins Zielverzeichnis
//
// Die Massliste in src/measure.json haelt je Karte Zeilenzahl und Entscheidung fest.
// R0-goodell.png wird NICHT neu gebaut - die Antwortkarte hat nur einen Block.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const DIR = path.resolve(__dirname, '..');
const CARDS = JSON.parse(fs.readFileSync(path.join(__dirname, 'cards.json'), 'utf8'));
const BOTH = process.argv.includes('--both');
const OUT = process.argv.includes('--calib') ? path.join(__dirname, 'calib') : DIR;
const MIN_LINES_ALONE = 3;

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const html = (c) => `<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:transparent}
body{font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased;width:1500px}
.card{background:#fff;border-radius:48px;padding:58px 61px 48.64px;
  box-shadow:0 1px 3px rgba(15,23,42,.06),0 10px 30px rgba(15,23,42,.045)}
.head{display:flex;align-items:baseline;gap:24px}
.to{font-size:22px;font-weight:600;letter-spacing:.09em;color:#94a3b8;text-transform:uppercase}
.name{font-size:42.5px;font-weight:700;color:#0f172a;letter-spacing:-.015em;line-height:1.15}
.right{margin-left:auto;display:flex;align-items:center;gap:12px;white-space:nowrap}
.date{font-size:26px;font-weight:600;color:#64748b}
.tag{font-size:19.3px;font-weight:700;letter-spacing:.07em;border-radius:999px;padding:8.8px 15.5px}
.tag.bad{background:#fee2e2;color:#b91c1c}
.tag.good{background:#dcfce7;color:#166534}
.tag.robot{background:#e0e7ff;color:#4338ca}
.subject{font-size:29px;font-weight:700;color:#1e293b;margin-top:25px}
hr{border:0;border-top:1px solid #e9edf2;margin:26px 0 28.5px}
p{font-size:30px;line-height:45px;color:#475569;letter-spacing:-.0008em}
p+p{margin-top:23px}
</style></head><body><div class="card">
  <div class="head"><span class="to">To</span><span class="name">${esc(c.to)}</span>
    <span class="right"><span class="date">${c.date}</span>${
      c.tag ? `<span class="tag ${c.tagKind}">${esc(c.tag)}</span>` : ''}</span></div>
  <div class="subject">${esc(c.subject)}</div><hr>
  <p id="p1">${esc(c.p1)}</p><p id="p2">${esc(c.p2)}</p>
</div></body></html>`;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1500, height: 900 }, deviceScaleFactor: 2 });
  const rows = [];
  for (const c of CARDS) {
    await pg.setContent(html(c), { waitUntil: 'load' });
    await pg.evaluate(() => document.fonts.ready);
    const lines = await pg.evaluate(() => {
      const r = document.createRange();
      r.selectNodeContents(document.getElementById('p1'));
      return r.getClientRects().length;
    });
    const alone = !BOTH && lines >= MIN_LINES_ALONE;
    if (alone) await pg.evaluate(() => document.getElementById('p2').remove());
    const h = await pg.evaluate(() => Math.ceil(document.querySelector('.card').getBoundingClientRect().height));
    await pg.setViewportSize({ width: 1500, height: h });
    const file = path.join(OUT, `${c.n}-${c.slug}.png`);
    await pg.screenshot({ path: file, omitBackground: true });
    rows.push({ n: c.n, to: c.to, p1_lines: lines, absaetze: alone ? 1 : 2 });
  }
  await b.close();
  fs.writeFileSync(path.join(__dirname, BOTH ? 'measure-both.json' : 'measure.json'),
    JSON.stringify(rows, null, 1));
  console.log(rows.map(r => `${r.n} ${r.to.padEnd(26)} p1=${r.p1_lines} -> ${r.absaetze}`).join('\n'));
})();
