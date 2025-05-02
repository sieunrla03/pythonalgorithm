# 피아노 체조
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

res = [0] * n
for i in range(len(data)-1):
    if data[i+1] < data[i]:
        res[i]=1

prefix_sum = [0] * (n+1)
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i-1] + res[i-1]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(prefix_sum[j-1] - prefix_sum[i-1])