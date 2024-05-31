def count_0(n):
    if n==0:
        return 1
    elif n<10:
        return 0
    else:
        if n%10==0:
            return count_0(n//10)+1
        else:
            return count_0(n//10)

n=int(input())
print(count_0(n))
