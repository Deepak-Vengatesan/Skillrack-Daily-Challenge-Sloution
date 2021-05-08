S = input().strip()
largestNum = 0
for ind1 in range(0,len(S)):
    for ind2 in range(ind1,len(S)):
        num = int(S[ind1:ind2+1])
        if num%2==1:
            largestNum = max(largestNum,num)
print(largestNum)