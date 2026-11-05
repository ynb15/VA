import sys, json, subprocess
import numpy as np
import imageio_ffmpeg
from faster_whisper import WhisperModel
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
pfad, modell, off = sys.argv[1], sys.argv[2], float(sys.argv[3])
roh = subprocess.run([FFMPEG, "-nostdin", "-v", "quiet", "-i", pfad,
                      "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                     capture_output=True, check=True).stdout
ton = np.frombuffer(roh, dtype=np.float32)
m = WhisperModel(modell, device="cpu", compute_type="int8")
seg, info = m.transcribe(ton, language="en", word_timestamps=True, vad_filter=False)
worte = []
for s in seg:
    for w in (s.words or []):
        if w.word.strip():
            worte.append({"t": round(w.start + off, 3), "e": round(w.end + off, 3), "w": w.word.strip()})
json.dump(worte, open("worte.json", "w"), ensure_ascii=False, indent=0)
print(len(worte), "Worte")
