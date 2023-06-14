import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [[False] * N for _ in range(N)]
graph = []
virus = []

for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for j in range(len(arr)):
        if arr[j] != 0:
            virus.append([arr[j], j, i])
            visited[i][j] = True
virus.sort()
S, Y, X = map(int, input().split())

# LTRB
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque(virus)
    cnt = 0
    while q:
        if S == cnt:
            break
        for _ in range(len(q)):
            k, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > (N - 1) or ny < 0 or ny > (N - 1):
                    continue
                if visited[ny][nx] == True:
                    continue

                visited[ny][nx] = True
                graph[ny][nx] = k
                q.append([k, nx, ny])
        cnt += 1
        
bfs()
print(graph[Y - 1][X - 1])