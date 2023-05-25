import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

ans = 0
for i in range(N):
    ans += abs((i + 1) - arr[i])

print(ans)