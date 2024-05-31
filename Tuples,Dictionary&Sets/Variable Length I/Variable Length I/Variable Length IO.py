def sum(a,b,*more):
    ans=a+b
    for i in more:
        ans=ans+i
    return ans
print(sum(1,2,3,4,5))

def sum_multiply(a,b,*more):
    sum_value = a+b
    m_value = a*b
    for i in more:
        sum_value += i
        m_value*=i
    return sum_value,m_value
print(sum_multiply(2,3,4,5,6,7))