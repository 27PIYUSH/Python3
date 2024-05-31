def sum_arr(arr):
    n=len(arr)
    if n==0:
        return 0
    else:
        return arr[0]+sum_arr(arr[1:])

arr=[int(x) for x in input().split()]
print(sum_arr(arr)) 