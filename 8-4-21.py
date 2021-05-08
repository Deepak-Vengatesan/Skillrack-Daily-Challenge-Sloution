R,C = map(int,input().split())
matrix = [list(input().split())for row in range(R)]
r,c=0,0
S = int(input())
sumval = 0
for row in range(0,R):
    for col in range(0,C):
        if matrix[row][col] == 'M':
            c= col 
            r= row
            break
for row in range(0,R):
    for col in range(0,C):
        if col == c and matrix[row][col] != 'M':
            sumval+=int(matrix[row][col])
sol = S-sumval
for row in range(0,R):
    for col in range(0,C):
        if matrix[row][col] =='M':
            matrix[row][col] = sol 
            print(matrix[row][col],end=" ")
        else:
            print(matrix[row][col],end=" ")
    print()



R,C = map(int,input().split())
matrix = [input().split() for row in range(R)]
S = int(input())
for row in range(0,R):
    for col in range(0,C):
        if matrix[row][col] != 'M':
           print(matrix[row][col],end=" ")
        else:
            sumofcol = [int(matrix[sRow][col])for sRow in range(R) if sRow!= row]
            print(S-sum(sumofcol),end= " ")
    print() 





'''

4 5
62 25 69 62 80
15 10 17 34 75
99 M  76 79 23
48 15 73 22 68
100 

3 3
2 5 8
1 5 M
9 7 6
17

'''