import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.arr = []
  
    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()
    
K = int(input())
stack = Stack() 
answer = 0

for _ in range(0, K):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.push(n)

for value in stack.arr:
    answer += value

print(answer)