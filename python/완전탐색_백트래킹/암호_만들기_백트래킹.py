import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
arr = sorted(list(map(str, input().split())))
combis = list(combinations(arr, L))

for combi in combis:
    aeiou = 0
    rest = 0
    for c in combi:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            aeiou += 1
        else:
            rest += 1
    if aeiou > 0 and rest > 1:
        print(''.join(combi))
