def power(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)
a,b=input().split()
a=int(a)
b=int(b)
print(power(a,b))