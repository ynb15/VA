#!/usr/bin/env python3
"""Rueckkatalog-Shorts im Stapel bauen — wiederaufnehmbar.

Der Container wird zwischen den Zuegen eingesammelt, und ein Lauf ueber
sieben Shorts dauert laenger als ein Zug. Deshalb entscheidet der
Dateistand, wo es weitergeht: jede Stufe prueft erst, ob ihr Ergebnis
schon daliegt.

    python3 video/rueckkatalog_batch.py --out ordner [--nur schluessel]
                                        [--frist 900]

Stufen je Short:
  1 roh.mp4        Fenster aus dem Drive-Master (nur die noetigen Bloecke)
  2 roh.json       Transkript des Fensters
  3 lage.json      wo die gesuchte Stelle im Fenster wirklich liegt
  4 plan.json      Bildausschnitt
  5 <name>.mp4     der fertige Short
  6 roh.mp4 weg    Platz freigeben, das Fenster wird nicht mehr gebraucht

Warum Stufe 2 und 3: die Zeiten der Auswahl stehen in der *veroeffentlichten*
Fassung, geschnitten wird im *Master*. Dazwischen liegt kein fester Versatz —
die Veroeffentlichung traegt Material, das im Master nicht vorkommt (der
Kaltstart am Anfang). Die Schaetzung unten ist deshalb nur der Startpunkt;
die genaue Lage wird im Fenster **gesucht**, nicht gerechnet.
"""
import argparse, json, os, subprocess, sys, time

HIER = os.path.dirname(os.path.abspath(__file__))

# Sutcliffe, veroeffentlicht frNOUgxE0IM (6993 s) / Master 7518 s.
# Anker aus video/sutcliffe-shorts.md: veroeffentlicht 4532 <-> Master 4799,
# lokales Tempo 1,1. Gilt **lokal**; fuer entfernte Stellen driftet er,
# deshalb das weite Fenster.
MASTER = '1oJjeQXjfIYtYph0gxfe8V1dhv17BBlPT'
MASTER_GROESSE = 19976733699
MASTER_DAUER = 7518.0
ANKER_PUB, ANKER_MASTER, TEMPO = 4532.0, 4799.0, 1.1

def schaetzung(pub):
    return max(0.0, min(MASTER_DAUER, ANKER_MASTER + (pub - ANKER_PUB) * TEMPO))

JOBS = [
    dict(schluessel='05-wer-ich-wurde', pub=(380, 420), rand=90,
         suche="didn't like who i was becoming",
         titel='I didn’t like who I was becoming'),
    dict(schluessel='06-angst-legitim', pub=(1300, 1340), rand=90,
         suche='the fear is legitimate',
         titel='Maybe your fear is legitimate'),
    dict(schluessel='07-wo-ist-der-vater', pub=(3116, 3160), rand=90,
         suche="where's the", titel='Where’s the father?'),
    dict(schluessel='08-respekt-tate', pub=(3780, 3820), rand=90,
         suche='respect that', titel='How do you not respect that?'),
    dict(schluessel='09-er-sah-mich-nie', pub=(5640, 5720), rand=110,
         suche='never saw me play', titel='He never saw me play'),
    dict(schluessel='10-ungewissheit', pub=(6940, 6970), rand=70,
         suche='embrace the uncertainty', titel='Embrace the uncertainty'),
    dict(schluessel='11-friends-gage', pub=(200, 250), rand=150,
         suche='three thousand', titel='They made $750,000. I made $3,000.'),
]

def lauf(cmd, **kw):
    return subprocess.run(cmd, **kw)

def stufe_fenster(j, o):
    roh = os.path.join(o, j['schluessel'] + '.roh.mp4')
    if os.path.exists(roh) and os.path.getsize(roh) > 1_000_000:
        return roh, False
    a = max(0.0, schaetzung(j['pub'][0]) - j['rand'])
    b = min(MASTER_DAUER, schaetzung(j['pub'][1]) + j['rand'])
    r = lauf([sys.executable, os.path.join(HIER, 'master_schnitt.py'),
              '--id', MASTER, '--groesse', str(MASTER_GROESSE),
              '--start', f'{a:.2f}', '--ende', f'{b:.2f}', '--out', roh],
             capture_output=True, text=True, timeout=900)
    if r.returncode != 0 or not os.path.exists(roh):
        raise RuntimeError('Fenster nicht geholt: ' + r.stderr[-300:])
    return roh, True

def stufe_transkript(j, o, roh):
    p = os.path.join(o, j['schluessel'] + '.roh.json')
    if os.path.exists(p):
        return json.load(open(p))
    from faster_whisper import WhisperModel
    import numpy as np
    # Ton selbst dekodieren: faster-whisper ruft PyAV mit einem Argument auf,
    # das die hier installierte Fassung nicht kennt (metadata_errors).
    r = lauf(['ffmpeg', '-nostdin', '-v', 'error', '-i', roh,
              '-f', 'f32le', '-ac', '1', '-ar', '16000', '-'],
             capture_output=True, timeout=600)
    ton = np.frombuffer(r.stdout, dtype=np.float32)
    m = WhisperModel('small', device='cpu', compute_type='int8')
    seg, _ = m.transcribe(ton, language='en', word_timestamps=False)
    d = [dict(start=s.start, end=s.end, text=s.text.strip()) for s in seg]
    json.dump(d, open(p, 'w'), indent=1)
    return d

def stufe_lage(j, o, segmente):
    p = os.path.join(o, j['schluessel'] + '.lage.json')
    if os.path.exists(p):
        return json.load(open(p))
    ziel = j['suche'].lower()
    treffer = [s for s in segmente if ziel in s['text'].lower()]
    if not treffer:
        # Zweiter Versuch: ueber die Wortmenge, falls Whisper anders schreibt.
        worte = set(ziel.split())
        bewertet = [(len(worte & set(s['text'].lower().split())), s)
                    for s in segmente]
        bewertet.sort(key=lambda x: -x[0])
        if not bewertet or bewertet[0][0] < max(2, len(worte) - 1):
            raise RuntimeError(
                f"Stelle nicht im Fenster: {j['suche']!r}. "
                f"Fenster erweitern oder Suchtext anpassen.")
        treffer = [bewertet[0][1]]
    lage = dict(treffer=treffer[0]['start'], text=treffer[0]['text'])
    json.dump(lage, open(p, 'w'), indent=1)
    return lage

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    ap.add_argument('--nur')
    ap.add_argument('--frist', type=float, default=0)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    stand_p = os.path.join(a.out, 'stand.json')
    start = time.time()
    for j in JOBS:
        if a.nur and a.nur not in j['schluessel']:
            continue
        if a.frist and time.time() - start > a.frist:
            print('Frist erreicht, Rest beim naechsten Aufruf.'); break
        fertig = os.path.join(a.out, j['schluessel'] + '.mp4')
        if os.path.exists(fertig) and os.path.getsize(fertig) > 100_000:
            print(f"{j['schluessel']} schon fertig"); continue
        t0 = time.time()
        try:
            roh, neu = stufe_fenster(j, a.out)
            print(f"  {j['schluessel']} Fenster {'geholt' if neu else 'lag da'}"
                  f" ({os.path.getsize(roh)//1_000_000} MB)", flush=True)
            seg = stufe_transkript(j, a.out, roh)
            lage = stufe_lage(j, a.out, seg)
            print(f"  Stelle bei Clipsekunde {lage['treffer']:.1f}: "
                  f"{lage['text'][:70]}", flush=True)
            stand = json.load(open(stand_p)) if os.path.exists(stand_p) else {}
            stand[j['schluessel']] = dict(lage=lage['treffer'],
                                          text=lage['text'],
                                          sekunden=round(time.time() - t0, 1))
            json.dump(stand, open(stand_p, 'w'), indent=1, ensure_ascii=False)
        except Exception as e:
            print(f"  {j['schluessel']} FEHLER: {e}", flush=True)
            continue

if __name__ == '__main__':
    main()
