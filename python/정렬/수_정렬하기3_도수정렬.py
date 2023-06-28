import sys

input = sys.stdin.readline

length = int(input())
count = [0] * 10001  # 메모리 제한에 따라 count 미리 지정

for i in range(length):
    N = int(input())  # 입력 받는 즉시 count 올려주기
    count[N] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)