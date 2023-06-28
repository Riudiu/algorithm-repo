import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split())) 
arr.sort()

answer = list(product(arr, repeat=M))
for a in answer:
    print(*a)