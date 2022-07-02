n=int(input())
l=list(map(int,input().split()))
c=0
m=0
t=l[0]
for i in range(n):
    c=0
    for j in range(i,n):
        if(l[i]==l[j]):
            c+=1
    if(c>=m):
        if m==c:
            if t>l[i]:
                t=l[i]
        else:
            t=l[i]
        m=c
print(t)