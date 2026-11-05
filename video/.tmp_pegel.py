import sys, subprocess, numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
pfad = sys.argv[1]
for mitte in [float(x) for x in sys.argv[2:]]:
    von, bis = mitte - 1.2, mitte + 1.2
    roh = subprocess.run([FF, "-nostdin", "-v", "error", "-ss", f"{von}", "-t", f"{bis-von}",
                          "-i", pfad, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(roh, dtype=np.float32)
    n = 16000 // 100  # 10 ms
    m = len(a) // n
    e = np.sqrt((a[:m*n].reshape(m, n)**2).mean(1)) + 1e-9
    db = 20*np.log10(e)
    print(f"=== um {mitte:.3f}")
    for i in range(m):
        t = von + i*0.01
        if i % 2: continue
        bar = "#" * max(0, int((db[i]+60)/2))
        print(f"  {t:9.3f} {db[i]:7.1f} {bar}")
