def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    total=(n//a)+(n//b)
    l=(a*b)//gcd(a,b)
    total-=(2*(n//l))
    if total>=k:
        print("Win")
    else:
        print("Lose")