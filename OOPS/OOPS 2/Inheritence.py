class Vehicle:
    """this is a parent class"""
    def __init__(self,model,brand,fuel_capacity):
        self.model=model
        self.brand=brand
        self.__fuel_capacity=fuel_capacity
    
    def __private_method_parent(self):
        print("THIS IS PRIVATE")
    
class Car(Vehicle):
    """this is a child class"""
    def __init__(self,model,brand,fuel_capacity,air_conditioning,sunroof):
        # Parent Attributes
        Vehicle.model=model
        Vehicle.brand=brand
        Vehicle.__fuel_capacity=fuel_capacity

        # Child Attributes
        self.air_conditioning=air_conditioning
        self.sunroof=sunroof
    
    def show_parent_attributes(self):
        print(Vehicle.model,Vehicle.brand,Vehicle.__fuel_capacity)
    
    def show_private_attributes_of_Parent(self):  # We define a public method inside child class and access the private attribute by _ParentClass name
        self._Vehicle__private_method_parent()

obj1=Car(2004,"TESLA","10L",True,False)

print(obj1.__dict__) # we cannot directly access the parent attributes
obj1.show_parent_attributes()
# obj1.__private_method_parent() # We cannot access private attributes with this method
obj1.show_private_attributes_of_Parent() 