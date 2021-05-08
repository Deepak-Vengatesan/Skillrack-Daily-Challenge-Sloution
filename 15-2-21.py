N=int(input())
startVal=1
for row in range(1,N+1):
    numList=[num*N for num in range(startVal,starVal+N)]
    if row%2==1:
        print(*numList)
    else:
        print(*numList[::-1])
    startVal+=N 