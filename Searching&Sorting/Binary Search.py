def binary_search(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[int(ele) for ele in input("Enter sorted array: ").split()]
x=int(input("Element to be searched: "))
ans=binary_search(arr,x)
if ans != -1:
    print("Element found at index: ",ans)
else:
    print("Element not found")