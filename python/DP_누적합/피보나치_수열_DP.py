fibo = [0, 1]

for i in range(2, 11):
    fibo.append(fibo[i - 1] + fibo[i - 2])

for i in range(1, 11):
    print(fibo[i])
