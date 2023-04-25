import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt
    global answer

    visited[v] = True
    cnt += 1
    if v == tn2:
        answer = cnt
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    cnt -= 1  # 더 이상 방문하지 않은 연결 노드가 없어서 위로 돌아올시 cnt 빼주기

N = int(input())
tn1, tn2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

answer = 0
cnt = 0
visited = [False] * (N + 1)

dfs(graph, tn1, visited)
print(answer - 1)