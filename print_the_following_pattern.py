n=int(input())
a=n
for i in range(1,n+1):
    for j in range(1,n+1):
        print(a,end=' ')
        a=a-1
    a=n
    print()