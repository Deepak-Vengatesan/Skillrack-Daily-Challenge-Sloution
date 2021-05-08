N=int(input())
midval=(N//2)+(N%2)
end=0
for i in range(midval):
    for j in range(N,end,-1):
        print(j,end=" ")
    N-=1
    end+=1