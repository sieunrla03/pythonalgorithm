def split_binary_file(file_path, chunk_size=5 * 1024 * 1024):  # 기본 5MB 단위
    part_num = 1
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            part_filename = f"part_{part_num}.bin"
            with open(part_filename, "wb") as part_file:
                part_file.write(chunk)
            print(f"[+] Saved: {part_filename} ({len(chunk)} bytes)")
            part_num += 1

# 실행
split_binary_file("large_data.bin")