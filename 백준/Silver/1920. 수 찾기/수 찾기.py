import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target: 
            start = mid + 1
        else:
            end = mid - 1
    return 0

if __name__== "__main__":
    length = int(input())
    N = list(map(int, input().split()))
    N.sort()

    length = int(input())
    M = list(map(int, input().split()))

    R = []

    for m in M:
        result = binary_search(N, m, 0, len(N) - 1)
        R.append(result)

    for r in R:
        print(r)