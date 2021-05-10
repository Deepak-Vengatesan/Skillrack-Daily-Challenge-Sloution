import datetime
matrix = [list(input().split()) for row in range(5)]
N1,N2 = input().split()
original = [['*', '11', '12', '1', '*'], ['10', '*', '*', '*', '2'], ['9', '*', '*', '*', '3'], ['8', '*', '*', '*', '4'], ['*', '7', '6', '5', '*']]
hr,minute = 0,0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == N1:
            hr = original[row][col]
        if matrix[row][col] == N2:
            minute = str((int(original[row][col])*5)%60)
print(f"{hr.zfill(2)}:{minute.zfill(2)}")


'''
* 8 9 1 1 *
3 * * * 5
6 * * * 7
4 * * * 1
* 2 12 10 *
8 10



* 4 9 1 *
12 * * * 6
7 * * * 5
8 * * * 10
* 3 2 11 *
6 7

* 6 3 11 *
2 * * * 7
12 * * * 5
8 * * * 1
* 4 10 9 *
3 3

'''