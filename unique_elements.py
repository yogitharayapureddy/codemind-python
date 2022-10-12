n=int(input())
a=list(map(int,input().split()))
temp=[]
sum=0
for e in a: 
    if(e not in temp):  
        temp.append(e) 
print(*temp)