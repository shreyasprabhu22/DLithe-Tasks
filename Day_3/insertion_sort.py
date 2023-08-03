n = int(input())
a=[]
for i in range(0, n):
    a.append(int(input()))


for i in range(1, len(a)):
    key = a[i]
    j = i-1
    while j >=0 and key < a[j] :
        a[j+1] = a[j]
        j -= 1
        a[j+1] = key

for j in range(0, n):
    print(a[j])