import sys
input = sys.stdin.readline

N = int(input())
times = []

for _ in range(N):
    start, end = map(int, input().split())
    times.append([start, end])  
times.sort(key=lambda x:(x[1], x[0]))  # 끝나는 시간을 기준으로 오름차순 정렬

end_time = 0
cnt = 0
for start, end in times:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)
