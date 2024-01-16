#프로그래머스 - 더 크게 합치기
def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    if (num1 > num2):
        return num1
    else:
        return num2  