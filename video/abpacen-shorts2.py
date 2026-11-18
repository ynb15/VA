#!/usr/bin/env python3
"""Eine Vorlage abpacen, damit der Short unter 60 Sekunden bleibt.

YouTube sperrt Shorts mit lizenzierter Musik ueber 60 Sekunden — genau das
ist der Ken-Aging-Fassung 11 passiert (63,2 s). Betroffen ist jeder Short
mit Musik, nicht nur dieser.

Zwei Werkzeuge, bewusst getrennt:

  * **Pausen kuerzen.** Harte Schnitte. Im Bild nur unsichtbar, wenn an
    der Stelle B-ROLL laeuft — sonst ist es ein Sprung im Gesicht. Das
    Werkzeug prueft das nicht; wer es benutzt, muss die B-Roll-Fenster
    kennen.
  * **Eine Strecke beschleunigen.** Kein Schnitt, also auch kein Sprung —
    dafuer hoerbar. `atempo` haelt die Tonhoehe, bis etwa 1,5 klingt es
    natuerlich. Das ist das Mittel fuer Strecken, in denen der Sprecher
    IM BILD ist.

**Alle Grenzen werden mitgerechnet.** Plan, B-Roll-Fenster und Blitzzeiten
liegen in Vorlagenzeit; wird in der Mitte Zeit herausgenommen, verschiebt
sich alles danach. Von Hand umzurechnen ist genau die Sorte Fehler, die auf
diesem Kanal schon zweimal passiert ist (die Blitzzeiten standen sieben
Umbauten lang falsch, die Quadratmitten waren zweimal um die halbe Seite
verschoben). Darum gibt `--karte` die Abbildung aus, statt sie dem
Gedaechtnis zu ueberlassen.

    python3 abpacen-shorts2.py --src vorlage.mov --ende 71.2334 \\
        --pause 1.76:2.60 --pause 14.60:15.02 --rest 0.15 \\
        --schneller 22.50:32.20:1.40 \\
        --plan plaene/x.json --plan-out plaene/x-kurz.json \\
        --fenster 1.60:4.20=d01.mp4 --fenster 4.20:5.25=d02.mp4 \\
        --blitz 1.60 --blitz 6.85 --tempo 1.2 --out vorlage-kurz.mov
"""
import argparse, json, subprocess
from pathlib import Path

FFMPEG = "ffmpeg"


def stuecke_bauen(ende, pausen, rest, schneller):
    """Die Vorlage in (von, bis, tempo) zerlegen."""
    st, t = [], 0.0
    for a, b in sorted(pausen):
        if a > t:
            st.append((t, a, 1.0))
        st.append((a, min(a + rest, b), 1.0))
        t = b
    if t < ende:
        st.append((t, ende, 1.0))
    for sa, sb, stp in sorted(schneller):
        fein = []
        for a, b, tp in st:
            for x, y, q in [(a, min(b, sa), tp), (max(a, sa), min(b, sb), stp),
                            (max(a, sb), b, tp)]:
                if y - x > 0.001:
                    fein.append((round(x, 4), round(y, 4), q))
        st = fein
    return st


def karte_bauen(stuecke):
    karte, n = [], 0.0
    for a, b, tp in stuecke:
        karte.append((a, b, tp, n))
        n += (b - a) / tp
    return karte, n


def ab(karte, laenge, t):
    for a, b, tp, nstart in karte:
        if t < b + 1e-6:
            return nstart + max(0.0, t - a) / tp
    return laenge


def vorlage_bauen(src, stuecke, ziel):
    v = [f"[0:v]trim={x}:{y},setpts=(PTS-STARTPTS)/{tp}[v{i}]"
         for i, (x, y, tp) in enumerate(stuecke)]
    a = [f"[0:a]atrim={x}:{y},asetpts=PTS-STARTPTS"
         + (f",atempo={tp}" if tp != 1.0 else "") + f"[a{i}]"
         for i, (x, y, tp) in enumerate(stuecke)]
    kette = ";".join(v + a) + ";" + "".join(f"[v{i}][a{i}]" for i in range(len(stuecke)))
    kette += f"concat=n={len(stuecke)}:v=1:a=1[v][a]"
    subprocess.run([FFMPEG, "-nostdin", "-v", "error", "-y", "-i", str(src),
                    "-filter_complex", kette, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "14",
                    "-pix_fmt", "yuv420p", "-r", "30",
                    "-c:a", "pcm_s16le", str(ziel)], check=True)


def paar(s):
    a, b = s.split(":")[:2]
    return float(a), float(b)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True)
    ap.add_argument("--ende", type=float, required=True, help="Laenge der Vorlage")
    ap.add_argument("--pause", action="append", default=[], metavar="VON:BIS")
    ap.add_argument("--rest", type=float, default=0.15,
                    help="soviel Pause bleibt stehen (Vorgabe 0,15 s)")
    ap.add_argument("--schneller", action="append", default=[], metavar="VON:BIS:TEMPO")
    ap.add_argument("--plan"); ap.add_argument("--plan-out")
    ap.add_argument("--fenster", action="append", default=[], metavar="VON:BIS=DATEI")
    ap.add_argument("--blitz", action="append", default=[], type=float,
                    help="Blockgrenze in VORLAGENZEIT; ausgegeben wird die Ausgabezeit")
    ap.add_argument("--tempo", type=float, default=1.0, help="Tempo beim Rendern")
    ap.add_argument("--outro", type=float, default=3.8)
    ap.add_argument("--out")
    a = ap.parse_args()

    schneller = []
    for s in a.schneller:
        t = s.split(":")
        schneller.append((float(t[0]), float(t[1]), float(t[2])))
    st = stuecke_bauen(a.ende, [paar(p) for p in a.pause], a.rest, schneller)
    karte, laenge = karte_bauen(st)
    haupt = laenge / a.tempo
    print(f"{len(st)} Stuecke · Vorlage {a.ende:.4f} -> {laenge:.4f} s "
          f"(gespart {a.ende-laenge:.3f} s)")
    print(f"Hauptteil bei Tempo {a.tempo}: {haupt:.3f} s + Outro {a.outro} = "
          f"{haupt+a.outro:.3f} s "
          f"{'— UNTER 60' if haupt+a.outro < 60 else '— UEBER 60, reicht nicht'}")

    if a.plan and a.plan_out:
        plan = json.loads(Path(a.plan).read_text(encoding="utf-8"))
        if a.out:
            plan["quelle"] = Path(a.out).name
        print("\nPlan:")
        for e in plan["einstellungen"]:
            v, b = e["start"], e["ende"]
            e["start"] = round(ab(karte, laenge, v), 4)
            e["ende"] = round(ab(karte, laenge, b), 4)
            print(f"  {v:9.4f}-{b:9.4f} -> {e['start']:9.4f}-{e['ende']:9.4f}")
        Path(a.plan_out).write_text(json.dumps(plan, indent=2, ensure_ascii=False),
                                    encoding="utf-8")

    if a.fenster:
        print("\nB-Roll:")
        spec = []
        for f in a.fenster:
            zeit, datei = f.split("=", 1)
            v, b = paar(zeit)
            nv, nb = round(ab(karte, laenge, v), 3), round(ab(karte, laenge, b), 3)
            d = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration", "-of", "default=nw=1:nk=1", datei],
                               capture_output=True, text=True).stdout.strip()
            dd = float(d) if d else 0.0
            warn = "" if dd >= nb - nv - 0.01 else "   <<< CLIP ZU KURZ"
            print(f"  {v:6.2f}-{b:6.2f} -> {nv:6.3f}-{nb:6.3f} "
                  f"({nb-nv:5.3f} s, Clip {dd:5.3f} s){warn}")
            spec.append(f"{nv}:{nb}={datei}")
        print("\n--broll \"" + ",".join(spec) + "\"")

    if a.blitz:
        zeiten = [ab(karte, laenge, x) / a.tempo for x in a.blitz]
        print("\n--blitze \"" + ",".join(f"{z:.3f}" for z in zeiten) + "\"")

    if a.out:
        vorlage_bauen(a.src, st, a.out)
        print(f"\ngebaut: {a.out}")


if __name__ == "__main__":
    main()
