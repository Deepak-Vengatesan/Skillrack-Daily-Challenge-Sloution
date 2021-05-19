class Test:
    def __init__(self,name,duration):
        self.name = name 
        self.duration = duration 

    def getName(self):
        return self.name
        
    def getDuration(self):
        return self.duration 

test1name = input().strip()
test1duration = int(input().strip())
test2name = input().strip() 
test2duration = int(input().strip())
test1 = Test(test1name,test1duration)
test2 = Test(test2name,test2duration)
print(test1.getName() + " + " + test2.getName())
print(test1.getDuration()+test2.getDuration())





'''
English I
90
English II
90

'''