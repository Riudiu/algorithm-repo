import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
arr1 = sorted(list(map(int, input().split())))

M = int(input())
arr2 = list(map(int, input().split()))

for t in arr2:
    print(bisect_right(arr1, t) - bisect_left(arr1, t), end=' ')