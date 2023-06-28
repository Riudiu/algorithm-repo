import sys
input = sys.stdin.readline

def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        e = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([e] + rest)
    return result

N, M = map(int, input().split())
arr = [n for n in range(1, N + 1)]
answer = combination(arr, M)

for a in answer:
    for value in a:
        print(value, end=' ')
    print()