# 세로읽기
word = [input() for _ in range(5)] # 2차원 배열 입력을 위해 for문으로 입력
result = '' # 공백 없이 연속해서 출력할 문자들이 들어갈 변수 result 선언

for i in range(15): # 한 줄에 단어가 최대 15개까지
    for j in range(5): # 총 단어가 5개
        if i <= len(word[j]) - 1: # 한줄에 입력한 글자들의 개수를 len() 함수로 구하고 range() 와의 차이를 반영해 -1 
            result += word[j][i]
print(result)