from abc import ABC , abstractmethod
class vehicle(ABC):
    @abstractmethod
    def get_value(self):
        pass

class car(vehicle):
    def __init__(self,make,model,fare):
        self.model=model
        self.make=make
        self.fare=fare
    
    def get_value(self):
        return 100*self.fare

myobj=car("tesla",2029,50)
print(myobj.get_value())