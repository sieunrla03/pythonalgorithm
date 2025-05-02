import struct

with open("5_sample.bmp", "rb") as f:
    # BMP 파일 헤더
    header_field = f.read(2)                     # Magic number (2 bytes)
    file_size = struct.unpack("<I", f.read(4))[0]  # File size (4 bytes)
    f.read(4)  # reserved
    f.read(4)  # data offset

    # DIB Header (BITMAPINFOHEADER)
    dib_header_size = struct.unpack("<I", f.read(4))[0] # struct.unpack("<I", f.read(4))는 리틀 엔디언 형식으로 unsigned int(4바이트) 값을 읽는 방식
    width = struct.unpack("<I", f.read(4))[0]
    height = struct.unpack("<I", f.read(4))[0]
    f.read(2)  # color planes
    bits_per_pixel = struct.unpack("<H", f.read(2))[0] # "<H"는 2바이트짜리 unsigned short

    # Raw image size (next 4 bytes)
    raw_size = width * height * (bits_per_pixel // 8)

# 출력
print(f"Magic number : {header_field}")
print(f"File size : {file_size}")
print(f"Width : {width}")
print(f"Height : {height}")
print(f"bits : {bits_per_pixel}")
print(f"Raw size : {raw_size}")