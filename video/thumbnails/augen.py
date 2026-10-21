"""Augenweite messen: sichtbares Weiss im Auge, auf Augenabstand normiert.

Bei Schreck und Ueberraschung steht das Lid offen und es ist viel Sklera zu
sehen; beim Lachen und Laecheln verengt sich das Auge. Gemessen wird ein
kleines Fenster um jeden Augenpunkt von YuNet: helle, farbarme Pixel.
Gruenliche Pixel fliegen raus, sonst zaehlen die Spiegelungen der Pflanzen in
seiner Brille mit.

Das ist ein Hilfsmass zum Vorsortieren, keine Entscheidung. Angeschaut wird
trotzdem.
"""
import cv2, numpy as np
import os
MODELL = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'modelle', 'yunet.onnx')
_D = {}


def _det(w, h):
    if (w, h) not in _D:
        _D[(w, h)] = cv2.FaceDetectorYN.create(MODELL, "", (w, h), 0.55, 0.3, 5000)
    d = _D[(w, h)]
    d.setInputSize((w, h))
    return d


def messen(pfad_oder_bgr):
    bgr = cv2.imread(pfad_oder_bgr, cv2.IMREAD_COLOR) if isinstance(pfad_oder_bgr, str) else pfad_oder_bgr
    h, w = bgr.shape[:2]
    _, res = _det(w, h).detect(bgr)
    if res is None or not len(res):
        return None
    # Nach Sicherheit waehlen, nicht nach Groesse. In der Ken-Stern-Aufnahme
    # meldete YuNet im selben Bild einen Rahmen von 574 px Hoehe — das war
    # das Mikrofon vor dem hellen Hemd, und weil es groesser war als das
    # Gesicht, gewann es. Gleicher Fehler wie der 109-px-"Kopf" in der
    # DJI-Datei, der eine Hand war.
    r = max(res, key=lambda r: r[-1])
    if float(r[-1]) < 0.80:
        return None
    ar, al = (float(r[4]), float(r[5])), (float(r[6]), float(r[7]))
    pd = ((ar[0] - al[0]) ** 2 + (ar[1] - al[1]) ** 2) ** 0.5
    if pd < 20:
        return None
    rad = int(round(pd * 0.34))
    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
    weiss = 0
    for (ex, ey) in (ar, al):
        x0, x1 = max(0, int(ex) - rad), min(w, int(ex) + rad)
        y0, y1 = max(0, int(ey) - rad), min(h, int(ey) + rad)
        if x1 <= x0 or y1 <= y0:
            continue
        f = hsv[y0:y1, x0:x1]
        H, S, V = f[:, :, 0].astype(int), f[:, :, 1].astype(int), f[:, :, 2].astype(int)
        gruen = (H > 35) & (H < 95) & (S > 60)
        weiss += int((((V > 140) & (S < 70)) & ~gruen).sum())
    # Mundoeffnung: Abstand der Mundwinkel zur Nase, grob
    nase = (float(r[8]), float(r[9]))
    mr, ml = (float(r[10]), float(r[11])), (float(r[12]), float(r[13]))
    mund_y = (mr[1] + ml[1]) / 2
    return dict(weiss=weiss / (pd * pd), pd=pd, box_h=float(r[3]),
                mund=(mund_y - nase[1]) / pd, sicher=float(r[-1]),
                augen_x=(ar[0] + al[0]) / 2, augen_y=(ar[1] + al[1]) / 2)
