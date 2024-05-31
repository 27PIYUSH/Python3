class vehicle():
    def __init__(self,model,brand,fuel):
        self.model=model
        self.brand=brand
        self.fuel=fuel

class car(vehicle):
    def __init__(self,model,brand,fuel,air_conditioning,sunroof):
        super(car,self).__init__(model,brand,fuel)
        self.air_conditioning=air_conditioning
        self.sunroof=sunroof
        
class electric(car):
    def __init__(self, model,brand,fuel,air_conditioning,sunroof,distance):
        super(electric,self).__init__(model,brand,fuel,air_conditioning,sunroof)
        self.distance=distance

myobj=electric(2023,"tesla","electric",True,True,"200km")
print(myobj.__dict__)