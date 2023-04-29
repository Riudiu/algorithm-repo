def isPrime(n):
    divisor = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)

    if len(divisor) == 2:
        return True
    else:
        return False

N = int(input())
arr = list(map(int, input().split()))
answer = 0
for num in arr:
    res = isPrime(num)
    if res: answer += 1 
print(answer)