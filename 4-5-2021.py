N = int(input())
inputList = [input().strip() for row in range(N)]
while len(inputList) > 0:
    MinLen = len(min(inputList,key = lambda val: len(val)))
    ctr = 0
    while ctr < len(inputList):
        if len(inputList[ctr]) <= MinLen:
            print(inputList[ctr])
            inputList.pop(ctr)
        else:
            print(inputList[ctr][:MinLen])
            inputList[ctr] = inputList[ctr][MinLen:]
            ctr+=1


'''

4
lion
kingdom
monday
car

'''