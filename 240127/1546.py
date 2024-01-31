# 백준 - 평균
# 세준이 이색히...성적조작을...
N = int(input())
M = list(map(int, input().split()))
arr = max(M)
for i in range (N):
    M[i] = M[i]/arr*100
print(sum(M)/N)
