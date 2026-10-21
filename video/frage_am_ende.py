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
STUECK, MAX_VERSUCHE, ZIEL = 210.0, 4, 72.0

LISTE = os.path.join(HIER, "meaningful-folgen.json")


def folgen_laden():
    """Die Folgen stehen in meaningful-folgen.json, nicht hier im Code.

    Eine neue Folge ist damit eine neue Zeile in einer Datendatei und kein
    Eingriff ins Werkzeug. Uebersprungen wird, was keinen erreichbaren Master
    hat — 'blockiert' (Freigabe oder Tonspur fehlt) und 'ohne Master'
    (nach der Veroeffentlichung geloescht). Deren Grund steht in der Liste.
    """
    roh = json.load(open(LISTE))["folgen"]
    return [f for f in roh if f.get("id") and f.get("stand", "").startswith("offen")]


def laufzeit(fid, groesse):
    """Laufzeit aus dem Kopf der Datei, ohne sie zu laden (rund 8 MB)."""
    import av
    sys.path.insert(0, HIER)
    from drive_fernzugriff import DriveDatei, bestaetigte_url
    q = DriveDatei(bestaetigte_url(fid), groesse=groesse, datei_id=fid)
    c = av.open(q)
    d = c.duration / 1_000_000.0
    c.close()
    q.close()
    return d


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


def eine(f):
    name, k, fid, nr = f["name"], f["k"], f["id"], f["nr"]
    groesse, gesamt = f.get("groesse"), f.get("gesamt")
    out = os.path.join(HIER, f"{nr:02d}-{k}-meaningful.mp4")
    befund = os.path.join(HIER, f"{k}_befund.json")
    if dauer(out) > 10:
        return f"{nr}. {name}: schon fertig ({dauer(out):.1f}s)"
    if gesamt is None:
        gesamt = laufzeit(fid, groesse)
        print(f"{nr}. {name}: Laufzeit {gesamt:.1f}s gemessen", flush=True)
        ganz = json.load(open(LISTE))
        for z in ganz["folgen"]:
            if z["nr"] == nr:
                z["gesamt"] = round(gesamt, 1)
        json.dump(ganz, open(LISTE, "w"), indent=1, ensure_ascii=False)

    clip = os.path.join(HIER, f"{k}_fertig.mp4")
    if dauer(clip) < 5:
        fenster, fstart, daten, idx = None, None, None, None
        ende = gesamt
        for v in range(MAX_VERSUCHE):
            start = max(0.0, ende - STUECK)
            w = os.path.join(HIER, f"{k}_f{v}.mp4")
            wstart = os.path.join(HIER, f"{k}_f{v}.beginn")
            jf = os.path.join(HIER, f"{k}_f{v}.json")
            # Liegt das Transkript schon vor, ist dieses Fenster durchsucht —
            # dann wird es nicht noch einmal geholt. Bei einem 34-GB-Master
            # sind das 580 MB je Fenster.
            if dauer(w) < 5 and not os.path.exists(jf):
                p = lauf([sys.executable, os.path.join(REPO, "video/master_schnitt.py"),
                          "--id", fid, "--start", str(start), "--ende", str(ende),
                          "--groesse", str(groesse), "--out", w],
                         capture_output=True, text=True)
                m = re.search(r"beginnt bei Master ([\d.]+)s", p.stdout)
                # Ohne diese Zahl ist die Masterzeitmarke bis zu 6 s daneben:
                # der Abruf setzt auf das Schluesselbild VOR dem bestellten
                # Start, Fensterzeit 0 ist dort und nicht bei `start`.
                if not m:
                    raise RuntimeError(f"Dateibeginn nicht gemeldet: {p.stdout[:160]}")
                open(wstart, "w").write(m.group(1))
            d = json.load(open(jf)) if os.path.exists(jf) else transkript(w)
            json.dump(d, open(jf, "w"), indent=1)
            tr = next((i for i, s in enumerate(d) if MUSTER.search(s["text"])), None)
            if tr is not None:
                gemessen = (float(open(wstart).read())
                            if os.path.exists(wstart) else None)
                fenster, fstart, daten, idx = w, gemessen, d, tr
                break
            ende = start
        if fenster is None:
            json.dump({"nr": nr, "name": name, "drive_id": fid,
                       "gefunden": False, "gesamt": round(gesamt, 1),
                       "durchsucht_ab": round(ende, 1),
                       "grund": "Muster in den letzten "
                                f"{MAX_VERSUCHE * STUECK:.0f}s nicht getroffen"},
                      open(befund, "w"), indent=1, ensure_ascii=False)
            return (f"{nr}. {name}: Frage NICHT in den letzten "
                    f"{MAX_VERSUCHE * STUECK:.0f}s — Befund abgelegt")
        schluss = schluss_waehlen(daten, idx)
        von = max(0.0, daten[idx]["start"] - 1.0)
        # Fensterzeit -> Masterzeit. Ohne diese beiden Zahlen ist das
        # Stueck in zwei Jahren nicht mehr zuzuordnen, und genau darum
        # geht es bei diesem Auftrag.
        json.dump({"nr": nr, "name": name, "drive_id": fid,
                   "master_von": round(fstart + von, 2) if fstart else None,
                   "master_bis": round(fstart + schluss, 2) if fstart else None,
                   "masterzeit_gemessen": fstart is not None,
                   "fenster": os.path.basename(fenster),
                   "fenster_von": round(von, 2), "fenster_bis": round(schluss, 2),
                   "frage": daten[idx]["text"].strip()},
                  open(befund, "w"), indent=1, ensure_ascii=False)
        lauf([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
              "-ss", f"{von:.2f}", "-i", fenster, "-t", f"{schluss - von:.2f}",
              "-c:v", "libx264", "-crf", "17", "-preset", "veryfast",
              "-c:a", "aac", "-b:a", "192k", clip])

    plan = os.path.join(HIER, f"{k}_fertig_plan.json")
    if not os.path.exists(plan):
        # Ohne Stapeln folgt der Kasten in der Totale dem Bewegungsgipfel,
        # also der gestikulierenden Hand statt dem Gesicht. Bei Kyle stand
        # dadurch 11 s lang Buecherregal im Bild und kein Kopf (gemessen am
        # 21.10. an ausgelesenen Einzelbildern). Gestapelt steht je Person
        # ein Kasten. --marke haelt den Ausschnitt aus dem eingebrannten
        # Logo heraus (gemessen x 55-205, y 911-1028).
        lauf([sys.executable, os.path.join(REPO, "video/bildausschnitt.py"), clip,
              "--zoom", "1.15", "--marke", "0,875,215,1080",
              "--json", plan], capture_output=True)
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
    for f in folgen_laden():
        try:
            print(eine(f), flush=True)
        except Exception as e:
            print(f'{f["nr"]}. {f["name"]}: Fehler {type(e).__name__}: {str(e)[:120]}',
                  flush=True)
    print("DURCHLAUF ENDE", flush=True)
