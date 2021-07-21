class Fruit:
    count = 0
    totalQuantity= 0
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
        Fruit.count += 1
        Fruit.totalQuantity += quantity


    def __del__(self):
        Fruit.count -= 1
        Fruit.totalQuantity -= self.quantity

    def __str__(self):
        return f"{self.name} : {self.quantity}"