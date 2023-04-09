num_map = {}
max = 0

for i in range(1, 10):
    num = int(input())
    num_map[num] = i 

    if(max < num):
        max = num

print(max)
print(num_map[max])