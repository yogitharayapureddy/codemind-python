n=int(input())
r=0
s=0
if n<0:
    n=-n
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(-s)
else:
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)