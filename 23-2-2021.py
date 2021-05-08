limit = int(input())
pattern = 'A'
char = ord('A')+1
for i in range(limit):
    print(pattern)
    pattern = pattern + chr(char) +pattern 
    char+=1 