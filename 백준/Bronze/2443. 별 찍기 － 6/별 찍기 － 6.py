N = int(input())

for i in reversed(range(1, N + 1)):
    star = ""   
    star += " " * (N - i) + "*" * (2 * i - 1)
    print(star)