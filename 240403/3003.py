# 킹, 퀸, 룩, 비숍, 나이트, 폰
A = [1, 1, 2, 2, 2, 8]
N = list(map(int, input().split()))
# 필요한 개수에서 보유 개수를 뺌
for i in range(6): 
    print(A[i] - N[i], end = ' ')