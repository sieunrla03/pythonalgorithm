#백준 - 합
'''
n이 주어졌을 때, 1~n까지 합을 구하는 프로그램 작성
'''
n = int(input())
answer = 0
for i in range(1,n+1):
    answer += i
print(answer)
'''
answer = ''처음에 이렇게도 안썼고..그리고 저딴식으로 썼고..구글링 후에 answer = 0이라 씀
심지어 
for i in range(1,n+1):
    answer += i
    print(answer)
이렇게 해놨었음..야야 정신 차려!!
근데 내가 진짜 파이썬 함수에 대해서 더 공부해야겟다 느낀 점..
다른 사람의 풀이>>
print(sum(range(1, int(input())+1)))
ㅜㅠㅠㅠ
이렇게 쉬웠어..더 공부하자!
'''