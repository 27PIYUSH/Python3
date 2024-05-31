def remove_duplicate(str):
    n=len(str)
    if n==0 or n==1:
        return str
    if str[0]==str[1]:
        smaller_string=remove_duplicate(str[1:])
        return smaller_string
    else: 
        return str[0]+remove_duplicate(str[1:])
    
str=input()
print(remove_duplicate(str))