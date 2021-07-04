class IntegerList:
    def __init__(self,numList):
        self.numList = numList 
    
    def updateRange(self,left,right,val):
        for index in range(left-1,right):
            self.numList[index]+=val 
    
    def getSum(self,left,right):
        return sum(self.numList[left-1:right])
    
