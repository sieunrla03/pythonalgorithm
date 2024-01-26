# 백준 - 공 넣기
N, M = map(int, input().split())
B = [0] * N # 0으로 초기화
for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i-1, j):
        B[y] = k
for y in range(N):
    print(B[y], end =" ")