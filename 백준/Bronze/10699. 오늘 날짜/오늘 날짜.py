import datetime as dt
x = dt.datetime.now()

if x.month < 10:
    month = '0' + str(x.month)
else: 
    month = x.month

if x.day < 10:
    day = '0' + str(x.day)
else: 
    day = x.day

print(f'{x.year}-{month}-{day}')