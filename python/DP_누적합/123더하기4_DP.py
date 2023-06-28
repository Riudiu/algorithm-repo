import sys
input = sys.stdin.readline

N = int(input())
n_list = []

for _ in range(N):
    n_list.append(int(input()))

dp = [0, 1, 2, 3]

for i in range(4, max(n_list) + 1):
    calc = dp[i - 1] + dp[i - 2] - dp[i - 3]
    if(i % 3 == 0):
        calc += 1
    dp.append(calc)

for n in n_list:
    print(dp[n])