import sys

input = sys.stdin.readline

length = int(input())
N = [input().strip() for _ in range(length)]

N = list(set(N))  # 중복제거

N.sort()  # 사전순
N.sort(key=len)  # 길이순

for n in N:
    print(n)