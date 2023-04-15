import sys

input = sys.stdin.readline

length = int(input())
N = [int(input()) for _ in range(length)] 

N.sort()

for n in N:
    print(n)