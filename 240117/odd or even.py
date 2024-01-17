# 프로그래머스 - 홀짝에 따른 다른 값 반환하기
'''
양의 정수 n이 매개변수로 주어질 때, 
n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
'''
def solution(n):
    answer = 0
    if n % 2 ==  1:
        for i in range(1, n+1):
            if i%2==1:
                answer += i
    else:
        for i in range(1, n+1):
            if i%2==0:
                answer += int(i*i)
    return answer
'''
다른 사람의 풀이>>
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)
개쩌는거 같긴 한데 나는 이해못하는중..

'''