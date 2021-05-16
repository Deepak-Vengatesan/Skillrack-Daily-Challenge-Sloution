R,C = map(int,input().split())
matrix = [list(map(int,input().split())) for row in range(R)]
X,Y = map(int,input().split())

left,right = matrix[X-1],matrix[Y-1][::-1]
for col in range(C):
    print(left[col]*right[col],end=" ")




'''
4 6
1 1 5 3 3 2
7 4 3 7 6 8
9 9 5 2 3 9
8 1 6 9 3 7
2 4


7 4
10 20 30 40
83 85 46 94
14 78 84 14
56 99 25 35
12 85 27 25
50 60 70 80
54 36 55 51
6 1
'''