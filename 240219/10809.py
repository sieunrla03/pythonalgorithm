# 알파벳 찾기
s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in alpha:
    print(s.find(i), end = ' ')
'''
a~z까지 문자열로 넣고 반복문을 돌린다.
find()함수를 사용하면 위치를 찾아낼 수 있다.
'''