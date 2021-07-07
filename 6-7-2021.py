S = input().strip()
R,C = (len(S)+1)//2 , len(S)
vpattern = [['*' for col in range(C)] for row in range(R)]
row,col = 0,0

for ind in range(R):
    vpattern[row][col] = S[ind]
    vpattern[R-row-1][col] = S[ind]
    vpattern[row][C-col-1] = S[len(S)-ind-1]
    vpattern[R-row-1][C-col-1] = S[len(S)-ind-1]
    row+=1
    col+=1

for i in vpattern:
    print(''.join(i))



'''
s***l***k
*k*l*r*c*
**i***a**
*k*l*r*c*
s***l***k

'''