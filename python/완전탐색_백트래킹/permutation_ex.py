# 순열 구현 예제(nPr)
# permutation([0,1,2,3], 2) =
#   ([0], permutation([1, 2, 3], 1)) +
#   ([1], permutation([0, 2, 3], 1)) +
#   ([2], permutation([0, 1, 3], 1)) +
#   ([3], permutation([0, 1, 2], 1))
def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        e = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([e] + rest)
    return result
    
print(permutation([0,1,2,3], 2))
# [[0, 1], [0, 2], [0, 3], [1, 0], [1, 2], [1, 3], [2, 0], [2, 1], [2, 3], [3, 0], [3, 1], [3, 2]]