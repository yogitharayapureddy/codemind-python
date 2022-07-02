n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in range(n):
    if(l[i]==1):
        c+=1
        if(c>m):
            m=c
    else:
        c=0
print(m)