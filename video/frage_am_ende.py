#!/usr/bin/env python3
"""Macht dort weiter, wo der letzte Lauf aufgehoert hat.

Der Container wird zwischen den Zuegen eingesammelt; Prozesse ueberleben das
nicht, Dateien schon. Darum ist hier nichts auf einen durchlaufenden Prozess
angewiesen: Was fertig ist, wird an den Dateien erkannt. Jeder Aufruf macht
genau den naechsten offenen Schritt und ist beliebig oft wiederholbar.
"""
import json, os, re, subprocess, sys
import numpy as np
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
REPO = "/home/user/VA"
HIER = os.path.dirname(os.path.abspath(__file__))
MUSTER = re.compile(r"(?i)(makes?\s+(a\s+)?(human\s+)?life\s+meaningful"
                    r"|what\s+makes\s+life\s+meaning"
                    r"|life\s+meaningful\s+(for|to)\s+you"
                    r"|makes\s+your\s+life\s+meaningful)")
STUECK, MAX_VERSUCHE, ZIEL = 210.0, 7, 72.0

FOLGEN = [
    ("David Sutcliffe", "sutcliffe", "1oJjeQXjfIYtYph0gxfe8V1dhv17BBlPT", 19976733699, 7518.0, 1),
    ("Scott Aaronson",  "aaronson",  "1C7CUI-B6_fBcdttR_zKIJBYraBMTtUvh", 16141727375, 6138.0, 2),
    ("Ken Stern",       "ken",       "1RGq-Mw0QEm5jE2WMthKPkP5OHrXvmotF", 16824141940, 6333.4, 3),
    ("Logan Gonzalez",  "logan",     "1ztggu2ua5-AntISFHHP9cBqjVhSn6Zmj",  2663541811, 5159.5, 4),
    ("Matt Defina",     "matt",      "1ubW-gMYb6_g0ZO-cOVyEFGQoKvIyGivj", 17449171699, 6572.3, 5),
    ("Rick Strassman",  "rick",      "1Hwt3_c_Ifhd7onXyC8nrHIdtjwJjxdjH", 15496441499, 7251.8, 6),
]


def lauf(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def dauer(pfad):
    if not os.path.exists(pfad):
        return 0.0
    p = subprocess.run([FF, "-hide_banner", "-i", pfad],
                       capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", p.stderr)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0


def transkript(clip):
    from faster_whisper import WhisperModel
    roh = subprocess.run([FF, "-nostdin", "-v", "quiet", "-i", clip, "-f", "f32le",
                          "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    m = WhisperModel("medium", device="cpu", compute_type="int8")
    seg, _ = m.transcribe(np.frombuffer(roh, dtype=np.float32),
                          language="en", vad_filter=True)
    return [{"start": round(s.start, 2), "end": round(s.end, 2),
             "text": s.text.strip()} for s in seg]


def schluss_waehlen(daten, idx):
    """Ende des Bogens: vor der naechsten Frage, auf dem letzten Satzende.

    Zweimal von zwei ist die erste Fassung ins Outro gelaufen („wo findet man
    dich") — die Antwort endet dort, wo er die naechste Frage stellt, und die
    kommt bei jedem Gast woanders.
    """
    neue_frage = re.compile(r"(?i)^(how|what|where|when|why|who|can|could|do|did|"
                            r"would|is|are|tell)\b.*\?\s*$")
    grenze = daten[-1]["end"]
    for d in daten[idx + 1:]:
        if d["start"] - daten[idx]["start"] > 15 and neue_frage.match(d["text"].strip()):
            grenze = d["start"] - 0.3
            break
    ziel = min(daten[idx]["start"] + ZIEL, grenze)
    kand = [d for d in daten[idx:] if d["end"] <= grenze]
    satz = [d for d in kand if d["text"].rstrip().endswith((".", "!", "?"))]
    wahl = satz or kand or daten[idx:]
    return min((d["end"] for d in wahl), key=lambda x: abs(x - ziel))


def eine(name, k, fid, groesse, gesamt, nr):
    out = os.path.join(HIER, f"{nr:02d}-{k}-meaningful.mp4")
    if dauer(out) > 10:
        return f"{nr}. {name}: schon fertig ({dauer(out):.1f}s)"

    clip = os.path.join(HIER, f"{k}_fertig.mp4")
    if dauer(clip) < 5:
        fenster, fstart, daten, idx = None, None, None, None
        ende = gesamt
        for v in range(MAX_VERSUCHE):
            start = max(0.0, ende - STUECK)
            w = os.path.join(HIER, f"{k}_f{v}.mp4")
            if dauer(w) < 5:
                lauf([sys.executable, os.path.join(REPO, "video/master_schnitt.py"),
                      "--id", fid, "--start", str(start), "--ende", str(ende),
                      "--groesse", str(groesse), "--out", w], capture_output=True)
            jf = os.path.join(HIER, f"{k}_f{v}.json")
            d = json.load(open(jf)) if os.path.exists(jf) else transkript(w)
            json.dump(d, open(jf, "w"), indent=1)
            tr = next((i for i, s in enumerate(d) if MUSTER.search(s["text"])), None)
            if tr is not None:
                fenster, fstart, daten, idx = w, start, d, tr
                break
            ende = start
        if fenster is None:
            return f"{nr}. {name}: Frage NICHT gefunden"
        schluss = schluss_waehlen(daten, idx)
        von = max(0.0, daten[idx]["start"] - 1.0)
        lauf([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
              "-ss", f"{von:.2f}", "-i", fenster, "-t", f"{schluss - von:.2f}",
              "-c:v", "libx264", "-crf", "17", "-preset", "veryfast",
              "-c:a", "aac", "-b:a", "192k", clip])

    plan = os.path.join(HIER, f"{k}_fertig_plan.json")
    if not os.path.exists(plan):
        lauf([sys.executable, os.path.join(REPO, "video/bildausschnitt.py"), clip,
              "--zoom", "1.15", "--kein-stapel", "--json", plan], capture_output=True)
    lauf([sys.executable, os.path.join(REPO, "video/shorts-render.py"),
          "--src", clip, "--plan", plan, "--out", out,
          "--tempo", "1.2", "--auto-captions", "--lang", "en", "--model", "medium",
          "--korrekturen", os.path.join(REPO, "video/korrekturen.txt"),
          "--schriftgroesse", "70", "--look", "warm",
          "--logo", os.path.join(REPO, "video/marke/ynb-logo-weiss.png"),
          "--logo-breite", "700", "--logo-hoehe", "0.877",
          "--srt-out", out.replace(".mp4", ".srt")], capture_output=True)
    return f"{nr}. {name}: FERTIG ({dauer(out):.1f}s)"


if __name__ == "__main__":
    for f in FOLGEN:
        try:
            print(eine(*f), flush=True)
        except Exception as e:
            print(f"{f[5]}. {f[0]}: Fehler {type(e).__name__}: {str(e)[:120]}",
                  flush=True)
    print("DURCHLAUF ENDE", flush=True)
