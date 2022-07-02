n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in range(n):
    c=0
    for j in range(i,n):
        if l[i]==l[j]:
            c+=1
            if(c>(n//2)):
                if m<l[i]:
                    m=l[i]
print(m)