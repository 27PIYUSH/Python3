# not jagged n,m both known

# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n=3
# m=4
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=" ")
#     print()

li=[[1,2,3],[4,5,6,7,8],[9,10]]
for ele in li:
    for char in ele:
        print(char,end=' ')
    print()
