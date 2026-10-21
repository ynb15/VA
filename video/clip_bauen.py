#!/usr/bin/env python3
"""Einen Clip (3-10 Min, 16:9) aus einem Master-Fenster bauen.

Anders als ein Short: kein Hochformat, kein Umrahmen, keine eingebrannten
Untertitel. Ein Clip ist ein Ausschnitt der Folge, wie sie ist - das Bild
des Masters bleibt unangetastet, hinten kommt das 16:9-Outro dran.

    python3 video/clip_bauen.py --src fenster.mp4 --von 4.5 --bis 213 \
            --outro video/marke/outro_16_9.mov --out clip.mp4

**Am Ton wird nichts gemacht.** Der Master liegt bei rund -31 LUFS, und
die naheliegende Angleichung hat er am 20.10. abgelehnt: der Rauschboden
stieg dabei von -62,7 auf -44,2 dB. Wer das anders will, sagt es
ausdruecklich; hier wird es nicht im Vorbeigehen getan.

Tempo 1,1, weil seine Folgen so exportiert werden - ein Clip soll neben
der veroeffentlichten Folge nicht langsamer laufen. (Shorts laufen auf
1,2; das ist seine getrennte Ansage.)
"""
import argparse, os, subprocess, sys

def ffmpeg(args, **kw):
    r = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error'] + args,
                       capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-500:])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--von', type=float, required=True)
    ap.add_argument('--bis', type=float, required=True)
    ap.add_argument('--tempo', type=float, default=1.1)
    ap.add_argument('--outro', default=None)
    ap.add_argument('--breite', type=int, default=1920)
    ap.add_argument('--hoehe', type=int, default=1080)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    zwischen = a.out + '.teil.mp4'
    if not (os.path.exists(zwischen) and os.path.getsize(zwischen) > 100_000):
        vf = f'fps=30,scale={a.breite}:{a.hoehe}:force_original_aspect_ratio=decrease,' \
             f'pad={a.breite}:{a.hoehe}:(ow-iw)/2:(oh-ih)/2'
        if abs(a.tempo - 1.0) > 1e-3:
            vf += f',setpts=PTS/{a.tempo}'
        af = f'atempo={a.tempo}' if abs(a.tempo - 1.0) > 1e-3 else 'anull'
        ffmpeg(['-ss', f'{a.von:.3f}', '-to', f'{a.bis:.3f}', '-i', a.src,
                '-vf', vf, '-af', af, '-c:v', 'libx264', '-crf', '18',
                '-preset', 'medium', '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
                zwischen, '-y'])
    if not a.outro:
        os.replace(zwischen, a.out); print(a.out); return

    # Das Outro auf dasselbe Format bringen, sonst scheitert das Aneinander-
    # setzen still oder liefert eine Datei, die nur der erste Teil ist.
    outro = a.out + '.outro.mp4'
    if not (os.path.exists(outro) and os.path.getsize(outro) > 50_000):
        ffmpeg(['-i', a.outro, '-vf',
                f'fps=30,scale={a.breite}:{a.hoehe}:force_original_aspect_ratio=decrease,'
                f'pad={a.breite}:{a.hoehe}:(ow-iw)/2:(oh-ih)/2',
                '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
                '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                '-ar', '48000', '-ac', '2', '-shortest', outro, '-y'])
    liste = a.out + '.liste.txt'
    with open(liste, 'w') as f:
        for p in (zwischen, outro):
            f.write(f"file '{os.path.abspath(p)}'\n")
    ffmpeg(['-f', 'concat', '-safe', '0', '-i', liste, '-c', 'copy',
            a.out, '-y'])
    for p in (zwischen, outro, liste):
        try: os.remove(p)
        except OSError: pass
    print(a.out)

if __name__ == '__main__':
    main()
