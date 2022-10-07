n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
t=[]
c=0
for i in a:
    if i>=x and i<=y:
        c+=11
        t.append(i)
if c>0:
    print(min(t))
else:
    print("-1")