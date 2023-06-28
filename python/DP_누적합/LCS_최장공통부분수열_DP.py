import sys
input = sys.stdin.readline

# 바텀업 방식
def lcs(x, y):
    x, y = ' ' + x, ' ' + y
    M, N = len(x), len(y)
    dp = [[0 for _ in range(N)] for _ in range(M)]

    for i in range (1, M):
        for j in range(1, N):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # 대각선 기법
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[M - 1][N - 1]

str1 = input().rstrip()
str2 = input().rstrip()
print(lcs(str1, str2))


# 재귀로 구현할시(탑다운, 비효율적)
# def lcs(x, y):
#     M, N = len(x), len(y)
#     if M == 0 or N == 0:
#         return 0
#     else:¡
#         if x[-1] == y[-1]:
#             return lcs(x[:(M - 1)], y[:(N - 1)]) + 1
#         else:
#             return max(lcs(x[:M], y[:(N - 1)]), 
#                        lcs(x[:(M - 1)], y[:N]))
