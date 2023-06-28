def fibo(n):
    if n == 1 or n == 2:  # 종료 조건
        return 1  
    return fibo(n-1) + fibo(n-2)
    
print(fibo(3))  # 2 
print(fibo(6))  # 8

for i in range(1, 11):
	print(fibo(i))  # 1, 1, 2, 3, 5, 8, 13, ...