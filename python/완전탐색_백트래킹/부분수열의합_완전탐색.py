import sys
input = sys.stdin.readline

def dfs(start, temp):
    global cnt
    if len(temp) > 0 and sum(temp) == S:
        cnt += 1

    for i in range(start, N):
        temp.append(arr[i])
        dfs(i + 1, temp)
        temp.pop()

N, S = map(int, input().split())
arr = list(map(int,input().split()))
cnt = 0

dfs(0, [])
print(cnt)