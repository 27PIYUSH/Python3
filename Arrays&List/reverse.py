def reverse(arr,n):
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    return arr

n=int(input())
arr=[int(x) for x in input().split()[:n]]
print(reverse(arr,n))
