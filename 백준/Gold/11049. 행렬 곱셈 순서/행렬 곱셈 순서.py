import sys
input = sys.stdin.readline

N = int(input())
d = list(map(int, input().split()))
for _ in range(N - 1):
    _, c = map(int, input().split())
    d.append(c)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for diff in range(1, N):  # diff - 1부터 N까지의 격차 / N이 4일 경우 -> (1,2) - (2,3) - (3,4) - (1,3) - (2,4) - (1,4)
     for i in range(1, N - diff + 1):
        j = i + diff
        
        if i == j: 
            continue

        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (d[i - 1] * d[k] * d[j]))

print(dp[1][N])
