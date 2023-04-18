import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.arr = []
  
    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()
    
def check_VPS(str):
    stack = Stack()

    for c in str:
        stack.push(c)
    length = len(stack.arr)

    PS_right = 0
    for _ in range(0, length):
        if(PS_right < 0): break
        pop_c = stack.pop()

        if pop_c == ')':
            PS_right += 1
        else:
            PS_right -= 1 

    if PS_right == 0:
        print('YES')
    else:
        print('NO')

if __name__== "__main__":
    T = int(input())
    arr = [input().strip() for _ in range(0, T)]

    for a in arr:
        check_VPS(a)