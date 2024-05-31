def checkPalindrome(str):
    start=0
    end=len(str)-1
    while start<=end:
        if str[start]!=str[end]:
            return False
            break
        else:
            start+=1
            end-=1
    return True

str=input()
if checkPalindrome(str)==True:
    print("true")
else:
    print("false")

# def palindrome(str):
#     i=0
#     j=len(str)-1
#     flag=True
#     while i<j:
#         if str[i]!=str[j]:
#             flag=False
#             break
#         else:
#             i+=1
#             j-=1
#     return flag