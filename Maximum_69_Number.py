n=int(input())
a=[]
t=0
s=0
while n!=0:
    r=n%10
    t=t*10+r
    n//=10
while t!=0:
    r=t%10
    a.append(r)
    s+=1
    t//=10
for i in range(0,s):
    if a[i]==6:
        a[i]=9
        break
for i in range(0,s):
    print(a[i],end='')