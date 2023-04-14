length = int(input())
N = [] 

for i in range(length):
    N.append(int(input()))

N.sort()

for n in N:
    print(n)