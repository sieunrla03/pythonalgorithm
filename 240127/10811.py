# 백준 - 바구니 뒤집기
# 또현,,,,도현아 죽을래,,,,
N, M = map(int, input().split())
B = [0] * N
for x in range(N):
  B[x] = x+1
for x in range(M):
    i, j = map(int, input().split())
    temp = B[i-1:j]
    temp.reverse()
    B[i-1:j] = temp
for x in range(N):
    print(B[x], end = " ")