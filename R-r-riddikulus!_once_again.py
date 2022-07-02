i,j=map(int,input().split())
a=list(map(int,input().split()))
print(*(a[j:]+a[:j]))