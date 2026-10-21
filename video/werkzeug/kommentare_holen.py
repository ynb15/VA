#!/usr/bin/env python3
"""Holt die Kommentare eines Videos oder der letzten N Videos des Kanals.

Ohne API-Schluessel, ohne OAuth. Setzt `pip install yt-dlp` voraus.
Der Trick ist `ignore_no_formats_error`: die Watch-Seite verweigert die
Videoformate ("Sign in to confirm you're not a bot"), der Kommentar-Endpunkt
antwortet trotzdem. Ohne das Flag gibt yt-dlp vorher auf.

    python3 kommentare_holen.py --video cMI3tsQp410
    python3 kommentare_holen.py --letzte 14
"""
import argparse, json, sys

KANAL = 'UC5r4pxlAtt2alIOIGjdn4Qw'

OPTS = {
    'quiet': True, 'no_warnings': True, 'skip_download': True,
    'getcomments': True,
    'ignore_no_formats_error': True, 'ignoreerrors': True,
    'extractor_args': {'youtube': {'max_comments': ['200', 'all', '200', '50']}},
}


def video_ids(anzahl):
    import yt_dlp
    opts = {'quiet': True, 'no_warnings': True, 'skip_download': True,
            'extract_flat': 'in_playlist', 'playlistend': anzahl}
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(
            f'https://www.youtube.com/channel/{KANAL}/videos', download=False)
    return [e['id'] for e in info['entries']]


def hole(vid):
    """-> dict mit Titel und Kommentarbaum, oder None."""
    import yt_dlp
    with yt_dlp.YoutubeDL(OPTS) as y:
        d = y.extract_info(f'https://www.youtube.com/watch?v={vid}', download=False)
    if not d:
        return None
    alle = d.get('comments') or []
    antworten_von_ihm = {
        c.get('parent') for c in alle
        if c.get('author_is_uploader') and c.get('parent') not in (None, 'root')
    }
    for c in alle:
        c['_beantwortet'] = c.get('id') in antworten_von_ihm
    return {
        'id': vid,
        'titel': d.get('title'),
        'aufrufe': d.get('view_count'),
        'gemeldet': d.get('comment_count'),
        'kommentare': alle,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--video')
    p.add_argument('--letzte', type=int)
    p.add_argument('--json', action='store_true')
    a = p.parse_args()

    if a.video:
        ids = [a.video]
    elif a.letzte:
        ids = video_ids(a.letzte)
    else:
        p.error('--video oder --letzte angeben')

    ergebnis = [r for r in (hole(v) for v in ids) if r]

    if a.json:
        json.dump(ergebnis, sys.stdout, ensure_ascii=False, indent=1)
        return

    offen = 0
    for r in ergebnis:
        top = [c for c in r['kommentare'] if c.get('parent') in (None, 'root')]
        ohne = [c for c in top if not c['_beantwortet']]
        offen += len(ohne)
        print(f"\n== {r['id']} | {r['titel']}")
        print(f"   {len(r['kommentare'])} Kommentare (YouTube meldet "
              f"{r['gemeldet']}), {len(ohne)} ohne seine Antwort")
        for c in ohne:
            herz = ' [Herz]' if c.get('is_favorited') else ''
            pin = ' [angepinnt]' if c.get('is_pinned') else ''
            text = ' '.join((c.get('text') or '').split())
            print(f"   - {c.get('author')} (♥{c.get('like_count')},"
                  f" {c.get('_time_text')}){herz}{pin}: {text[:200]}")
    print(f"\nOffen insgesamt: {offen}")


if __name__ == '__main__':
    main()
