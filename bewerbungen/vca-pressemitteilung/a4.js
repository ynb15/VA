const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file:///home/user/VA/bewerbungen/vca-pressemitteilung/index.html', {waitUntil:'networkidle'});
  await p.emulateMedia({ media: 'print' });
  await p.pdf({
    path: '/home/user/VA/bewerbungen/vca-pressemitteilung/VcA-Bewerbung-YNB.pdf',
    format: 'A4', printBackground: true,
    margin: { top:'16mm', bottom:'14mm', left:'18mm', right:'18mm' }
  });
  await b.close(); console.log('pdf ok');
})();
