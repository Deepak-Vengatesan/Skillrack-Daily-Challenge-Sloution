R,C = map(int,input().split())
M1 = [list(map(int,input().split())) for _ in range(R)]
M2 = [list(map(int,input().split()))for _ in range(R)]

for row in range(R):
    for col in range(C):
        print(M1[row][col]+M2[row][C-col-1],end=" ")
    print()


'''
10 20 30
40 50 60
70 80 90

100 200 300 
400 500 600
700 800 900

'''