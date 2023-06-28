import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split())) 
arr.sort()

answer = list(permutations(arr, M))
for a in answer:
    print(*a)