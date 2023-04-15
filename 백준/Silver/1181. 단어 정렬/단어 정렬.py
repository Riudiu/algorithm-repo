import sys

input = sys.stdin.readline

length = int(input())
N = [input().strip() for _ in range(length)]

N = list(set(N))

N.sort()
N.sort(key=len)

for n in N:
    print(n)