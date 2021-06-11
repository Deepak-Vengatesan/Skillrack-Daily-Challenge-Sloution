R,C = map(int,input().split())
matrix = [list(map(int,input().split())) for row in range(R)]
K = int(input())
row,col=-1,-1
for i in range(R):
    for j in range(C):
        if i==0 or i==R-1 or j==0 or j==C-1:
            if matrix[i][j] == K and row == -1 and col == -1:
                row = i
                col = j 
if row == -1 and col == -1 :
    print(-1)
    exit()

size = (R*2) + ((C-2)*2) 
border,ind= [],-1
i1,j1=0,0

for i in range(0,size):
    if i1==row and j1==col:
        ind = i 
    border.append(matrix[i1][j1])
    if i1==0 and j1==0:
        j1+=1 
    elif i1 ==0 and j1 == C-1:
        i1+=1
    elif i1==R-1 and j1==C-1:
        j1-=1
    elif i1==R-1 and j1==0:
        i1-=1
    elif i1==0:
        j1+=1
    elif j1==C-1:
        i1+=1
    elif i1==R-1:
        j1-=1
    elif j1==0:
        i1-=1

left,right,l=ind,ind,size 
while size>0:
    ind1 = left%l
    ind2 = right%l 
    if ind1 == ind2:
        print(border[ind1],end=" ")
        size-=1 
    else:
        print(border[ind1],end=" ")
        print(border[ind2],end=" ")
        size-=2
    if left==0:
        left=l 
    left-=1
    right+=1






'''
5 5
74 21 77 95 58
97 21 35 98 73
94 23 39 38 14
64 47 17 58 54
38 61 22 72 25
54

'''


