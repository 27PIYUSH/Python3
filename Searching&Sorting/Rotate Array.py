# def rotate(arr,n,shift):
#     for i in range(0,shift):
#         temp=arr[n-1]
#         for j in range(n-1,0,-1):
#             arr[j]=arr[j-1]
#         arr[0]=temp
#     return arr

n=int(input())
d=int(input())
arr=[int(x) for x in input().split()[:n]]
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def rotate(arr,n,d):
    reverse(arr,0,n-1)
    reverse(arr,0,n-d-1)
    reverse(arr,n-d,n-1)
    return arr

if d<=n:
    print(rotate(arr, n, d))
else:
    d=d%n
    print(rotate(arr, n, d))
