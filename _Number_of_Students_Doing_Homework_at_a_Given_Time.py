n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
q=int(input())
c=0
for i in range(n):
    for j in range(l[i],l1[i]+1):
        if(q==j):
            c+=1
            break
print(c)