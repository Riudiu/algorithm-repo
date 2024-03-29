import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0] * (M + 1)]
for _ in range(N):
    arr = [0] + list(map(int, input().split()))
    matrix.append(arr)

dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1])