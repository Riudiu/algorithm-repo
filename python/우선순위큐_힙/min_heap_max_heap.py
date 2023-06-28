import heapq

heap = []

# 최소 힙 (min heap)
# 아래 for문을 실행하고 나면 heap은 [1,2,3,5,4]로 힙 정렬이 되게 된다.
for i in range(1,6):
	heapq.heappush(heap, i)

# 작은 숫자 순서대로 1,2,3,4,5가 출력된다.
for i in range(5):
	print(heapq.heappop(heap))

heap = []
values = [1,5,3,2,4]

# 최대 힙 (max heap)
# 파이썬의 경우 힙 자료구조는 기본적으로 최소 힙(min_heap)으로 지원하므로 (-)를 앞에 넣어준다
# 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
for value in values:
	heapq.heappush(heap, -value)

# 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
for i in range(5):
	print(-heapq.heappop(heap))