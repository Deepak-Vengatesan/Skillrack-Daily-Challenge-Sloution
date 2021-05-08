R,C = map(int,input().split())
matrix = [list(input().split()) for row in range(R)]
for row in range(0,R):
    for col in range(0,C//2):
        C1 = matrix[row][col]
        C2 = matrix[row][C-col-1]
        if C1+C2 == 'RR':
            print('R',end = " ")
        elif C1+C2 == 'BB':
            print('B',end = " ")
        elif C1+C2 == 'GG':
            print('G',end = " ")
        elif C1+C2 == 'GB' or C1+C2 == 'BG':
            print('C',end = " ")
        elif C1+C2 == 'RB' or C1+C2 == 'BR':
            print('M',end = " ")
        else:
            print('Y',end = " ")
    print() 





'''

5 6
R G B B G B
B R B G R G
R G R R B R
R R G R G R
G R B R R G


'''
           
