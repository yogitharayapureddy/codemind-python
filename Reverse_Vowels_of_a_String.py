a=input()
v="aeiouAEIOU"
arr=[]
for i in a:
    if i in v:
        arr.append(i)
i=len(arr)-1
s2=""
for j in a:
    if j in v:
        s2+=arr[i]
        i-=1
    else:
        s2+=j
print(s2)