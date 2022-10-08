n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for e in a:
    if(e in b and e not in res):
        res.append(e)
print(len(res))