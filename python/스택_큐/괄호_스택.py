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
    
def check_VPS(str):
    stack = Stack()

    for c in str:
        if c == '(':
            stack.push(c)
        else:
            # 스택 비어있을 때 ')' 괄호가 들어오면 NO 출력
            if stack.size() == 0:
                print('NO')
                return
            # 스택에 '(' 괄호가 있으면 해당 괄호 꺼내기
            else:
                stack.pop()

    # 반복문 종료 후에도 스택에 '(' 괄호가 남아있으면 NO 출력
    if stack.size() > 0:
        print('NO')
    else: 
        print('YES')
            
if __name__== "__main__":
    T = int(input())
    arr = [input().strip() for _ in range(0, T)]

    for a in arr:
        check_VPS(a)