N = int(input())

for i in range(1, 2 * N):
    star = ""   
    if (i > N):
        star += " " * (i - N) + "*" * (4 * N - 2 * i - 1)
    else:
        star += " " * (N - i) + "*" * (2 * i - 1)
    print(star)