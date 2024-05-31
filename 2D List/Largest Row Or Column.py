def find_largest(arr,n,m):
    max_row_sum=-1
    max_row_index=-1
    max_col_sum=-1
    max_col_index=-1
    for i in range(n):
        row_sum=0
        for j in range(m):
            row_sum+=arr[i][j]
        if row_sum>max_row_sum:
            max_row_index=i
            max_row_sum=row_sum
    for j in range(m):
        col_sum=0
        for i in range(n):
            col_sum+=arr[i][j]
        if col_sum>max_col_sum:
            max_col_index=j
            max_col_sum=col_sum
    if max_col_sum>max_row_sum:
        return "column"+format(max_col_index, max_col_sum)
    else:
        print("row",max_row_index,max_row_sum)
    
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
print(find_largest(arr,n,m))

