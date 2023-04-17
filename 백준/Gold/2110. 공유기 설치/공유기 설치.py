import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = list(int(input()) for _ in range(0, N))
X.sort()

start = 1  # 최소 거리
end = X[-1] - X[0]  # 좌표 간 최대 거리

answer = 0
while start <= end:
    mid = (start + end) // 2
    router = 1  # 공유기 설치 개수
    current = X[0]

    for i in range(1, len(X)):  # 두번째 좌표부터
        if X[i] >= current + mid:  # 두번째 좌표 값이 (첫번째 좌표 값+거리) 보다 크면 공유기 설치
            current = X[i]
            router += 1

    if router < C:  # 설치한 공유기 개수가 목표치보다 작으면
        end = mid - 1  # 거리 간격 줄이기
    else:
        answer = mid
        start = mid + 1  # 거리 간격 늘리기

print(answer)