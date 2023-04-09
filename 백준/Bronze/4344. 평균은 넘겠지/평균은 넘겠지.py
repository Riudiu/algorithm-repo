length = int(input())
rate_list = []

# 평균 넘는 점수 비율 구하기
def getAboveAverageRate(score_list):
    allStudents = score_list.pop(0) # 학생 수 구하기 
    
    sum = getSum(score_list)
    averageScore = int(sum / allStudents) # 평균 점수 구하기

    aboveAverageStudents = getAboveAverageStudents(score_list, averageScore)
    aboveAverageRate = (aboveAverageStudents / allStudents) * 100

    return f'{aboveAverageRate:.3f}%'

# 점수 총합 가져오기
def getSum(score_list):
    sum = 0
    for score in score_list:
        sum += score
    return sum

# 평균 점수 넘는 학생수 구하기
def getAboveAverageStudents(score_list, averageScore):
    aboveAverageStudents = 0
    for score in score_list:
        if score > averageScore:
            aboveAverageStudents += 1
    return aboveAverageStudents

# main
for i in range(0, length):
    score_list = list(map(int, input().split()))
    aboveAverageRate = getAboveAverageRate(score_list)
    rate_list.append(aboveAverageRate)

# 정답 출력
for rate in rate_list:
    print(rate)
    