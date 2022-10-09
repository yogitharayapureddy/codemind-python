def create(n,index):
    target=[]
    for num,ind in zip(n,index):
        target.insert(ind,num)
    return target
n1=int(input())
n=list(map(int,input().split()))
n2=int(input())
index=list(map(int,input().split()))
print(*create(n,index))