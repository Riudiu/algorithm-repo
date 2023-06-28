# 조합 dfs 적용 예시
def dfs(start, temp):
    if len(temp) == N:
        print(temp)
        return

    for i in range(start, len(arr)):
        temp.append(arr[i])
        dfs(i + 1, temp)
        temp.pop()

arr = [0, 1, 2, 3]
N = 2
dfs(0, [])

"""
[0, 1]
[0, 2]
[0, 3]
[1, 2]
[1, 3]
[2, 3]
"""