def multiplication(m,n):
    if m==0 or n==0:
        return 0
    elif m<n:
        return n+multiplication(m-1,n)
    else:
        return m+multiplication(m,n-1)
    
m=int(input())
n=int(input())
print(multiplication(m,n))