import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) 

distance = [0] * (N + 1)
visited = [False] * (N + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0

    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[v] + 1

bfs(X)

if distance.count(K) == 0:
    print(-1)
else:
    for i in range(N + 1):
        if distance[i] == K:
            print(i)