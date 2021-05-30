def getCh(row):
    for ch in row:
        if ch.isalpha():
            return ch 

R,C = map(int,input().split())
matrix = [input().split()for row in range(R)]
matrix = matrix[::-1]
matrix = sorted(matrix, key = lambda X: getCh(X))
for i in matrix:
    print(*i)

'''
5 6
27 24 84 19 72 d
70 b 89 14 46 95
c 12 31 92 53 27
39 96 40 a 63 15
52 68 58 27 39 b


5 4
64 70 x 16
11 z 85 79 
23 40 5 x
y 54 96 36
20 x 10 44

'''