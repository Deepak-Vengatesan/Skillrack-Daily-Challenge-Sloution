R,C = map(int,input().split())
matrix = [list(map(int,input().split())) for row in range(R)]

for row in range(0,R,3):
    for col in range(0,C,3):
        arr = []
        for sRow in range(row,row+3):
            for sCol in range(col,col+3):
                arr.append(matrix[sRow][sCol])
        if len(set(arr)) == 9:
            num=1
            for sRow in range(row,row+3):
                for sCol in range(col,col+3):
                    matrix[sRow][sCol] = num 
                    num+=1 
for i in matrix:
    print(*i)




'''
6 6
8 8 4 1 8 5
4 9 7 9 7 2
5 3 3 6 3 4
1 7 2 6 2 3
8 6 3 7 6 4
5 9 4 3 5 1

'''