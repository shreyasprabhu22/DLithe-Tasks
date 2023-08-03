import numpy as np

n = int(input())
flag = 0


for i in range(2, int(np.sqrt(n))):
    if(n%i == 0):
        print("not prime")
        flag=1
        break
if flag==0:
    print("prime")

