import sys, av, numpy as np
pfad, off = sys.argv[1], float(sys.argv[2])
c = av.open(pfad); v = c.streams.video[0]
prev = None; diffs = []
for f in c.decode(v):
    t = float(f.pts * v.time_base)
    g = f.to_ndarray(format="gray")[::8, ::8].astype(np.float32)
    if prev is not None:
        diffs.append((t + off, float(np.abs(g - prev).mean())))
    prev = g
c.close()
werte = sorted(d for _, d in diffs)
ruhe = float(np.median(werte))
schwelle = max(6 * ruhe, 6.0)
print(f"Ruhepegel {ruhe:.2f}, Schwelle {schwelle:.2f}")
for t, d in diffs:
    if d >= schwelle:
        print(f"  {t:9.4f}   {d:6.2f}")
