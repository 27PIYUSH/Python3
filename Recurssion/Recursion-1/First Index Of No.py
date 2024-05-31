def first_index(arr,x):
    n=len(arr)
    if n==0:
        return -1
    elif arr[0]==x:
        return 0
    smallerListOutput = first_index(arr[1:], x)
    if smallerListOutput==-1:
        return -1
    else:
        return smallerListOutput+1


x=int(input())
arr=[int(x) for x in input().split()]
print(first_index(arr,x))

# USING START INDEX METHOD:::

# def first_index(arr,x,si):
#     n=len(arr)
#     if si==n:
#         return -1
#     elif arr[si]==x:
#         return si
#     else: 
#         return first_index(arr,x,si+1)

# si=int(input())