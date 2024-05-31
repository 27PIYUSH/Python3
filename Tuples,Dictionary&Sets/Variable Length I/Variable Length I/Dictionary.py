dict1 = {1: "one", 2: "two"}   
dict1.clear()   # removes all the items from the dictionary
print(dict1)

dict2={1:'one',2:'two',3:"three",4:'four'}
a=dict2.copy()      # copy the dictionary
print(a)

key=[1,2,3,4]
value='hello'
d=dict.fromkeys(key,value)  # creates a dictionary with keys and value
print(d)

print(dict2.get(3))         # returns the value for the specified key if the key is in the dictionary else NONE

print(dict2.items())        # returns a view object that displays a list of dictionary's (key, value) tuple pairs

print(dict2.keys())         # method extracts the keys of the dictionary and returns the list of keys

print(dict2.values())       # method extracts the values of the dictionary and returns the list of values
  
print(dict1.update(dict2))  # update the values of dictionary
print(dict1)

dict2.pop(4)                #pop the assigned key
print(dict2)

del dict2[3]                #delete the assigned key and can also del dictionary 
print(dict2)

for i in dict2:
    print(i,dict2[i],end=" ")

