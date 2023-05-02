import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
setArr = set(list(combinations_with_replacement(arr, M)))

answer = list(setArr)
answer.sort()
for a in answer:
    print(*a)