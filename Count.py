n=int(input())
a=list(map(int,input().split()))
c=0
v=0
for i in range(0,n):
    if a[i]%2==0:
        c+=1
    if a[i]%2!=0:
        v+=1
print(c,v)