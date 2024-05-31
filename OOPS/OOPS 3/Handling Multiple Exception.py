#NESTED TRY & ELSE CONDITIONS:::
class vehicle:
    def __init__(self,make,model,fare):
        self.make=make
        self.model=model
        self.fare=fare
    
    def get_value(self):
        try:
            age=2020-self.model
            return 1000*(1/age)
        except TypeError:
            try:
                age=2020-int(self.model)
                return 1000*(1/age)
            except ZeroDivisionError:
                age=2020-int(self.model)
                return 1000*(1)
            except:
                return "Entered data in incorrect format"

myobj=vehicle("tesla",'2020',"electric")
print(myobj.get_value())