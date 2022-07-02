n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    l[i]=(l[i]**2)
l.sort()
for i in range(n):
    print(l[i],end=' ')