import sys 
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]

for a in arr:
    if LIS[-1] < a:
        LIS.append(a)
    else:
        idx = bisect_left(LIS, a)
        LIS[idx] = a

print(len(LIS))