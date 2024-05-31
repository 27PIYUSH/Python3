def sum_unique(list):
    s=set(list)
    sum=0
    for i in s:
        sum+=i
    return sum

list=[int(x) for x in input().split()]
print(sum_unique(list))