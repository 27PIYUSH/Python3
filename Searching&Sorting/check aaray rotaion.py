def check_rotation(arr,n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return i+1
    return 0

n=int(input())
arr=[int(x) for x in input().split()[:n]]
print(check_rotation(arr,n))