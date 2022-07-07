n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        continue
s=0
for i in range(len(b)):
    if(b[i]%2==1):
        s=s+b[i]
print(s)
        