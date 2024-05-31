def Max_col_sum(arr,n,m):
    max_col_sum=-1
    max_col_index=-1
    for j in range(m):
        col_sum=0
        for i in range(n):
            col_sum+=arr[i][j]
        if col_sum>max_col_sum:
            max_col_index=j
            max_col_sum=col_sum
    return max_col_index,max_col_sum

str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
print(Max_col_sum(arr,n,m))