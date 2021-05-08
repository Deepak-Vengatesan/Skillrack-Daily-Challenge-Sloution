N = int(input())
matrix = [list(input().split())for row in range(N)]

transpose = [list(row) for row in zip(*matrix)]
for row in matrix:
    if row in transpose or row[::-1] in transpose:
        print("YES")
        break 
else:
    print("NO")


'''

4
2 3 4 5
3 5 10 9
6 10 8 8
7 9 2 1


'''