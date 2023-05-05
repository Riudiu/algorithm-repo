import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]
arr += list(map(int, input().split()))
dp = [0] * (N + 1)

for x in range(N + 1):
    dp[x] = dp[x - 1] + arr[x]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])