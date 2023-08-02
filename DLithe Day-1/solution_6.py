# find 2nd greatest and minimum element 

max1=-999
min1=999
for i in range(5):
    
    e= int(input())
    if(e<min1):
        min2=min1
        min1=e
    if(e>max1):
        max2=max1
        max1=e
    
print("second min: ",min2)
print("second max: ",max2)