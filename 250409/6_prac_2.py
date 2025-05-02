import wave
import numpy as np
import scipy.signal as signal

# 원본 오디오 파일 경로 및 이름 지정
input_file = '6_input_audio.wav'

# resampling 할 새로운 샘플링 주파수
new_sample_rate = 5000

# wave 모듈을 사용하여 원본 오디오 파일 읽기
with wave.open(input_file, 'rb') as wave_file:
    n_channels = wave_file.getnchannels()
    sample_width = wave_file.getsampwidth()
    sample_rate = wave_file.getframerate()
    n_frames = wave_file.getnframes()

    # 오디오 데이터를 numpy 배열로 읽어들임
    audio_data = wave_file.readframes(n_frames)
    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    # resample 함수를 사용하여 새로운 샘플링 주파수로 변환
    resampled_data = signal.resample(audio_data, int(len(audio_data) * float(new_sample_rate) / sample_rate))

# wave 모듈을 사용하여 새로운 오디오 파일 저장
output_file = 'resampled.wav'
with wave.open(output_file, 'wb') as wave_file:
    wave_file.setnchannels(n_channels)
    wave_file.setsampwidth(sample_width)
    wave_file.setframerate(new_sample_rate)
    wave_file.writeframes(resampled_data.astype(np.int16).tobytes())
