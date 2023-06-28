import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
setArr = set(list(product(arr, repeat=M)))

answer = list(setArr)
answer.sort()
for a in answer:
    print(*a)