import sys

def move(num: int, start: int, to: int, other:int): #원판 개수, 시작 기둥, 목적지 기둥, 나머지 기둥
    if num == 0: return
    move(num - 1, start, other, to)
    print(f'{start} {to}') # 원판 n개를 start기둥에서 to기둥으로 이동
    move(num - 1, other, to, start)

N = int(sys.stdin.readline()) #원판 개수
print(2**N-1)
if not N > 20: move(N, 1, 3, 2)