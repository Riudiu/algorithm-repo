import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

num_list = []
while True:
    try:
        num_list.append(int(input()))
    except:
        break

def post_order(start, end):
        if start > end:
            return
        mid = end + 1  # 루트보다 큰 값이 존재하지 않을 경우를 대비 
        
        for i in range(start + 1, end + 1):
            if num_list[i] > num_list[start]:
                mid = i
                break

        post_order(start + 1, mid - 1)  # 왼쪽 서브 트리
        post_order(mid, end)   # 오른쪽 서브 트리
        print(num_list[start])

post_order(0, len(num_list) - 1)