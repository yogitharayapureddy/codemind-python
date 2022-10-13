n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
c=0
for i in l:
    if i>=a and i<=b:
        c+=1
        k.append(i)
if c>0:
    print(max(k))
else:
    print("-1")