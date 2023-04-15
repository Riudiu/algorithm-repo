import sys

input = sys.stdin.readline

length = int(input())
count = [0] * 10001

for i in range(length):
    N = int(input())
    count[N] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)