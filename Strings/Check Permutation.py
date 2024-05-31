size=256
def isPermutation(string1, string2) :
    frequency_array=[0]*size
    for i in string1:
        frequency_array[ord(i)]+=1
    for i in string2:
        frequency_array[ord(i)]-=1
    if frequency_array==[0]*size:
        return True
    else:
        return False

string1=input()
string2=input()
print(isPermutation(string1,string2))