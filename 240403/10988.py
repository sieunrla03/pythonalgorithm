# 팰린드롬인지 확인하기
N = input()
if N == N[::-1]: # 뒤집어도 같다는 팰린드롬 확인하는 부분
    print("1")
else:
    print("0")