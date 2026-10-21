#!/usr/bin/env python3
"""Rick, dritte Runde: seinen Streichungsauftrag nachtragen und neu rechnen.

Am 21.10. hat er gefragt, ob seine Kommentare eingearbeitet sind — waren
sie nur zum Teil. Beim Wechsel auf die laengere Quelle (rick3_quelle) ist
die Streichung „a couple of things … almost 1000 pages" liegen geblieben;
uebernommen war nur die Verleger-Abschweifung.

**Gestrichen wird nach Text, nicht nach Nummer.** Die Nummern einer
Schnittliste haengen am Transkript, und das wird hier neu gerechnet — eine
Nummer aus einer aelteren Liste zeigt dann woanders hin. Gesucht wird
also die Stelle selbst, und das Skript sagt, was es streicht.

  python3 video/rick_drei.py --ordner <nacht-ordner>
"""
import argparse, os, subprocess, sys, time

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import importlib.util
_sp = importlib.util.spec_from_file_location("sl", os.path.join(HIER, "schnittliste.py"))
sl = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(sl)

TEMPO = 1.15
KASTEN, LIPPE = "780:14:528:939", 965
# Was raus soll, als Text. Beide Marken muessen im selben Abschnitt oder in
# aufeinanderfolgenden Abschnitten liegen; alles dazwischen faellt mit.
# Whisper schreibt Zahlen mal als Ziffer, mal als Wort — die erste Fassung
# suchte nur „1000 pages", das Transkript sagte „a thousand pages", und der
# Lauf brach nach fuenf Minuten Transkription ergebnislos ab. Also mehrere
# Schreibweisen, und der Fund wird protokolliert.
VON = ["a couple of things"]
BIS = ["1000 pages", "thousand pages", "1,000 pages"]


def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}]", *a, flush=True)


def dauer(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", p]).decode().strip())


def fertig(p, soll=None, anteil=0.97):
    if not os.path.exists(p) or os.path.getsize(p) < 100_000:
        return False
    try:
        d = dauer(p)
    except Exception:
        log("unvollstaendig, wird neu gerechnet:", os.path.basename(p))
        os.remove(p); return False
    if soll and d < soll * anteil:
        log(f"zu kurz ({d:.1f}s statt {soll:.1f}s):", os.path.basename(p))
        os.remove(p); return False
    return True


def _norm(t):
    return " ".join(t.lower().replace(",", " ").replace(".", " ").split())


def streichen_finden(abschnitte):
    """Nummern der Abschnitte, die zwischen VON und BIS liegen (beide mit)."""
    a = b = None
    for i, abs_ in enumerate(abschnitte, 1):
        t = _norm(abs_["text"])
        if a is None and any(_norm(v) in t for v in VON):
            a = i
        if any(_norm(x) in t for x in BIS):
            b = i
    if a is None or b is None or b < a:
        log("Stelle nicht gefunden — hier sind die ersten Abschnitte:")
        for i, abs_ in enumerate(abschnitte[:10], 1):
            log(f"   {i}: {abs_['text'].strip()[:95]}")
        sys.exit(f"von={a}, bis={b} — nichts gestrichen.")
    return list(range(a, b + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ordner", required=True)
    ap.add_argument("--logo", default=os.path.join(HIER, "marke", "ynb-logo-weiss.png"))
    a = ap.parse_args()
    o = a.ordner
    quelle = os.path.join(o, "rick4_mit.mp4")
    gekuerzt = os.path.join(o, "rick5_mit.mp4")

    if not fertig(gekuerzt):
        # Die Transkription kostet Minuten. Sie wird abgelegt, damit ein
        # zweiter Versuch nicht wieder von vorn anfaengt — beim ersten Lauf
        # brach die Textsuche danach ab, und die fuenf Minuten waren weg.
        import json
        cache = os.path.join(o, "rick5_abschnitte.json")
        if os.path.exists(cache):
            abschnitte = json.load(open(cache))
            log(f"{len(abschnitte)} Abschnitte aus {os.path.basename(cache)}")
        else:
            log("Abschnitte von rick4_mit.mp4 bilden")
            woerter = sl.woerter_holen(quelle)
            abschnitte = sl.saetze_bilden(woerter)
            json.dump(abschnitte, open(cache, "w"))
        raus = streichen_finden(abschnitte)
        log(f"{len(abschnitte)} Abschnitte, es fallen {raus}:")
        for i in raus:
            log(f"   {i}: {abschnitte[i - 1]['text'].strip()[:90]}")
        sl.anwenden(quelle, abschnitte, set(raus), gekuerzt, TEMPO)

    ohne = os.path.join(o, "rick5_ohne.mp4")
    if not fertig(ohne):
        log("Fuellwoerter entfernen")
        subprocess.run([sys.executable, os.path.join(HIER, "fuellwoerter.py"),
                        "--clip", gekuerzt, "--out", ohne], check=True)

    for q, name in ((gekuerzt, "08-rick-mit"), (ohne, "08-rick-ohne")):
        ziel = os.path.join(o, f"{name}.mp4")
        if fertig(ziel, soll=dauer(q) / TEMPO):
            log(f"{name}.mp4 liegt schon da"); continue
        plan = ziel.replace(".mp4", "_plan.json")
        with open(plan, "w") as f:
            import json
            json.dump({"quelle": q, "groesse": [1920, 1080],
                       "einstellungen": [{"layout": "einzel", "kasten": KASTEN,
                                          "lippe": LIPPE, "start": 0.0,
                                          "ende": round(dauer(q), 2),
                                          "tot": False}]}, f, indent=1)
        log("rendere", name)
        cmd = [sys.executable, os.path.join(HIER, "shorts-render.py"),
               "--src", q, "--out", ziel, "--plan", plan, "--auto-captions",
               "--model", "medium", "--lang", "en", "--tempo", str(TEMPO),
               "--srt-out", os.path.join(o, f"{name}.srt"),
               "--korrekturen", os.path.join(HIER, "korrekturen.txt")]
        if a.logo and os.path.exists(a.logo):
            cmd += ["--logo", a.logo]
        subprocess.run(cmd, check=True)

    log("fertig")


if __name__ == "__main__":
    main()
