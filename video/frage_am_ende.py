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
STUECK, MAX_VERSUCHE, ZIEL_MAX = 210.0, 4, 100.0

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
    """Ende des Bogens: am Uebergang, auf dem letzten Satzende davor.

    Dreimal ist die erste Fassung zu weit gelaufen — Logan und Matt ins Outro
    ("wo findet man dich", Instagram, Spotify), Kyle in die Ankuendigung
    seiner Community. Bei Eben Britton kam ein vierter Fall dazu, und der
    zeigt die eigentliche Ursache: dort stand 108 Sekunden lang keine neue
    Frage, also entschied die feste Ziellaenge von 72 Sekunden — und landete
    mitten in einer ganz anderen Antwort (Byron Katies "is it true?"), 25 s
    nach dem Ende des Bogens.

    Deshalb entscheidet die Ziellaenge jetzt nichts mehr. Sie ist nur noch
    eine Obergrenze fuer den Fall, dass gar kein Uebergang gefunden wird; die
    laengste gemessene Antwort war Aaronsons mit 78 s Masterzeit.
    """
    # Eine Frage faengt nicht immer mit einem Fragewort an und steht oft nicht
    # in einem Abschnitt. Whitney Wheelocks Bogen endet auf "then you have a
    # meaningful life, perhaps" — danach fragt er "So you don't agree that a
    # cute little poodle called Mauro doesn't make life a little bit more
    # meaningful?", und das Fragezeichen steht zwei Abschnitte spaeter.
    # Deshalb wird ab einem Abschnitt der Satz zusammengesetzt, bis ein
    # Satzzeichen kommt, und dieser ganze Satz geprueft.
    # "so" allein ist zu gierig: Kyle Kingsburys eigener Satz "So when you speak
    # about the infallible nature of God ... it's beyond language, right?"
    # beginnt mit "so" und endet acht Sekunden spaeter auf ein Fragezeichen —
    # der Schnitt waere 31 s statt 61 s lang geworden. "so" zaehlt deshalb nur,
    # wenn direkt ein Frage- oder Anredewort folgt.
    OEFFNER = (r"how|what|where|when|why|who|can|could|do|does|did|would|will|"
               r"is|are|tell|don't|doesn't|aren't|didn't|"
               r"so[,\s]+(?:you|do|don't|does|is|are|would|can|did|didn't)")
    neue_frage = re.compile(rf"(?i)^({OEFFNER})\b.*\?\s*$", re.S)

    def satz_ab(j):
        """Der Satz, der bei Abschnitt j beginnt — ueber Abschnittsgrenzen hinweg.

        Begrenzt auf 12 s, damit nicht eine ganze Antwort ohne Interpunktion
        als ein Satz gilt. Das haelt zugleich das rhetorische "right?" mitten
        in einer Antwort draussen: der Satz beginnt dort mit "because" oder
        "like", nicht mit einem Oeffner.
        """
        teile = []
        for x in daten[j:]:
            if x["start"] - daten[j]["start"] > 12:
                break
            teile.append(x["text"].strip())
            if x["text"].rstrip().endswith((".", "!", "?")):
                break
        return " ".join(teile)
    # Was die vier Faelle teilen, ist nicht die Satzform, sondern das Thema:
    # ab hier wird abgebunden oder es geht ums Geschaeft. Der Uebergang steht
    # dabei nicht immer am Anfang eines Abschnitts — bei Britton steckt
    # "and to close it off" im selben Abschnitt wie sein Schlusssatz
    # ("Ubuntu baby. That's it. That's it and to close it off").
    UEBERGANG = re.compile(
        r"(?i)\b(speaking of|news to share|to close (it|us) (off|out)|"
        r"one question to ask|where can (people|we|they)|how can people|"
        r"(find|follow|reach) you|get in touch|your (book|website|community|"
        r"podcast|channel|program)|instagram|spotify|link in|"
        r"before we (go|wrap)|last question|ladies and gentlemen)\b")

    beginn = daten[idx]["start"]
    grenze = min(daten[-1]["end"], beginn + ZIEL_MAX)
    getroffen = False
    for d in daten[idx + 1:]:
        if d["start"] - beginn <= 15:
            continue
        t = d["text"].strip()
        if neue_frage.match(satz_ab(daten.index(d))):
            grenze, getroffen = min(grenze, d["start"]), True
            break
        m = UEBERGANG.search(t)
        if m:
            # Steckt der Uebergang mitten im Abschnitt, wird seine Lage ueber
            # den Zeichenabstand geschaetzt — Whisper liefert hier keine
            # Wortzeiten. Bei Britton ergibt das 97,0 s statt 94,5 s und haelt
            # damit "That's it. That's it" im Stueck.
            anteil = m.start() / max(1, len(t))
            grenze = min(grenze, d["start"] + anteil * (d["end"] - d["start"]))
            getroffen = True
            break

    # Ab idx+1, nicht ab idx: die Frage selbst endet auf ein Fragezeichen und
    # waere sonst das einzige "Satzende". Bei Britton hat Whisper keinen
    # einzigen Antwortabschnitt interpunktiert — damit waere der Schnitt auf
    # der Frage gelandet, also bei 6 s Laenge.
    kand = [d for d in daten[idx + 1:] if d["end"] <= grenze + 0.05]
    if not kand:
        return grenze
    satz = [d for d in kand if d["text"].rstrip().endswith((".", "!", "?"))]
    # Das letzte Satzende vor dem Uebergang, nicht das naechste an einer
    # Wunschlaenge. Die Antwort laeuft bis zum Uebergang, und wie lang sie
    # ist, entscheidet der Gast. Interpunktiert Whisper gar nicht, entscheidet
    # die Grenze — ein frueher Satzanfang waere schlechter als ein Schnitt
    # auf der gemessenen Uebergangsstelle.
    ende = max(d["end"] for d in (satz or kand))
    # Ist der Uebergang gemessen, ist er selbst ein gueltiger Schnittpunkt —
    # und der bessere, wenn das letzte Satzende deutlich davor liegt. Bei
    # Britton waeren das 94,52 statt 97,0 und damit faellt "Ubuntu baby.
    # That's it." heraus, also genau die Pointe. Liegt das Satzende dicht an
    # der Grenze (Kyle: 0,25 s), bleibt es beim Satzende.
    if getroffen and grenze - ende > 2.0:
        return grenze
    return ende


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
            # Die Quelle steckt im Namen. Sonst gelten nach einem Wechsel der
            # Quelldatei die Transkripte der alten weiter — bei Whitney
            # Wheelock waere das die Kamera gewesen, die 42 Minuten vor dem
            # Gespraech endet, und der Fehler haette nach einem Treffer
            # ausgesehen.
            st = f"{k}_{fid[:8]}_f{v}"
            w = os.path.join(HIER, f"{st}.mp4")
            wstart = os.path.join(HIER, f"{st}.beginn")
            jf = os.path.join(HIER, f"{st}.json")
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
        # Laeuft die Antwort ueber die Fenstergrenze? Gesucht wird rueckwaerts,
        # das Anschlussfenster (v-1) liegt also naeher am Folgenende und ist
        # bereits geholt. Bei Whitney Wheelock endete das Stueck mitten im Satz
        # auf 211,29 s bei 211,4 s Fensterlaenge — der Schnitt stand auf der
        # Fensterkante, nicht am Ende des Bogens.
        anschluss = None
        if fenster is not None and v > 0:
            vorn = os.path.join(HIER, f"{k}_{fid[:8]}_f{v - 1}")
            if os.path.exists(vorn + ".json"):
                versatz = dauer(fenster)
                weiter = [{"start": x["start"] + versatz,
                           "end": x["end"] + versatz, "text": x["text"]}
                          for x in json.load(open(vorn + ".json"))]
                daten = daten + weiter
                anschluss = (vorn + ".mp4", versatz)

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

        quelle, fende = fenster, None
        if anschluss and schluss > anschluss[1] - 0.05:
            # Beide Fenster aneinandersetzen und daraus schneiden. Sie sind
            # luckenlos aneinander geholt worden; die Zeitrechnung des
            # zusammengesetzten Stuecks ist dieselbe wie die des Versatzes.
            quelle = os.path.join(HIER, f"{k}_{fid[:8]}_f{v}+{v - 1}.mp4")
            if dauer(quelle) < 5:
                liste = os.path.join(HIER, f"{k}_{fid[:8]}_concat.txt")
                with open(liste, "w") as fh:
                    fh.write(f"file '{fenster}'\nfile '{anschluss[0]}'\n")
                lauf([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
                      "-f", "concat", "-safe", "0", "-i", liste,
                      "-c", "copy", quelle])
            fende = anschluss[1]
            print(f"{nr}. {name}: Antwort laeuft ueber die Fenstergrenze, "
                  f"Anschlussfenster f{v - 1} angesetzt", flush=True)
        # Fensterzeit -> Masterzeit. Ohne diese beiden Zahlen ist das
        # Stueck in zwei Jahren nicht mehr zuzuordnen, und genau darum
        # geht es bei diesem Auftrag.
        def master(t):
            if fstart is None:
                return None
            if fende is None or t <= fende:
                return round(fstart + t, 2)
            vorn_beginn = float(open(os.path.join(
                HIER, f"{k}_{fid[:8]}_f{v - 1}.beginn")).read())
            return round(vorn_beginn + (t - fende), 2)

        json.dump({"nr": nr, "name": name, "drive_id": fid,
                   "master_von": master(von),
                   "master_bis": master(schluss),
                   "masterzeit_gemessen": fstart is not None,
                   "fenster": os.path.basename(fenster),
                   "fenster_von": round(von, 2), "fenster_bis": round(schluss, 2),
                   "frage": daten[idx]["text"].strip()},
                  open(befund, "w"), indent=1, ensure_ascii=False)
        lauf([FF, "-nostdin", "-y", "-hide_banner", "-loglevel", "error",
              "-ss", f"{von:.2f}", "-i", quelle, "-t", f"{schluss - von:.2f}",
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
