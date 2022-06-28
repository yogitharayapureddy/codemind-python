n=int(input())
for i in range(0,n):
    a=int(input())
    i=a
    s=0
    while(a>0):
        d=a%10
        s=s*10+d
        a=a//10
    if(i==s):
        print("True")
    else:
        print("False")