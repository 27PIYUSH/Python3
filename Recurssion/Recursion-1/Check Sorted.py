def check_sorted(arr):
    l=len(arr)
    if l==0 or l==1:
        return True
    else:
        return arr[0]<=arr[1] and check_sorted(arr[1:])

arr=[int(x) for x in input().split()]    
if check_sorted(arr):
    print("sorted")
else:
    print("not sorted")

# USING STARTING INDEX:::

# def sorted(arr,s):
#     n=len(arr)
#     if s==n or s==n-1 :
#         return True
#     elif arr[s]>arr[s+1]:
#         return False
#     else:
#         return sorted(arr,s+1)