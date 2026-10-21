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

# Mit einer Grafik in der Mitte ruecken die Koepfe nach aussen und werden
# kleiner, sonst bleibt kein Platz. Werte aus den drei DOAC-Vorlagen, die er
# am 20.10. als Beispiel geschickt hat, mit demselben Detektor gemessen.
ZIEL_LINKS_MITTE = dict(augen_x=167, augen_y=293, box_h=459)
ZIEL_RECHTS_MITTE = dict(augen_x=1128, augen_y=316, box_h=426)
# Das Mittelfeld bei DOAC: x 300-960, bis zur Unterkante durchlaufend, und
# die Schrift sitzt darueber statt mittig.
MITTE_FELD = dict(x0=300, x1=960, oben=230, unten=720)
TEXT_Y_MITTE = 140


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


def gesicht_messen(png, mit_unterkante=False):
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
    if mit_unterkante:
        # Unterkante des Gesichtsrahmens, als Kinnlinie benutzbar
        return augen_x, augen_y, float(r[3]), float(r[1]) + float(r[3])
    return augen_x, augen_y, float(r[3])


def kopf_setzen(leinwand, png, ziel, kontrast=1.14, helligkeit=1.06,
                spiegeln=False):
    """ziel: dict mit augen_x, box_h und entweder augen_y oder scheitel_y.

    **`scheitel_y` ist meist das richtige Mass.** Zwei Koepfe auf dieselbe
    Gesichtsrahmenhoehe zu bringen heisst nicht, dass sie gleich im Bild
    sitzen: der Abstand Scheitel-zu-Auge haengt von Kopfhaltung und Abstand
    zur Kamera ab. Bei gleicher Rahmenhoehe lag Yannicks Scheitel bei y = 11
    und Aaronsons bei y = 71. Mit `scheitel_y` wird die Oberkante gesetzt und
    die Augenhoehe daraus gerechnet — die Koepfe werden oben gleich
    angeschnitten, ohne dass einer groesser gezogen werden muss.

    Kontrast und Helligkeit leicht angehoben: in seinen Vorlagen steht das
    Gesicht hart vor dem abgesoffenen Hintergrund, das Kamerabild kommt
    flacher aus der Aufnahme. Nur die Farbkanaele, die Maske bleibt wie sie ist.
    """
    if spiegeln:
        # Beide Kameras koennen denselben Blickwinkel zeigen; dann muss einer
        # gespiegelt werden, damit sie sich anschauen. Die Messung laeuft auf
        # dem gespiegelten Bild, sonst sitzt die Augenposition seitenverkehrt.
        gespiegelt = Image.open(png).convert('RGBA').transpose(
            Image.FLIP_LEFT_RIGHT)
        png = png.rsplit('.', 1)[0] + '__gespiegelt.png'
        gespiegelt.save(png)
    ax, ay, bh, by = gesicht_messen(png, mit_unterkante=True)
    k_vor = ziel['box_h'] / bh
    if 'kinn_y' in ziel:
        # Kinnlinie als Anker. Scheitel-zu-Kinn ist bei zwei Menschen
        # verschieden; wer beide oben buendig setzt, bekommt unten
        # verschiedene Kinnhoehen. Fuer A/B-Tests muessen die Elemente
        # gleich sitzen, also wird unten gebuendigt.
        ziel = dict(ziel, augen_y=ziel['kinn_y'] - (by - ay) * k_vor)
    elif 'scheitel_y' in ziel:
        al = np.asarray(Image.open(png))[:, :, 3] > 40
        oben = int(np.nonzero(al.sum(1) > 6)[0][0])
        ziel = dict(ziel, augen_y=ziel['scheitel_y'] + (ay - oben) * k_vor)
    im = Image.open(png).convert('RGBA')
    # Je Kopf einstellbar: die beiden Kameras belichten verschieden, und ein
    # ueberbelichtetes Gesicht neben einem dunklen faellt sofort auf.
    kontrast = ziel.get('kontrast', kontrast)
    helligkeit = ziel.get('helligkeit', helligkeit)
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


def karte(pfad, breite, kippung=4.0, rand=14, schatten=(12, 16, 22, 150),
          dunkel=1.0):
    """Ein echtes Foto als gekippte Karte mit hellem Rand und Schlagschatten.

    Das Mittel, das in drei seiner sechs veroeffentlichten Thumbnails steht
    (`-0NES3TOiIg`, `GxpvzT3rUBQ`, `f79ehF4zP3I`) und das im Bauplan bisher
    nur beschrieben war. Rand und Kippung sind abgelesen, nicht pixelgenau
    gemessen — beides laesst sich im Plan ueberschreiben.

    schatten: (versatz_x, versatz_y, weichzeichnung, deckkraft)
    """
    im = Image.open(pfad).convert('RGB')
    if dunkel != 1.0:
        im = Image.eval(im, lambda v: int(min(255, v * dunkel)))
    k = breite / im.width
    im = im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    mit_rand = Image.new('RGB', (im.width + 2 * rand, im.height + 2 * rand),
                         (242, 241, 235))
    mit_rand.paste(im, (rand, rand))

    vx, vy, weich, deck = schatten
    rahmen = Image.new('RGBA', (mit_rand.width + 2 * (abs(vx) + weich * 2),
                                mit_rand.height + 2 * (abs(vy) + weich * 2)),
                       (0, 0, 0, 0))
    mx = (rahmen.width - mit_rand.width) // 2
    my = (rahmen.height - mit_rand.height) // 2

    schlag = Image.new('RGBA', rahmen.size, (0, 0, 0, 0))
    ImageDraw.Draw(schlag).rectangle(
        [mx + vx, my + vy, mx + vx + mit_rand.width, my + vy + mit_rand.height],
        fill=(0, 0, 0, deck))
    schlag = schlag.filter(ImageFilter.GaussianBlur(weich))
    rahmen = Image.alpha_composite(rahmen, schlag)
    rahmen.paste(mit_rand, (mx, my))
    return rahmen.rotate(kippung, resample=Image.BICUBIC, expand=True)


def logo_setzen(bild, maske_pfad, mitte_xy, groesse, farbe=(0xF0, 0x48, 0x60),
                schein=2.1):
    """Ein Logo als Maske einfaerben, mit Neon-Schein hinterlegen und setzen.

    `maske_pfad` ist ein Graustufenbild: hell = Logo. So liegt die Marke als
    Form vor und wird hier frisch gefaerbt, statt ein fremdes Rendering zu
    uebernehmen. `schein` ist der Radius des Scheins in Vielfachen von einem
    Zwanzigstel der Logogroesse; 0 schaltet ihn ab.
    """
    m = Image.open(maske_pfad).convert('L')
    k = groesse / max(m.size)
    m = m.resize((max(1, int(m.width * k)), max(1, int(m.height * k))),
                 Image.LANCZOS)
    cx, cy = mitte_xy
    x0, y0 = int(cx - m.width / 2), int(cy - m.height / 2)

    if schein:
        rand = int(groesse * 0.5)
        gross = Image.new('L', (m.width + 2 * rand, m.height + 2 * rand), 0)
        gross.paste(m, (rand, rand))
        for r, deck in ((groesse * 0.22 * schein, 0.70),
                        (groesse * 0.09 * schein, 0.95),
                        (groesse * 0.03 * schein, 1.0)):
            weich = gross.filter(ImageFilter.GaussianBlur(r))
            weich = Image.eval(weich, lambda v: int(v * deck))
            schicht = Image.new('RGBA', gross.size, farbe + (0,))
            schicht.putalpha(weich)
            bild.alpha_composite(schicht, dest=(max(0, x0 - rand),
                                                max(0, y0 - rand)))

    kern = Image.new('RGBA', m.size, farbe + (0,))
    kern.putalpha(m)
    bild.alpha_composite(kern, dest=(max(0, x0), max(0, y0)))
    return bild


def pfeil(bild, von, nach, bogen=0.28, dicke=18, farbe=(255, 255, 255),
          kopf=3.1, gezeichnet=True, schwung=0.30):
    """Ein gebogener Pfeil von `von` nach `nach`.

    `bogen` ist die Auslenkung quer zur Verbindungslinie, als Anteil ihrer
    Laenge; positiv biegt nach unten. `kopf` ist die Spitzenlaenge in
    Vielfachen der Strichdicke.

    `gezeichnet` gibt dem Strich einen Handschrift-Zug: er laeuft am Anfang
    duenn aus und wird zur Spitze hin voll, dazu ein leichtes Schlenkern quer
    zur Linie (`schwung`, in Vielfachen der Dicke). Ohne das sieht der Pfeil
    nach Zeichenprogramm aus, nicht nach Hand.
    """
    import math
    (x0, y0), (x1, y1) = von, nach
    dx, dy = x1 - x0, y1 - y0
    laenge = max(1.0, (dx * dx + dy * dy) ** 0.5)
    sx = (x0 + x1) / 2 - dy / laenge * bogen * laenge
    sy = (y0 + y1) / 2 + dx / laenge * bogen * laenge

    def punkt(t):
        u = 1 - t
        return (u * u * x0 + 2 * u * t * sx + t * t * x1,
                u * u * y0 + 2 * u * t * sy + t * t * y1)

    ende = max(0.05, min(0.98, 1.0 - (kopf * dicke) / laenge * 0.70))
    d = ImageDraw.Draw(bild)
    n = 240
    for i in range(n + 1):
        t = ende * i / n
        px, py = punkt(t)
        if gezeichnet:
            # Tangente fuer das Querschlenkern
            ax, ay = punkt(max(0.0, t - 0.01))
            bx, by = punkt(min(1.0, t + 0.01))
            tx, ty = bx - ax, by - ay
            tl = max(1e-6, (tx * tx + ty * ty) ** 0.5)
            nx, ny = -ty / tl, tx / tl
            v = math.sin(t * math.pi * 1.7 + 0.6) * schwung * dicke
            px, py = px + nx * v, py + ny * v
            r = dicke / 2 * (0.40 + 0.60 * (t / max(ende, 1e-6)) ** 0.7)
        else:
            r = dicke / 2
        d.ellipse([px - r, py - r, px + r, py + r], fill=farbe + (255,))

    ax, ay = punkt(ende)
    bx, by = punkt(min(1.0, ende + 0.02))
    tx, ty = bx - ax, by - ay
    tl = max(1e-6, (tx * tx + ty * ty) ** 0.5)
    tx, ty = tx / tl, ty / tl
    nx, ny = -ty, tx
    lang = kopf * dicke
    breit = kopf * dicke * (0.52 if gezeichnet else 0.62)
    d.polygon([(x1, y1),
               (x1 - tx * lang + nx * breit, y1 - ty * lang + ny * breit),
               (x1 - tx * lang * 0.82 - nx * breit, y1 - ty * lang * 0.82
                - ny * breit)],
              fill=farbe + (255,))
    return bild


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
         max_breite=760, max_hoehe=470, grad=None, zeilenhoehe=None):
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
    if zeilenhoehe is None:
        zeilenhoehe = ZEILENHOEHE
    d = ImageDraw.Draw(bild)

    def passt(g):
        f = ImageFont.truetype(SCHRIFT, g)
        breit = max(_mass(d, t, f)[0] for t in zeilen)
        hoch = (len(zeilen) - 1) * g * zeilenhoehe + g * CAP
        return breit <= max_breite and hoch <= max_hoehe

    if grad is None:
        grad = 60
        while grad < 175 and passt(grad + 1):
            grad += 1

    f = ImageFont.truetype(SCHRIFT, grad)
    cap = grad * CAP
    schritt = grad * zeilenhoehe
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
          text_mitte_y=None, max_breite=None, max_hoehe=None, grad=None,
          hg_dunkel=0.08, hg_weich=6.0, ziel_links=None, ziel_rechts=None,
          mitte=None, mitte_kippung=4.0, mitte_rand=14, mitte_breite=None,
          mitte_unten=700, mitte_dunkel=0.82, mitte_karte=True,
          mitte_weich_rand=70, logo=None, logo_xy=(528, 370), logo_groesse=128,
          logo_farbe=(0xF0, 0x48, 0x60), logo_oben=True, pfeil_von=None,
          pfeil_nach=None, pfeil_bogen=0.28, pfeil_dicke=18,
          pfeil_farbe=(0xDF, 0x2D, 0x00), pfeil_gezeichnet=True,
          pfeil_kopf=3.1, links_spiegeln=False, rechts_spiegeln=False,
          zeilenhoehe=None):
    """zeilen: Liste von Texten · kasten: Zeilenindex, oder [index, "teil"].

    `mitte` ist ein echtes Foto fuer die Bildmitte. Liegt eines vor, ruecken
    die Koepfe nach aussen und die Schrift nach oben — nach den Werten, die an
    seinen DOAC-Vorlagen gemessen sind.
    """
    mit_mitte = mitte is not None
    if text_mitte_y is None:
        text_mitte_y = TEXT_Y_MITTE if mit_mitte else 360
    if max_breite is None:
        max_breite = 720 if mit_mitte else 760
    if max_hoehe is None:
        max_hoehe = 265 if mit_mitte else 470

    bild = hintergrund(hg, dunkel=hg_dunkel, weich=hg_weich)

    if mit_mitte:
        feld_b = MITTE_FELD['x1'] - MITTE_FELD['x0']
        if mitte_karte:
            k = karte(mitte, mitte_breite or int(feld_b * 0.70),
                      kippung=mitte_kippung, rand=mitte_rand,
                      dunkel=mitte_dunkel)
            bild.paste(k, (640 - k.width // 2, mitte_unten - k.height), k)
        else:
            # Randlos wie bei DOAC: das Bild laeuft bis zur Unterkante und
            # verliert sich seitlich im Schwarz, damit keine Kante steht.
            br = mitte_breite or feld_b
            im = Image.open(mitte).convert('RGB')
            kk = br / im.width
            im = im.resize((br, int(im.height * kk)), Image.LANCZOS)
            if mitte_dunkel != 1.0:
                im = Image.eval(im, lambda v: int(min(255, v * mitte_dunkel)))
            maske = Image.new('L', im.size, 0)
            ImageDraw.Draw(maske).rectangle(
                [mitte_weich_rand, 0,
                 im.width - mitte_weich_rand, im.height], fill=255)
            maske = maske.filter(ImageFilter.GaussianBlur(mitte_weich_rand / 2))
            im = im.convert('RGBA')
            im.putalpha(maske)
            y = mitte_unten - im.height
            bild.alpha_composite(im, dest=(max(0, 640 - im.width // 2),
                                           max(0, y)))

    if logo and not logo_oben:
        logo_setzen(bild, logo, logo_xy, logo_groesse, logo_farbe)

    if links:
        kopf_setzen(bild, links,
                    ziel_links or (ZIEL_LINKS_MITTE if mit_mitte else ZIEL_LINKS),
                    spiegeln=links_spiegeln)
    if rechts:
        kopf_setzen(bild, rechts,
                    ziel_rechts or (ZIEL_RECHTS_MITTE if mit_mitte else ZIEL_RECHTS),
                    spiegeln=rechts_spiegeln)
    if logo and logo_oben:
        # Auf die Koepfe geworfen, nicht dahinter: wer „ein Logo auf ihn
        # werfen" sagt, meint davor.
        logo_setzen(bild, logo, logo_xy, logo_groesse, logo_farbe)

    _, grad = satz(bild, zeilen, kasten, text_mitte, text_mitte_y,
                   max_breite, max_hoehe, grad, zeilenhoehe)

    if pfeil_von and pfeil_nach:
        pfeil(bild, tuple(pfeil_von), tuple(pfeil_nach), pfeil_bogen,
              pfeil_dicke, tuple(pfeil_farbe), pfeil_kopf, pfeil_gezeichnet)
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
