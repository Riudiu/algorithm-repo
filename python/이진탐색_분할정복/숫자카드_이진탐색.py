import sys
input = sys.stdin.readline

def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
arr1 = sorted(list(map(int, input().split())))

M = int(input())
arr2 = list(map(int, input().split()))

for t in arr2:
    print(binary(arr1, t, 0, len(arr1) - 1), end=' ')