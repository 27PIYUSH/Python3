def frequency_k(str,k):
    words=str.split()
    dict={}
    for i in words:
        dict[i]=dict.get(i,0)+1
    for i in dict:
        if dict[i]==k:
            print(i)
str=input()
k=int(input())
frequency_k(str,k)