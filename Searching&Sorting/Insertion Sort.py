# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         j=i  #iterates list to the left and swap
#         while arr[j-1]>arr[j] and j>0:  #if left ele is greater
#             arr[j-1],arr[j]=arr[j],arr[j-1]
#             j-=1  # move left
#     return arr
     
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while arr[j]>key and j>=0:  
            arr[j+1]=arr[j]
            j-=1  
        arr[j+1]=key
    return arr

arr=[int(x) for x in input("Enter the array: ").split()]
print("Sorted array is: ",insertion_sort(arr))
   