#max count of number of parking lots filled 

r=int(input())
c=int(input())
max_count=-1
for i in range(r):
    count=0
    for j in range(c):
        e = int(input())
        if e==1:
            count+=1
    max_count = max(count, max_count)
print("output:",max_count)