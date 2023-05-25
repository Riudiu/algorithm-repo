import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

tuple_list = []
for i in range(N):
    tuple_list.append((arr[i], i + 1))

ans = 0
for a, b in tuple_list:
    ans += abs(a - b)

print(ans)