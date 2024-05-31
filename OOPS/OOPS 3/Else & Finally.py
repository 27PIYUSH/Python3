class NegativeZeroModelYear(Exception):
    def __init__(self,value,msg="model year cannot be equal or greater than 2023"):
        self.value=value
        self.msg=msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.msg} --> {self.value}"

class CarModelYearAsString(Exception):
    def __init__(self,value,msg="model year cannot be strings. Try passing int values"):
        self.value=value
        self.msg=msg
        super().__init__(self.msg)
    
    def __str__(self):
        return f"{self.msg} --> {self.value}"

class vehicle:
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel
        self.current_year=2023
        self.value=None
    
    def get_value(self):
        try:
            if type(self.model)==str:
                status="custom"
                raise CarModelYearAsString(self.model)
            elif self.model>=self.current_year:
                status="custom"
                raise NegativeZeroModelYear(self.model)
            else:
                self.age=self.current_year-self.model
                self.value=1000*(1/self.age)
                status="success"
        except TypeError:
            self.age=self.current_year-self.model
            self.value=1000*(1/self.age)
            status="inbuilt"
        else:
            print("code ran withoput any exception")
        finally:
            if status=="custom":
                print("code has custom exceptions,rectify them")
            elif status=="inbuilt":
                print("code has inbuilt exceptions,rectify them")
            else:
                print("value without any exception ->",self.value)

myobj=vehicle("tesla",2030,"electric")
print(myobj.get_value())

            
