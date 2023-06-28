import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    # 위치 벗어나면 False 리턴
    if x < -1 or x > (M - 1) or y < -1 or y > (N - 1):
        return False
    
    # 이미 방문했던 곳이라면 False 반환
    if visited[y][x] == True:
        return False
    
    visited[y][x] = True
    # 현재 index의 모양이 '-'일 경우
    if graph[y][x] == '-' and (x == (M - 1) or graph[y][x + 1] == '-'):
        dfs(x + 1, y) # 오른쪽 이동
    elif graph[y][x] == '|' and (y == (N - 1) or graph[y + 1][x] == '|'):
        dfs(x, y + 1) # 아래쪽 이동
    return True

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

visited = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(False)
    visited.append(temp)
    
answer = 0
for y in range(N):
    for x in range(M):
        if dfs(x, y) == True:
            answer += 1
            
print(answer)