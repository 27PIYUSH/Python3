# RAISE EXCEPTION ::: 
class NegativeCarValue(Exception):
    def __init__(self,value,msg="car value cannot be negative"):
        self.value=value
        self.msg=msg
        super().__init__(self.msg)
        
    def __str__(self):
        return f"{self.msg} --> {self.value}" 

class vehicle:
    def __init__(self,make,model,fare):
        self.make=make
        self.model=model
        self.fare=fare
        self.current_year = 2023

    def get_value(self):
        age=self.current_year-self.model
        if age<0:
            raise NegativeCarValue(age)
        else:
            return 1000*(1/age)

myobj=vehicle("tesla",2027,90)
print(myobj.get_value())