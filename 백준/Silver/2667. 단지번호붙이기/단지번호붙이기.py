import sys
from collections import deque
input = sys.stdin.readline

# LTRB
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > (N - 1) or ny > (N - 1):
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]

for _ in range(N):
    arr = list(map(int, input().rstrip()))
    graph.append(arr)

ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for a in ans:
    print(a)