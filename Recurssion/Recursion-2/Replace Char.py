def replace_char(str,char1,char2):
    n=len(str)
    if n==0:
        return str
    small_string=replace_char(str[1:],char1,char2)
    if str[0]==char1:
        return char2+small_string
    else:
        return str[0]+small_string

str=input()
char1=input()
char2=input()
print(replace_char(str,char1,char2))
    
