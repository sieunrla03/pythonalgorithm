import os
import random

def generate_large_binary_file(file_path, file_size=50 * 1024 * 1024, pattern=b'\xDE\xAD\xBE\xEF', insert_count=10):
    # file_size: 파일 크기 (바이트 단위)
    # pattern: 삽입할 바이너리 패턴
    # insert_count: 삽입 횟수
    
    with open(file_path, "wb") as file:
        # 1. 랜덤한 바이너리 데이터로 파일 전체를 채운다
        file.write(os.urandom(file_size))

        # 2. 지정된 횟수만큼 랜덤한 위치에 패턴 삽입
        for _ in range(insert_count):
            position = random.randint(0, file_size - len(pattern))
            file.seek(position)
            file.write(pattern)

# 실행
generate_large_binary_file("large_data.bin", file_size=50 * 1024 * 1024, insert_count=10)
