import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

length = int(input())
N = [] 

for i in range(length):
    N.append(int(input()))

N = quick_sort(N)

for n in N:
    print(n)