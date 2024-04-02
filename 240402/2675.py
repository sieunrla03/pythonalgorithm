# 문자열 반복
S = int(input()) #테스트 케이스 개수
for _ in range(S):
    N, M = input().split()
    for i in range(len(M)):
        print(int(N) * M[i], end = '')#각 문자를 N번 반복해서 출력
    print() #한 테스트 케이스가 끝날 대마다 개행 출력