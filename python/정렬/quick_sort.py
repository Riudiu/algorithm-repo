#1
def quick_sort_original(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

#2 - 파이썬 장점 살린 방식
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]  # 피벗은 첫번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    # 리스트 컴프리헨션 사용
    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

length = int(input())
N = [] 

for i in range(length):
    N.append(int(input()))
print(N)

N = quick_sort(N)
print(N)

for n in N:
    print(n)