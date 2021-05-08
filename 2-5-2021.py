R,C = map(int,input().split())
matrix = [input().split() for row in range(R)]
S = input().strip()

top = "".join(matrix[0])
bottom = "".join(matrix[-1])
right = "".join(matrix[row][-1] for row in range(R))
left = "".join(matrix[row][0] for row in range(R))

if S in top or S[::-1] in top:
    print("Top")
elif S in right or S[::-1] in right:
    print("right")
elif S in bottom or S[::-1] in bottom:
    print("Bottom")
elif S in left or S[::-1] in left:
    print("left")
else:
    print(-1)