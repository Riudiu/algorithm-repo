import sys
input = sys.stdin.readline

def lcs(x, y):
    x, y = ' ' + x, ' ' + y
    M, N = len(x), len(y)
    dp = [[0 for _ in range(N)] for _ in range(M)]

    for i in range (1, M):
        for j in range(1, N):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[M - 1][N - 1]

str1 = input().rstrip()
str2 = input().rstrip()
print(lcs(str1, str2))