import sys 
import math 
input = sys.stdin.readline

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    a, b = n // 2, n // 2
    while a > 0: 
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
       