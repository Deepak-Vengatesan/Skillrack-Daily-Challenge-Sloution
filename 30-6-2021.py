class Distance:
    def __init__(self,feet,inches):
        self.feet = feet 
        self.inches = inches 
    
    def __add__(self,other):
        newFeet = self.feet + other.feet
        newInches = self.inches + other.inches
        return Distance(newFeet+newInches//12,newInches%12)
 
    def __str__(self):
        return str(self.feet)+" "+str(self.inches)

    def addInches(self,X):
        self.feet = self.feet+(self.inches+X)//12 
        self.inches = (self.inches+X)%12
