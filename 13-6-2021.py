N,X = map(int,input().split())
for ctr in range(1,X+1):
    print(N,end=" ")
    N += len(str(N))