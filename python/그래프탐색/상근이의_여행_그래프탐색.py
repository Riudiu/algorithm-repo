import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(start):
    v_count = 0
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                v_count += 1

    return v_count

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1))
