import sys
input = sys.stdin.readline

formula = input().split('-')
num = []

for n in formula:
    sum = 0
    arr = n.split('+')
    for a in arr:
        sum += int(a)
    num.append(sum)

answer = num[0]
for i in range(1, len(num)):
    answer -= num[i]

print(answer)