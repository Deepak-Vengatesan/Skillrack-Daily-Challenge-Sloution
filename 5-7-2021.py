numSet = []
while True:
    try:
        numList = list(map(int,input().split()))
        numSet.extend(numList)
    except:
        break
numSet = sorted(set(numSet))
print(*numSet)