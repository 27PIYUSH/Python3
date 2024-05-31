def last_index(arr,x):
    n=len(arr)
    if n==0:
        return -1
    smallerList=last_index(arr[1:],x)
    if smallerList!=-1:
        return smallerList+1
    else:
        if arr[0]==x:
            return 0
        else:
            return -1
x=int(input())
arr=[int(x) for x in input().split()]
print(last_index(arr,x))

# def last_index(arr,x,si):
#     n=len(arr)
#     if si==n:
#         return -1
#     smallerList=last_index(arr,x,si+1)
#     if smallerList!=-1:
#         return smallerList
#     else:
#         if arr[si]==x:
#             return si
#         else:
#             return -1