import os

# 랜덤 바이너리 파일 생성
def generate_random_binary_file(file_path, size=2048):
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size))
    print(f"{file_path} 생성 완료 ({size} bytes)")

# XOR 암호화/복호화 함수
def xor_encrypt(input_file, key, output_file):
    with open(input_file, "rb") as fin, open(output_file, "wb") as fout:
        while True:
            chunk = fin.read(4096)
            if not chunk:
                break
            encrypted = bytes([b ^ key for b in chunk])
            fout.write(encrypted)
    print(f"Complete : {output_file}")

# 결과 미리보기 함수
def print_binary_preview(file_path, num_bytes=64):
    with open(file_path, "rb") as f:
        data = f.read(num_bytes)
        print(f"{file_path} {num_bytes} Bytes:")
        print(data.hex(" "))
        print()
    return data

# 사용자 입력 및 전체 동작
def main():
    # XOR 키 입력
    xor_key = int(input("XOR key (0~255): "))

    # 파일 경로
    secret_file = "secret_data_2.bin"
    encrypted_file = "encrypted_data_2.bin"
    decrypted_file = "decrypted_data_2.bin"

    # 랜덤 파일 생성
    generate_random_binary_file(secret_file)

    # 암호화
    print("암호화 수행")
    print(f"input file : {secret_file}")
    print(f"output file : {encrypted_file}")
    print(f"input XOR key(0~255) : {xor_key}")
    xor_encrypt(secret_file, xor_key, encrypted_file)

    # 복호화
    print("\n복호화 수행")
    print(f"input file : {encrypted_file}")
    print(f"output file : {decrypted_file}")
    print(f"input XOR key(0~255) : {xor_key}")
    xor_encrypt(encrypted_file, xor_key, decrypted_file)

    # 결과 미리보기
    data_secret = print_binary_preview(secret_file)
    data_encrypted = print_binary_preview(encrypted_file)
    data_decrypted = print_binary_preview(decrypted_file)

    # 복호화 성공 여부 확인
    if data_secret == data_decrypted:
        print("복호화 성공")
    else:
        print("복호화 실패")

if __name__ == "__main__":
    main()