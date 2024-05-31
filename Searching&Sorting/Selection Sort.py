def selection_sort(arr,size):
    for i in range(size):
        minimum=i
        for j in range(i+1,size):
            if arr[j]<arr[minimum]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]
    return arr

size=int(input("Enter size of aaray: "))
arr=[int(x) for x in input("Enter the array: ").split() [:size]]
print("Sorted array is: ",selection_sort(arr,size))
        
