size=256
def highestOccuringChar(string):
    max=0
    c=''
    frequency_arrary=[0]*size
    for i in string:
        frequency_arrary[ord(i)]+=1
    for i in string:
        if max<frequency_arrary[ord(i)]:
            max=frequency_arrary[ord(i)]
            c=i
    return c 


string=input()
print(highestOccuringChar(string))