import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0

for n in reversed(arr):
    if K < n: continue
    cnt += K // n
    K %= n

print(cnt)