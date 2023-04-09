num_list = list(input().split())
first = num_list[0]
second = num_list[1]

first_list = list(first)
second_list = list(second)

first_list.reverse()
second_list.reverse()

# 요소들 합치기
def putting(list):
    result = ''
    for e in list:
        result += e
    return result

# 더 큰 수 출력
def printBigger(first, second):
    if(first > second):
        print(first)
    else:
        print(second)

printBigger(int(putting(first_list)), int(putting(second_list)))