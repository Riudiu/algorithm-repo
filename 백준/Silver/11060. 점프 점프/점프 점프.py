import sys
input = sys.stdin.readline

N = int(input())
jumps = list(map(int, input().split()))

dp = [N] * N
dp[0] = 0

for i in range(N):
    for j in range(jumps[i]):
        if i + j + 1 >= N: break
        dp[i + j + 1] = min(dp[i + j + 1] , dp[i] + 1)

if dp[-1] == N:
    print(-1)
else:
    print(dp[-1])