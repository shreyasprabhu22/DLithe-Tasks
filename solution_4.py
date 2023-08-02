#count of elements where ith element is greater than previous greater element

n = int(input())
c=0
e= int(input())
m=e
for i in range(1,n):
    e= int(input())
    if(m<e):
         c=c+1
         m=e
print("output",c)