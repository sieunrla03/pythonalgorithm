# 최소 힙
# 시간복잡도는 O(log2n)
import sys
import heapq

n = int(input())
heap = [] # 배열

#Max Heap
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)