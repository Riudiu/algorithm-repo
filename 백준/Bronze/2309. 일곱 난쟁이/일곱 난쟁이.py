import sys
from itertools import combinations

input = sys.stdin.readline

H = [int(input()) for _ in range(9)]
combis = list(combinations(H, 7))
result = []

for c in combis:
    v_sum = 0
    for value in c:
        v_sum += value
    if v_sum == 100:
        result = list(c)

result.sort()

for r in result:
    print(r)