length = int(input())
score_list = []

def setTypeList(string):
    type_list = list(map(str, string))
    return type_list

def getScore(type_list):
    score = 0
    bonus = 0
    for type in type_list:
        if(type == 'O'):
            score += bonus + 1
            bonus += 1
        else: 
            bonus = 0
    return score

for i in range(0, length):
    typeString = input()
    type_list = setTypeList(typeString)
    score = getScore(type_list)
    score_list.append(score)

for score in score_list:
    print(score)
    