import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [[0, 0]]
for _ in range(N):
    items.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):  # 감당할 수 있는 무게만큼만 
        weight = items[i][0]  # 물건의 무게
        value = items[i][1]  # 물건의 가치

        if weight <= j:  # 물건의 무게가 해당 열의 무게보다 작을 경우
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        else:  # 물건의 무게가 해당 열의 무게보다 클 경우
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])