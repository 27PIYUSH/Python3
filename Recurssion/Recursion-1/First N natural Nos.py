def print_N(n):
    if n==0:
        return
    else:
        print_N(n-1)
        print(n)
        return
n=int(input())
print_N(n)