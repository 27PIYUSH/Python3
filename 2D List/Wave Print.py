def wave_print(arr,n,m):
    for j in range(m):
        if j%2==0:
            for i in range(n):
                print(arr[i][j],end=" ")
        else:
            for i in range(n-1,-1,-1):
                print(arr[i][j],end=" ")


str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)]for i in range(n)]
wave_print(arr,n,m)