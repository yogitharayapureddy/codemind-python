a=input()
s1,s2=a.split()
s2a=[]
for i in s2:
    s2a.append(i)
f=0
for i in s1:
    if i in s2a:
        f=1
        s2a.remove(i)
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")