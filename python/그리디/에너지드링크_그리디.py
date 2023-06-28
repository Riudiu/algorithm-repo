import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

main = arr.pop()
for ed in reversed(arr):
    main += (ed / 2)

print(main)