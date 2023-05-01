import sys
input = sys.stdin.readline

N = int(input())

d = list(map(int, input().split()))
for _ in range(N - 1):
    r, c = map(int, input().split())
    d.append(c)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for diff in range(1, N):  # diff - 1부터 N까지의 격차 / N이 4일 경우 -> (1,2) - (2,3) - (3,4) - (1,3) - (2,4) - (1,4)
     for i in range(1, N - diff + 1):
        j = i + diff
        
        if i == j:  # 조건 1: 서로 같은 경우 -> 0, dp테이블에 이미 0으로 초기화 된 상태이므로 건너뛰기
            continue

        # 조건 2: i보다 j가 클 경우
        dp[i][j] = float('inf')  # 무한으로 먼저 세팅
        for k in range(i, j):  # k의 범위 - i ≤ k ≤ j-1
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (d[i - 1] * d[k] * d[j]))

print(dp[1][N])
