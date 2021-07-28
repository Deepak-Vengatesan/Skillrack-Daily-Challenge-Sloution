N = int(input())
ema = input().split()
num, char = '' , ''
fema = []
for word in ema:
    for ch in word:
        if ch.isnumeric():
            num += ch 
        else:
            char += ch 
    fema.append([char,int(num)])
    num,char = '',''
fema.sort(key=lambda x: int(x[1]))

fema.sort(key = lambda x : x[0])

for i in fema:
    print(i[1],end = " ")