s=input()
s=s.lower()
temp=[]
v=''
c=0
for i in s:
    if i not in temp:
        if i==' ':
            continue
        else:
            temp.append(i)
            
print(len(temp))