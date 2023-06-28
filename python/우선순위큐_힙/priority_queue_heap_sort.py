# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
# 파이썬의 경우 힙 자료구조는 기본적으로 최소 힙(min_heap)으로 지원함
import heapq
import sys
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(N):
    print(res[i])