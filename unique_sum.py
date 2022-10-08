n=int(input())
a=list(map(int,input().split()))
temp=[]
s=0
for e in a:
    if(e not in temp):
        temp.append(e)
        if e in temp:
            s+=e
            continue
print(s)