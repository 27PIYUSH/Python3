# i,next0,next2
def sort012(arr) :
    next0=0
    next2=len(arr)-1
    current=0
    while current<=next2:
        if arr[current]==0:
            arr[current],arr[next0]=arr[next0],arr[current]
            current+=1
            next0+=1
        elif arr[current]==2:
            arr[current],arr[next2]=arr[next2],arr[current]
            next2-=1
        else:
            current+=1
    return arr
arr=[int(x) for x in input().split()]
print(sort012(arr))