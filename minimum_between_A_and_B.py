n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
k=[]
for i in l:
    if i>=a and i<=b:
        c+=1
        k.append(i)
if c>0:
    print(min(k))
else:
    print("-1")
    
    
    
    
    
    
    
    
    
    
    
    
    