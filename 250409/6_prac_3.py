import wave
import audioop

# 원본 wav 파일 열기
input_file = '6_input_audio.wav'
wav_file = wave.open(input_file, 'rb')

# 기존 파라미터 추출
n_channels = wav_file.getnchannels()
sampwidth = wav_file.getsampwidth()
framerate = wav_file.getframerate()
n_frames = wav_file.getnframes()
audio_data = wav_file.readframes(n_frames)
wav_file.close()

# 변경 전 샘플링 레이트 출력
print("변경 전")
print("Sample rate:", framerate)

# 변경할 샘플링 레이트 설정
new_framerate = 11025

# 샘플링 레이트 변경 (resample)
resampled_data, _ = audioop.ratecv(audio_data, sampwidth, n_channels,
                                   framerate, new_framerate, None)

# 새 파일로 저장
output_file = 'example_resampled.wav'
with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(n_channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(new_framerate)
    wf.writeframes(resampled_data)

# 변경 후 샘플링 레이트 출력
print("변경 후")
print("Sample rate:", new_framerate)
