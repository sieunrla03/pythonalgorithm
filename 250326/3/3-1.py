import pickle
import os

FILENAME = "media_data.pkl"
VALID_TYPES = ['image', 'video', 'audio']

# media_data.pkl 파일이 이미 존재하는 경우 불러오기
if os.path.exists(FILENAME):
    try:
        with open(FILENAME, 'rb') as file:
            media_data = pickle.load(file)
    except Exception:
        media_data = {}
else:
    media_data = {} # 파일 없으면 빈 딕셔너리로 

print("멀티미디어 태그 관리 시스템")

while True:
    print("\n1. 콘텐츠 등록")
    print("2. 종료")
    
    try:
        choice = int(input("메뉴 선택 (1~2): "))
    except ValueError:
        print("숫자를 입력하세요.")
        continue

    if choice == 2:
        break
    elif choice != 1:
        print("1 또는 2를 선택하세요.")
        continue

    try:
        # 유효성 검사
        content_id = input("콘텐츠 ID 입력: ").strip()
        if not content_id:
            raise ValueError("ID는 빈 칸일 수 없습니다.") # 예외를 따로 else로 안하고 그냥 강제로 예외 두기- raise
        if content_id in media_data:
            raise ValueError("이미 존재하는 ID입니다.")
        
        title = input("제목 입력: ").strip()
        if not title:
            raise ValueError("제목은 빈 칸일 수 없습니다.")
        
        ctype = input("타입 (image/video/audio): ").strip().lower()
        if ctype not in VALID_TYPES:
            raise ValueError("타입은 image, video, audio 중 하나여야 합니다.")
        
        tags_input = input("태그 입력 (쉼표 구분): ").strip()
        if not tags_input:
            raise ValueError("태그는 빈 칸일 수 없습니다.")
        tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

        media_data[content_id] = {
            "title": title,
            "type": ctype,
            "tags": tags
        }

        # 파일에 저장
        with open(FILENAME, 'wb') as file:
            pickle.dump(media_data, file)

        print("데이터가 저장되었습니다.")
    # 오류 처리
    except ValueError as ve:
        print("입력 오류:", ve)
    except Exception as e:
        print("예상치 못한 오류 발생:", e)
