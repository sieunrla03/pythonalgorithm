# N번째 큰 수
T = int(input())
for i in range(T):
    A = list(map(int, input().split()))
    A.sort()
    print(A[-3])