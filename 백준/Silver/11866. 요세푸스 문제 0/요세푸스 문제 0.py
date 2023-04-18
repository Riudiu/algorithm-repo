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
    
    def rotate(self, item):
        return self.arr.rotate(item)  # 1: 오른쪽으로 이동, -1: 왼쪽으로 이동

    def size(self):
        return len(self.arr)
    
def josephus(n, k):
    queue = Queue()
    for i in range(1, n+1):
        queue.enqueue(i)
    
    while queue.size() > 0:
        for _ in range(k - 1):
            queue.rotate(-1)
        answer.append(queue.dequeue())

if __name__== "__main__":
    N, K = map(int, input().split())
    global answer
    answer = []
    josephus(N, K)

    print("<",end='')
    for i in range(len(answer)-1):
        print("%d, "%answer[i], end='')
    print(answer[-1], end='')
    print(">")