def checkCycle(num, count):
    count += 1
    first = num // 10
    last = num % 10
    result = last * 10 + (first + last) % 10
    
    if(result == N):
        return count
    else: 
        return checkCycle(result, count)
    
N = int(input())
count = 0

count = checkCycle(N, count)
print(count)