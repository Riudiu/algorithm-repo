import sys
input = sys.stdin.readline

T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1   # 0원을 만들기 위한 경우의 수는 1

    for coin in coins:
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]  # DP 점화식
    
    answer.append(dp[M])

for a in answer:
    print(a)  