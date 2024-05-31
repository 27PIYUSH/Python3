a={'abc','random',27,'56'}

a.add("new word")   # add element
print(a)

b={'hey',69}
a.update(b)
print(a)

a.remove('56')
a.discard('abc')
print(a)

a.pop() # pop any random element
print(a)

s=set()
print(s)

arr=[1,2,3,4,5,1,2,3,4,5]
s=set(arr)
print(s)