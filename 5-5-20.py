R,C = map(int,input().split())
matrix = [list(input().strip()) for row in range(R)]
k = int(input())
for row in range(0,R-k+1):
    for col in range(0,C-k+1):
        if len(set(matrix[row][col],matrix[row+k-1][col],matrix[row][col+k-1],matrix[row+k-1][col+k-1])) == 1:
            for ctr in range(0,k):
                matrix[row+ctr][col+ctr] = '*'
                matrix[row+ctr][k+col-ctr-1] = '*'
            for row in range(R):
                for col in range(C):
                    print(matrix[row][col])
            quit() 


'''

7 6
a d z d o t
t g y e g b
y d c d i c
s y x v a l
b g s f g f
u a c r p c
k v z n i h
4

'''