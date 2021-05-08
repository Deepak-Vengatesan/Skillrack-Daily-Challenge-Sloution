R,C=map(int,input().split())
matrix=[list(input().split()) for row in range(R)]
for row in range(R):
    for col in range(C):
        if row%2==0 and row <C:
            print(*matrix[row][0:row+1],sep='') 
            break 
        elif row%2==1 and row<C:
            print(*matrix[row][C-row-1::],sep='')
            break 
        elif row>=C:
            print(*matrix[row][::],sep='')
            break 
# print(matrix)




"""

6 6
a b c d e f
g h i j k l
m n o p q r
s t u v w x 
y z a b c d
e f g h i j


8 5
v f b z c
w o h E a
o F f b k
s o f x l
v n i n C
o u r r B
c p w E x
E r b l o

"""