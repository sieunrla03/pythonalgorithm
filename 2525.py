#백준 - 오븐 시계
a, b = map(int, input().split())
c = int(input())
a += c//60
b += c%60
if(b>=60):
    a+=1
    print(a%24,b-60)
else:
    print(a%24,b)
"""
처음에 접근 잘못하고 하나하나 세세하게 접근해가지고 에러가 떴었는데
역시..난 바보였나봐ㅜ
일단 코드정리를 해보자면,
필요한 시간을 받아서 그 시간의 몫과 나머지를 각각 시와 분에 더한다.
그리고 그 결과에서 분으로 조건문if를 사용하는데
분b가 60보다 크거나 같으면 시에 +1이 되고 결과로 시를 24로 나눈 나머지, 분에서 -60을 한 갑이 정답이 되고
분b가 60보다 작으면 시를 24로 나눈 나머지, b는 그대로 출력된다.

"""