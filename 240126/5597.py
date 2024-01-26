# 백준 - 과제 안 내신 분..?
students = [i for i in range(1,31)] #1~30까지 숫자를 만들어준다
for x in range(28): #28번까지 반복하는 for문
    students.remove(int(input())) # 입력받은 숫자는 리스트에서 제거
for x in students: # 리스트에 남아있는 숫자들을 최종적으로 출력
    print(x)
'''
list(range(1, 31)) 이렇게도 선언 가능
remove를 사용해서 제거할 수 있다는 것, 중요
'''