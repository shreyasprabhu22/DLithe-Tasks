# Find the greatest element

max1=-999
min1=999
for i in range(10):
    e= int(input())
    max1 = max(max1, e)
    min1 = min(min1, e)
print("min",min1)
print("max",max1)