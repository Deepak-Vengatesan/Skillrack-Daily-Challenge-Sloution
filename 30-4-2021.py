N = int(input())
teamName,groundName = [], []
for ctr in range(0,N):
    inputstring = input().split("-")
    teamName.append(inputstring[0].strip())
    groundName.append(inputstring[-1].strip())
for ctr in range(0,N-1):
    for ind in range(ctr+1,N):
        print(teamName[ctr],"vs",teamName[ind],"("+groundName[ctr]+")")
        print(teamName[ind],"vs",teamName[ctr],"("+groundName[ind]+")")



'''

Chennai Super Kings - M.A.Chidambaram Stadium
Kolkata Knight Riders - Eden Gardens
Mumbai Indians - Warkheda Stadium
Royal Challengers Bangalore - M.Chinnaswamy Stadium

'''