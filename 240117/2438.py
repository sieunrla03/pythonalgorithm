#백준 - 별찍기 - 1
'''
대망의 별찍기...! 
첫째줄부터 N번쨰 줄까지 차례대로 별 출력
5입력하고
*
**
***
****
***** 나오게 출력
'''
N = int(input())
for i in range(1, N+1):
    print("*" * i)
