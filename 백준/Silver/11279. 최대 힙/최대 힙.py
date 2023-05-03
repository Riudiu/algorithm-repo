import sys
import heapq
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(pq) == 0:
            print(0)
            continue
        else:
            print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -num)