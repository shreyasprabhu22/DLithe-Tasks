#string that contains '*' and '#'

s=input()
count=0
c=0
for i in s:
    if(i=='*'):
        count=count+1
    else:
        c=c+1
        
if(c==count):
    print(0)
elif(c>count):
    print("negative")
else:
    print("positive")