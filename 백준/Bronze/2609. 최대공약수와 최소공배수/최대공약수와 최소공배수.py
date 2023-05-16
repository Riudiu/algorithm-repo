import sys
import math
input = sys.stdin.readline

A, B = map(int, input().split())
print(math.gcd(A, B))  # 최대공약수
print(math.lcm(A, B))  # 최소공배수