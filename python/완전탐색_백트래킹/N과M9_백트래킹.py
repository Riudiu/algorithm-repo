import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
setArr = set(list(permutations(arr, M)))

answer = list(setArr)
answer.sort()
for a in answer:
    print(*a)