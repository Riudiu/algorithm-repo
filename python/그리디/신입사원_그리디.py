import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        A, B = map(int, input().split())
        arr.append([A, B])
    arr.sort()
    
    cnt = 1
    standard = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][1] < standard:
            cnt += 1
            standard = arr[i][1]
    print(cnt)