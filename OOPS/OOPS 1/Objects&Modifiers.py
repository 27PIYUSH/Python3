class ExpenseTracker:
    # Class attribute
    expense_tracker_version=0.1
    def __init__(self,date,description,transaction_type,amount):
        #  Instance/object attribute

        # Public modifier
        self.date=date
        self.description=description
        self.transaction_type=transaction_type

        # Private modifier
        self.__amount=amount        # {cannot access amount directly it will give attribute error}

    def show_private_attributes__of_child(self):
        print(self._ExpenseTracker__amount)

# CLASS OBJECTS
obj1=ExpenseTracker("3 may","rishita spend money on chilli","canteen payment","60")
obj2=ExpenseTracker("1 may","himanshu spend money on tickets","ticket payment","100")

print(obj1.__dict__)
# print(obj2.amount) # Will give attribute error
print(obj2._ExpenseTracker__amount) # first way to access private modifier
obj2.show_private_attributes__of_child() # Second way to access private modifier