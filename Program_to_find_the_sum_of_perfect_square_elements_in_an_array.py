import math
def perfect(c):
    if c>0:
        s=int(math.sqrt(c))
        return(s*s==c)
    return false
n=int(input())
a=list(map(int,input().split()))
t=0
for i in range(n):
    if perfect(a[i]):
        t+=a[i]
print(t)