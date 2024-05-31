class ExpenseTracker:
    # CLASS ATTRIBUTE
    expense_tracker_version=1
    def __init__(self,name,date,amount):        # {class attribute doesn't change with different objects but instance attribute changes}
        # INSTANCE/OBJECT ATTRIBUTE
        self.name=name
        self.date=date
        self.amount=amount

first=ExpenseTracker("ABC","07 JAN","6700")
second=ExpenseTracker("XYZ","27 FEB","900")

# DICT : SHOWS THE CLASS OF SPECIFIC OBJ AS DICTIONARY
print(first.__dict__)

# GETATTR : RETURNS THE VALUE OF OBJ 
print(getattr(first,'name'))

# HASATTR : RETURNS TRUE IF PROPERTY OF OBJ IS PRESENT OTHERWISE FALSE
print(hasattr(second,'amountsss'))

# DELATTR : DELETE THE PARTICULAR PROPERTY
delattr(second,'date')

print(second.__dict__)