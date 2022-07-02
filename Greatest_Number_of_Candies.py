n=int(input())
a=list(map(int,input().split()))
p=int(input())
c=max(a)
for i in a:
    if(i+p>=c):
        print("True",end=' ')
    else:
        print("False",end=' ')