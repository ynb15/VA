#!/usr/bin/env python3
"""Prueft einen Beschreibungsentwurf gegen die Fehler, die ich wiederholt habe.

    python3 -I video/werkzeug/beschreibung_pruefen.py entwurf.txt
    cat entwurf.txt | python3 -I video/werkzeug/beschreibung_pruefen.py -

Kein Stilurteil. Nur die Konstruktionen, die er einzeln beanstandet hat.
Jeder Treffer nennt die Regel und die Stelle. Exitcode 1, wenn etwas sitzt.
"""
import re, sys

# --- 1. Der leere Cliffhanger ------------------------------------------
# Leeres Kopfnomen + Nebensatz, der es bewertet statt es zu fuellen.
LEER = r"(?:sentence|thing|line|word|answer|moment|question|part|reason|piece|somewhere|something|man|woman|person)"
BEWERTUNG = (r"(?:worth the clip|I(?:'| ha)ve carried|I(?:'ll| will) never forget|"
             r"(?:the )?hardest|the kindest|I did ?n[o']t see coming|that changed everything|"
             r"that closed the door|nobody says out loud|most people would recognise|"
             r"you(?:'| wi)ll never|stayed with me|still repeats?|is the reason this clip)")
LEERER_HAKEN = re.compile(
    rf"\b(?:one|the|a|an)\s+(?:\w+\s+){{0,2}}{LEER}\b[^.!?\n]{{0,70}}?{BEWERTUNG}", re.I)

# --- 2. Selbstbewertung des Materials ----------------------------------
SELBSTLOB = re.compile(
    r"\b(?:the (?:hardest|best|most honest|wildest) (?:sentence|part|answer|line|thing)"
    r"|is worth the clip on its own|why this clip exists|the part that stopped me"
    r"|further than I expected|the thing (?:almost )?nobody .{0,30}(?:say|admit)"
    r"|the most .{0,20}(?:I(?:'| ha)ve (?:ever )?heard))", re.I)

# --- 3. Verbotene Eroeffnungen -----------------------------------------
OEFFNUNG = re.compile(r"^\s*(What if\b|What happens when\b|What does it really take\b)", re.I)
IN_THIS_CLIP = re.compile(r"\bin this clip\b", re.I)

# --- 4. Gestrichene Formeln --------------------------------------------
GESTRICHEN = [
    (r"we go far past the highlight reel", "gestrichene Scharnierformel"),
    (r"\bAlmost 2 hours\b", "er will die runde Zahl: '2 hours'"),
]

# --- 5. Zeichen --------------------------------------------------------
# In BESCHREIBUNGEN ist der en dash seins (gemessen, beschreibungen.md).
# Der normale Bindestrich gilt fuer Kommentare und Mails, nicht hier.
# Geprueft wird nur der em dash, den er selbst nicht benutzt.
EM_DASH = re.compile(r"—")

def zeige(text, treffer, regel):
    a = max(text.rfind("\n", 0, treffer.start()) + 1, 0)
    e = text.find("\n", treffer.end())
    zeile = text[a:e if e > 0 else len(text)].strip()
    nr = text.count("\n", 0, treffer.start()) + 1
    print(f"  Zeile {nr}: {regel}")
    print(f"    > {zeile[:150]}")
    print(f"    ^ {treffer.group(0)[:90]}")

def pruefen(text, folge=False):
    """folge=True: volle Episodenbeschreibung statt Clip.

    Gemessen an seinen zwei veroeffentlichten Folgenbeschreibungen
    (2_CZfN2iOFk 697 Woerter, JaOju2tb-CI 781): dort ist "What if" seine
    eigene Eroeffnung, der Korridor liegt bei 700-900 statt 145-190 (gemessen: 766 und 878), und
    eine Laufzeit im Pitch gibt es nicht. Beides waren Fehlalarme, als der
    Clip-Pruefer am 27.11. zum ersten Mal auf eine Folge losgelassen wurde.
    Bullets: beide Folgen haben exakt 5, je 10-17 Woerter. Clips haben 0.
    """

    fehler = 0
    # Die Eroeffnungszeile einer Folge ist seine, nicht meine: sein
    # Kingsbury-Opener lautet "What if the hardest thing a UFC fighter ever
    # lived through happened years after he left the cage?" - Kopfnomen plus
    # Bewertung, aber der Satz loest es selbst auf. Gleiche Ausnahme wie beim
    # Abbinder. Im Rumpf und in jedem Clip bleibt die Regel scharf.
    kopf = text.split("\n", 1)[0] if folge else ""
    rest = text[len(kopf):] if folge else text

    print("== leerer Cliffhanger (Kopfnomen ohne Inhalt + Bewertung) ==")
    for m in LEERER_HAKEN.finditer(rest):
        zeige(rest, m, "leeres Kopfnomen, das der Nebensatz nur bewertet"); fehler += 1
    print("== Selbstbewertung des Materials ==")
    for m in SELBSTLOB.finditer(rest):
        zeige(rest, m, "sagt dem Leser, wie gut es ist, statt es zu zeigen"); fehler += 1
    print("== Eroeffnung ==")
    if not folge:
        for zeile in text.split("\n"):
            m = OEFFNUNG.match(zeile)
            if m:
                print(f"  verbotene Eroeffnungsform: {m.group(1)}"); fehler += 1
    for m in IN_THIS_CLIP.finditer(text):
        zeige(text, m, "'in this clip' - mag er nicht"); fehler += 1
    print("== gestrichene Formeln ==")
    for muster, grund in GESTRICHEN:
        for m in re.finditer(muster, text, re.I):
            zeige(text, m, grund); fehler += 1
    print("== Zeichen ==")
    for m in EM_DASH.finditer(text):
        zeige(text, m, "em dash - in Beschreibungen benutzt er den en dash"); fehler += 1

    rumpf = re.sub(r"[—–]", "-", text)
    woerter = len(re.findall(r"\b[\w'*]+\b", rumpf))
    lo, hi = (700, 900) if folge else (145, 190)
    print(f"\n== Laenge: {woerter} Woerter (sein Korridor {lo}-{hi}) ==")

    if folge:
        print("== Bullets (seine zwei Folgen: exakt 5, je 10-17 Woerter) ==")
        bul = [z.strip() for z in text.split("\n") if z.strip().startswith("\u2022")]
        if len(bul) != 5:
            print(f"  {len(bul)} Bullets statt 5"); fehler += 1
        for b in bul:
            n = len(b.split()) - 1
            if not 10 <= n <= 17:
                print(f"  Bullet mit {n} Woertern: {b[:60]}"); fehler += 1

    print("== Abbinder ==")
    if not folge and not re.search(r"\b\d+\s*(?:minutes|hours|hour)\b", text, re.I):
        print("  keine Laufzeit im Pitch"); fehler += 1
    if "…" not in text and "..." not in text:
        print("  keine Auslassungspunkte am Ende des Pitches"); fehler += 1

    print(f"\n{'KEIN TREFFER' if not fehler else str(fehler) + ' TREFFER'}")
    return fehler

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--folge"]
    folge = "--folge" in sys.argv
    q = args[0] if args else "-"
    t = sys.stdin.read() if q == "-" else open(q, encoding="utf-8").read()
    sys.exit(1 if pruefen(t, folge) else 0)
