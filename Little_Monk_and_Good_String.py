a=input()
c=m=0
v="aeiouAEIOU"
for i in range(len(a)):
    c=0
    for j in range(i,len(a)):
        if a[j] in v:
            c+=1
            if m<c:
                m=c
        else:
            break
print(m)