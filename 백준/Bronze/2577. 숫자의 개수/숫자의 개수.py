a = int(input())
b = int(input())
c = int(input())

multiply = a * b * c

# 각각의 숫자 세기
def countEachNumber(eachNum):
    count = 0
    number_list = list(map(int, str(multiply)))

    for number in number_list:
        if number == eachNum:
            count += 1
    
    return count

# 출력
for i in range(0, 10):
    print(countEachNumber(i))
    