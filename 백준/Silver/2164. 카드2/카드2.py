from collections import deque

import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.arr = deque()
  
    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.popleft()

    def size(self):
        return len(self.arr)
    
N = int(input())
queue = Queue() 

for i in range(1, N + 1):
    queue.enqueue(i)

while queue.size() > 1:
    queue.dequeue()
    pop_num = queue.dequeue()
    queue.enqueue(pop_num)

print(queue.arr[0])