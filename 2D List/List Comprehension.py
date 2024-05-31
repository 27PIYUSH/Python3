# li=[1,2,3,4,5]
# li2= [ ele**2 if ele%2==0 else ele for ele in li ]         #[output... for_expression... condition]   (multiple for loops and conditions)
# print(li2)

li=['PIYUSH','SATI','12345']
li_2d=[[char for char in ele] for ele in li]
print(li_2d)