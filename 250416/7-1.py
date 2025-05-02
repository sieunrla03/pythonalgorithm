import struct

def parse_wave_raw(filename):
    with open(filename, 'rb') as wav_file:
        # Main Header
        chunk_id = wav_file.read(4)
        chunk_size = struct.unpack('<I', wav_file.read(4))[0]
        wav_format = wav_file.read(4)

        # Sub Chunk 1
        sub_chunk_1_id = wav_file.read(4)
        sub_chunk_1_size = struct.unpack('<I', wav_file.read(4))[0]
        audio_format = struct.unpack('<H', wav_file.read(2))[0]
        num_channels = struct.unpack('<H', wav_file.read(2))[0]
        sample_rate = struct.unpack('<I', wav_file.read(4))[0]
        byte_rate = struct.unpack('<I', wav_file.read(4))[0]
        block_align = struct.unpack('<H', wav_file.read(2))[0]
        bits_per_sample = struct.unpack('<H', wav_file.read(2))[0]

        # Sub Chunk 2 
        sub_chunk_2_id = wav_file.read(4)
        sub_chunk_2_size = struct.unpack('<I', wav_file.read(4))[0]

        #  Sample Reading
        samples = []
        bytes_per_sample = bits_per_sample / 8
        sample_count = int(sub_chunk_2_size / bytes_per_sample)

        for _ in range(sample_count):
            sample = wav_file.read(int(bytes_per_sample))
            samples.append(sample)

        # Assertions 
        assert chunk_size == (
            len(wav_format) +
            len(sub_chunk_1_id) + sub_chunk_1_size + 4 +
            len(sub_chunk_2_id) + sub_chunk_2_size + 4
        ), chunk_size

        assert sub_chunk_1_size == (
            2 + 2 + 4 + 4 + 2 + 2
        ), sub_chunk_1_size

        assert byte_rate == (
            sample_rate * num_channels * bytes_per_sample
        ), byte_rate

        assert block_align == (
            num_channels * bytes_per_sample
        ), block_align

        assert sub_chunk_2_size == (
            len(samples) * bytes_per_sample
        ), sub_chunk_2_size

        length_in_seconds = len(samples) / sample_rate

        # 결과 출력 
        print("chunk_id:", chunk_id)
        print("wav_format:", wav_format)
        print("sample_rate:", sample_rate)
        print("byte_rate:", byte_rate)
        print("chunk_size:", chunk_size)
        print("length_in_seconds:", length_in_seconds)

# 실행
parse_wave_raw('7_3seconds.wav')
