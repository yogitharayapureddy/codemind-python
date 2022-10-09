t=int(input())
i=0
while i<t:
    n,r=input().split()
    num=list(map(int,input().split()))
    r=int(r)%int(n)
    print(" ".join(str(x) for x in num[-int(r):]+num[:-int(r)]))
    i+=1