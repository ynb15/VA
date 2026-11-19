#!/bin/bash
# Pressemitteilung -> A4-PDF (3 Seiten) + Lebenslauf als randlose 4. Seite + PNGs
set -e
D=/home/user/VA/bewerbungen/vca-pressemitteilung
S=/tmp/claude-0/-home-user-VA/b4c58509-d98d-5c79-b820-5dca1272ba15/scratchpad
cd "$D"
node "$S/a4.js"                                   # index.html -> release.pdf
python3 -I -c "
from PIL import Image
im=Image.open('$D/bilder/lebenslauf.jpg').convert('RGB').resize((1654,2339),Image.LANCZOS)
im.save('$S/cv.pdf','PDF',resolution=200.0)"
mv VcA-Bewerbung-YNB.pdf "$S/release.pdf"
pdfunite "$S/release.pdf" "$S/cv.pdf" VcA-Bewerbung-YNB.pdf
rm -f a4-seite*.png
pdftoppm -png -r 200 VcA-Bewerbung-YNB.pdf a4-seite
ls a4-seite*.png
