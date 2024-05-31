class vehicle:
    def __init__(self,make,model,fare):
        self.make=make
        self.model=model
        self.fare=fare
        
    def __str__(self):
        return f"the make of car is {self.make} and the model is of {self.model} with a fare of {self.fare}"
    
    def __add__(self,other):
        return self.fare+other.fare
    
obj1=vehicle("tesla",2020,50)
obj2=vehicle("ford",2011,70)
print(obj1+obj2)
