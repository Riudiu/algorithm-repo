# 선형 탐색
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None

if __name__== "__main__":
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))
    # target(찾고자 하는 값)을 입력 받기
    target = int(input())

    # 수행 결과 출력
    result = linear_search(array, target)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)