def second_largest(arr,n):
    largest=arr[0]
    second_large=0
    for i in range(n):
        if largest<arr[i]:
            second_large=largest
            largest=arr[i]
        elif second_large<arr[i] and arr[i]!=largest:
            second_large=arr[i]
    return second_large
n=int(input())
arr=[int(x) for x in input().split()[:n]]
print(second_largest(arr,n))

