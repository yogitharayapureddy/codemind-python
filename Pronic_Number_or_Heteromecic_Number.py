n=int(input())
c=0
for i in range(1,n):
    if n==i*(i+1):
        print("YES")
    else:
        c=c+1
    if c==n-1:
        print("NO")