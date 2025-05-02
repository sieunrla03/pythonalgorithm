import pickle

# 저장된 prob2-1.bat 파일에서 딕셔너리 로드
with open("prob2-1.bat", "rb") as file:
    data = pickle.load(file)

# 데이터 수정
data["python"] = "자바"

# 수정 후 다시 저장
with open("prob2-1.bat", "wb") as file:
    pickle.dump(data, file)

# 출력
for key, value in data.items():
    print(f"{key}: {value}")