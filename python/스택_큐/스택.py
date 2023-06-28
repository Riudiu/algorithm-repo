import sys
input = sys.stdin.readline

def checkCommend(str):
    if len(str) > 5:
        stack.append(int(str[5:]))
        
    elif str == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
        
    elif str == 'size':
        print(len(stack))
        
    elif str == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
        
    elif str == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])

N = int(input())
arr = [input().strip() for _ in range(0, N)]
stack = []

for a in arr:
    checkCommend(a)