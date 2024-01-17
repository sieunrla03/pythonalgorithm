#백준 - 코딩은 체육과목 입니다
'''
int 앞에 long이 붙으면 4바이트
long long int면 8바이트인거임
이런식으로 문제 풀기
예제 입력 20/ 예제 출력 long long long long long int
'''
N = int(input())
for i in range(N//4): #N//4 -> 몫,20이면 20//4 = 5 따라서 long 5개
    print("long", end = " ")
print("int")
'''
입력 받은 N을 4로 나누고, 그 결과만큼 반복하여 long을 출력해야하고
문제 조건에 따라서 중간에 공백을 두도록 end = " "추가
마지막으로 반복문 벗어나서 마지막에 int 출력
'''