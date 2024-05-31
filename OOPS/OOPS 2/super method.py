class Vehicle:
    """this is a parent class"""
    def __init__(self,model,brand,fuel_capacity):
        self.model=model
        self.__brand=brand
        self.__fuel_capacity=fuel_capacity
    
    def __private_method_parent(self):
        print("THIS IS PRIVATE")
    
class Car(Vehicle):
    """this is a child class"""
    def __init__(self,model,brand,fuel_capacity,air_conditioning,sunroof):
        # Parent Attribute
        super(Car,self).__init__(model,brand,fuel_capacity)

        # Child Attributes
        self.air_conditioning=air_conditioning
        self.sunroof=sunroof

obj1=Car(2004,"TESLA","10L",True,False)

print(obj1.__dict__)
obj1._Vehicle__private_method_parent()
