import sys
input = sys.stdin.readline
from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
all_combis = []

for i in range(1, N + 1):
    res = list(combinations(arr, i))
    all_combis.append(res)

answer = 0
for combis in all_combis:
    for c in combis:
        sum = 0
        for elem in c:
            sum += elem
        if sum == S: 
            answer += 1

print(answer)