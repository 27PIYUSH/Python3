class car():
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel

    def get_car_detail(self):
        return "the make of the car is",self.model,"from car class"

class electric:
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel

    def get_car_detail(self):
        return "the make of the car is",self.model,"from electric class"

class taxi(car,electric): #MULTIPLE INHERITANCE
    def __init__(self, make, model, fuel):
        super().__init__(make, model, fuel)

myobj=taxi("tesla",2019,"electric")
print(myobj.get_car_detail())
print(taxi.__mro__)
print(taxi.mro())