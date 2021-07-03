def getRow(ch):
    for row in range(0,3):
        if ch in keyRow[row]:
            return row 

keyRow = list(input() for row in range(3))
S = input().strip()
keyIndex,ind,count,prevMaxCount = [],getRow(S[0]),1,1
for ctr in range(1,len(S)):
    if getRow(S[ctr]) == getRow(S[ctr-1]):
        ind,count = getRow(S[ctr]),count+1 
    else:
        if count > prevMaxCount:
            keyIndex= [ind]
            prevMaxCount = count 
        elif prevMaxCount == count and count > 1:
            keyIndex.append(ind)
            prevMaxCount = count 
        count,ind = 1,getRow(S[ctr]) 
if len(S) > 1 and getRow(S[-1]) == getRow(S[-2]):
    if count > prevMaxCount:
        keyIndex = [ind]
    elif prevMaxCount == count and count > 1:
        keyIndex.append(ind)
if keyIndex:
    keyIndex = sorted(set(keyIndex))
    for ind in keyIndex:
        print(keyRow[ind])
else:
    print(-1)