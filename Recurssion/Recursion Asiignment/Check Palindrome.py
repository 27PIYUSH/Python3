def palindrome_check(str):
    n=len(str)
    if n==0:
        return True
    else:
        if str[0]==str[-1]:
            return palindrome_check(str[1:-1])
        else:
            return False
        
str=input()
if palindrome_check(str):
    print("PALINDROME")
else:
    print("NOT")