import pickle
import os

FILENAME = "media_data.pkl"
VALID_TYPES = ['image', 'video', 'audio']

# 파일에서 데이터 불러오기
def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return {}
    return {}

# 데이터 저장
def save_data(data):
    with open(FILENAME, 'wb') as file:
        pickle.dump(data, file)

# 콘텐츠 등록
def register_content():
    data = load_data()
    content_id = input("콘텐츠 ID 입력: ").strip()
    if not content_id:
        print("ID는 빈 칸일 수 없습니다.")
        return
    if content_id in data:
        print("이미 존재하는 ID입니다.")
        return

    title = input("제목 입력: ").strip()
    if not title:
        print("제목은 빈 칸일 수 없습니다.")
        return

    ctype = input("타입 (image/video/audio): ").strip().lower()
    if ctype not in VALID_TYPES:
        print("타입은 image, video, audio 중 하나여야 합니다.")
        return

    tags_input = input("태그 입력 (쉼표 구분): ").strip()
    if not tags_input:
        print("태그는 빈 칸일 수 없습니다.")
        return
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

    data[content_id] = {
        "title": title,
        "type": ctype,
        "tags": tags
    }

    save_data(data)
    print("데이터가 저장되었습니다.")

# 태그로 검색
def search_by_tag():
    data = load_data()
    tag_input = input("검색할 태그 입력: ").strip().lower()
    found = False
    for cid, content in data.items():
        tags_lower = [tag.lower() for tag in content['tags']]
        if tag_input in tags_lower:
            print(f"- ID: {cid}, 제목: {content['title']}, 타입: {content['type']}, 태그: {content['tags']}")
            found = True
    if not found:
        print("해당 태그가 포함된 콘텐츠가 없습니다.")

# 콘텐츠 태그 수정
def edit_tags():
    data = load_data()
    content_id = input("수정할 콘텐츠 ID 입력: ").strip()
    if content_id not in data:
        print("해당 ID의 콘텐츠가 존재하지 않습니다.")
        return

    new_tags_input = input("새로운 태그 입력 (쉼표 구분): ").strip()
    if not new_tags_input:
        print("태그는 빈 칸일 수 없습니다.")
        return
    new_tags = [tag.strip() for tag in new_tags_input.split(',') if tag.strip()]
    data[content_id]['tags'] = new_tags
    save_data(data)
    print("데이터가 저장되었습니다.")
    print(f"{content_id}의 태그가 수정되었습니다.")

# 메인 메뉴
while True:
    print("\n멀티미디어 태그 관리 시스템")
    print("1. 콘텐츠 등록")
    print("2. 태그로 검색")
    print("3. 콘텐츠 태그 수정")
    print("4. 종료")

    try:
        choice = int(input("메뉴 선택 (1~4): "))
    except ValueError:
        print("숫자를 입력하세요.")
        continue

    if choice == 1:
        register_content()
    elif choice == 2:
        search_by_tag()
    elif choice == 3:
        edit_tags()
    elif choice == 4:
        break
    else:
        print("1~4 중에서 선택하세요.")

# 뭐 쳐도 다 없다나오는데 따로 다 등록을 해둬야하는거,,?