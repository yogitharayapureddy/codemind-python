n=int(input())
f=0
for i in range(1,n+1):
    if(i*(i+1)==n):
        f=1
        print("YES")
        break
if f==0:
    print("NO")