def converToMins(time):
    return int(time[:2])*60 + int(time[-2:])

startTime,endTime = input().split()
x,y = map(int,input().split())
startTime,endTime = converToMins(startTime),converToMins(endTime)
slots = []
while True:
    if startTime+x <= endTime:
        slots.append([startTime,startTime+x])
        startTime+=x+y 
    else:
        break 
print(slots)
if slots:
    for time in slots:
        print(f"{str(time[0]//60).zfill(2)}:{str(time[0]%60).zfill(2)}",end = ' - ')
        print(f"{str(time[1]//60).zfill(2)}:{str(time[1]%60).zfill(2)}")
else:
    print(-1)
