import sys
from bisect import bisect_left, bisect_right 
input = sys.stdin.readline

N = int(input())
have = sorted(list(map(int, input().split())))

M = int(input())
find = list(map(int, input().split()))

for m in find:
    print(bisect_right(have, m) - bisect_left(have, m), end=' ')