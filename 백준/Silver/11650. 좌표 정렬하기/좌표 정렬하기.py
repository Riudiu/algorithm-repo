import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()
for a in arr:
    print(a[0], end=' ')
    print(a[1])