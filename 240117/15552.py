#백준 - 빠른 A+B
''' input 쓰지말고 sys.stdin.readline, 문자열 저장할 땐 .rstip()써서 문제 풀기
테스트케이스 개수 입력받고 계산할 정수 두 개 입력 후 덧셈 계산
'''
import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int,sys.stdin.readline().split())
    answer = a + b
    print(answer)
'''
두 개의 입력 한 번에 받을 때 제발..a, b = map(int,sys.stdin.readline().split())
이거 잊지마..!!!ㅜㅠㅠ
그리고
answer = a + b 말고 print(a + b)로 코드 줄이기도 가능하니까
최대한 코드 줄이기도 생각해보기!
'''