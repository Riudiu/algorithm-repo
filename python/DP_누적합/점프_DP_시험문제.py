import sys
input = sys.stdin.readline

N = int(input())
matrix = [[]] * N
for i in range(N):
    matrix[i] = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        jump = matrix[i][j]
        if jump == 0: continue    

        if not (i + jump) > (N - 1):
            dp[i + jump][j] += dp[i][j]

        if not (j + jump) > (N - 1): 
            dp[i][j + jump] += dp[i][j]

print(dp[-1][-1])