#입력받는 방법은 추후에 배울 예정이므로 아래 코드를 그대로 사용하면 됩니다.
score = input().split()
kor = int(score[0])
eng = int(score[1])
math = int(score[2])

# 총합, 평균 계산
a = kor + eng + math
b = (a/3)
print(a)
print(b)