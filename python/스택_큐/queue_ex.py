from collections import deque

class Queue:
    def __init__(self):
        self.arr = deque()
  
    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        if len(self.arr) == 0: return print('큐가 비어있습니다.')
        return self.arr.popleft()
    
    def peek(self):
        if len(self.arr) == 0: return print('큐가 비어있습니다.')
        return self.arr[0]

    def clear(self):
        self.arr = deque()
        
    def size(self):
        return len(self.arr)
    
queue = Queue() 

queue.enqueue(3)
queue.enqueue(7)
queue.enqueue(5)
queue.enqueue(1)
print(queue.arr)  # deque([3, 7, 5, 1])
queue.dequeue() 
print(queue.arr)  # deque([7, 5, 1])

queue.dequeue() 
queue.enqueue(9)  
print(queue.arr)  # deque([5, 1, 9])
print(queue.peek())  # 5

queue.clear()
print(queue.arr)  # deque([])
queue.enqueue(9)  
print(queue.arr)  # deque([9])
print(queue.size())  # 1