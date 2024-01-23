# 프로그래머스 - n의 배수
def solution(num, n):
    answer = 0
    if (num%n == 0):
        answer = 1
    else:
        answer = 0
    return answer
'''
num n result
98 2 1
34 3 0
'''