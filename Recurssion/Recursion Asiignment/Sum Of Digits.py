def digits_sum(n):
    if n==0:
        return 0
    else:
        return n%10 +digits_sum(n//10)
n=int(input())
print(digits_sum(n))