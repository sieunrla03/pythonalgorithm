# 백준 - A+B-7
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성해라
출력에서 각 테스트 케이스마다 Case #x를 출력한 다음 A+B를 출력
'''
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+':',a+b)
'''
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i} : {a+b}')
처음에 이렇게 코드를 짰는데 case #0부터 출력이 되길래 i+1을 해줬는데
이렇게가 아니라 
T = int(input())
for i in range(1,T+1):
    a, b = map(int, input().split())
    print(f'Case #{i} : {a+b}')
이렇게가 더 좋은 방법인 듯하다.
print(f'Case #{i+1} : {a+b}') 이것도 생각하기!"", ""이런식도 좋지만 헷갈리니까
저 방법으로 문제에 적용할 것!
근데 저게 틀렸습니다가 자꾸 나옴..왜지..
i가..정수니까..str로 문자열로 바꿔줘야햇다...왜..?대체 왜...?
그럼 문제에 적시를 해줘야지,,
'''