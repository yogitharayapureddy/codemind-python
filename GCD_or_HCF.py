a,b=map(int,input().split())
a=min(a,b)
i=a
while i:
    if a%i==0 and b%i==0:
        print(i)
        break
    i-=1