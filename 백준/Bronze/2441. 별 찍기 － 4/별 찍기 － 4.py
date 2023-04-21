N = int(input())

for i in reversed(range(1, N + 1)):
    star = ""   
    star += " " * ((N) - i) + ("*" * i)
    print(star)