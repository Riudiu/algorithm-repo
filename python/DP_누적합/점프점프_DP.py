import sys
input = sys.stdin.readline

N = int(input())
jumps = list(map(int, input().split()))

dp = [N] * N
dp[0] = 0

for i in range(N):
    for j in range(1, jumps[i] + 1):
        if i + j >= N: break
        dp[i + j] = min(dp[i + j] , dp[i] + 1)

if dp[-1] == N:
    print(-1)
else:
    print(dp[-1])