import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# group = 1 or -1
def dfs(v, group):
    global result
    visited[v] = group
    for i in graph[v]:
        if not visited[i]:
            if(group == 1):
                dfs(i, -1)
            else:
                dfs(i, 1)
        else:
            if group == visited[i]:
                result = False

K = int(input())
answer = []

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True

    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i, 1)

        if result == False: break

    answer.append('YES' if result else 'NO')

for i in range(K):
    print(answer[i])