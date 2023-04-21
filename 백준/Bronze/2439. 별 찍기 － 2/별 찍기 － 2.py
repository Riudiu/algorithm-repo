N = int(input())

for i in reversed(range(0, N)):
    star = ""   
    star += (" " * i) + "*" * ((N) - i)
    print(star)