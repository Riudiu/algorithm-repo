import sys
input = sys.stdin.readline
from collections import deque

# LTRB
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]   

def bfs(x, y):
    queue = deque()    
    queue.append((x, y))
    visited[y][x] = True

    # 큐가 빌때까지
    while queue:
        x, y = queue.popleft()
        
        # 4가지 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기에 체크
            if nx < 0 or nx > (M - 1) or ny < 0 or ny > (N - 1):
                continue

            # 벽이므로 진행 불가
            if graph[ny][nx] == 0:
                continue

            # 방문한 적 있으면 건너뛰기
            if visited[ny][nx] == True:
                continue
            
            visited[ny][nx] = True
            graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))
    
    return graph[N - 1][M - 1]

N, M = map(int, input().split())

graph = [] 
for _ in range(N):
    graph.append(list(map(int, input().strip())))
 
visited = []
for _ in range(N):
    temp = []
    for _ in range(M):
        temp.append(False)
    visited.append(temp)

print(bfs(0, 0))