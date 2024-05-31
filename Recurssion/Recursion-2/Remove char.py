def remove_char(str,char):
    n=len(str)
    if n==0:
        return str
    small_string=remove_char(str[1:],char)
    if str[0]==char:
        return small_string
    else:
        return str[0]+small_string

str=input()
char=input()
print(remove_char(str,char))