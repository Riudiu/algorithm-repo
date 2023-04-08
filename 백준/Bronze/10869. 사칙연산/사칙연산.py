try:
    first, second = map(int, input().split())

    print(first + second)
    print(first - second)
    print(first * second)
    print(int((first / second) if second != 0 else 0)) 
    print(first % second if second != 0 else 0)

except ValueError:
    print("값을 입력해주세요")
        