def spiral_print(arr,n,m):
    col_start=0
    col_end=m-1
    row_start=0
    row_end=n-1
    while(row_start<=row_end and col_start<=col_end):
        #top
        for i in range(col_start,col_end+1):
            print(arr[row_start][i],end=" ")
        row_start+=1

        #top to bottom
        for i in range(row_start,row_end+1):
            print(arr[i][col_end],end=" ")
        col_end-=1

        if row_start<=row_end and col_start<=col_end:
            #bottom
            for i in range(col_end,col_start-1,-1):
                print(arr[row_end][i],end=" ")
            row_end-=1

            #bottom to top
            for i in range(row_end,row_start-1,-1):
                print(arr[i][col_start],end=" ")
            col_start+=1
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
spiral_print(arr,n,m)
