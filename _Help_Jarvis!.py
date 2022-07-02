t=int(input())
for i in range(t):
    l=input()
    li=[]
    for i in l:
        li.append(int(i))
    mi=min(li)
    m=max(li)
    c=0
    a=[]
    for i in range(mi,m+1):
        a.append(i)
    if sorted(li)==sorted(a):
        print("YES")
    else:
        print("NO")        