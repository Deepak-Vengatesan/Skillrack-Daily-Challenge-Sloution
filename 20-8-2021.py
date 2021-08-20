N = int(input())
lis = list(input().split())
X = int(input())
flag = 0
for i in range(N-1):
    if int(lis[i]+lis[i+1])%X == 0:
        flag = 1
        print(lis[i], lis[i+1])
    elif int(lis[i+1]+lis[i])%X == 0:
        flag = 1 
        print(lis[i+1], lis[i])
if flag == 0:
    print(-1)
    