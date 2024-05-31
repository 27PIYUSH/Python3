n=int(input())
m=int(input())
arr1=[int(x) for x in input().split()[:n]]
arr2=[int(x) for x in input().split()[:m]]
def sum_of_two_arrays(arr1,n,arr2,m):
    i=n-1
    j=m-1
    k=max(n,m)+1
    carry=0
    output=[0]*k 
    while i>=0 and j>=0:
        num=arr1[i]+arr2[j]+carry
        s=num%10
        carry=num//10
        output[k-1]=s
        k-=1
        i-=1
        j-=1
    while i>=0:
        num=arr1[i]+carry
        s=num%10
        carry=num//10
        output[k-1]=s
        k-=1
        i-=1
    while j>=0:
        num=arr2[j]+carry
        s=num%10
        carry=num//10
        output[k-1]=s
        k-=1
        j-=1
    if carry!=0:
        output[0]=carry
    return output
print(sum_of_two_arrays(arr1,n,arr2,m))
