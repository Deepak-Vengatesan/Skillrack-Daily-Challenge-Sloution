R,C = map(int,input().split())
Matrix = list(input().split() for row in range(R))
T = int(input())

for ctr in range(1,T+1):
    apple = Matrix[R-1].count('A')
    orange = Matrix[R-1].count('O')
    if apple >= orange:
        fruitToBeRemoved = 'A'
    else:
        fruitToBeRemoved = 'O'
    for col in range(0,C):
        if Matrix[R-1][col] == fruitToBeRemoved:
            for row in range(R-1,0,-1):
                Matrix[row][col] = Matrix[row-1][col]
            Matrix[0][col] = '*'

for i in Matrix:
    print(*i)








'''

5 6
A O O A O O 
O A O A A A
A A O A A O
O A O O A O
O A A A O A
3

TAKING THE TRACSPOSE 

 # if Matrix[ctr][col] != '*':
            #     Matrix[ctr][col] = '*'
            # else:
            #     while(Matrix[ctr][col]!='*'):
            #         ctr-=1
            #     Matrix[ctr][col]= '*'

'''