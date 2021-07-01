calendar = [input().split() for row in range(6)]
if len(calendar[0]) == 6:
    calendar.append(input().split())
    calendar = [list(row) for row in zip(*calendar)]
date = 1
days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
holidays =False 
for row in range(0,6):
    for col in range(0,7):
        if calendar[row][col].isdigit():
            date+=1 
        elif calendar[row][col] == '#':
            print(date,days[col])
            holidays = True
            date+=1 

if holidays == False:
    print(-1)


'''

* * 1 2 3 4 5
6 7 8 9 10 11 12
13 14 # 16 17 18 19
20 21 22 23 24 25 #
# # 29 30 * * * 
*  * * * * * * 
'''