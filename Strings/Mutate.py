string=input()
position=int(input())
character=input()
def mutate_string(string, position, character):
    str=''
    for i in range(len(string)):
        if i==position:
            str+=character
        else:
            str+=string[i]
    return str
print(mutate_string(string,position,character))