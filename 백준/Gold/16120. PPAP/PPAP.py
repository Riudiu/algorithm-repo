import sys
input = sys.stdin.readline

S = input().strip()
stack = []
ppap = ['P', 'P', 'A', 'P']

for c in S:
    if stack[-4:] == ppap:  
        for _ in range(4):
            stack.pop() 
        stack.append('P')
    stack.append(c)

if stack == ppap or stack == ['P']:
    print("PPAP")
else: 
    print("NP")

