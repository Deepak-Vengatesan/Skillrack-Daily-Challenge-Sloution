import math
M,N = map(int,input().split())
matrix1 = [list(map(int,input().split())) for row in range(M)]
R,C = map(int,input().split())
matrix2 = [list(map(int,input().split())) for row in range(R)]

for row in range(min(M,R)):
    for col in range(min(N,R)):
        print(math.gcd(matrix1[row][col],matrix2[row][col]),end=" ")
    print()



'''

2 6
4 4 3 2 2 4
8 8 6 3 8 5
3 3
4 2 6
7 2 6
5 1 8

'''