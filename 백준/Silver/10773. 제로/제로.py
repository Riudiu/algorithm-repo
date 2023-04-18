import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.arr = []
  
    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()
    
    def getSum(self):
        return sum(self.arr)
    
K = int(input())
stack = Stack() 

for _ in range(0, K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.push(n)

print(stack.getSum())