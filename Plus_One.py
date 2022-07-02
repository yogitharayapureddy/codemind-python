n=int(input())
l=list(map(int,input().split()))
k=''
for i in l:
    k+=str(i)
k=int(k)+1
for i in str(k):
    print(i,end=' ')