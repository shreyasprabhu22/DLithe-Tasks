#palindrome numbers

n=int(input())
m=n
sum1 = 0
while n!=0:
    digit = n%10
    sum1=sum1*10+digit
    n=n//10

if m==sum1:
    print("Yes, Palindrome")
else:
    print("not a palindrome")