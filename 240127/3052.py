#백준 - 나머지
arr = []
for i in range(10):
    A = int(input())
    B = A % 42
    arr.append(B)
print(len(set(arr)))
'''
배열 선언을 좀,,,해라,,,ㅜㅠ
append함수도 좀 더 익숙해져야겠다.
그리고 여기서 처음 set()함수를 알았다. 이부분에 대해서 공부 더 하기
set은 수학에서 이야기하는 집합과 비슷하다
'''