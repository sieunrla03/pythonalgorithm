# 백준 - A+B-5
'''
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.
입력의 마지막에는 0 두 개가 들어온다
'''
while 1:
    a, b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)
'''
while 1해도 되고 while True해도 된다.
break뒤에 콜론 안붙임
'''