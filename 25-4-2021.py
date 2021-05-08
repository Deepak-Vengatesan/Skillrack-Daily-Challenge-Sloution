R,C = map(int,input().split())
matrix = [input().split() for row in range(R)]
for col in range(C):
    matrix[0][col] = 'x'
    for row in range(R):
        if matrix[row][col] == '=':
            break 
        else:
            matrix[row][col] = 'x'
for i in matrix:
    print(*i)


'''
5 5
= = - - =
= - - - -
= - - = -
- - = = =
= - = - -

'''
