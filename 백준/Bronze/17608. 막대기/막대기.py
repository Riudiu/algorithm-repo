import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.arr = []
  
    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()
    
    def size(self):
        return len(self.arr)
    
N = int(input())
arr = [int(input()) for _ in range(0, N)]
stack = Stack()

for a in arr:
    stack.push(a)

len = stack.size()
standard = 0
answer = 0

for _ in range(0, len):
    pop_num = stack.pop()
    if pop_num > standard: 
        standard = pop_num
        answer += 1

print(answer)