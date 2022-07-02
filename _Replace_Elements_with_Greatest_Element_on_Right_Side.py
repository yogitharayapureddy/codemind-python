n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    m=-1
    for j in range(i+1,n):
        if(m<l[j]):
            m=l[j]
    print(m,end=' ')