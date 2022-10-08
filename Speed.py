t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=1
    ma=l[0]
    for i in range(1,n):
        if l[i]<=ma:
            c+=1
            ma=l[i]
    print(c)