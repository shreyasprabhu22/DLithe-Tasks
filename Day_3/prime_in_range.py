start = int(input())
end = int(input())
a=[]
for i in range(start, end+1):
    flag = 0
    for j in range(2, i//2):
        if(i%j == 0):
            flag = 1
            break
    if(flag == 0):
        print(i)


