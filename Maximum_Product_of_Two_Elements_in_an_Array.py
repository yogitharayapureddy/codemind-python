li=list(map(int,input().split()))
l=len(li)
g=0
m=0
for i in range(l):
    m=0
    for j in range(i+1,l):
        m=(li[i]-1)*(li[j]-1)
        if(m>g):
            g=m
print(g)