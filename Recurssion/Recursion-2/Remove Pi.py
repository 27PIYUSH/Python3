def remove_pi(str):
    n=len(str)
    if n==0 or n==1 :
        return str
    if str[0]=='p' and str[1]=='i':
        smaller_string=remove_pi(str[2:])
        return '3.14'+smaller_string
    else:
        smaller_string=remove_pi(str[1:])
        return str[0]+smaller_string

str=input()
print(remove_pi(str))