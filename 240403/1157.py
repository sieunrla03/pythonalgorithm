# 단어 공부
N = input().upper()
M = list(set(N)) # M의 요소를 하나씩 확인, N 배열에 같은 요소가 몇개 있는 지 확인
count = [] # 그리고 count 배열에 담아준다
for i in M:
    count.append(N.count(i)) # M의 요소를 하나씩 확인해, N 배열 안에 같은 요소의 수를 M 배열에 넣음
if count.count(max(count)) > 1: # count 배열안의 숫자가 최대인 것이 가장 많이 등장한 알파벳이다, -> max함수 이용
    print("?") # 최댓값이 2개 이상이면 ?를 출력
else:
    index = count.index(max(count)) # count 배열과 M배열의 index가 일치하기 때문에 count의 max값의 index값을 찾아서 M 출력
    print(M[index])