#!/usr/bin/env python3
"""Ein YouTube-Video als Kontaktabzug sehen, ohne es zu laden.

YouTube liefert zu jedem Video einen Vorschaustreifen (storyboard): ein
Gitter kleiner Einzelbilder ueber die volle Laufzeit, auf i.ytimg.com und
ohne Anmeldung erreichbar - anders als die Mediendaten selbst.

Damit laesst sich messen, was sonst nur durch Ansehen zu klaeren waere:
wie oft ein Video das Bild wechselt, und ob es lange Einstellungen hat
oder im Sekundentakt schneidet.

Wiederaufnehmbar: was schon geholt ist, wird nicht noch einmal geholt.
Der Container wird zwischen den Zuegen eingesammelt.

    python3 video/vorschaustreifen.py <id> [<id> ...] --out ordner
    python3 video/vorschaustreifen.py --liste datei.txt --out ordner
"""
import argparse, json, os, subprocess, sys, time, urllib.request

def meta(vid, ordner):
    p = os.path.join(ordner, f'{vid}.meta.json')
    if os.path.exists(p):
        try: return json.load(open(p))
        except Exception: pass
    # Die Bot-Pruefung greift je nach Player-Zugang: android_vr kommt am
    # 21.10. durch, visionos/tv/web_safari/web_embedded/mweb nicht.
    #
    # Sie weist trotzdem zwischendurch ab, und zwar mengenabhaengig, nicht
    # videoabhaengig - sie loest sich erst nach Minuten wieder. Lange
    # Wartepausen an dieser Stelle verbrauchen also nur die Frist, ohne die
    # Lage zu aendern. Deshalb kurze Kette und schnell aufgeben: der naechste
    # Aufruf holt den Rest, die Datei merkt sich den Stand.
    d = None
    for versuch, zugang in enumerate(['android_vr', 'android_vr', 'visionos']):
        r = subprocess.run([sys.executable, '-m', 'yt_dlp', '-J', '--skip-download',
                            '--extractor-args', f'youtube:player_client={zugang}',
                            f'https://www.youtube.com/watch?v={vid}'],
                           capture_output=True, text=True, timeout=240)
        if r.returncode == 0 and len(r.stdout) > 200:
            try:
                d = json.loads(r.stdout); break
            except Exception: pass
        time.sleep(8 * (versuch + 1))
    if d is None: return None
    sb = [f for f in d.get('formats', []) if str(f.get('format_id','')).startswith('sb')]
    sb.sort(key=lambda f: -(f.get('width') or 0))
    if not sb: return None
    f = sb[0]
    kurz = dict(id=vid, titel=d.get('title'), kanal=d.get('channel'),
                dauer=d.get('duration'), breite=f.get('width'), hoehe=f.get('height'),
                zeilen=f.get('rows'), spalten=f.get('columns'),
                teile=[x['url'] for x in (f.get('fragments') or [])])
    json.dump(kurz, open(p, 'w'))
    return kurz

def hole(m, ordner):
    """Die Gitterbilder laden. Gibt die lokalen Pfade zurueck."""
    pfade = []
    for i, url in enumerate(m['teile']):
        p = os.path.join(ordner, f"{m['id']}.sb{i:03d}.jpg")
        if not os.path.exists(p) or os.path.getsize(p) < 500:
            try:
                with urllib.request.urlopen(url, timeout=60) as r, open(p, 'wb') as f:
                    f.write(r.read())
            except Exception as e:
                print(f"  teil {i} nicht geholt: {e}", file=sys.stderr); continue
        pfade.append(p)
    return pfade

def kacheln(m, pfade):
    """Die Gitter in Einzelbilder zerlegen, in zeitlicher Reihenfolge."""
    from PIL import Image
    aus = []
    for p in pfade:
        g = Image.open(p).convert('RGB')
        bw, bh = m['breite'], m['hoehe']
        sp = max(1, g.size[0] // bw); ze = max(1, g.size[1] // bh)
        for r in range(ze):
            for c in range(sp):
                k = g.crop((c*bw, r*bh, (c+1)*bw, (r+1)*bh))
                if k.size[0] < 8 or k.size[1] < 8: continue
                aus.append(k)
    return aus

def messen(ks, dauer, schwelle=14.0):
    """Wie oft wechselt das Bild, und wie lang stehen die Strecken?

    Der Abstand zwischen zwei Kacheln ist die Aufloesung dieser Messung -
    kuerzere Einstellungen als ein Kachelabstand sind nicht zu sehen.
    Was sie beantwortet: schneidet das Video schnell oder langsam.
    """
    import numpy as np
    if len(ks) < 2: return None
    takt = dauer / len(ks)
    a = [np.asarray(k.convert('L'), float) for k in ks]
    d = [float(np.abs(a[i]-a[i-1]).mean()) for i in range(1, len(a))]
    wechsel = [i for i, x in enumerate(d) if x > schwelle]
    strecken, letzt = [], 0
    for i in wechsel:
        strecken.append((i+1-letzt)*takt); letzt = i+1
    strecken.append((len(ks)-letzt)*takt)
    strecken.sort()
    med = strecken[len(strecken)//2]
    return dict(kacheln=len(ks), takt=round(takt,2), wechsel=len(wechsel),
                wechsel_je_min=round(len(wechsel)/(dauer/60),1),
                strecke_median=round(med,1),
                strecke_max=round(strecken[-1],1),
                anteil_ueber_3s=round(sum(1 for s in strecken if s >= 3.0)/len(strecken),2),
                strecken=len(strecken))

def blatt(m, ks, ordner, spalten=20, hoch=3):
    from PIL import Image, ImageDraw
    if not ks: return None
    bw, bh = ks[0].size
    z = (len(ks)+spalten-1)//spalten
    b = Image.new('RGB', (spalten*bw*hoch, z*bh*hoch), (12,12,12))
    d = ImageDraw.Draw(b)
    takt = m['dauer']/len(ks)
    for i, k in enumerate(ks):
        x, y = (i % spalten)*bw*hoch, (i//spalten)*bh*hoch
        b.paste(k.resize((bw*hoch, bh*hoch)), (x, y))
        d.text((x+3, y+3), f'{int(i*takt)}', fill=(255,255,0))
    p = os.path.join(ordner, f"{m['id']}.blatt.png")
    b.save(p)
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ids', nargs='*')
    ap.add_argument('--liste')
    ap.add_argument('--out', default='vorschau')
    ap.add_argument('--schwelle', type=float, default=14.0)
    ap.add_argument('--kein-blatt', action='store_true')
    ap.add_argument('--pause', type=float, default=20.0,
                    help='Pause zwischen zwei Videos. Die Bot-Pruefung greift '
                         'mengenabhaengig, nicht pro Video.')
    ap.add_argument('--frist', type=float, default=0,
                    help='Nach so vielen Sekunden geordnet aufhoeren. Der Rest '
                         'wird beim naechsten Aufruf geholt.')
    a = ap.parse_args()
    ids = list(a.ids)
    if a.liste:
        ids += [z.split('#')[0].strip() for z in open(a.liste) if z.split('#')[0].strip()]
    os.makedirs(a.out, exist_ok=True)
    ergebnis = os.path.join(a.out, 'messung.json')

    def lies():
        try: return json.load(open(ergebnis))
        except Exception: return {}

    def merke(vid, eintrag):
        # Frisch einlesen und nur den eigenen Eintrag setzen: laeuft ein
        # zweiter Durchgang parallel, haette ein Schreiben aus dem Stand
        # vom Start dessen Ergebnisse geloescht. Genau das ist am 21.10.
        # passiert - ein fertig gemessenes Video stand hinterher wieder
        # als offen in der Datei.
        d = lies(); d[vid] = eintrag
        json.dump(d, open(ergebnis, 'w'), indent=1, ensure_ascii=False)

    alle = lies()
    start = time.time()
    for vid in ids:
        if a.frist and time.time() - start > a.frist:
            print('Frist erreicht, Rest beim naechsten Aufruf.'); break
        alle = lies()
        if vid in alle and alle[vid].get('fertig') and not alle[vid].get('fehler'):
            print(f'{vid} schon gemessen'); continue
        m = meta(vid, a.out)
        if not m:
            # Nicht als fertig abhaken: beim naechsten Aufruf erneut versuchen.
            merke(vid, dict(fertig=False, fehler='abgewiesen'))
            print(f'{vid} abgewiesen, kommt beim naechsten Aufruf dran', flush=True)
            time.sleep(a.pause); continue
        ks = kacheln(m, hole(m, a.out))
        r = messen(ks, m['dauer'] or 1, a.schwelle) or {}
        p = None if a.kein_blatt else blatt(m, ks, a.out)
        merke(vid, dict(fertig=True, titel=m['titel'], kanal=m['kanal'],
                        dauer=m['dauer'], blatt=p, **r))
        print(f"{vid} {m['dauer']}s  {r.get('wechsel')} Wechsel  "
              f"Median {r.get('strecke_median')}s  {m['titel'][:48]}", flush=True)
        time.sleep(a.pause)

if __name__ == '__main__':
    main()
