#!/usr/bin/env python3
"""Holt Transkript und Metadaten einer veröffentlichten Folge direkt von YouTube.

    python3 video/yt-transkript.py swZGLesMb8Y --out video/transkripte/

Braucht die Netzwerk-Freigabe für youtube.com (seit 19.10.2026 gesetzt).
Keinen API-Schlüssel, kein OAuth: die automatischen Untertitel stehen öffentlich.
Die Mediendatei holt das hier NICHT — YouTube liefert die Bytes nur an Clients
mit Browser-Fingerabdruck, und der fehlt im Container.
"""
import argparse, os, re, sys

def vtt_zu_cues(pfad):
    """VTT -> [(start_sek, text)].

    YouTubes automatische Untertitel wiederholen in jedem Cue das Ende des
    vorigen und haengen ein paar neue Woerter an. Hier wird je Cue nur der
    Zuwachs behalten: die laengste Wortfolge, mit der der Cue am bereits
    gesammelten Text anschliesst, wird abgeschnitten.
    """
    roh = open(pfad, encoding='utf-8').read()
    treffer = re.findall(
        r'(\d\d):(\d\d):(\d\d)\.\d\d\d --> [\d:.]+.*?\n(.*?)(?=\n\n|\Z)', roh, re.S)

    def saeubern(body):
        text = re.sub(r'<[^>]+>', '', body)
        zeilen = [l.strip() for l in text.split('\n') if l.strip()]
        text = ' '.join(dict.fromkeys(zeilen))
        text = text.replace('&gt;&gt;', ' ').replace('&gt;', ' ').replace('&nbsp;', ' ')
        return re.sub(r'\s+', ' ', text).strip()

    cues, schwanz = [], []
    for h, m, s, body in treffer:
        worte = saeubern(body).split()
        if not worte:
            continue
        # laengste Ueberlappung zwischen dem Ende von schwanz und dem Anfang von worte
        k = min(len(schwanz), len(worte))
        while k > 0 and schwanz[-k:] != worte[:k]:
            k -= 1
        zuwachs = worte[k:]
        if not zuwachs:
            continue
        cues.append((int(h) * 3600 + int(m) * 60 + int(s), ' '.join(zuwachs)))
        schwanz = (schwanz + zuwachs)[-40:]
    return cues

def main():
    p = argparse.ArgumentParser()
    p.add_argument('video_id')
    p.add_argument('--lang', default='en')
    p.add_argument('--out', default='.')
    a = p.parse_args()

    import yt_dlp
    os.makedirs(a.out, exist_ok=True)
    stamm = os.path.join(a.out, a.video_id)
    opts = {'quiet': True, 'skip_download': True, 'writeautomaticsub': True,
            'writesubtitles': True, 'subtitleslangs': [a.lang],
            'subtitlesformat': 'vtt', 'outtmpl': stamm + '.%(ext)s'}
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(f'https://www.youtube.com/watch?v={a.video_id}', download=True)

    vtt = f'{stamm}.{a.lang}.vtt'
    if not os.path.exists(vtt):
        sys.exit(f'kein Untertitel in "{a.lang}" geladen — vorhanden: '
                 f'{sorted((info.get("automatic_captions") or {}).keys())[:20]}')

    cues = vtt_zu_cues(vtt)
    ziel = f'{stamm}.transkript.md'
    with open(ziel, 'w', encoding='utf-8') as f:
        f.write(f'# {info.get("title")}\n\n')
        f.write(f'**ID** `{a.video_id}` · **Dauer** {info.get("duration")} s '
                f'({int(info.get("duration", 0)) // 60}:{int(info.get("duration", 0)) % 60:02d}) · '
                f'**Aufrufe** {info.get("view_count")} · **Likes** {info.get("like_count")} · '
                f'**Kommentare** {info.get("comment_count")}\n\n')
        f.write(f'Hochgeladen {info.get("upload_date")} · Quelle: automatische Untertitel '
                f'(`{a.lang}`), geholt ohne API-Schlüssel.\n\n---\n\n')
        for sek, text in cues:
            f.write(f'**[{sek // 3600:02d}:{sek % 3600 // 60:02d}:{sek % 60:02d}]** {text}\n\n')
    print(f'{ziel}  ·  {len(cues)} Zeitmarken  ·  {info.get("view_count")} Aufrufe')

if __name__ == '__main__':
    main()
