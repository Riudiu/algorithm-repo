import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(7):
    score = float(input().rstrip())
    heapq.heappush(pq, -score)  # 최대 힙으로

for _ in range(N - 7):  # 7명 이후의 학생 수만큼 반복
    score = float(input().rstrip())
    popScore = -heapq.heappop(pq)
    if score < popScore:  # 최대 힙의 가장 큰 수와 비교해서 더 작을 경우에
        heapq.heappush(pq, -score)  # 점수 push
    else:
        heapq.heappush(pq, -popScore)  # pop한 점수 push

answer = []
for _ in range(7):
    answer.append(-heapq.heappop(pq))

answer.sort()

for a in answer:
    print(f'{a :.3f}')