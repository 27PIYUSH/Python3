def merge(arr1, n, arr2, m) : 
    arr3=[]
    i,j=0,0
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while i<n:
        arr3.append(arr1[i])
        i+=1
    while j<m:
        arr3.append(arr2[j])
        j+=1
    return arr3

n=int(input())
arr1=[int(x) for x in input().split()[:n]]
m=int(input())
arr2=[int(x) for x in input().split()[:m]]
print(merge(arr1, n, arr2, m))