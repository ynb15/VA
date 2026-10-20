"""Alle Bilder eines Ordners nach Augenweite sortieren und als Bogen zeigen."""
import sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from augen import messen
from PIL import Image, ImageDraw

AUS = {'y': (230, 70, 830, 670), 'a': (760, 170, 1450, 860)}

def rang(ordner, wer, top=24, ziel=None, sp=6, k=320):
    werte = []
    for f in sorted(glob.glob(f'{ordner}/*.jpg')):
        m = messen(f)
        if m and m['pd'] > 55:
            werte.append((m['weiss'], f, m))
    werte.sort(reverse=True, key=lambda t: t[0])
    beste = werte[:top]
    if ziel:
        ze = (len(beste) + sp - 1) // sp
        bl = Image.new('RGB', (sp*k, ze*(k+18)), (18,18,18)); d = ImageDraw.Draw(bl)
        for i, (w, f, m) in enumerate(beste):
            im = Image.open(f).crop(AUS[wer]).resize((k,k), Image.LANCZOS)
            cx, cy = (i%sp)*k, (i//sp)*(k+18)
            bl.paste(im, (cx, cy+18))
            d.text((cx+4, cy+3), f'{os.path.basename(f)[:-4]}  {w:.3f}', fill=(245,245,245))
        bl.save(ziel, quality=92)
    return beste

if __name__ == '__main__':
    ordner, wer, ziel = sys.argv[1], sys.argv[2], sys.argv[3]
    top = int(sys.argv[4]) if len(sys.argv) > 4 else 24
    b = rang(ordner, wer, top, ziel)
    print(f'{ziel}: {len(b)} von {len(glob.glob(ordner+"/*.jpg"))}')
    for w, f, m in b[:12]:
        print('  %-14s weiss=%.4f mund=%.3f' % (os.path.basename(f)[:-4], w, m['mund']))
