import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
combis = list(combinations(arr, 3))

ans = 0
for i in range(len(combis)):
    tmp = 0
    for c in combis[i]:
        tmp += c
    if tmp <= M and tmp > ans:
        ans = tmp
        
print(ans)