def merge(arr,left,right):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

def merge_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    else:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr,left,right)
        return arr

arr=[int(x) for x in input().split()]
print(merge_sort(arr))
