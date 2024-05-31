# The first list has the elements that are present only in nums1, while the second list has the elements that are present only in nums2.
li1=[2,3,9,6]
li2=[0,9,6,0]
def kprint(li1,li2):
    for i in li1:
        if i in li2:
            li1.remove(i)
            li2.remove(i)
    return [li1,li2]
print(kprint(li1,li2))