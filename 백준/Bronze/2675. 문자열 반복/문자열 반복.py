length = int(input())
rp_str_list = []

# 반복된 문자열 가져오기
def getRepeatedString(str_tuple):
    repeatedString = ""
    repeat = int(str_tuple[0]) # 반복횟수
    string = str_tuple[1] # ex) ABC

    string_list = list(map(str, string)) # ex) ['A', 'B', 'C']
    for string in string_list:
        repeatedString += string * repeat

    return repeatedString

# main
for i in range(0, length):
    str_tuple = tuple(map(str, input().split())) # 튜플이 리스트보다 더 빠르다
    repeatedString = getRepeatedString(str_tuple) # ex) str_tuple - (3, ABC)
    rp_str_list.append(repeatedString)

# 출력
for str in rp_str_list:
    print(str)