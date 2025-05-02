import pickle
import os
import shutil

FILENAME = "media_data.pkl"
BACKUP_FILENAME = "media_data_backup.pkl"

# 데이터 불러오기
def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'rb') as file:
                return pickle.load(file)
        except Exception:
            print("파일을 불러올 수 없습니다.")
    return {}

# 데이터 저장 (백업 포함)
def save_data(data):
    if os.path.exists(FILENAME):
        shutil.copy(FILENAME, BACKUP_FILENAME)  # 백업 생성
    with open(FILENAME, 'wb') as file:
        pickle.dump(data, file)

# 전체 콘텐츠 출력
def show_all_contents():
    data = load_data()
    if not data:
        print("저장된 콘텐츠가 없습니다.")
        return

    print("전체 콘텐츠 목록:")
    for cid, content in data.items():
        print(f"- ID: {cid}, 제목: {content['title']}, 타입: {content['type']}, 태그: {content['tags']}")

# 예시: 전체 보기 호출
if __name__ == "__main__":
    print("1. 전체 콘텐츠 보기")
    print("2. 샘플 저장 테스트 (백업 발생)")
    print("3. 종료")
    choice = input("메뉴 선택 (1~3): ")

    if choice == '1':
        show_all_contents()
    elif choice == '2':
        # 테스트용 샘플 데이터 저장 (백업 생성됨)
        sample_data = {
            "sample001": {
                "title": "샘플 영상",
                "type": "video",
                "tags": ["sample", "video"]
            }
        }
        save_data(sample_data)
        print("샘플 데이터를 저장했습니다 (백업 파일 생성됨).")
    elif choice == '3':
        print("종료합니다.")
    else:
        print("올바른 메뉴를 선택하세요.")