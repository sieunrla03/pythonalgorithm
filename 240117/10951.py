# 백준 - A+B-4
'''
이건 따로 뭐 조건도 없고 break를 어떻게 달라는거지..
두 정수를 입력받고 A+B를 출력하는 프로그램을 작성하라고만 되어 있음
'''
while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

'''
알고보니 테스트케이스가 더 이상 들어오지 않을 때 break해야하는 것이였다.
그렇기 때문에 try excetp구문을 사용해야했다.
try는 안의 코드를 시도하는 것
except는 try코드가 안될 경우 except 안의 명령어를 수행하라는 것
문제의 의도도 잘 파악할 수 있는 능력을 길러야할 듯 하다..
'''