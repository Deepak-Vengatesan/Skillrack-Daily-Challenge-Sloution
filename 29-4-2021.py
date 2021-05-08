def replace(row,col,ch):
    for sRow in range(row,row+N):
        for sCol in range(col,col+N):
            cube[sRow][sCol] = ch

faces = input().split()
N = int(input())
cube = [['*' for col in range(N*4)]for row in range(N*3)]
replace(N,N,faces[0])
replace(N,N*2,faces[1])
replace(N,N*3,faces[2])
replace(N,0,faces[3])
replace(N*2,N,faces[4])
replace(0,N,faces[5])

for i in cube:
    print(*i)


'''
a b c d e f
3

* * * f f f * * * * * *
* * * f f f * * * * * *
* * * f f f * * * * * *
d d d a a a b b b c c c
d d d a a a b b b c c c
d d d a a a b b b c c c
* * * e e e * * * * * *
* * * e e e * * * * * *
* * * e e e * * * * * *

'''