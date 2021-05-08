def sumofdigit(num):
    sumval=0
    while num>0:
        sumval+=num%10
        num//=10
    return sumval 

N=int(input())
nList=list(map(int,input().split()))
maxval=-1
for ind1 in range(0,N):
    for ind2 in range(ind1+1,N):
        if sumofdigit(nList[ind1]) == sumofdigit(nList[ind2]):
            maxval=max(maxval,nList[ind1]+nList[ind2])
print(maxval)