N = int(input())
intList = list(map(int,input().split()))
R,C = map(int,input().split())
matrix = [[0]*C for row in range(R)]
row,ind,flag = R-1,0,False

while True:
    if row%2 == R%2:
        for col in range(C-1,-1,-1):
            matrix[row][col] = intList[ind]
            ind+=1
            if ind == N:
                flag = True
                break 
    else:
        for col in range(0,C):
            matrix[row][col] = intList[ind]
            ind+=1 
            if ind == N:
                flag = True 
                break 
    if flag == True:
        break 
    row -= 1
    if row == -1:
        row = R-1 
for i in matrix:
    print(*i[::-1])
