def pushZerosAtEnd(arr, n):
    next0=0
    for current in range(n):
        if arr[current]!=0:
            arr[current],arr[next0]=arr[next0],arr[current]
            next0+=1
    return arr

n=int(input())
arr=[int(x) for x in input().split()[:n]]
print(pushZerosAtEnd(arr,n))
    
