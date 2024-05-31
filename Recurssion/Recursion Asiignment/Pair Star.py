def pair_star(str):
    if len(str)==1:
        return str
    else:
        if str[0]==str[1]:
            return str[0]+ "*" +pair_star(str[1:])
        else:
            return str[0]+pair_star(str[1:])
str=input()
print(pair_star(str))