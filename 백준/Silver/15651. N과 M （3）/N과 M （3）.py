import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [n for n in range(1, N + 1)]

answer = list(product(arr, repeat=M))
for a in answer:
    print(*a)