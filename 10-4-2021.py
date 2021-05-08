import re 
matrix = [input().split()for row in range(5)]
S = input().strip()
record = []
for row in range(5):
    for col in range(5):
        if len(matrix[row][col])== 1:
            if matrix[row][col] in S:
                record.append([matrix[row][col],str(row+1)+str(col+1)])
        else:
            x,y=matrix[row][col].split("/")
            if x in S:
                record.append([x,str(row+1)+str(col+1)])
            if y in S:
               record.append([y,str(row+1)+str(col+1)])
string = ''
for i in S:
    for j in record:
        if i in j:
            string+=j[1]
        if i == ' ':
            string+=' '  
res = re.sub(' +',' ',string)
print(str(res))









'''
a b c d e
f g h i/p j
k l m n o
q r s t u
v w x y z
apple juice


'''
