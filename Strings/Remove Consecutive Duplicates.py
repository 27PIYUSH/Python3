def removeConsecutiveDuplicates(string):
    str=''
    for char in string:
        if str=='' or char!=str[len(str)-1]:
            str+=char

    return str

string=input()
print(removeConsecutiveDuplicates(string))