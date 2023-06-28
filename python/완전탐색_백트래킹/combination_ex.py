# 조합 구현 예제(nCr)
# combination([0,1,2,3], 2) = 
#   ([0], combination([1, 2, 3], 1)) +
#   ([1], combination([2, 3], 1)) +
#   ([2], combination([3], 1)))
def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        e = arr[i]
        for rest in combination(arr[i + 1:], n - 1):
            result.append([e] + rest)
    return result

print(combination([0,1,2,3], 2))
# [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]