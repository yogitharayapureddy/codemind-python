def find_gcd(x,y):
    while(y):
        x,y = y,x % y
        
    return x
n=int(input())
l=list(map(int,input().split()))
n1=l[0]
n2=l[1]
gcd=find_gcd(n1,n2)
for i in range(2,len(l)):
    gcd=find_gcd(gcd,l[i])
print(gcd)