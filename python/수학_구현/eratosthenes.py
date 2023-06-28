import math

# 소수 판별
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수 확인 
    # 제곱근 쓰는 이유는 가운데 약수까지만 나누어 떨어지는지 확인하면 되기 때문
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
        return True  # 소수임
    
print(is_prime_number(4))
print(is_prime_number(7))

# 에라토스테네스의 체 
# N보다 작거나 같은 모두 소수 찾을 때 사용
N = 1000
array = [True for _ in range(N + 1)]  # 먼저 모든 수가 소수(True)인 것으로 초기화(0,1 제외)

def eratos(n):
    # 2부터 n의 제곱근까지의 모든 수 확인 
    for i in range(2, int(math.sqrt(n)) + 1):
        # i가 소수인 경우(또는 아직 처리하지 않은 수인 경우)
        if array[i] == True:
            # i를 제외한 i의 모든 배수를 지움
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
eratos(N)

# 모든 소수 출력
for i in range(2, N + 1):
    if array[i]:
        print(i, end=' ')
