def dig(n):
    c=0
    while n:
        c+=1
        n//=10
    return c
n=int(input())
l=list(map(int,input().split()))
m=dig(max(l))
c=0
for i in range(n):
    if(dig(l[i])==m):
        c+=1
print(c)
