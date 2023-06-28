import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split())) 
arr.sort()

answer = list(combinations(arr, M))
for a in answer:
    print(*a)