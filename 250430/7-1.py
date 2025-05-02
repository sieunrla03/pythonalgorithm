from PIL import Image
import os

# 이미지 파일 목록
image_files = ['5_Dcu.png', '5_sample.bmp', '5_nuts.jpg']

# 파일별 포맷 출력
for file in image_files:
    with Image.open(file) as img:
        print(f"{file} 파일은 {img.format} 포맷 이미지입니다.")
