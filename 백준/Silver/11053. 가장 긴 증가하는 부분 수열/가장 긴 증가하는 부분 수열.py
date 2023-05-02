import sys
input = sys.stdin.readline

N = int(input())
arr = [0]
arr += list(map(int, input().split()))

dp = [1] * (N + 1)
for i in range(2, N + 1):
    temp = 0
    for j in range(1, i):
        if arr[i] > arr[j]:
            if temp < dp[j]:
                temp = dp[j]
    dp[i] = temp + 1

print(max(dp))