import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = [[]] * N
for i in range(N):
    idx, start, end = map(int, input().split())
    lectures[i] = [start, end, idx]

lectures.sort(key=lambda x:x[0])
pq = []
room = []
K = 0
for start, end, idx in lectures:
    room_num = K + 1
    if len(pq) > 0:
        if start >= pq[0][0]:
            pl = heapq.heappop(pq)    
            room_num = pl[3]
            room.append(pl)
    heapq.heappush(pq, [end, start, idx, room_num])    
    if len(pq) > K: 
        K = len(pq)

for l in pq:
    room.append(l)
room.sort(key=lambda x:x[2])

print(K)
for i in range(len(room)):
    print(room[i][3])
