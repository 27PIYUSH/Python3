str=input()
def swap_case(str):
    str1=''
    for char in str:
        if char>='a' and char<='z':
            str1+=char.upper()
        elif char>='A' and char<='Z':
            str1+=char.lower()
        else:
            str1+=char
    return str1
print(swap_case(str))