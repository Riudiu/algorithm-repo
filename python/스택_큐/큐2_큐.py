from collections import deque

import sys
input = sys.stdin.readline

def checkCommend(str):
    if len(str) > 5:
        queue.append(int(str[5:]))
        
    elif str == 'pop':
        if len(queue) == 0: print(-1)
        else: print(queue.popleft())
        
    elif str == 'size':
        print(len(queue))
        
    elif str == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
        
    elif str == 'front':
        if len(queue) == 0: print(-1)
        else: print(queue[0])

    elif str == 'back':
        if len(queue) == 0: print(-1)
        else: print(queue[-1])

N = int(input())
arr = [input().strip() for _ in range(0, N)]
queue = deque()

for a in arr:
    checkCommend(a)