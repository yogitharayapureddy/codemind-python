n=int(input())
sum=0
temp=n
while(temp>0):
    f=1
    i=temp%10
    for i in range(1,i+1):
        f=f*i
    sum=sum+f
    temp=temp//10
if(sum==n):
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)
