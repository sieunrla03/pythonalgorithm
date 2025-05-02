# 복호화
N = int(input())
 
for _ in range(N):
    M = input().replace(' ', '')
    count_s = [0] * 26
 
    for i in M:
        count_s[ord(i) - 97] += 1
 
    if count_s.count(max(count_s)) > 1:
        print('?')
    else:
        print(chr(97 + count_s.index(max(count_s))))
