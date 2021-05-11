Num = int(input())
matrix = [input().split() for row in range(Num)]
for ctr in range(0,Num//2):
    row,col = ctr , Num-ctr-1
    matrix[row][row], matrix[row][col], matrix[col][col], matrix[col][row] = matrix[row][col], matrix[col][col], matrix[col][row], matrix[row][row]
for val in matrix:
    print(*val,end="")
    print()


'''

4
e k m v
b h t o 
u r d k
i d i w


5
z R p Y v
A h W t r
z W l v e
g v R  l p
p q C l z

'''