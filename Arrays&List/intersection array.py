
import sys

def intersections(arr1, arr2,n,m) :
    #Your code goes here
    arr1.sort()
    arr2.sort()
    arr3=[]
    i=0
    j=0
    while i<=n and j<=m:
        if arr1[i]==arr2[j]:
            arr3.append(arr1[i])
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            i+=1
    return arr3

#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1,arr2)
    print()

    t -= 1