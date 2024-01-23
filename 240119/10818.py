# 백준 - 최소, 최대
'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''
N = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[0],arr[-1])
'''
처음엔 
N = int(input())
arr = list(map(int,input().split()))
print(min(arr), max(arr)) 로 풀었었는데
이것도 좋지만 좀 더 다른식의 접근도 좋을 것 같아서 다르게 풀어보았다.
arr.sort()로 오름차순으로 정렬해주고
그리고 리스트 인덱싱으로 최소값은[0], 최대값은[-1]로 찾아 출력하도록 풀었다.
'''