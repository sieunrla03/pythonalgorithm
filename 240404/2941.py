# 크로아티아 알파벳
C  = ['c-', 'c=', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()
for i in C:
    N = N.replace(i, 'a')
print(len(N))
'''
replace 함수는 문자열을 변경하는 함수이다.
문자열안에서 특정 문자를 새로운 문자로 변경하는 기능
사용 방법은 '변수. replace(현재 문자열에서 변경할 문자, 새로 바꿀 문자, [변경할 횟수])' 형식으로 사용
문자를 변경하는 예시
>>> a = 'hello world'
>>> a.replace('hello','hi')
hi world
횟수를 써도 안써도 됨
'''