def replace(str,char1,char2):
    s=""
    for char in str:
        if char==char1:
            s+=char2
        else:
            s+=char
    return s

str=input("enter string: ")
char1=input("enter the character to be replaced: ")
char2=input("enter the new character: ")
str=replace(str,char1,char2)
print(str)