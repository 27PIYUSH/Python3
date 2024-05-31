def ispresent(arr,x):
    n=len(arr)
    if n==0:
        return False
    elif arr[0]==x:
        return True
    else:
        return ispresent(arr[1:],x)
    
arr=[int(x)for x in input().split()]
x=int(input())
print(ispresent(arr,x))