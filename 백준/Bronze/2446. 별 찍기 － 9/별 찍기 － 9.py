N = int(input())

for i in range(0, N):
    print(" " * i + "*" * ((2 * N - 1) - 2 * i))
for i in reversed(range(0, N)):
    if i == N - 1: continue
    print(" " * i + "*" * ((2 * N - 1) - 2 * i))