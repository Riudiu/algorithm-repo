import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()

def check(txt):
    if txt[:4] == "push":
        _, x = txt.split()
        q.append(x)
    if txt == "pop":
        if len(q) == 0: print(-1)
        else:
            x = q.popleft()
            print(x)
    if txt == "size":
        print(len(q))
    if txt == "empty":
        if len(q) == 0: print(1)
        else: print(0)
    if txt == "front":
        if len(q) == 0: print(-1)
        else: print(q[0])
    if txt == "back":
        if len(q) == 0: print(-1)
        else: print(q[-1])

for _ in range(N):
    check(input().rstrip())
