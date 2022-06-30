t=int(input())
while t:
    t-=1
    n=int(input())
    s=n*(n+1)//2
    a=list(map(int,input().split()))
    s1=0
    for i in range(n-1):
        s1+=a[i]
    print(s-s1)