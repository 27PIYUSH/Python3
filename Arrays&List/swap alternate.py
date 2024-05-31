# from sys import stdin

# def swapAlternate(arr,n) :
#     #Your code goes here
#     temp=0
#     if n%2==0:
#         for i in range(0,n,2):
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp
#     else:
#         for i in range(0,n-1,2):
#             temp = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = temp
#     return arr

# #Taking Input Using Fast I/O
# def takeInput() :
#     n = int(stdin.readline().rstrip())

#     if n == 0 :
#         return list(), 0

#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     return arr, n


# #Printing the array/list
# def printList(arr, n) :
#     for i in range(n) :
#         print(arr[i], end = " ")
#     print()


# #main
# t = int(stdin.readline().rstrip())

# while t > 0 :
#     arr, n = takeInput()
#     if n != 0 :
#         swapAlternate(arr,n)
#         printList(arr, n)
#     t -= 1
def swap(li,n):
    for i in range (0,n-1,2):
        li[i],li[i+1]=li[i+1],li[i]
    return li
def printList(li, n) :
    for i in range(n) :
        print(li[i], end = " ")
    print()
t=int(input())
n=int(input())
li=[int(x) for x in input().split()[:n]]
swap(li,n)
printList(li, n)

