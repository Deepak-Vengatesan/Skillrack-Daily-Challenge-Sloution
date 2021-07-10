R,C = map(int,input().split())
cities =[input().split() for row in range(R)]
signal,signalR = [['0']*C for row in range(R)],0
for row in range(0,R):
    for col in range(0,C):
        if cities[row][col] == 'L':
            for sRow in range(max(0,row-2),min(R,row+3)):
                for sCol in range((0,col-2),min(C,col+3)):
                    signal[sRow][sCol] = '#'
        elif cities[row][col] == 'S':
            for sRow in range(max(0,row-1),min(R,row+2)):
                for sCol in range(max(0,col-1),min(C,col+2)):
                    signal[sRow][sCol] = '#'

for row in signal:
    signalR += row.count('#')
print(signalR)