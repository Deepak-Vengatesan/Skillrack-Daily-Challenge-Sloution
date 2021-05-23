class Stick:
    def __init__(self,sticklenght):
        self.sticklength = sticklenght 
    def __add__(self,new):
        return f"Length: {self.sticklenght+new.sticklenght}"
        

stick1 = Stick(int(input().strip))
stick2 = Stick(int(input().strip))
stick3 = stick1 + stick2 
print(stick3)