def removeAllOccurrencesOfChar(string, ch) :
    str=""
    for char in string:
        if char!=ch:
            str+=char
    return str
string=input()
ch=input()
print(removeAllOccurrencesOfChar(string,ch))
