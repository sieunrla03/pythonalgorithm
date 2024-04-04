# 행렬 덧셈
N, M = map(int, input().split()) # 행렬의 크기 입력
A, B = [], [] # 합할 두 개의 행렬 선언

for i in range(N):
    i = list(map(int, input().split()))
    A.append(i)
for i in range(N):
    i = list(map(int, input().split()))
    B.append(i)
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = " ")
    print()
