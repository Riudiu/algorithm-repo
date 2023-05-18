import sys
import math
input = sys.stdin.readline

prime = [False, False] + [True] * 1000000
for i in range(2, int(math.sqrt(1000000)) + 1):
    if prime[i]:
        j = 2
        while i * j <= 1000000:
            prime[i * j] = False
            j += 1

M, N = map(int, input().split()) 

for i in range(M, N + 1):
    if prime[i]:
        print(i)
    