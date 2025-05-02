# 쉽게 푸는 문제
import sys

a, b = map(int, sys.stdin.readline().split())

temp = []

# b까지의 수열 만들기
for i in range(1, b + 1):
    for j in range(i):
        temp.append(i)

# 만든 수열의 a부터 b까지 더한 값을 출력
print(sum(temp[a - 1:b]))