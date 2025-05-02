def find_binary_pattern(file_path, pattern):
    positions = []
    offset = 0
    pattern_len = len(pattern)
    buffer = b''

    print(f"패턴 {pattern} 찾기...")

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break

            chunk = buffer + chunk  # 경계 고려
            index = chunk.find(pattern)

            while index != -1:
                real_pos = offset + index - len(buffer)
                positions.append(real_pos)
                index = chunk.find(pattern, index + 1)

            # 다음 chunk를 위한 buffer 저장
            if len(chunk) >= pattern_len - 1:
                buffer = chunk[-(pattern_len - 1):]
            else:
                buffer = chunk

            offset += len(chunk) - len(buffer)

    print(f"총 {len(positions)}회 발견됨.")
    print(f"위치: {positions}")

# 실행 예시
find_binary_pattern("large_data.bin", b'\xde\xad\xbe\xef')
