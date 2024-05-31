class ExpenseTracker:
    # Class Attribute
    expense_tracker_version=0.1
    def __init__(self,track_category,opening_balance,tracker_budget):
        # Instance/Object Attribute
        self.track_category=track_category
        self.opening_balance=opening_balance
        self.tracker_budget=tracker_budget
    
    # Instance Method
    def get_opening_balance(self):
        return self.opening_balance
    
    # Instance Method
    def check_balance(self,limit=1000):
        if self.tracker_budget>=limit:
            return True
        else:
            return "Opening balance is less than limit!!!"
    
    @staticmethod   
    def convert_amount(amount): # No self
        return float(amount)

    # Factory Method
    @classmethod
    def get_attributes_from_string(cls,entry:str):
        track_category,opening_balance,tracker_budget = entry.split(" ")
        return ExpenseTracker(track_category.capitalize(),cls.convert_amount(opening_balance),cls.convert_amount(tracker_budget))


obj1=ExpenseTracker("home",0,1000)
obj2=ExpenseTracker("business",10000,100000)
obj3=ExpenseTracker.get_attributes_from_string("shopping 10000 50000")
print(obj1.check_balance(limit=10000))
print(obj2.get_opening_balance())
print(obj1.convert_amount(1000))
print(obj3.__dict__)