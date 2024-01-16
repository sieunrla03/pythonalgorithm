#프로그래머스 - 두 수의 연산값 비교하기
def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = 2 * int(str(a)) * int(str(b))
    if (num1 > num2):
        return num1
    else:
        return num2
    return answer