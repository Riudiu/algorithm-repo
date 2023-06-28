import sys 
import math 
input = sys.stdin.readline

prime = [False, False] + [True] * 10000
for i in range(2, int(math.sqrt(10000)) + 1):
    if prime[i]:
        j = 2
        while i * j <= 10000:
            prime[i * j] = False
            j += 1

T = int(input())

for _ in range(T):
    n = int(input())
    a = b = n // 2
    while a > 0: 
        if prime[a] and prime[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1