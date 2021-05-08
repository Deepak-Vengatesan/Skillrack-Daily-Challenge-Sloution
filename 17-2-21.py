N=int(input())
nList=list(map(int,input().split()))
K=int(input())
solList=[]
for val in range(nList[0],nList[-1]):
    if val not in nList:
        solList.append(val)
if len(solList) >= K:
    print(*solList[:K])
else:
    print(-1)