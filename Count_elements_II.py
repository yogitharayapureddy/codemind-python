n,m=(map(int,input().split()))
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
temp=[]
for e in a1:
    if e in a1 and e not in a2 and e not in temp:
        temp.append(e)
for e in a2:
    if e in a2 and e not in a1 and e not in temp:
        temp.append(e)
print(len(temp))