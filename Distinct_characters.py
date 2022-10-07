l=input('')
l=l.lower()
temp=[]
v=""
for e in l:
    if(e not in temp):
        if e==" ":
            continue
        else:
            temp.append(e)
r=sorted(temp)
for i in r:
    if i==" ":
        continue
    else:
        v+=i
print(v)