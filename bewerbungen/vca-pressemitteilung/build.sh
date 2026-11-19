#!/bin/bash
# Pressemitteilung -> A4-PDF (3 Seiten) + Lebenslauf als randlose 4. Seite + PNGs
set -e
D=/home/user/VA/bewerbungen/vca-pressemitteilung
S=/tmp/claude-0/-home-user-VA/b4c58509-d98d-5c79-b820-5dca1272ba15/scratchpad
cd "$D"
node "$D/a4.js"                                   # index.html -> release.pdf
mv VcA-Bewerbung-YNB.pdf "$S/release.pdf"
# Lebenslauf als Original-PDF anhaengen: Links und Text bleiben erhalten
pdfunite "$S/release.pdf" "$D/bilder/lebenslauf.pdf" VcA-Bewerbung-YNB.pdf
rm -f a4-seite*.png
pdftoppm -png -r 200 VcA-Bewerbung-YNB.pdf a4-seite
ls a4-seite*.png
