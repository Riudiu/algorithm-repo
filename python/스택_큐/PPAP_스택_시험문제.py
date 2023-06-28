import sys
input = sys.stdin.readline

S = input().strip()
stack = []
ppap = ['P', 'P', 'A', 'P']

for c in S:
    stack.append(c)
    if stack[-4:] == ppap:  
        for _ in range(3):
            stack.pop() 

if stack == ppap or stack == ['P']:
    print("PPAP")
else: 
    print("NP")