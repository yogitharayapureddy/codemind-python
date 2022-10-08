n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for e in a:
    if(e not in b and e not in res):
        res.append(e)
for e in b:
    if(e not in a and e not in res):
        res.append(e)
print(*res)
