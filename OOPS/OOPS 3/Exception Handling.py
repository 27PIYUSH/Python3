# TRY AND EXCEPT :::

class vehicle:
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel

    def get_value(self):
        try:
            age=2020-self.model
            return 1000*(1/age)
        except TypeError:
            age=2020-int(self.model)
            return 1000*(1/age)
        except ZeroDivisionError:
            age=2020-int(self.model)
            return 1000*(1)

myobj=vehicle("tesla",2020,"electric")
print(myobj.get_value())