# 다이얼
dial = ['ABC', 'DEF', 'GHI','KJL','MNO', 'PQRS', 'TUV', 'WXYZ']
N = input()
result = 0 # 결과값 저장할 변수를 초기화
for J in range(len(N)):
    for i in dial: # 현재 검사 중인 문자가 어떤 다이얼에 속하는 지 확인
        if N[J] in i: # 헤딩 다이얼 인덱스를 dial리스트에서 찾아 result에 추가
            result += dial.index(i) +3
print(result)