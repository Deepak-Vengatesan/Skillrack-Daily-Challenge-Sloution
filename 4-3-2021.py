def isvalidNum(num):
    strval = str(num)
    if num%int(strval[0]+strval[-1])== 0:
        return True 
    return False 

N = int(input())
for ctr in range(0,N+1):
    if isvalidNum(N-ctr):
        print(N-ctr)
        break 
    if isvalidNum(N+ctr):
        print(N+ctr)
        break 
