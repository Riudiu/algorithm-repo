first = int(input())
second = input()

second_list = list(map(int, second))
second_list.reverse()

for num in second_list:
    print(first * num)

print(first * int(second))
