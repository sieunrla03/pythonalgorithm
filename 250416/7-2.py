import wave
import numpy as np
from comp import compare_lowdata  # 동일 경로에 comp.py 필요

def extract_samples(filename):
    with wave.open(filename, 'rb') as wav:
        frames = wav.readframes(wav.getnframes())
        samples = np.frombuffer(frames, dtype=np.int16).tolist()
    return samples

samples = extract_samples('7_3seconds.wav')

# 비교 실행
print(compare_lowdata(samples))
