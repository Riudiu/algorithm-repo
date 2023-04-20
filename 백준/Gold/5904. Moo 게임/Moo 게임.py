import sys

input = sys.stdin.readline 
N = int(input())

length = 0  # 문자열 길이
lenArr = [0]  # 길이를 담는 배열
k = 0  # 현재 차수

# s(k) 단계별로 문자열의 길이를 배열에 저장, N이 포함된 만큼의 단계까지만 호출
while length <= N:
    length = 2 * length + (k + 3)  # 문자열 길이 = 이전 차수의 문자열 길이 X 2 + (현재 차수) + 3
    lenArr.append(length)
    k += 1

# 재귀로 생각하면 s(k-1) + (k+3) + s(k-1) 이렇게 앞, 가운데, 뒤 3파트로 나눌 수 있다. s(k-1)은 이전 차수
for lenCnt in reversed(range(len(lenArr))):  # for문 역순으로
    if  N <= lenArr[lenCnt]:  # N이 이전 차수의 길이보다 작거나 같을 때 -> N이 앞 파트에 있는 경우, 이전 차수로 이동 
        continue
    elif  N <= lenArr[lenCnt] + lenCnt+3: # N이 (이전 차수의 길이 + k+3)보다 작거나 같을 때 -> 가운데 파트에 N이 포함된 경우 정답 출력
        if lenArr[lenCnt] + 1 == N:  #첫번째만 'm'이고 나머진 'o'
            print('m')
        else:
            print('o')
        break
    else:  # Ndl 뒤 파트에 있는 경우, 앞과 가운데 파트의 문자열 길이만큼을 N에서 빼주고 이전 차수로 이동. 
        N = N - (lenArr[lenCnt] + lenCnt+3)