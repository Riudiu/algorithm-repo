import math

dayMeter, nightSlipMeter, destination = map(int, input().split())

dayWalk = dayMeter - nightSlipMeter
day = (destination / dayWalk) - (nightSlipMeter / dayWalk)
    
print(math.ceil(day))
