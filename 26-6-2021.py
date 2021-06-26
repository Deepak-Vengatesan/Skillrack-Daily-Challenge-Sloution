N = int(input())
ctr = 0
for i in range(N):
    for j in range(i+1):
        print('- '*ctr,end="")
        print('* '*(i+1))
    ctr+=j+1 
