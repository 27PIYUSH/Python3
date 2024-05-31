def row_wise_sum(arr,n,m):
    for i in range (n):
        row_sum=0
        for j in range(m):
            row_sum+=arr[i][j]
        print(row_sum,end=" ")
    print()

str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
row_wise_sum(arr,n,m)