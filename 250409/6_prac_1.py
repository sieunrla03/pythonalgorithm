import wave

# 분석할 오디오 파일
file_name = '6_input_audio.wav'

# wave 모듈로 파일 열기
with wave.open(file_name, 'rb') as wav_file:
    channels = wav_file.getnchannels()           # 채널 수
    sampwidth = wav_file.getsampwidth()          # 샘플 폭 (바이트)
    framerate = wav_file.getframerate()          # 샘플링 레이트
    nframes = wav_file.getnframes()              # 총 프레임 수

    duration = nframes / float(framerate)        # 재생 시간 (초)

    # 출력
    print(f'Channels : {channels}')
    print(f'Width : {sampwidth}')
    print(f'original frame rate : {framerate}')
    print(f'num frames : {nframes}')
    print(f'Duration : {duration:.1f}')
