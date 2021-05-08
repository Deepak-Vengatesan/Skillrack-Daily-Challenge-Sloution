R,C = map(int,input().split())
CharMatrix = [list(map(int,input().split)) for row in range(r)]
S = input().strip()
for row in range(0,R-2):
    for col in range(0,C-2):
        if CharMatrix[row+1][col+1] == S[0]:
            continue 
        for sRow in range()
