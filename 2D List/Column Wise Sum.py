def col_wise_sum(arr,n,m):
    for j in range (m):
        col_sum=0
        for i in range(n):
            col_sum+=arr[i][j]
        print(col_sum,end=" ")
    print()

str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
col_wise_sum(arr,n,m)