import pickle

# 저장된 prob2-1.bat 파일에서 딕셔너리 로드
with open("prob2-1.bat", "rb") as file:
    data = pickle.load(file)

# 딕셔너리 전체 출력
for key, value in data.items():
    print(f"{key}: {value}")

# 사용자로부터 검색할 단어 입력
word = input("\nEnter the word to search : ").strip()

# 단어 검색 결과 출력
if word in data:
    print(f"meaning of '{word}' you searched for is '{data[word]}'")
else:
    print(f"'{word}' is a word that does not exist")
