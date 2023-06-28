import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [n for n in range(1, N + 1)]

answer = list(combinations_with_replacement(arr, M))
for a in answer:
    print(*a)