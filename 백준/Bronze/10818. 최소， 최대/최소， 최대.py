import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
print(min(arr), end=' ')
print(max(arr), end=' ')