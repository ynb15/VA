#!/usr/bin/env python3
"""Thumbnail setzen: zwei freigestellte Koepfe, echter Hintergrund, Typo.

Erzeugt nichts. Die Koepfe sind Einzelbilder aus den Kameradateien, der
Hintergrund ist ein Einzelbild aus der Totalen derselben Aufnahme, die Schrift
ist Poppins Bold. Gebaut nach den in `video/thumbnails.md` gemessenen Werten:
1280x720, Kopf ueber die volle Bildhoehe mit angeschnittenem Scheitel, genau
ein Wort auf einem Kasten in #DF2C00, keine Kontur und kein Schlagschatten auf
der Schrift.
"""
import argparse
import json
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

BREITE, HOEHE = 1280, 720
KASTEN = (0xDF, 0x2D, 0x00)   # aus seinem Canva-File, nicht aus dem JPEG geschaetzt
ZEILENHOEHE = 1.11            # Canva lineHeight, der haeufigste Wert in seinem File
KASTEN_H = 1.01               # Kastenhoehe / Schriftgrad, Median seiner sieben Kaesten
KASTEN_PAD = 0.10             # seitliches Polster / Schriftgrad, ebenda
KASTEN_PAD_Y = 0.14           # Polster oben/unten / Schriftgrad, aus denselben
                              # fuenf Kaesten rueckgerechnet
CAP = 0.700          # Versalhoehe von Poppins in em, gemessen
HIER = os.path.dirname(os.path.abspath(__file__))
SCHRIFT = os.path.join(HIER, 'marke', 'Poppins-Bold.ttf')
YUNET = os.path.join(HIER, 'modelle', 'yunet.onnx')

# An seinen drei veroeffentlichten Zwei-Kopf-Thumbnails gemessen (frNOUgxE0IM,
# ewgUIZGJaWQ, RG-K0fIA2-w), je Mittelwert aus dreien: Augenmitte und
# YuNet-Gesichtshoehe. Danach wird hier platziert und skaliert.
ZIEL_LINKS = dict(augen_x=170, augen_y=281, box_h=508)
ZIEL_RECHTS = dict(augen_x=1109, augen_y=304, box_h=497)


def kopfmass(png):
    """Scheitel, Schulterlinie und Kopfmitte eines Freistellers messen.

    Ohne Landmark-Modell: die Maske wird von oben Zeile fuer Zeile vermessen.
    Der Kopf ist der schmale Teil; wo die Breite springt, faengt die Schulter
    an. Zurueckgegeben wird **nicht** das Kinn, sondern diese Schulterlinie —
    am Bild nachgeprueft liegt sie rund 15 % unter dem Kinn. Als Anker genuegt
    das, weil der Fehler bei allen Bildern derselbe ist; Scheitel-zu-Schulter
    ist das Mass, nach dem hier skaliert wird.
    """
    a = np.asarray(Image.open(png))[:, :, 3] > 40
    zeilen = a.sum(1)
    belegt = np.nonzero(zeilen > 6)[0]
    scheitel = int(belegt[0])
    # Kopfbreite aus dem oberen Drittel des belegten Bereichs
    probe = zeilen[scheitel:scheitel + max(40, (len(belegt)) // 6)]
    kopfbreite = float(np.median(probe[probe > 0])) if (probe > 0).any() else 1.0
    schulter = belegt[-1]
    for y in range(scheitel, int(belegt[-1])):
        if zeilen[y] > kopfbreite * 1.75:
            schulter = y
            break
    spalten = np.nonzero(a[scheitel:schulter].sum(0) > 0)[0]
    mitte = int((spalten[0] + spalten[-1]) / 2) if len(spalten) else a.shape[1] // 2
    flaeche = float(a[scheitel:schulter].sum())
    return scheitel, int(schulter), mitte, flaeche


def gesicht_messen(png):
    """Augenmitte und Gesichtshoehe eines Freistellers messen (YuNet).

    Maskenmasse wie Scheitel-zu-Schulter taugen nicht zum Skalieren: legt
    jemand den Kopf in den Nacken, springt das Mass kaum, der Kopf im Bild
    aber deutlich. YuNet liefert Augen und Gesichtsrahmen direkt. Das ist
    Erkennung auf einem echten Foto, kein Erzeugen.

    Gibt (augen_x, augen_y, box_h) im Pixelmass der Datei zurueck.
    """
    rgba = np.asarray(Image.open(png).convert('RGBA'))
    # Auf Grau legen, sonst stoert der transparente Rand die Erkennung.
    alpha = rgba[:, :, 3:4] / 255.0
    rgb = (rgba[:, :, :3] * alpha + 128 * (1 - alpha)).astype(np.uint8)
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    h, w = bgr.shape[:2]
    d = cv2.FaceDetectorYN.create(YUNET, "", (w, h), 0.6, 0.3, 5000)
    d.setInputSize((w, h))
    _, res = d.detect(bgr)
    if res is None or not len(res):
        raise RuntimeError(f'kein Gesicht erkannt: {png}')
    r = max(res, key=lambda r: r[3])          # groesster Rahmen
    augen_x = (float(r[4]) + float(r[6])) / 2
    augen_y = (float(r[5]) + float(r[7])) / 2
    return augen_x, augen_y, float(r[3])


def kopf_setzen(leinwand, png, ziel, kontrast=1.14, helligkeit=1.06):
    """ziel: dict mit augen_x, augen_y, box_h — die gemessenen Vorlagenwerte.

    Kontrast und Helligkeit leicht angehoben: in seinen Vorlagen steht das
    Gesicht hart vor dem abgesoffenen Hintergrund, das Kamerabild kommt
    flacher aus der Aufnahme. Nur die Farbkanaele, die Maske bleibt wie sie ist.
    """
    ax, ay, bh = gesicht_messen(png)
    im = Image.open(png).convert('RGBA')
    if kontrast != 1.0 or helligkeit != 1.0:
        farbe, maske = im.convert('RGB'), im.getchannel('A')
        farbe = ImageEnhance.Contrast(farbe).enhance(kontrast)
        farbe = ImageEnhance.Brightness(farbe).enhance(helligkeit)
        im = farbe.convert('RGBA')
        im.putalpha(maske)
    k = ziel['box_h'] / bh
    neu = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))),
                    Image.LANCZOS)
    x = int(round(ziel['augen_x'] - ax * k))
    y = int(round(ziel['augen_y'] - ay * k))
    leinwand.paste(neu, (x, y), neu)
    return leinwand


def hintergrund(pfad, dunkel=0.08, weich=6.0):
    im = Image.open(pfad).convert('RGB')
    k = max(BREITE / im.width, HOEHE / im.height)
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    x = (im.width - BREITE) // 2
    y = (im.height - HOEHE) // 2
    im = im.crop((x, y, x + BREITE, y + HOEHE))
    if weich:
        im = im.filter(ImageFilter.GaussianBlur(weich))
    return Image.eval(im, lambda v: int(v * dunkel)).convert('RGBA')


def _mass(zeichner, text, font):
    """Tintenmass eines Wortes: Breite, Links- und Oben-Versatz."""
    l, t, r, b = zeichner.textbbox((0, 0), text, font=font)
    return r - l, l, t


def satz(bild, zeilen, kasten, mitte_x=640, mitte_y=360,
         max_breite=760, max_hoehe=470, grad=None):
    """Alle Zeilen in EINEM Schriftgrad und EINEM Zeilenabstand setzen.

    So macht er es selbst: in seinem Canva-File hat ein Textblock genau einen
    `fontSize` und genau einen `lineHeight` (meist 1.11), `textAlign: center`.
    Ein frueherer Entwurf hier gab jeder Zeile eine eigene Versalhoehe — damit
    wird der Zeilenabstand ungleich und der Block franst aus.

    Der Block wird auf `mitte_y` zentriert. Der Grad wird, wenn nicht gesetzt,
    so gross gewaehlt wie Breite und Hoehe es zulassen.

    `kasten` ist entweder der Index der Zeile, die ganz auf den Kasten kommt,
    oder ein Paar `[index, "teilwort"]` — dann liegt der Kasten nur hinter
    diesem Teil der Zeile. Das braucht man fuer „Human **Extinction**?", wo
    das Fragezeichen neben dem Kasten stehen soll. In seinem Canva-File gibt
    es beides: „Coincidence?" liegt ganz auf dem Kasten, bei „Did I REALLY /
    Make It Up?" nur das Wort REALLY.
    """
    if isinstance(kasten, (list, tuple)):
        kasten_index, kasten_teil = kasten[0], kasten[1]
    else:
        kasten_index, kasten_teil = kasten, None
    d = ImageDraw.Draw(bild)

    def passt(g):
        f = ImageFont.truetype(SCHRIFT, g)
        breit = max(_mass(d, t, f)[0] for t in zeilen)
        hoch = (len(zeilen) - 1) * g * ZEILENHOEHE + g * CAP
        return breit <= max_breite and hoch <= max_hoehe

    if grad is None:
        grad = 60
        while grad < 175 and passt(grad + 1):
            grad += 1

    f = ImageFont.truetype(SCHRIFT, grad)
    cap = grad * CAP
    schritt = grad * ZEILENHOEHE
    block = (len(zeilen) - 1) * schritt + cap
    y = mitte_y - block / 2                      # Oberkante der ersten Versalhöhe

    for i, text in enumerate(zeilen):
        breit, lx, ty = _mass(d, text, f)
        x = mitte_x - breit / 2
        oben = y + i * schritt
        if i == kasten_index:
            # Der Kasten sitzt auf dem Tintenband des Wortes: Oberkante der
            # Tinte bis Grundlinie, rundum gleich viel Luft. Nicht bis zur
            # Unterlaenge — in seinen Thumbnails haengt die heraus, siehe das
            # y von „Patriarchy" in frNOUgxE0IM.
            ursprung_y = oben - ty
            grundlinie = ursprung_y + f.getmetrics()[0]
            kp = grad * KASTEN_PAD
            kpy = grad * KASTEN_PAD_Y
            if kasten_teil:
                # Tintenmass, nicht Vorschubmass. `textlength` gibt die
                # Vorschubbreite inklusive Seitenabstand; nimmt man die, steht
                # rechts mehr Luft als links und der Kasten sitzt schief.
                stelle = text.index(kasten_teil)
                vor = d.textlength(text[:stelle], font=f)
                tl, tt, tr, _ = d.textbbox((0, 0), kasten_teil, font=f)
                ursprung_x = x - lx + vor
                kx0, kx1 = ursprung_x + tl, ursprung_x + tr
                ky0 = ursprung_y + tt
            else:
                kx0, kx1 = x, x + breit
                ky0 = oben
            d.rectangle([kx0 - kp, ky0 - kpy, kx1 + kp, grundlinie + kpy],
                        fill=KASTEN)
        d.text((x - lx, oben - ty), text, font=f, fill=(255, 255, 255))
    return bild, grad


def bauen(hg, links, rechts, zeilen, kasten, ziel, text_mitte=640,
          text_mitte_y=360, max_breite=760, max_hoehe=470, grad=None,
          hg_dunkel=0.08, hg_weich=6.0, ziel_links=None, ziel_rechts=None):
    """zeilen: Liste von Texten · kasten: Zeilenindex, oder [index, "teil"]."""
    bild = hintergrund(hg, dunkel=hg_dunkel, weich=hg_weich)
    if links:
        kopf_setzen(bild, links, ziel_links or ZIEL_LINKS)
    if rechts:
        kopf_setzen(bild, rechts, ziel_rechts or ZIEL_RECHTS)
    _, grad = satz(bild, zeilen, kasten, text_mitte, text_mitte_y,
                   max_breite, max_hoehe, grad)
    bild.convert('RGB').save(ziel, quality=95)
    return ziel, grad


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--plan', required=True, help='JSON mit den Fassungen')
    a = p.parse_args()
    with open(a.plan) as fh:
        plan = json.load(fh)
    for f in plan:
        pfad, grad = bauen(**f)
        print(f'{pfad}  (Schriftgrad {grad})')
