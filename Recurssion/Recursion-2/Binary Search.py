def binary_search(arr,low,high,x):
    n=len(arr)
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1
arr=[int(x) for x in input().split()]
x=int(input())
print(binary_search(arr,0,len(arr)-1,x))