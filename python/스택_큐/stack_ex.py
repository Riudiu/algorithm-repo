class Stack:
    def __init__(self):
        self.arr = []
  
    def push(self, item):
        self.arr.append(item)

    def pop(self):
        if len(self.arr) == 0: return print('스택이 비어있습니다.')
        return self.arr.pop()
    
    def peek(self):
        if len(self.arr) == 0: return print('스택이 비어있습니다.')
        return self.arr[-1]
    
    def clear(self):
        self.arr = []
        
    def size(self):
        return len(self.arr)
  
stack = Stack() 

stack.push(3)
stack.push(7)
stack.push(5)
print(stack.arr)  # [3, 7, 5]
print(stack.pop()) # 5
print(stack.arr)  # [3, 7]
print(stack.peek())  # 7

stack.push(9)  
print(stack.arr)  # [3, 7, 9]

stack.clear()
print(stack.size())  # 0