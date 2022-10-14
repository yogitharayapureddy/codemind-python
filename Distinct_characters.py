s=input()
s=s.lower()
a=''
v=''
for i in s:
    if s.count(i)==1:
        a+=i
r=sorted(a)
for i in r:
    if i==' ':
        continue
    else:
        v+=i
print(v)