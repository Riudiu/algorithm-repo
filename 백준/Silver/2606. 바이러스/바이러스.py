from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global answer
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                answer += 1

N = int(input())
E = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(E):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
bfs(1)

print(answer)