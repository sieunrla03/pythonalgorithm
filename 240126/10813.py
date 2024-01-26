# 백준 - 공 바꾸기
N, M = map(int,input().split())
B = [0] * N
temp = 0
for x in range(N):
  B[x] = x+1
for x in range(M):
    i, j = map(int, input().split())
    temp = B[i-1]
    B[i-1] = B[j-1]
    B[j-1] = temp
for x in range(N):
    print(B[x], end = " ")
'''
파이썬 배열에서 0부터 시작하는걸 알고 +1 해주는 걸 좀 기본적으로 생각하길
처음에
for x in range(N):
  B[x] = x+1
이 부분을 빼먹어서인지 결과값이 0 0 0 0 0이 나옴
그리고 첨에 temp = 0 이것도 안했다ㅏ,,,
'''