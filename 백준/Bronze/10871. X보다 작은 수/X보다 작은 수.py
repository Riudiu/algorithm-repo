length, criteria = map(int, input().split())
num_list = list(map(int, input().split()))

for num in num_list:
    if criteria > num:
        print(num)
