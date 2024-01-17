#백준 - A+B-3
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    answer = a+b
    print(answer)
'''
a, b = map(int, input().split()) 이 형태를 좀 생각하자..
map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 또는 tuple로 형 변환시켜줘야 함
map(적용시킬 함수, 적용할 값들)
'''

