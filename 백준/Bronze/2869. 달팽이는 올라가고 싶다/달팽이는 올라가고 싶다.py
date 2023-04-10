import math

# A, B, V
dayMeter, nightSlipMeter, destination = map(int, input().split())

dayWalk = dayMeter - nightSlipMeter  # 낮과 밤 포함헤서 달팽이가 하루동안 올라가는 거리
day = (destination - nightSlipMeter) / dayWalk

print(math.ceil(day))
