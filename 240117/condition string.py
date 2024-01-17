# 프로그래머스 - 조건 문자열
'''
">", "=" : n >= m
"<", "=" : n <= m
">", "!" : n > m
"<", "!" : n < m
두 문자열 ineq와 eq가 주어집니다. 
ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 
그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.
'''
def solution(ineq, eq, n, m):
    if eq == "!":
        if ineq == ">":
            return int(n>m)
        else:
            return int(n<m)
    else:
        if ineq == ">":
            return int(n>=m)
        else:
            return int(n<=m)