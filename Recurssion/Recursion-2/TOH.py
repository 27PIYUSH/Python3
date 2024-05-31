def TOH(n,source,medium,destination):
    if n==1:
        print("MOVE DISK ",n, " FROM ",source, " TO " ,destination)
        return 
    else:
        TOH(n-1,source,destination,medium)
        print("MOVE DISK ",n, " FROM ",source, " TO " ,destination)
        TOH(n-1,medium,source,destination)
        return

n=int(input())
print(TOH(n,'A','B','C'))