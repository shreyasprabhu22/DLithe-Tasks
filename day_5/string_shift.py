

a=input()
a=list(a)
r=[]
l=[]
for i in range(len(a)):
    l.append(int(input()))
for i in range(len(a)):
    for j in range(i+1):
        c=a[j]
        x=(ord(c) + l[i])
        if x>122:
            x=(x%122)+96
        a[j]=chr(x)
        
str1='' 
for ele in a:
    str1 += ele
print(str1)

