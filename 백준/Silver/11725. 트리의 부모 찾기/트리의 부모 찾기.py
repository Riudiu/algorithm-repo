import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
        else:
            parent[v] = i
    
N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

visited = [False] * (N + 1)
dfs(1)

for i in range(2, N + 1):
    print(parent[i])