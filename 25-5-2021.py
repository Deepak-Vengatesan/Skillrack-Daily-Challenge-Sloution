N,X = map(int,input().split())
B = bin(N)[2::]
count = 0
for index in  range(0,len(B)):
    if int(B[:index+1],2)%X==0:
        count+=1 
print(count)