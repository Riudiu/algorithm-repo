length = int(input())
sum_list = []

for i in range(0, length):
    a, b = map(int, input().split())
    sum_list.append(a + b)

for item in sum_list:
    print(item)