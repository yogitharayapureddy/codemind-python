n=int(input())
l=list(map(int,input().split()))
c=0
count=0
k=[]
for i in l:
    while(i):
        d=i%10
        c+=1
        i=i//10
    k.append(c)
    c=0
v=max(k)
for j in k:
    if j==v:
        count+=1
print(count)