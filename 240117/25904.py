#백준 - 영수증
'''
영수증에 구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액을 보고
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치여부 확인
'''
X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a, b = map(int,input().split())
    sum += a*b
if X==sum:
    print("Yes")
else:
    print("No")
'''
X = int(input())
N = int(input())이거랑 X ,N= int(input()) 이걸 같게 생각함..
X = int(input())
N = int(input()) 이거는 두 개의 입력 따로 각각 받는거고
X ,N= int(input()) 이건 한 번에 두 개의 값을 받는 것
이 문제의 경우는 첫 번째로 해야함
'''