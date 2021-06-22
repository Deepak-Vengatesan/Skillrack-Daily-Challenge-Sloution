N = input()
val = ''
for i in N:
    if i.isnumeric():
        val+=i 
val = int(val)
bs = []
for i in range(1,val+1):
    para = N[0]*i+N[-1]*i
    print(para.strip(),end="")
    for i in bs[::-1]:
        print(i,end="")
    print()
    bs.append(para)
