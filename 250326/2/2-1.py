import pickle

data = {
    "dictionary": "사전",
    "python": "파이썬",
    "Zoo": "동물원",
    "School": "학교",
    "University": "대학교"
}

# 딕셔너리를 바이너리 형식으로 파일에 저장 (encoding 제거)
with open("prob2-1.bat", "wb") as file:
    pickle.dump(data, file)

# 저장된 파일에서 다시 불러오기 (encoding 제거)
with open("prob2-1.bat", "rb") as file:
    loaded_data = pickle.load(file)

# 출력
for key, value in loaded_data.items():
    print(f"{key}: {value}")