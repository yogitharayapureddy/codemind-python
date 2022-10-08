n=int(input())
a=list(map(int,input().split()))
temp=[]
c=0
for e in a:
    if(e not in temp):
        temp.append(e)
    c=0
    for e in temp:
        if e%2!=0:
            c+=1
print(c)