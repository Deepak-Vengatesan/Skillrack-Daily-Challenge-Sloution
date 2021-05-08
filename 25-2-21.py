R,C=map(int,input().split())
vehicleCount=0
for ctr in range(1,R+1):
    slots = input().split()
    for index in range(0,C-1):
        if slots[index] == 'V' and slots[index+1] == '.':
            vehicleCount+=1 
    if slots[-1] == 'V':
        vehicleCount+=1
print(vehicleCount)









"""
3 5
V V . V .
. . . V .
. V V V V

"""
# R,C = map(int,input().split())
# parkstatus = [list(input().split()) for i in range(R)]
# counter=0
# for i in range(R-1):
#     for j in range(C-1):
#         if parkstatus[i][j] == "V" and parkstatus[i][j+1] == '.':
#             counter+=1 
#     print(counter)
#     if parkstatus[i][j+1] == 'V':
#         counter+=1
# print(counter)
