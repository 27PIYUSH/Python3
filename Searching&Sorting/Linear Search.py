# # linear search:::

def linear_search(lst,ele):
    for i in range (len(lst)):
        if lst[i]==ele:
            return i
    return -1

lst=[int(x) for x in input("Enter array: ").split()]
ele=int(input("Element to be searched: "))
ans=linear_search(lst,ele)
if ans != -1:
    print("Element found at index: ",ans)
else:
    print("Element not found")