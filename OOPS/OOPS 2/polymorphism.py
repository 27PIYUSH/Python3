class Vehicle:
    """this is a parent class"""
    current_year=2023
    base_price=1000
    def __init__(self,model,brand,fuel_capacity):
        self.model=model
        self.__brand=brand
        self.__fuel_capacity=fuel_capacity
    
    #default function to get value of car
    def get_value(self):
        age=Vehicle.current_year-self.model
        print("This is defalult method of parent")
        return Vehicle.base_price*(1/age)

class Car(Vehicle):
    """this is a child class"""
    def __init__(self,model,brand,fuel_capacity,air_conditioning,sunroof):
        # Parent Attribute
        super(Car,self).__init__(model,brand,fuel_capacity)

        # Child Attributes
        self.air_conditioning=air_conditioning
        self._sunroof=sunroof #Protected

    # overriding method - replaces the parent defalut method
    def get_value(self):
        Vehicle.base_price=5000
        age=Vehicle.current_year-self.model
        print("This is child override method")
        return Vehicle.base_price*(1/age)          

obj1=Car(2004,"TESLA","10L",True,False)
obj2=Vehicle(2007,"ford","15L")

print(obj1.get_value())
print(obj2.get_value())
print(obj1._sunroof)
