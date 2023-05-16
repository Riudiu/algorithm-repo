import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(0, T):
    A, B = map(int, input().split())
    print(math.lcm(A, B))