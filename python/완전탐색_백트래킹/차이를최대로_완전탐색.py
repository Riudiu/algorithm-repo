import sys
input = sys.stdin.readline

def permutation(arr, n):
    result = []
    if n == 0: return [[]]
    for i in range(len(arr)):
        e = arr[i]
        for rest in permutation(arr[:i] + arr[i + 1:], n - 1):
            result.append([e] + rest)
    return result

def calc_permus(arr):
    sum = 0
    for i in range(1, N):
        calc = arr[i - 1] - arr[i]
        if calc < 0:
            calc *= -1
        sum += calc
    absolutes.append(sum)

N = int(input())
A = list(map(int, input().split()))
absolutes = []
permutations = permutation(A, N)

for p in permutations:
    calc_permus(p)

print(max(absolutes))