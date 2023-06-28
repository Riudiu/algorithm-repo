import sys
import math
input = sys.stdin.readline

A, B = map(int, input().split())
for _ in range(0, math.gcd(A, B)):
    print(1, end='')
