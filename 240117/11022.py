# 백준 - A+B-8
'''
이것도 덧셈 계산이지만 출력이 Case #1: a + b = c 이렇게 되어야 함
'''
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+':',a ,'+',b ,'=',a+b)